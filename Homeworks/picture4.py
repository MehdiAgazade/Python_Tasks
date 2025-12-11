import qrcode

url = "Screenshot 2025-11-20 210717"
image = qrcode.make(url)
image.save("Click me4.jpg")