from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

image_name = input("image: ")
check_edit = input(
    'press "r" for rotate, "c" to chace color style, "d" to draw rect, "re" for resize, "ci" to chace crop, "wt" to write text\nedit: ')
save_or_not = input("save (y/n): ")


def rotate_image(image):
    image_rotion_deg = int(input("degrees: "))
    if image_rotion_deg > 360:
        image_rotion_deg = 360
    elif image_rotion_deg < 0:
        image_rotion_deg = 0
    img = Image.open(image)
    img.show()
    new_img = img.copy()
    new_img = new_img.rotate(image_rotion_deg)
    mat_img = new_img.load()

    if save_or_not == "y":
        new_img.save("C:\\Users\\Ariel\\Desktop\\json files and other files\\copy(" +
                     image_name.split("\\")[-1] + ")." + image_name.split(".")[-1])
    return new_img


def change_image_color(image):
    image_mode = input(
        "this is the mods: 1, L, P, RGB, RGBA, CMYK, YCbCr, I, F\nmode: ").upper()
    img = Image.open(image)
    img.show()
    new_img = img.copy()
    new_img = new_img.convert(image_mode)
    if save_or_not == "y":
        new_img.save("C:\\Users\\Ariel\\Desktop\\json files and other files\\copy(" +
                     image_name.split("\\")[-1] + ")." + image_name.split(".")[-1])
    return new_img


def draw_rect(image):
    r_x = int(input("rect x: "))
    r_y = int(input("rect y: "))
    r_w = int(input("rect width: "))
    r_h = int(input("rect height: "))
    r_color = input("rect color in rgb hex: ")

    img = Image.open(image)
    img.show()
    new_img = img.copy()
    mat_img = new_img.load()
    for x in range(r_x, r_w):
        for y in range(r_y, r_h):
            new_img[x, y] = r_color

    if save_or_not == "y":
        new_img.save("C:\\Users\\Ariel\\Desktop\\json files and other files\\copy(" +
                     image_name.split("\\")[-1] + ")." + image_name.split(".")[-1])
    return new_img


def resize_image(image):
    print("if you don't want to resize one of the values put \"-\" ")
    new_width = input("new width: ")
    new_height = input("new height: ")
    if new_width == "-":
        new_width = image.size[0]
    else:
        new_width = int(new_width)
    if new_height == "-":
        new_height = image.size[1]
    else:
        new_height = int(new_height)
    img = Image.open(image)
    img.show()
    new_img = img.copy()
    new_img = new_img.resize((new_width, new_height))

    if save_or_not == "y":
        new_img.save("C:\\Users\\Ariel\\Desktop\\json files and other files\\copy(" +
                     image_name.split("\\")[-1] + ")." + image_name.split(".")[-1])
    return new_img


def crop_img(image):
    x = int(input("x: "))
    y = int(input("y: "))
    w = int(input("width: "))
    h = int(input("height: "))

    img = Image.open(image)
    img.show()
    new_img = img.copy()
    new_img = new_img.crop((x, y, w, h))

    if save_or_not == "y":
        new_img.save("C:\\Users\\Ariel\\Desktop\\json files and other files\\copy(" +
                     image_name.split("\\")[-1] + ")." + image_name.split(".")[-1])

    return new_img


def write_in_img(image):
    text = input("text: ")
    t_x = int(input("text x: "))
    t_y = int(input("text y: "))
    t_s = int(input("text size: "))
    t_c = input("text color in rgb hex: ")

    img = Image.open(image)
    img.show()
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("arial.ttf", t_s)
    new_img = img.copy()
    mat_img = new_img.load()
    d = ImageDraw.Draw(new_img)
    d.text((t_x, t_y), text, fill=t_c, font=fnt)

    if save_or_not == "y":
        new_img.save("C:\\Users\\Ariel\\Desktop\\json files and other files\\copy(" +
                     image_name.split("\\")[-1] + ")." + image_name.split(".")[-1])

    return new_img


if check_edit == "r":
    finall_image = rotate_image(image_name)
elif check_edit == "c":
    finall_image = change_image_color(image_name)
elif check_edit == "d":
    finall_image = draw_rect(image_name)
elif check_edit == "re":
    finall_image = resize_image(image_name)
elif check_edit == "ci":
    finall_image = crop_img(image_name)
elif check_edit == "wt":
    finall_image = write_in_img(image_name)

finall_image.show()
