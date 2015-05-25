import json
import platform
import os
import base64
import subprocess
import xmltodict


def main(file_name):
    if not os.path.exists(file_name):
        print 'The file does not exist'        
    else:
        try:
            json_object = json.load(open(file_name))
        except ValueError as e:
            print e
            if platform.system() == 'Linux':
                file_type = subprocess.check_output(['file','-b','--mime-type',file_name])
                file_type = file_type.strip()
                if 'text' in file_type:
                    with open(file_name) as fr:
                        content = fr.read()
                        json_object = {'type':file_type,'content':content}
                elif 'xml' in file_type:
                    with open(file_name) as fr:
                        content = fr.read()
                        json_object = xmltodict.parse(content)                  
                else:
                    with open(file_name,'rb') as fd:
                        content = base64.b64encode(fd.read())
                        json_object = {'type':file_type,'content':content}
            else:
                with open(file_name,'rb') as fd:
                    content = base64.b64encode(fd.read())
                    json_object = {'type':'None','content':content}
        print json_object
    
        
        
if __name__ == '__main__':
    file_name = 'config.xml'
    main(file_name)       
