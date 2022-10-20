#in this code we put some data in a QR code, and then we save that as an image
import qrcode

link='https://t.me/Dayana_Docs'   #our data (here a URL link)
#bulding the QR code. version specify the storage capacity of QR,
#erroe-correction determines how much data can be restored in case of data loss (here is set to Low)
#other parameters are related to shape
qr=qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,)

#now we add data to the QR
qr.add_data(link)
#making the image and saving it
img=qr.make_image()
img.save('Dayana_Docss.png')