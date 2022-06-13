from flask import Flask, jsonify
from flask_restful import Resource, Api, abort, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import json

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///prolifeequipmentdb.db')
db = SQLAlchemy(app)

class TestRecordModel(db.Model):
    __tablename__ = 'TestRecord'
    test_record_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    date = db.Column(db.String)
    record = db.Column(db.String)
    template = db.Column(db.String)
    device_serial_number = db.Column(db.String)
    device_model = db.Column(db.String)
    mti_test_instrument = db.Column(db.String)
    mti_serial_number = db.Column(db.String)
    mti_firmware_version = db.Column(db.String)
    testResults = relationship("TestResultModel", cascade="all, delete")
    
class TestResultModel(db.Model):
    __tablename__ = "TestResult"
    test_result_id = db.Column(db.Integer, primary_key=True)
    test_record_id = db.Column(db.Integer, ForeignKey("TestRecord.test_record_id", ondelete="CASCADE"))
    test_element = db.Column(db.String)
    test_type = db.Column(db.String)
    procedure = db.Column(db.String)
    testResultItems = relationship("TestResultItemModel", cascade="all, delete")

		    
class TestResultItemModel(db.Model):
    __tablename__ = "TestResultItem"
    test_result_item_id = db.Column(db.Integer, primary_key=True)
    test_result_id = db.Column(db.Integer, ForeignKey("TestResult.test_result_id", ondelete="CASCADE"))
    result = db.Column(db.String)
    value = db.Column(db.Float)
    unit = db.Column(db.String)
    high_limit = db.Column(db.Float)
    low_limit = db.Column(db.Float)
    standard = db.Column(db.String)


testRecordArgs = reqparse.RequestParser()
testRecordArgs.add_argument("status", type=str, help="O campo status deve ser informado", required=True)
testRecordArgs.add_argument("date", type=str, help="A data deve ser informada", required=True)
testRecordArgs.add_argument("record", type=str,  required=False)
testRecordArgs.add_argument("template", type=str,  required=False)
testRecordArgs.add_argument("device_serial_number", type=str, help="O campo device_serial_number é obrigatório!", required=True)
testRecordArgs.add_argument("device_model", type=str,  required=False)
testRecordArgs.add_argument("mti_test_instrument", type=str,  required=False)
testRecordArgs.add_argument("mti_serial_number", type=str,  required=False)
testRecordArgs.add_argument("mti_firmware_version", type=str,  required=False)
testRecordArgs.add_argument("testResults", type=str,  required=False)
testRecordArgs.add_argument("testResultItems", type=str,  required=False)

testResultItem_resource_fields = {
    'test_result_id' : fields.Integer,
    'test_result_item_id' : fields.Integer,
    'result' : fields.String,
    'value' : fields.Float,
    'unit' : fields.String,
    'high_limit' : fields.Float,
    'low_limit' : fields.Float,
    'standard' : fields.String,
}

testResult_resource_fields = {
    'test_record_id' : fields.Integer,
    'test_result_id' : fields.Integer,
    'test_element' : fields.String,
    'test_type'   : fields.String,
    'procedure' : fields.String,
    'testResultItems' : fields.List(fields.Nested(testResultItem_resource_fields)),
}


testRecord_resource_fields = {
    'test_record_id' : fields.Integer,
    'status' : fields.String,
    'date'   : fields.String,
    'record' : fields.String,
    'template' : fields.String,
    'device_serial_number' : fields.String,
    'device_model' : fields.String,
    'mti_test_instrument' : fields.String,
    'mti_serial_number' : fields.String,
    'mti_firmware_version' : fields.String,
    'testResults' : fields.List(fields.Nested(testResult_resource_fields)),
    'uri' : fields.Url('TestRecords', absolute=True) ,
}

class EquipamentosAPI(Resource):
    @marshal_with(testRecord_resource_fields)
    def get(self, test_record_id):
        test_record_id = int(test_record_id)
        if(test_record_id==0):
            testRecords = TestRecordModel.query.all()
            if(testRecords):
                return testRecords, 200
            else:
                return 404
        else:
            testRecord = TestRecordModel.query.filter_by(test_record_id=test_record_id).first()
            if not testRecord:
                abort(404, error=True, message=('Não foi possível encontrar TestRecord com id = {}').format(test_record_id))
            else:
                return testRecord, 200


    @marshal_with(testRecord_resource_fields)
    def put(self, test_record_id):
        updateError = False
        args = testRecordArgs.parse_args()
        testRecord = TestRecordModel.query.filter_by(test_record_id=test_record_id).first()
        if not testRecord:
            updateError = True
            #  Se o método atualiza um recurso existente, retorna 200 (OK) ou 204 (Sem conteúdo).
            abort(204, error=True, message=('Não foi possível encontrar TestRecord com id = {}').format(test_record_id))
        else:
            testRecord.status =  args['status']
            testRecord.date =  args['date']
            testRecord.record =  args['record']
            testRecord.template =  args['template']
            testRecord.device_serial_number =  args['device_serial_number']
            testRecord.device_model =  args['device_model']
            testRecord.mti_test_instrument =  args['mti_test_instrument']
            testRecord.mti_serial_number =  args['mti_serial_number']
            testRecord.mti_firmware_version =  args['mti_firmware_version']
            try:
                db.session.commit()
            except SQLAlchemyError as e:
                abort(204, error=True, message=e)

            if('testResults' in args and str(args['testResults'])!="None"):
                trString = args['testResults'].replace("'",'"')
                testResultArgs = json.loads(trString)
                testResultId = testResultArgs['test_result_id']
                if(testResultId):
                    testResult = TestResultModel.query.filter_by(test_result_id=testResultId, test_record_id=testRecord.test_record_id).first()
                    if(testResult):
                        testResult.test_element =  testResultArgs['test_element']
                        testResult.test_type =  testResultArgs['test_type']
                        testResult.procedure =  testResultArgs['procedure']
                        try:
                            db.session.commit()
                        except SQLAlchemyError as e:
                            message = e
                if("testResultItems" in testResultArgs and str(testResultArgs['testResultItems'])!="None" and testResult.test_result_id):
                    tritemString = testResultArgs['testResultItems']
                    # testResultItems = json.loads(tritemString)
                    if(tritemString):
                        for tri in tritemString:
                            testResultItem = TestResultItemModel(test_result_id = testResult.test_result_id, 
                                            result = tri['result'], 
                                            value = tri['value'],
                                            unit = tri['unit'],
                                            high_limit = tri['high_limit'],
                                            low_limit = tri['low_limit'],
                                            standard =  tri['standard'])
                            db.session.add(testResultItem)
                            try:
                                db.session.commit()
                            except SQLAlchemyError as e:
                                message = e
            
                        
        if(not updateError):
            return testRecord, 200


    def delete(self, test_record_id):
        testRecord = TestRecordModel.query.filter_by(test_record_id=test_record_id).first()
        if not testRecord:
            abort(404, error=True, message=('Não foi possível encontrar TestRecord com id = {}').format(test_record_id))
        else:
            db.session.delete(testRecord)
            try:
                db.session.commit()
            except SQLAlchemyError as e:
                abort(404, error=True, message=e)
        # Se a exclusão for bem-sucedida, responder com código HTTP 204 
        return  "TestRecord excluído com sucesso! ", 204


class EquipamentoAPI(Resource):

    @marshal_with(testRecord_resource_fields)
    def post(self):
        args = testRecordArgs.parse_args()
            
        testRecord = TestRecordModel(status=args['status'], date=args['date'], record=args['record'], 
                                template=args['template'], device_serial_number=args['device_serial_number'], 
                                device_model=args['device_model'], mti_test_instrument = args['mti_test_instrument'],
                                mti_serial_number = args['mti_serial_number'], mti_firmware_version = args['mti_firmware_version'])
        db.session.add(testRecord)
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            # Executa algum processamento, mas não cria um novo recurso, retorna o código 200 e inclui o resultado da operação no corpo da resposta.
            return testRecord, 200
        
        if('testResults' in args and str(args['testResults'])!="None"):
            trString = args['testResults'].replace("'",'"')
            testResultArgs = json.loads(trString)
            if(testResultArgs):
                testResult = TestResultModel(test_record_id = testRecord.test_record_id, 
                                test_element = testResultArgs['test_element'], 
                                test_type = testResultArgs['test_type'],
                                procedure =  testResultArgs['procedure'])
                db.session.add(testResult)
                try:
                    db.session.commit()
                except SQLAlchemyError as e:
                    message = e
        
            if("testResultItems" in testResultArgs and str(testResultArgs['testResultItems'])!="None" and testResult.test_result_id):
                tritemString = testResultArgs['testResultItems']
                # testResultItems = json.loads(tritemString)
                if(tritemString):
                    for tri in tritemString:
                        testResultItem = TestResultItemModel(test_result_id = testResult.test_result_id, 
                                        result = tri['result'], 
                                        value = tri['value'],
                                        unit = tri['unit'],
                                        high_limit = tri['high_limit'],
                                        low_limit = tri['low_limit'],
                                        standard =  tri['standard'])
                        db.session.add(testResultItem)
                        try:
                            db.session.commit()
                        except SQLAlchemyError as e:
                            message = e
        

        #Se um método POST cria um novo recurso, ele retornará o código de status HTTP 201 (Criado).
        return testRecord,201


api.add_resource(EquipamentosAPI, '/equipamentos/<string:test_record_id>', endpoint='TestRecords')
api.add_resource(EquipamentoAPI, '/equipamentos/', endpoint='TestRecord')

@app.errorhandler(404)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 404

@app.errorhandler(405)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 405


if __name__ == '__main__':
    app.run(debug=True) 