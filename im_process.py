from PIL import Image

if __name__ == '__main__':
    with Image.open("results/blue.png") as image:
        x, y = image.size
        image = image.resize((x // 4, y // 4), Image.ANTIALIAS)
        print(image.size)
        image.save("results/blue_aa.png")