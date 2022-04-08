from PIL import Image, ImageOps

filenames = ["nmdr1.jpg", "bupreme.jpg", "sweatpants.jpg"]
for i in range(len(filenames)):
    im = Image.open(filenames[i])
    gray_image = ImageOps.grayscale(im)
    grey_image = gray_image.resize((28,28))
    grey_image = ImageOps.invert(grey_image)
    grey_image.save("g" + filenames[i])