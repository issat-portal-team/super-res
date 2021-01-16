from keras.preprocessing import image 

def read(path):
    img = image.load_img(path, target_size=(80,80,3))
    img = image.img_to_array(img)
    img = img/255.
    return img

