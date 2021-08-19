import requests

### Edit these variables
message = 'Here are my screenshots of netacad-devasc skills-based exam'
###

# Gets access token from file
with open('token') as t:
    access_token = t.read()
    t.close()

with open('latest_room') as r:
    room_id = r.read()
    r.close()

# Posts a message in the room
url = 'https://webexapis.com/v1/messages'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)

if res.status_code == 200:
    print('The following message has been posted in the room:')
    print(res.json()['markdown'])
else:
    print(res.json())