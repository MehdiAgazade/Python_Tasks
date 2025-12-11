import qrcode

url = "https://www.youtube.com/channel/UC-xUcuhrCOIUTa_k2W-s_CA"
image = qrcode.make(url)
image.save("My youtube channel ! Subcribe.jpg")