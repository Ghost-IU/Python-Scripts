import requests 

url = 'https://api.pwnedpasswords.com/range/' + ' '
res = requests.get(url)
print(res)
