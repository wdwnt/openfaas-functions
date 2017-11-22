import requests
import json


def handle(req):
    r = requests.get(
        'https://assets.adobedtm.com/b213090c5204bf94318f4ef0539a38b487d10368/scripts/satellite-546fba5c3765610015fd0200.json'
    )
    disney_json = json.loads(r.text)
    for msg in disney_json['messages']:
        if msg['messageId'] == '505a54e3-6a21-40e6-a40b-06c68e3d5a9b':
            for trigger in msg['triggers']:
                if trigger['key'] == 'page.detailname' and trigger['matches'] != 'nc':
                    print json.dumps(trigger['values'])