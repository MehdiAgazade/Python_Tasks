import qrcode

url = "Screenshot 2025-12-08 221829"
image = qrcode.make(url)
image.save("Click me6.jpg")