from PIL import Image

def rotate_image(image_path, angle):
    # Load the image
    image = Image.open(image_path)

    # Rotate the image
    rotated_image = image.rotate(angle, expand=True)

    # Return the rotated image
    return rotated_image

# Đường dẫn của ảnh cần xoay
image_path = r"C:\Users\OS\Desktop\Workspace\python code\CPV301\2\2.png"

# Góc xoay (45 độ)
angle = 50

# Xoay ảnh và lưu lại
rotated_image = rotate_image(image_path, angle)
rotated_image.save("1r.png")
