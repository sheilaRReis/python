from flask import Flask
from flask_restful import Resource, Api, abort, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

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


testRecordPostArgs = reqparse.RequestParser()
testRecordPostArgs.add_argument("status", type=str, help="O campo status deve ser informado", required=True)
testRecordPostArgs.add_argument("date", type=str, help="A data deve ser informada", required=True)
testRecordPostArgs.add_argument("record", type=str,  required=False)
testRecordPostArgs.add_argument("template", type=str,  required=False)
testRecordPostArgs.add_argument("device_serial_number", type=str, help="O campo device_serial_number é obrigatório!", required=True)
testRecordPostArgs.add_argument("device_model", type=str,  required=False)
testRecordPostArgs.add_argument("mti_test_instrument", type=str,  required=False)
testRecordPostArgs.add_argument("mti_serial_number", type=str,  required=False)
testRecordPostArgs.add_argument("mti_firmware_version", type=str,  required=False)
testRecordPostArgs.add_argument("testResults", type=str,  required=False)


testRecordUpdateArgs = reqparse.RequestParser()
testRecordUpdateArgs.add_argument("status", type=str, help="O campo status deve ser informado", required=True)
testRecordUpdateArgs.add_argument("date", type=str, help="A data deve ser informada", required=True)
testRecordUpdateArgs.add_argument("record", type=str,  required=False)
testRecordUpdateArgs.add_argument("template", type=str,  required=False)
testRecordUpdateArgs.add_argument("device_serial_number", type=str, help="O campo device_serial_number é obrigatório!", required=True)
testRecordUpdateArgs.add_argument("device_model", type=str,  required=False)
testRecordUpdateArgs.add_argument("mti_test_instrument", type=str,  required=False)
testRecordUpdateArgs.add_argument("mti_serial_number", type=str, required=False)
testRecordUpdateArgs.add_argument("mti_firmware_version", type=str,  required=False)


testResultItem_resource_fields = {
    'test_result_id' : fields.Integer,
    'test_result_item_id' : fields.Integer,
    'result' : fields.String,
    'value' : fields.Float,
    'high_limit' : fields.Float,
    'low_limit' : fields.Float,
    'standard' : fields.String,
}

testResult_resource_fields = {
    'test_record_id' : fields.Integer,
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
            return testRecords
        else:
            testRecord = TestRecordModel.query.filter_by(test_record_id=test_record_id).first()
            if not testRecord:
                abort(404, error=True, message=('Não foi possível encontrar TestRecord com id = {}').format(test_record_id))
            else:
                return testRecord


    @marshal_with(testRecord_resource_fields)
    def put(self, test_record_id):
        args = testRecordUpdateArgs.parse_args()
        testRecord = TestRecordModel.query.filter_by(test_record_id=test_record_id).first()
        if not testRecord:
            abort(404, error=True, message=('Não foi possível encontrar TestRecord com id = {}').format(test_record_id))
        else:
            if args['status']:
                testRecord.status =  args['status']
            if args['date']:
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
                abort(404, message = e)

        return testRecord


    def delete(self, test_record_id):
        testRecord = TestRecordModel.query.filter_by(test_record_id=test_record_id).first()
        if not testRecord:
            abort(404, message='TestRecord não encontrado')
        db.session.delete(testRecord)
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            abort(404)
        return  "TestRecord excluído com sucesso! ", 204


class EquipamentoAPI(Resource):
    
    @marshal_with(testRecord_resource_fields)
    def post(self):
        args = testRecordPostArgs.parse_args()
            
        testRecord = TestRecordModel(status=args['status'], date=args['date'], record=args['record'], 
                                template=args['template'], device_serial_number=args['device_serial_number'], 
                                device_model=args['device_model'], mti_test_instrument = args['mti_test_instrument'],
                                mti_serial_number = args['mti_serial_number'], mti_firmware_version = args['mti_firmware_version'])
        db.session.add(testRecord)
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            abort(404)

        return testRecord,201


api.add_resource(EquipamentosAPI, '/equipamentos/<string:test_record_id>', endpoint='TestRecords')
api.add_resource(EquipamentoAPI, '/equipamentos/', endpoint='TestRecord')

if __name__ == '__main__':
    app.run(debug=True) 