from PIL import Image, ImageDraw

# 創建一個圖像列表
images = []
for i in range(100, 201, 10):
    # 創建一個200x200的透明背景
    img = Image.new('RGBA', (200, 200), (255, 255, 255, 0))
    
    # 在正中間繪製紅色正方形
    draw = ImageDraw.Draw(img)
    upper_left = (100 - i//2, 100 - i//2)
    lower_right = (100 + i//2, 100 + i//2)
    draw.rectangle([upper_left, lower_right], fill='red')
    
    images.append(img)

# 將圖像列表保存為GIF
images[0].save(r'square_animation.gif',
               save_all = True, 
               append_images = images[1:], 
               optimize = False, 
               duration = 100, 
               loop = 0)