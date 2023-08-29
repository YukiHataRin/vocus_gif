from PIL import Image

base_images = [Image.open(f'example4\\{img}.png') for img in range(3)]
base_images.append(base_images[0])
images = []

for i in range(len(base_images) - 1):
    # 將目前圖像加入至images
    images.append(base_images[i])

    # 每幀淡出圖像的透明度增加10%
    for alpha in range(10):
        blend = Image.blend(base_images[i], base_images[i + 1], alpha = alpha / 10)
        images.append(blend)

durtions = []

for i in range(len(images)):
    if i % 11:
        durtions.append(100)
    
    else:
        durtions.append(300)

images[0].save(r'example4\fade_out.gif', 
               save_all = True,
               append_images = images[1:],
               optimize = False,
               duration = durtions,
               loop = 0)