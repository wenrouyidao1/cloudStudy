from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def registry():
    with open(file='registry.conf', mode='r', encoding='utf8') as file:
        results = json.loads(file.readline())
        result = requests.get(url=results['registry_IP'])
        str01 = '<table><thead><tr><th>' + '{:<20}'.format('REPOSITORIES') + '</th><th>' + '{:<30}'.format('TAGS') + '</th></tr></thead><tbody>'
        for element in result.json()['repositories']:
            result02 = requests.get(url=results['registry_TAGS'].format(element))
            data = result02.json()
            if len(data['tags']) == 1:
                str02 = '<tr><td>' + '{:<20}'.format(data['name'].upper()) + '</td><td>' + '{:<30}'.format(data['tags'][0]) + '</td></tr>'
                str01 += str02
            else:
                for index in range(len(data['tags'])):
                    str02 = '<tr><td>' + '{:<20}'.format(data['name'].upper()) + '</td><td>' +  '{:<30}'.format(data['tags'][index]) + '</td></tr>'
                    str01 += str02
        str01 += '</tbody></table>'
    return str01

if __name__ == '__main__':
    app.run(host='0.0.0.0')
