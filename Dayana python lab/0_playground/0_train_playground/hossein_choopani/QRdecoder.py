#here we extract data stored in a QR code

from pyzbar.pyzbar import decode
from PIL import Image

qr=Image.open('Dayana_Docss.png')
data = decode(qr)
#the output of the decode function (data) is a list containing one tuple,
#the first element of tuple has the stored data as bytes
#so we use str() function to convert bytes to strings for a better display 
print(str(data[0][0],"utf-8"))