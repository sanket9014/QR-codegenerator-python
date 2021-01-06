import qrcode

data="aniker"
img=qrcode.make(data)
img.save(f"C:\\Users\\lenovo\\Downloads\\{data}.png")
