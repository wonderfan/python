from pymongo import MongoClient
from pymongo import MongoReplicaSetClient
from bson.objectid import ObjectId
from pymongo.read_preferences import ReadPreference
import base64
from bson.binary import Binary

def init_schema_data(db=None):
		
	collection_credential = db['credential']
	user = {"user_name":"wonderfan","role":"cloud_change_manager","user_password":"aq1sw2de"}
	collection_credential.insert(user)
	
	collection_subscription = db['subscription']
	subscription = {"ci_id":"abd","ci_short_name":"C14","ci_description":"development environment","offering_item":"LA_CLOUD","item_quality":"1","from_appdirect":"N","appdirect_account":"","appdirect_subscription_id":"","CFTS_customer_number":"","CFTS_country_code":"","CFTS_contract_number":"","CFTS_company_code":"","create_ts":"2014-08-15","start_billing_ts":"2014-08-15","end_billing_ts":""}
	collection_subscription.insert(subscription)
	
	collection_history = db['subscription_process_history']
	process_history = {"subscription_id":"","user_id":"","process_ts":"2014-08-15","process_type":"create_new_cloud_instance"}
	collection_history.insert(process_history)
	
	collection_cloud_instance = db['cloud_instance']
	cloud_instance = {"ci_short_name":"C14","ci_description":"development environment","change_manager_id":""}
	collection_cloud_instance.insert(cloud_instance)
	
	collection_check_point = db['check_point']
	check_point = {"check_ts":"2014-08-15","period_start_ts":"","period_end_ts":"","subscription_id":"","ci_id":"","ci_short_name":"","ci_description":"","offering_item":"LA_CLOUD","item_quantity":"1","from_appdirect":"N","appdirect_account":"","appdirect_subscription_id":"","CFTS_customer_number":"","CFTS_country_code":"","CFTS_contract_number":"","CFTS_company_code":"","start_billing_ts":"2014-08-15","end_billing_ts":"","period_usage_start_ts":"2014-08-15","period_usage_end_ts":"2014-09-15","period_usage_total":"31","period_usage_uom":"day"}
	collection_check_point.insert(check_point)
	
def db_operation(db=None):
	print "CRUD operations";
			
if __name__ == "__main__":
	
	import json
	
	print json.load(open('phone.png'))
	import sys
	sys.exit(0)
	
	print "Start the MongoDB connection"	
	flag = False
	client = MongoClient("127.0.0.1",27017)
	db = client['deployment_db']
	test = db.test
	record = test.find()
	file_name = 'test.xml'	
	with open(file_name,"rb") as fd:
		content = base64.b64encode(fd.read())
		record = {"_id":"test","date":"2014-10-15","data":content}
	ret_value =test.save(record)

	db_record = test.find_one({"_id":"test"})
	
	import json
	print json.dumps(db_record,indent=4)
	import sys
	sys.exit()
	
	with open("new.png","wb") as fw:
		fw.write(db_record['data'].decode('base64'))
		fw.close()


	"""
	print content	
	import xmltodict
	content = xmltodict.parse(content)
	print content
	"""
	

	
	"""
	if flag:
		init_schema_data(db)
	else:
		db_operation(db)
	"""	
	client.close()
	print "End the MongoDB connection"
