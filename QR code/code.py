import qrcode as qr
img = qr.make("https://www.swiggy.com")
img.save("Swiggy.png")
