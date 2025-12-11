import qrcode

url = "Screenshot 2025-11-11 220316"
image = qrcode.make(url)
image.save("Click me3.jpg")