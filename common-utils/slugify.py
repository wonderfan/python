import re
import unicodedata

def generate_slug_value(base_text):
    base_text = unicode(base_text)
    value = unicodedata.normalize('NFKD', base_text).encode('ascii', 'ignore').decode('ascii')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    value = re.sub('[-\s]+', '-', value)
    return value    
    
    
if __name__ == '__main__':
    
    print generate_slug_value("this is my test")
