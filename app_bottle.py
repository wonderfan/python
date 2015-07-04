from bottle import route, run,request, response
# route is used to mapp the url to controller function
# request is used to get the request parameter and data
# response is used as the return result after request processing
# run is used to start the http server and request handler
import os
import json
import pprint

@route('/home', method='POST')
def home():
	file_path = os.path.dirname(os.path.abspath(__file__))
	file_name = file_path + "/config.xml"
	file = open(file_name, 'w')
	#pp = pprint.PrettyPrinter(depth=6)
	#pp.pprint(request.forms.allitems());	
	file.write('<?xml version="1.0"?> \n');
	file.write('<hmpc_setup> \n');
	isrvce = [];
	filewall = [];
	dnat = [];
	snat = [];
	new_data = {}
	for key in request.forms.allitems():
		if key[0] in new_data:
			orig = new_data[key[0]]
			if type(orig) is list :
				orig.append(key[1])
			else:
				temp = [orig,key[1]]
				orig = temp
				
			new_data[key[0]] = orig
		else:
			new_data[key[0]] = key[1]
		
	
	print new_data
	
	for key in new_data:
		if key.find('isrvce') > 1:
			data = new_data[key]
			print key
			print data
			user = {"firstname":data[0],"lastname":data[1],"email":data[2],"workphone":data[3],"cellphone":data[4],"jobtitle":data[5],"mirrorlogin":data[6],"rolegroups":data[7]};
			isrvce.append(user)
			continue;
	
		file.write('\t')
		file.write('<' + key + '>' + new_data[key] + '</'+key+'>')
		file.write('\n')
	
	file.write('\t<isrvce> \n');
	for item in isrvce:
		file.write('\t\t <user> \n')
		for p in item:
			file.write('\t\t\t');
			file.write('<' + p + '>' + item[p] + '</'+p+'>');
			file.write('\n');		
		file.write('\t\t </user> \n')
	file.write('\t</isrvce> \n');
	file.write('</hmpc_setup>');
	file.close()
	result = '<!DOCTYPE html><html><head><title>Private Cloud Settings</title><link rel="stylesheet" href="css/style.css"></head><body><div class="alert alert-success"><strong>Success! </strong> You have successfully configurated your private cloud. Click <a href="index.html">here</a> to go back.</div></body></html>'
	return result


@route('/data')
def init_data():
	file_path = os.path.dirname(os.path.abspath(__file__))
	file_name = file_path + "/config.xml"	
	result = None
	if os.path.exists(file_name) :
		fo = open(file_name, "r+")
		result = fo.read();
		fo.close()
	else:
		result = '<?xml version="1.0"?> <hmpc_setup> </hmpc_setup>'
	response.content_type = 'application/xml'	
	response.add_header("Access-Control-Allow-Origin", "*"); 	
	return result


run(host='localhost', port=8000, debug=True)

