<<<<<<< HEAD
import urllib.request, urllib.parse, urllib.error
import ssl
import json
import api_keys as keys
import os
import webbrowser

# Read JSON file
file_name = input('Filename: ')
with open(file_name, encoding='UTF-8') as file_handle :
    json_file = json.load(file_handle)
print('Reading file', file_name)

# Connect to API
print('Connecting to Papago Translation API...')
print('See browser for supported languages.')
webbrowser.open_new('https://bit.ly/2Tkq4f7')
srcLanguage = input('Source Language: ')
targLanguage = input('Target Language: ')
url = 'https://openapi.naver.com/v1/papago/n2mt'
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", keys.client_keys('client_id'))
request.add_header("X-Naver-Client-Secret", keys.client_keys('client_secret'))
print('Connected to API.')

# Exchange data with API
translations = {}
print('Translating...')

for word in json_file['korean-words'] :
    encoded_text = urllib.parse.quote(word)
    data = 'source=' + srcLanguage.lower() + '&target=' + targLanguage.lower() + '&text=' + encoded_text
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        response_json = json.loads(response_body.decode('utf-8'))
        translation = response_json['message']['result']['translatedText']
        translations[word] = translations.get(word, translation)
    else:
        print("Error Code:" + rescode)

print('Translation successful.')

# Generate JSON File from Results
translations_export = {}
translations_export['srcLangType'] = translations_export.get('srcLangType', srcLanguage)
translations_export['tarLangType'] = translations_export.get('tarLangType', targLanguage)
translations_export['translations'] = translations_export.get('translations', translations)

with open('translations.json', 'w', encoding='utf-8') as translations_file:
    json.dump(
        translations_export,
        translations_file,
        ensure_ascii = False,
        indent = 4)

# Open Translations JSON File
osCommandString = 'notepad.exe translations.json'
os.system(osCommandString)
os._exit()

"""
# Print Results
print('\nResults:')
for source, translation in translations.items() :
    print(source, '=', translation)
"""
=======
import urllib.request, urllib.parse, urllib.error
import ssl
import json
import api_keys as keys
import os
import webbrowser

# Read JSON file
file_name = input('Filename: ')
with open(file_name, encoding='UTF-8') as file_handle :
    json_file = json.load(file_handle)
print('Reading file', file_name)

# Connect to API
print('Connecting to Papago Translation API...')
print('See browser for supported languages.')
webbrowser.open_new('https://bit.ly/2Tkq4f7')
srcLanguage = input('Source Language: ')
targLanguage = input('Target Language: ')
url = 'https://openapi.naver.com/v1/papago/n2mt'
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", keys.client_keys('client_id'))
request.add_header("X-Naver-Client-Secret", keys.client_keys('client_secret'))
print('Connected to API.')

# Exchange data with API
translations = {}
print('Translating...')

for word in json_file['korean-words'] :
    encoded_text = urllib.parse.quote(word)
    data = 'source=' + srcLanguage.lower() + '&target=' + targLanguage.lower() + '&text=' + encoded_text
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        response_json = json.loads(response_body.decode('utf-8'))
        translation = response_json['message']['result']['translatedText']
        translations[word] = translations.get(word, translation)
    else:
        print("Error Code:" + rescode)

print('Translation successful.')

# Generate JSON File from Results
translations_export = {}
translations_export['srcLangType'] = translations_export.get('srcLangType', srcLanguage)
translations_export['tarLangType'] = translations_export.get('tarLangType', targLanguage)
translations_export['translations'] = translations_export.get('translations', translations)

with open('translations.json', 'w', encoding='utf-8') as translations_file:
    json.dump(
        translations_export,
        translations_file,
        ensure_ascii = False,
        indent = 4)

# Open Translations JSON File
osCommandString = 'notepad.exe translations.json'
os.system(osCommandString)
os._exit()

"""
# Print Results
print('\nResults:')
for source, translation in translations.items() :
    print(source, '=', translation)
"""
>>>>>>> 9a6d365b086b23afd6c2d7f97c2dfa5eabeb3176
