from PIL import Image

img = Image.open(r'example3\landscape.png')
images = []
width, height = img.size

for step in range(0, height - 300 + 1, 5):
    box = (0, 0 + step, width, 300 + step)
    cropped = img.crop(box)
    images.append(cropped)

images += images[-2:0:-1]

images[0].save(r'example3\sliding_window.gif',
                save_all = True, 
                append_images = images[1:], 
                optimize = False, 
                duration = 50, 
                loop = 0)