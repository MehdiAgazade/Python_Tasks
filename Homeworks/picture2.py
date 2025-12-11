import qrcode

url = "Screenshot 2025-10-28 202945"
image = qrcode.make(url)
image.save("Click me2.jpg")