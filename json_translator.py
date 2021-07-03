import urllib.request, urllib.parse, urllib.error
import json
import api_keys as keys
import lang_detection as langDet
import os
import webbrowser

def connect_to_api(url) :
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", keys.file_trans_keys('client_id'))
    request.add_header("X-Naver-Client-Secret", keys.file_trans_keys('client_secret'))
    return request

def get_translation(file, request, source_language, target_language) :

    translations = {}

    for word in file['words'] :

        if source_language == '1' :
            source_language = langDet.getLangCode(word)

        encoded_text = urllib.parse.quote(word)
        data = 'source=' + source_language.lower() + '&target=' + target_language.lower() + '&text=' + encoded_text
        response = urllib.request.urlopen(request, data = data.encode("utf-8"))
        rescode = response.getcode()

        if(rescode==200):
            response_body = response.read()
            response_json = json.loads(response_body.decode('utf-8'))
            translation = response_json['message']['result']['translatedText']
            translations[word] = translations.get(word, translation)
        else:
            print("Error Code:" + rescode)

    return (translations, source_language)

def generate_file(translations) :

    # Generate JSON File from Results
    translations_export = {}
    translations_export['srcLangType'] = translations_export.get('srcLangType', translations[1])
    translations_export['tarLangType'] = translations_export.get('tarLangType', targLanguage)
    translations_export['translations'] = translations_export.get('translations', translations[0])

    with open('translations.json', 'w', encoding='utf-8') as translations_file:
        json.dump(
        translations_export,
        translations_file,
        ensure_ascii = False,
        indent = 4)

    # Open Translations JSON File
    osCommandString = 'notepad.exe translations.json'
    os.system(osCommandString)
    os._exit(0)

    return

# Read JSON file
file_name = input('Filename: ')
with open(file_name, encoding='UTF-8') as json_file :
    json_file = json.load(json_file)
print('Reading file', file_name)

"""
print('See browser for supported languages.')
webbrowser.open_new('https://bit.ly/2Tkq4f7')   # Open NAVER Translate Supported Languages
"""

# Language Input
srcLanguage = input("Source Language ('1' for auto-detect): ")
targLanguage = input('Target Language: ')

# Connect to API
print('Connecting to Papago Translation API...')
url = 'https://openapi.naver.com/v1/papago/n2mt'
request = connect_to_api(url)
print('Connected to API.')

# Translate
print('Translating...')
translations = get_translation(json_file, request, srcLanguage, targLanguage)
print('Translation successful.')

print(translations)
generate_file(translations)

"""
# Print Results
print('\nResults:')
for source, translation in translations.items() :
    print(source, '=', translation)
"""
