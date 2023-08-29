from PIL import Image
# 創建一個水藍色圖像
base_img = Image.new('RGB', (100, 100), color = 'aqua')

# 旋轉圖像
rotated_images = [base_img.rotate(angle) for angle in range(0, 360, 10)]

# 將旋轉的圖像保存為GIF
rotated_images[0].save(r'example2\rotated_animation.gif',
                      save_all = True, 
                      append_images = rotated_images[1:], 
                      optimize = False, 
                      duration = 100, 
                      loop = 0)