import qrcode
url = input("enter a link: ").strip()
path = "C:\\Users\\Asus\\Desktop\\qrcode.png"
qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image()
the_user_input = input("do you want to save the qrcode? y/n").strip().lower()
if the_user_input == "y":
    img.show()
    img.save(path)
    print("done!")
elif the_user_input == "n":
    img.show()
    print("done!")
else:
    print("!!! the only acceptable inputs are y or n !!!")