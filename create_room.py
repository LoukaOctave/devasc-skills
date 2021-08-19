import requests

### Edit these variables
room_name = 'netacad_devasc_skills_LO'
new_member_email = 'yvan.rooseleer@biasc.be'
###

# Gets access token from file
with open('token') as t:
    access_token = t.read()
    t.close()

# Created a room
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'title': room_name}
res = requests.post(url, headers=headers, json=params)

if res.status_code == 200:
    print('Room "' + res.json()['title'] + '" created')
    room_id = res.json()['id']
    with open('latest_room', 'w') as r:
        r.write(room_id)
else:
    print(res.json())
    room_id = ''

# Adds a user to that room
url = 'https://webexapis.com/v1/memberships'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': new_member_email}
res = requests.post(url, headers=headers, json=params)

if res.status_code == 200:
    print('User ' + res.json()['personDisplayName'].title() + ' added to room')
else:
    print(res.json())