import requests 
import hashlib 

url = 'https://api.pwnedpasswords.com/range/' + ' '
res = requests.get(url)
print(res)
sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest).upper)
