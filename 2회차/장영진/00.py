# API문서와 requests 활용
# BTC의 KRW(원) 전일종가를 출력

import requests

order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(URL)

data = response.json()
result = data.get('data').get('closing_price')

print(result)