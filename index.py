import qrcode


#qr = qrcode.make('https://astrylinc.com/')

#qr.save('astryl.png')


qr = qrcode.QRCode (version=1, box_size=15, border = 5)


#data = 'https://astrylinc.com/'

data = str(input('Enter your Product URL'))


qr.add_data(data)
qr.make(fit ='True')

img = qr.make_image(fill='red', back_color = 'white')

save_image = str(input('Enter ur image name with a .png towards the end'))

img.save(save_image+'.png')
