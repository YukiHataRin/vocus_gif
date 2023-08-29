from PIL import Image

images = [Image.open(f'example4\\{img}.png') for img in range(3)]
images[0].save(r'example4\blend.gif', 
               save_all = True,
               append_images = images[1:],
               optimize = False,
               duration = 500,
               loop = 0)