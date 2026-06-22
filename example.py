import requests

HOST = 'https://release-gs.qa-playground.com/api/v1'

response = requests.post(
    url=f'{HOST}/setup',
    headers={'Authorization': 'Bearer iMTQ4ZC1LY2MOLTQ4ODctOGJiZCALMTYZYikxNZA3NDIifl.KXZuNHXp66RiDdmXZXNi-Q16n3KvLaPf5s-jJvd4'}
)
