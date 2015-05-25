""" class variable """

class Test(object):
    name = "wh"
    
    def __init__(self,name):
        self.name = name
    
    def get_instance_name(self):
        print '*'*5
        print self.name
        
    def get_class_name(self):
        print '-'*5
        print self.__class__.name
    
    def __private_method(self):
        print '@' * 10
        
    def __call__(self):
        print '#' * 20    
    
if __name__ == '__main__':
    
    print dir(Test)
    print Test.name
    instance = Test('sh')
    print dir(instance)
    instance.__call__()
    instance.get_instance_name()
    instance.get_class_name()
            
    
