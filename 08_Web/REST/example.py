

import requests


url = 'http://13.125.222.176/quiz/jordan/'

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

data = {'nickname' : '서울3반주지환','yourAnswer': 'KUBERNETES' }

res = requests.post(url, headers=headers ,json=data)

print(res.json())