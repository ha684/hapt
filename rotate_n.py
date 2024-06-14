from PIL import Image

def rotate_image(image_path, angle):
    # Load the image
    image = Image.open(image_path)

    # Rotate the image
    rotated_image = image.rotate(angle, expand=True)

    # Return the rotated image
    return rotated_image

def rotate_back(rotated_image, angle):
    # Rotate the rotated image back to the original orientation
    original_image = rotated_image.rotate(-angle, expand=True)

    # Return the original image
    return original_image

# Đường dẫn của ảnh đã xoay
rotated_image_path = r"C:\Users\OS\Desktop\Workspace\hapt\2.png"

# Góc xoay đã sử dụng (50 độ)
angle = 50

# Quay lại ảnh ban đầu và lưu lại
rotated_image = Image.open(rotated_image_path)
original_image = rotate_back(rotated_image, angle)
original_image.save(r"C:\Users\OS\Desktop\Workspace\hapt\3.png")

print("Image rotated back to its original orientation and saved successfully.")
