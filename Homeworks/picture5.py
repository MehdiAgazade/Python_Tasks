import qrcode

url = "Screenshot 2025-11-20 212246"
image = qrcode.make(url)
image.save("Click me5.jpg")