from PIL import Image, ImageOps
import sys
import os

ext_in = os.path.splitext(sys.argv[1])[1]
ext_out = os.path.splitext(sys.argv[2])[1]

rules = [ext_in==".jpg" or ext_in==".png" or ext_in==".jpeg",
         ext_out==".jpg" or ext_out==".png" or ext_out==".jpeg"]

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif all(rules) and ext_in != ext_out:
    sys.exit("Input and output have different extensions")

elif all(rules) and ext_in == ext_out:
    #open image
    im = Image.open(sys.argv[1])

    #default shirt image
    im_shirt = Image.open("shirt.png")

    #get shirt image size
    im_size = im_shirt.size

    #crop image to fit shirt image size
    im = ImageOps.fit(im, (im_size))

    #overlay and save new image
    im.paste(im_shirt, im_shirt)
    im.save(sys.argv[2])

else:
    sys.exit("Invalid input")
