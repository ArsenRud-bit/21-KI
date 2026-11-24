from PIL import Image


def demo_pillow():
    try:
        img = Image.new("RGB", (200, 100), "orange")
        print("Розмір зображення:", img.size)
        img = img.rotate(90, expand=True)
        print("Після повороту:", img.size)
    except Exception as e:
        print("Помилка pillow:", e)