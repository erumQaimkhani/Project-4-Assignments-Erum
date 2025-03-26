# Project 7 - QR Code Generator
# Made by: Erum Azeemi Qaimkhani

# install  this library first
# pip install qrcode[pil]
import qrcode
data ="QR Code using make() function"
img = qrcode.make(data)
img.save("qr code project 7.png")
print("QR Code Generated Successfully")