//manually create qr code
import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=5,)
qr.add_data("https://www.youtube.com/watch?v=4HRC6c5-2lQ&list=RD4HRC6c5-2lQ&start_radio=1")
qr.make(fit=True)
img = qr.make_image(fill_color = "red", back_color = "black")
img.save("qr_manual.png")


//easy to create qr code
import qrcode as qr
img = qr.make("https://auth.geeksforgeeks.org/user/princekarns/")
img.save("qr_automatic.png")
