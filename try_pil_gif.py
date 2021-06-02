from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageSequence
import io

def write(img, text, x, y, font=r"C:\Windows\Fonts\arial.ttf", fill="#000000", fontsize=30):
    font = ImageFont.truetype(font, fontsize)
    draw = ImageDraw.Draw(img)
    draw.text((int(x), int(y)), text, font=font, fill=fill)
    return img


hi = r"""


def get_gif_frames(im):
    print("start2")
    # A list of the frames to be outputted
    frames = []
    # Loop over each frame in the animated image
    for frame in ImageSequence.Iterator(im):
        # Draw the text on the frame

        # However, 'frame' is still the animated image with many frames
        # It has simply been seeked to a later frame
        # For our list of frames, we only want the current frame

        # Saving the image without 'save_all' will turn it into a single frame image, and we can then re-open it
        # To be efficient, we will save it to a stream, rather than to file
        b = io.BytesIO()
        frame.save(b, format="GIF")
        frame = Image.open(b)

        # Then append the single frame image to a list of frames
        frames.append(frame)
        print("end2")
        return frames


def write_on_frames(gif, t, x, y, font=r"C:\Windows\Fonts\arial.ttf", fill="#000000", fontsize=30):
    print("start1")
    frames = get_gif_frames(gif)
    print(len(frames))
    for i in frames:
        w = write(i, t, x, y, font, fill, fontsize)
        frames.append(w)
    print("end1")
    return frames


img = Image.open(r"C:\Users\Ariel\Desktop\pillow_imagedraw.gif")
print("hi1")
new_gif_frames = write_on_frames(img, "test", 0, 0, fill="#ff0000")
print("hi2")
new_gif_frames[0].save('pillow_imagedraw.gif',
                       save_all=True, append_images=new_gif_frames[1:], optimize=False, duration=40, loop=0)
print("ended")
"""
images = []

width = 200
center = width // 2
color_1 = (0, 0, 0)
color_2 = (255, 255, 255)
max_radius = int(center * 1.5)
step = 8





for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_1)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center +
                  i, center + i), fill=color_2)
    im = write(im, "test", 0, 0, fill="#0000ff")
    images.append(im)

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_2)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center +
                  i, center + i), fill=color_1)
    im = write(im, "test", 0, 0, fill="#ff0000")
    images.append(im)

images[0].save('pillow_imagedraw.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)



