import json
import urllib
import urllib2


def query(url, payload):
    url = 'https://api.quickquest.ru/stock/'+url
    data = json.dumps(payload)

    request = urllib2.Request(url, data)
    request.add_header('Authorization', 'Token 2222222222222222222222222222222222222222')
    
    try:
        answer = json.loads(urllib2.urlopen(request).read())
        code = 200
    except urllib2.HTTPError as e:
        code = e.code
        answer = ''
    return_array = {"data": answer, "http_code": code}
    return return_array

payload = {
    "number_card": "123123123"    
}
return_query = query("read_card", payload)
print(return_query)