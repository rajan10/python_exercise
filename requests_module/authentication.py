import requests
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('user', 'pass')
authentication = requests.get('https://httpbin.org/basic-auth/user/pass', auth =  basic)
print(authentication)
