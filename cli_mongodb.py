import os
import sys
import optparse
import json
import pymongo
import ConfigParser
from datetime import datetime
import uuid
import utils

__date__ = '2014-08-20'
__updated__ = '2014-08-20'

command_list = ['cloud-scale-up','cloud-scale-up-complete']

def message(msg):
	print msg
	return 0
	
def dispatch(options,args):	
	#The json file scenario
	"""
	file_path = os.path.dirname(os.path.abspath(__file__)) # os.getcwd()	
	json_file = os.path.join(file_path,options.filename)
	json_data = json.load(open(json_file))	# with statement
	"""

	if args[0] not in command_list:
		msg="You do not type the command cloud_scale_up correctly"
		message(msg)
	json_data = {"ci_id":options.ci_id,"effective_date":options.effective_date}
	cloud_items = [options.items]
	cloud_items.extend(args)
	scale_items = []
	for item in cloud_items:
		if item:
			list_item = item.split(":") # take consideration of regular expression to support more delimiters
			if len(list_item)==2:
				cloud_item = {"subcomponent_id":list_item[0],"quantity":list_item[1]}
				scale_items.append(cloud_item)
	if len(scale_items) > 0:
		json_data['items'] = scale_items
	if len(json_data) != 3:
		msg="The command line needs three parameters: ci_id,effective_date and items"
		message(msg)
	return command_db_operation(json_data)


	
def command_db_operation(json_data):	
	config_file = "cli.config"
	config = ConfigParser.ConfigParser()   
	file_path = os.path.dirname(os.path.abspath(__file__))
	config_file = os.path.join(file_path,config_file)
	config.readfp(open(config_file), "r")
	connection_parameters = config.get("database", "connection")
	client = pymongo.MongoClient(connection_parameters,connectTimeoutMS=5000)
	db = client['deployment']
	c_cloud_instances = db['cloud_instances']
	c_subscription_audit_trail = db['subscription_audit_trail']
	instance_id = json_data['ci_id'].upper()	
	cloud_instance = c_cloud_instances.find_one({"_id": instance_id})	
	if cloud_instance is None:
		client.close()
		msg = "The cloud instance can not be found by your provided cloud id"
		return message(msg)	
	c_subscription = db['subscription']	
	subscription = c_subscription.find_one({"_id":instance_id})
	if subscription is None:
		client.close()
		msg = "The subscription record is not existed"
		return message(msg)
	#check the service request status, the decide whether to add new record
	service_requests = subscription['service_requests']
	request_id = str(uuid.uuid4())
	effective_date = datetime.strptime(json_data['effective_date'],'%Y-%m-%d')
	requests = {"_id":request_id,"service_request_type":"scale_up_cloud","service_request_items":json_data['items'],"service_request_status":"request","process_history":[{"service_request_status":"request","effective_ts":str(effective_date),"process_ts":str(datetime.now()),"process_by":"CBO"}]}
	d_audit_trail = {"_id":str(uuid.uuid4()),"subscription_id":instance_id,"process_ts":str(datetime.now()),"process_by":"CBO","process_type":"scale_up_cloud","subscription_old_copy":subscription}
	if service_requests is None:
		c_subscription_audit_trail.insert(d_audit_trail)
		subscription['service_requests'] = requests
		c_subscription.save(subscription)	
		client.close()
		return request_id
	list_status = []
	for req in service_requests:
		list_status.append(req["service_request_status"])
	if "request" in list_status:
		client.close()
		msg = "There are pending request list.Please request after they are complete"
		return message(msg)
	
	c_subscription_audit_trail.insert(d_audit_trail)
	service_requests.append(requests)
	subscription['service_requests'] = service_requests
	c_subscription.save(subscription)
	client.close()
	return request_id
	
	
def main():
	argv = sys.argv[1:]

	program_name = os.path.basename(sys.argv[0])
	program_usage = 'Usage: %prog --ci_id CI4 --effective_date 2014-08-20 --items "ENTERPRISE_CLOUD_BASE:2" "ENTERPRISE_CLOUD_COMPUTE:2" '
	program_version = "v0.1"
	program_build_date = "%s" % __updated__
	program_version_string = '%%prog %s (%s)' % (program_version, program_build_date)
	program_longdesc = 'This command line is used to scale up the cloud instance'
	program_license = "Copyright 2014 WonderFan"

	parser = optparse.OptionParser(usage=program_usage,version=program_version_string, epilog=program_longdesc, description=program_license,prog=program_name)
	parser.add_option("-?", action="help", help=optparse.SUPPRESS_HELP)
	parser.add_option("-c", "--ci_id", dest="ci_id", metavar="ID", help="cloud instance ID")
	parser.add_option("-e", "--effective_date", dest="effective_date", metavar="DATE", help="effective date")
	parser.add_option("-i","--items",dest="items",metavar="ITEMS",help="subcomponent and its quantity")

	
	if len(sys.argv)==1:
		parser.print_help()
	else:
		(options, args) = parser.parse_args() #option is object type and args is list type		
		return dispatch(options, args)	


class ScaleUpCommand(object):
	
	
	def __init__(self,opts, args,parser):		
		self.parser = parser
		self.options = opts
		self.args = args
		self.json_data = None
    
	def validateArgs(self):    	
		if self.args[0] not in command_list:
			msg="You do not type the command cloud_scale_up correctly"
			message(msg)
		self.json_data = {"ci_id":self.options.id,"effective_date":self.options.effective_date}
		cloud_items = self.options.items.split(',')		
		scale_items = []
		for item in cloud_items:
			if item:
				list_item = item.split(":") # take consideration of regular expression to support more delimiters
				if len(list_item)==2:
					cloud_item = {"subcomponent_id":list_item[0],"quantity":list_item[1]}
					scale_items.append(cloud_item)
		if len(scale_items) > 0:
			self.json_data['items'] = scale_items
		if len(self.json_data) != 3:
			msg="The command line needs three parameters: ci_id,effective_date and items"
			message(msg)
    	
	def processCommand(self):
		db = utils.getDatabase()
		c_cloud_instances = db['cloud_instances']
		c_subscription_audit_trail = db['subscription_audit_trail']
		instance_id = self.json_data['ci_id'].upper()	
		cloud_instance = c_cloud_instances.find_one({"_id": instance_id})	
		if cloud_instance is None:
			db.connection.close()
			msg = "The cloud instance can not be found by your provided cloud id"
			return message(msg)	
		c_subscription = db['subscription']	
		subscription = c_subscription.find_one({"_id":instance_id})
		if subscription is None:
			db.connection.close()
			msg = "The subscription record is not existed"
			return message(msg)
		#check the service request status, the decide whether to add new record
		service_requests = subscription['service_requests']
		request_id = str(uuid.uuid4())
		effective_date = datetime.strptime(self.json_data['effective_date'],'%Y-%m-%d')
		requests = {"_id":request_id,"service_request_type":"scale_up_cloud","service_request_items":self.json_data['items'],"service_request_status":"request","process_history":[{"service_request_status":"request","effective_ts":str(effective_date),"process_ts":str(datetime.now()),"process_by":"CBO"}]}
		d_audit_trail = {"_id":str(uuid.uuid4()),"subscription_id":instance_id,"process_ts":str(datetime.now()),"process_by":"CBO","process_type":"scale_up_cloud","subscription_old_copy":subscription}
		if service_requests is None:
			c_subscription_audit_trail.insert(d_audit_trail)
			subscription['service_requests'] = requests
			c_subscription.save(subscription)	
			db.connection.close()
			return request_id
		list_status = []
		for req in service_requests:
			list_status.append(req["service_request_status"])
		if "request" in list_status:
			db.connection.close()
			msg = "There are pending request list.Please request after they are complete"
			return message(msg)
		
		c_subscription_audit_trail.insert(d_audit_trail)
		service_requests.append(requests)
		subscription['service_requests'] = service_requests
		c_subscription.save(subscription)
		db.connection.close()
		return request_id



    
