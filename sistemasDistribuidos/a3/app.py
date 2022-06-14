from doctest import TestResults
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

testResultArgs = reqparse.RequestParser()
testResultArgs.add_argument("test_record_id", type=str, help='O campo test_record_id deve ser informado',required=True)
testResultArgs.add_argument("test_element", type=str, required=False)
testResultArgs.add_argument("test_type", type=str, required=False)
testResultArgs.add_argument("procedure", type=str, required=False)
testResultArgs.add_argument("testResultItems", type=str, required=False)

testResultItemArgs = reqparse.RequestParser()
testResultItemArgs.add_argument("test_result_id",  type=str, help='O campo test_result_id deve ser informado',required=True)
testResultItemArgs.add_argument("result", type=str, required=False)
testResultItemArgs.add_argument("value", type=str, required=False)
testResultItemArgs.add_argument("unit", type=str, required=False)
testResultItemArgs.add_argument("high_limit", type=str, required=False)
testResultItemArgs.add_argument("low_limit", type=str, required=False)
testResultItemArgs.add_argument("standard", type=str, required=False)

testResultItem_resource_fields = {
    'test_result_id' : fields.Integer,
    'test_result_item_id' : fields.Integer,
    'result' : fields.String,
    'value' : fields.Float,
    'unit' : fields.String,
    'high_limit' : fields.Float,
    'low_limit' : fields.Float,
    'standard' : fields.String,
    # 'uri' : fields.Url('TestResultItems', absolute=True) ,
}

testResult_resource_fields = {
    'test_record_id' : fields.Integer,
    'test_result_id' : fields.Integer,
    'test_element' : fields.String,
    'test_type'   : fields.String,
    'procedure' : fields.String,
    'testResultItems' : fields.List(fields.Nested(testResultItem_resource_fields)),
    'uri' : fields.Url('TestResult', absolute=True) ,
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

class TestResultsAPI(Resource):
    @marshal_with(testResult_resource_fields)
    def get(self, test_result_id):
        test_result_id = int(test_result_id)
        if(test_result_id==0):
            testResults = TestResultModel.query.all()
            if not testResults:
                # Se o recurso não puder ser encontrado, o método deve retornar 404 (Não encontrado)
                abort(404, error=True, message=('Não existem registros de TestResult'))
        else:
            testResults = TestResultModel.query.filter_by(test_result_id=test_result_id).all()
            if not testResults:
                # Se o recurso não puder ser encontrado, o método deve retornar 404 (Não encontrado)
                abort(404, error=True, message=('Não foi possível encontrar TestResult com id = {}').format(test_result_id))

        # Um método GET bem-sucedido retorna o código de status HTTP 200(OK).
        return testResults, 200

    @marshal_with(testResult_resource_fields)
    def put(self, test_result_id):
        args = testResultArgs.parse_args()
        testResult = TestResultModel.query.filter_by(test_result_id=test_result_id).first()
        if not testResult:
            abort(409, error=True, message=('Não foi possível encontrar TestResult com id = {}').format(test_result_id))
        else:
            if args['test_record_id']!="":
                testRecordId = int(args['test_record_id'])
                if(testRecordId==0):
                    abort(409, error=True, message=('Não foi possível encontrar um registro de TestRecord associado ao id = {}').format(test_result_id))
                else:
                    testRecord = TestRecordModel.query.filter_by(test_record_id=testRecordId).first()
                    if(testRecord):
                        testResult.test_record_id = testRecordId            
                        testResult.test_element =  args['test_element']
                        testResult.test_type =  args['test_type']
                        testResult.procedure =  args['procedure']
                        try:
                            db.session.commit()
                        except SQLAlchemyError as e:
                            db.session.rollback()
                            abort(204, error=True,message = e)
                    else:
                        abort(409, error=True, message=('O valor de test_record_id é inválido. Não foi possível encontrar um registro de TestRecord associado ao id = {}').format(test_result_id))
                                           
            if("testResultItems" in args and str(args['testResultItems'])!="None"):
                tritemString = args['testResultItems'].replace("'",'"')
                testResultItems = json.loads(tritemString)
                if('test_result_item_id' in testResultItems):
                    test_result_item_id = testResultItems['test_result_item_id']
                    if(test_result_item_id):
                        testResultItem = TestResultItemModel.query.filter_by(test_result_item_id = test_result_item_id).first()
                        if(testResultItem):
                            testResultItem.result = testResultItems['result']
                            testResultItem.value = testResultItems['value']
                            testResultItem.unit = testResultItems['unit']
                            testResultItem.high_limit = testResultItems['high_limit']
                            testResultItem.low_limit = testResultItems['low_limit']
                            testResultItem.standard =  testResultItems['standard']
                            try:
                                db.session.commit()
                            except SQLAlchemyError as e:
                                message = e
                
            return testResult, 200

    def delete(self, test_result_id):
        testResult = TestResultModel.query.filter_by(test_result_id=test_result_id).first()
        if not testResult:
            abort(404, error=True, message=('Não existem TestResults associados ao id = {}').format(test_result_id))
        else:
            db.session.delete(testResult)
            try:
                db.session.commit()
            except SQLAlchemyError as e:
                app.logger.error(e)
                db.session.rollback()
            else:
                # Se a exclusão for bem-sucedida, responder com código HTTP 204 
                return  "TestRecord excluído com sucesso! ", 204

class TestResultAPI(Resource):
    @marshal_with(testResult_resource_fields)
    def post(self):
        args = testResultArgs.parse_args()
        if('test_record_id' in args):
            testRecordId = args['test_record_id']
            if(testRecordId):
                testRecord = TestRecordModel.query.filter_by(test_record_id=testRecordId    ).first()
                if not testRecord:
                    abort(404, error=True, message=('Você informou um valor inválido para testRecordID. Não existem registros de TestRecord associados ao id = {}').format(testRecordId))
                else:
                    testResult = TestResultModel(test_record_id=args['test_record_id'], test_element = args['test_element'],
                                                test_type = args['test_type'], procedure = args['procedure'])
                    try:
                        db.session.add(testResult)
                        db.session.commit()
                    except SQLAlchemyError as e:
                        app.logger.error(e)
                        db.session.rollback()
                        # Executa algum processamento, mas não cria um novo recurso, retorna o código 200 e inclui o resultado da operação no corpo da resposta.
                        return e, testResult, 200


                    if("testResultItems" in args):
                        tritemString = args['testResultItems'].replace("'",'"')
                        triArgs = json.loads(tritemString)
                        if(triArgs):
                            testResultItem = TestResultItemModel(test_result_id=testResult.test_result_id,
                                                result = triArgs['result'], value = triArgs['value'],
                                                unit = triArgs['unit'], high_limit = triArgs['high_limit'],
                                                low_limit = triArgs['low_limit'],standard =  triArgs['standard'])
                            try:
                                db.session.add(testResultItem)  
                                db.session.commit()
                            except SQLAlchemyError as e:
                                app.logger.error(e)
                                db.session.rollback()
                                
        # Se um método POST cria um novo recurso, ele retornará o código de status HTTP 201 (Criado)
        return testResult, 201

class TestResultItemsAPI(Resource):
    @marshal_with(testResultItem_resource_fields)
    def get(self, test_result_item_id):
        test_result_item_id = int(test_result_item_id)
        if(test_result_item_id==0):
            testResultItems = TestResultItemModel.query.all()
            if not testResultItems:
                # Se o recurso não puder ser encontrado, o método deve retornar 404 (Não encontrado)
                abort(404, error=True, message=('Não existem registros de TestResultItem'))
        else:
            testResultItems = TestResultItemModel.query.filter_by(test_result_item_id=test_result_item_id).first()

        if not testResultItems:
            # Se o recurso não puder ser encontrado, o método deve retornar 404 (Não encontrado)
            abort(404, error=True, message=('Não foi possível encontrar TestResultItem com id = {}').format(test_result_item_id))
        else:
            # Um método GET bem-sucedido retorna o código de status HTTP 200(OK).
            return testResultItems, 200    

    @marshal_with(testResultItem_resource_fields)
    def put(self, test_result_item_id):
        args = testResultItemArgs.parse_args()
        testResultItem = TestResultItemModel.query.filter_by(test_result_item_id=test_result_item_id).first()
        if not testResultItem:
            #  Se o método atualiza um recurso existente, retorna 200 (OK) ou 204 (Sem conteúdo).
            abort(404, error=True, message=('Não foi possível encontrar TestResultItem com id = {}').format(test_result_item_id))
        else:
            if('test_result_id' in args and args['test_result_id']!=None):
                testResultId = int(args['test_result_id'])
                if(testResultId!=0):
                    testResult = TestResultModel.query.filter_by(test_result_id=testResultId).first()
                    if(testResult):
                        testResultItem.test_result_id = testResultId
                    else:
                        # Não foi possível atualizar recurso, retornar o código de status HTTP 409 (Conflito)
                        abort(409, error=True, message=('test_result_id inválido. Não foi possível encontrar TestResult com id = {}').format(testResultId))
            
            if args['result']!=None and args['result']!="":
                testResultItem.result =  args['result']
            if args['value']!=None and args['value']!="":
                testResultItem.value =  args['value']
            if args['unit']!=None and args['unit']!="":
                testResultItem.unit =  args['unit']
            if args['high_limit']!=None and args['high_limit']!="":
                testResultItem.high_limit =  args['high_limit']
            if args['low_limit']!=None and args['low_limit']!="":
                testResultItem.low_limit =  args['low_limit']
            if args['standard']!=None and args['standard']!="":
                testResultItem.standard =  args['standard']
            try:
                db.session.commit()
            except SQLAlchemyError as e:
                db.session.rollback()
                abort(409, error=True,message = e)
            else:
                return testResultItem, 200

    def delete(self, test_result_item_id):
        triId = int(test_result_item_id)
        if(triId!=0):
            testResultItem = TestResultItemModel.query.filter_by(test_result_item_id=triId).first()
            if not testResultItem:
                abort(404, error=True, message=('Não foi possível encontrar TestResultItem com id = {}').format(triId))
            else:
                db.session.delete(testResultItem)
                try:
                    db.session.commit()
                except SQLAlchemyError as e:
                    db.session.rollback()
                    abort(404, error=True, message=e)
                else:
                    # Se a exclusão for bem-sucedida, responder com código HTTP 204 
                    return  "TestResultItem excluído com sucesso! ", 204

        else:
            abort(404, error=True, message="Favor informar um id válido")

class TestResultItemAPI(Resource):
    @marshal_with(testResultItem_resource_fields)
    def post(self):
        args = testResultItemArgs.parse_args()
        if('test_result_id' in args and args['test_result_id']!=""):
            testResultId = int(args['test_result_id'])
            if(testResultId!=0):
                testResult = TestResultModel.query.filter_by(test_result_id=testResultId).first()
                if not testResult:
                    # Dados inválidos na solicitação, retornar o código de status HTTP 400 (Solicitação incorreta)
                    abort(400, error=True, message=('Você informou um valor inválido para test_result_id. Não existem registros de TestResult associados ao id = {}').format(testResultId))
                else:
                    testResultItem = TestResultItemModel(result=args['result'], value=args['value'],unit=args['unit'],
                                            high_limit=args['high_limit'],low_limit=args['low_limit'],
                                            standard=args['standard'], test_result_id = args['test_result_id'])
                    try:
                        db.session.add(testResultItem)
                        db.session.commit()
                    except SQLAlchemyError as e:
                        app.logger.error(e)
                        db.session.rollback()
                        # Executa algum processamento, mas não cria um novo recurso, retorna o código 200 e inclui o resultado da operação no corpo da resposta.
                        return e, testResultItem, 200
                    else:
                        # Se cria um novo recurso, retornar o código de status HTTP 201 (Criado)
                        return testResultItem, 201
            else:
                abort(400, error=True, message=('Você informou um valor inválido para test_result_id.'))

class EquipamentosAPI(Resource):
    @marshal_with(testRecord_resource_fields)
    def get(self, test_record_id):
        test_record_id = int(test_record_id)
        if(test_record_id==0):
            testRecords = TestRecordModel.query.all()
            if(testRecords):
                return testRecords, 200
            else:
                abort(404, error=True, message=('Não foi possível encontrar nenhum TestRecord'))
        else:
            testRecord = TestRecordModel.query.filter_by(test_record_id=test_record_id).first()
            if not testRecord:
                abort(404, error=True, message=('Não foi possível encontrar TestRecord com id = {}').format(test_record_id))
            else:
                return testRecord, 200

    @marshal_with(testRecord_resource_fields)
    def put(self, test_record_id):
        args = testRecordArgs.parse_args()
        test_record_id = int(test_record_id)
        testRecord = TestRecordModel.query.filter_by(test_record_id=test_record_id).first()
        if not testRecord:
            #  Se o método atualiza um recurso existente, retorna 200 (OK) ou 204 (Sem conteúdo).
            abort(204, error=True, message=("Não foi possível encontrar TestRecord com id = {}").format(test_record_id))
        else:
            if args['status']!=None and args['status']!="":
                testRecord.status =  args['status']
            if args['date']!=None and args['date']!="":
                testRecord.date =  args['date']
            if args['device_serial_number']!=None and args['device_serial_number']!="":
                testRecord.device_serial_number =  args['device_serial_number']
            if args['record']!=None:
                testRecord.record =  args['record']
            if args['template']!=None:
                testRecord.template =  args['template']
            if args['device_model']!=None:
                testRecord.device_model =  args['device_model']
            if args['mti_test_instrument']!=None:
                testRecord.mti_test_instrument =  args['mti_test_instrument']
            if args['mti_serial_number']!=None:
                testRecord.mti_serial_number =  args['mti_serial_number']
            if args['mti_firmware_version']!=None:
                testRecord.mti_firmware_version =  args['mti_firmware_version']
            try:
                db.session.commit()
            except SQLAlchemyError as e:
                db.session.rollback()
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
                            db.session.rollback()

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
                db.session.rollback()
                abort(404, error=True, message=e)
            else:
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
api.add_resource(TestResultsAPI, '/testresults/<string:test_result_id>', endpoint='TestResults')
api.add_resource(TestResultAPI, '/testresults/', endpoint='TestResult')
api.add_resource(TestResultItemsAPI, '/testresultitems/<string:test_result_item_id>', endpoint='TestResultItems')
api.add_resource(TestResultItemAPI, '/testresultitems/', endpoint='TestResultItem')


@app.errorhandler(404)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 404


@app.errorhandler(405)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 405


if __name__ == '__main__':
    app.run(debug=True)     