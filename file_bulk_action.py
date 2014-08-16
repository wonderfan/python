import os
import string


def task(source,target):    
    files = os.listdir(source)
    target_files = {}
    
    for source_file in files:
        if source_file.endswith('.java'):
            file_list = source_file.split('.')
            new_file = file_list[0]+'Test.java'
            new_class = file_list[0]+'Test'
            target_files.update({new_class:new_file})
            
    for new_class,target_file in target_files.items():
        absolute_file = target + target_file
        file_stream = open(absolute_file,'a')        
        code_template = '''
        public class $class {
            
            @Test
            public void test$source(){
            
            }
                                    
        }                        
        '''        
        t = string.Template(code_template)
        file_stream.write(t.substitute({'class':new_class,'source':new_class.strip('Test')}));
        file_stream.close()      

if __name__ == '__main__':
    print 'The task starts'
    source_directory = 'F:\eclipse\workspace\ZenJava\src\main\java\com\wonderfan\\'
    target_directory = 'F:\eclipse\workspace\ZenJava\src\test\java\com\wonderfan\\'
    task(source_directory,target_directory)
    print 'The task is over'
