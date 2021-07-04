import urllib.request, urllib.parse, urllib.error
import json
import api_keys as keys
import lang_detection as langDet
import os
import webbrowser

def connect_to_api(url) :
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", keys.file_trans('client_id'))
    request.add_header("X-Naver-Client-Secret", keys.file_trans('client_secret'))
    return request

def get_translation(file, filetype, request, source_language, target_language) :


    if filetype == 'json' :

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

    elif filetype == 'txt' :

        if source_language == '1' :
            source_language = langDet.getLangCode(file)

        encoded_text = urllib.parse.quote(file)
        data = 'source=' + source_language.lower() + '&target=' + target_language.lower() + '&text=' + encoded_text
        response = urllib.request.urlopen(request, data = data.encode("utf-8"))
        rescode = response.getcode()

        if(rescode==200):
            response_body = response.read()
            response_json = json.loads(response_body.decode('utf-8'))
            translations = response_json['message']['result']['translatedText']
        else:
            print("Error Code:" + rescode)

        return translations

def generate_file(translations, filetype) :

    if filetype == 'json' :

        # Generate JSON File from Results
        translations_export = {}
        translations_export['srcLangType'] = translations_export.get('srcLangType', translations[1])
        translations_export['tarLangType'] = translations_export.get('tarLangType', targLanguage)
        translations_export['translations'] = translations_export.get('translations', translations[0])

        with open('translations.json', 'w', encoding = 'utf-8') as translations_file:
            json.dump(
            translations_export,
            translations_file,
            ensure_ascii = False,
            indent = 4)

        # Open Translations JSON File
        osCommandString = 'notepad.exe translations.json'
        os.system(osCommandString)
        os._exit(0)

    elif filetype == 'txt' :

        # Generate TXT File from results
        with open('translations.txt', 'w', encoding = 'utf-8') as translations_file:
            translations_file.write(translations)

        # Open Translations TXT File
        osCommandString = 'notepad.exe translations.txt'
        os.system(osCommandString)
        os._exit(0)
    return

# Read JSON file
file_name = input('Filename: ')

s_file_name = file_name.split('.')

with open(file_name, encoding='UTF-8') as file_handle :
    if s_file_name[1] == 'json' :
        file = json.load(file_handle)
    elif s_file_name[1] == 'txt' :
        file = file_handle.read().replace('\n', '')

file_type = s_file_name[1]
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
translations = get_translation(file, file_type, request, srcLanguage, targLanguage)
print('Translation successful.')

generate_file(translations, file_type)

"""
# Print Results
print('\nResults:')
for source, translation in translations.items() :
    print(source, '=', translation)
"""
