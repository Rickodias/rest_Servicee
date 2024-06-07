import requests

# Sunucudaki /square endpoint'ine istek gönderelim
response = requests.get('http://127.0.0.1:5000/square', params={'number': 5})

# Cevabı yazdıralım
if response.status_code == 200:
    print(response.json())
else:
    print(f"Hata: {response.status_code}, {response.text}")