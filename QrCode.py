# import the qrcode module
import qrcode as qr

# create qrcode using make function 
img = qr.make("Hello Friends, Use this to create the QrCode")

# save the qrcode
img.save("video_Youtube.png")