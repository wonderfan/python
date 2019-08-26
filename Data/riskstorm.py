# -*- encoding:utf-8 -*-
import requests

def exe_query(uid):
    api_url = 'https://data.riskstorm.com/v1/company/%s' % uid
    headers = {'apikey': 'i4NgBZCAV6JwUrIQ0CD7ww'}
    params = {'size': 10}
    try:
        response = requests.get(url=api_url, headers=headers, params=params)
        print(response.text)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print('-*- start -*-')
    uid = '913300002539329145'
    exe_query(uid)
    print('-*- end -*-')
