# import the qrcode module
import qrcode as qr

# input for qr
qr_text = input("Enter Text/Link to generate the QR Code : ")
# create qrcode using make function 
img = qr.make(qr_text)

# save the qrcode
img.save("video_Youtube.png")
img.show()
