import urllib.request, urllib.parse, urllib.error
import api_keys as keys
import json

def getLangCode(text) :
    encoded_text = urllib.parse.quote(text)
    data = 'query=' + encoded_text
    url = 'https://openapi.naver.com/v1/papago/detectLangs'
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", keys.lang_det('client_id'))
    request.add_header("X-Naver-Client-Secret", keys.lang_det('client_secret'))
    response = urllib.request.urlopen(request, data = data.encode('UTF-8'))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        decoded_response = json.loads(response_body.decode('UTF-8'))
        return decoded_response['langCode']
    else:
        return ("Error Code:" + rescode)
