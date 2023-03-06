# import qrcode
import qrcode 

# import Image from PIL
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10,border=4,)

# create qrcode 
qr.add_data("Hello Friends, Use this to create the QrCode")
qr.make(fit=True)

# color of qrcode
img = qr.make_image(fill_color="black", back_color="white")

# save qrcode 
img.save("Qrwithcolor.png")