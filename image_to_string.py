from PIL import Image
import tkinter as tk

# /Users/rylwrn/Desktop/random_tihngs/naruto_poster.jpg
image = Image.open("/Users/rylwrn/Desktop/random_tihngs/naruto_poster.jpg")
image = image.convert("L")
mat = image.load()

width, height = image.size
final_string = ""
for i in range(0, width):
    for j in range(0, height):
        try:
            if mat[i, j] == 0:
                final_string = final_string + " "
            elif mat[i, j] >= 0 and mat[i, j] < 25:
                final_string = final_string + "U"
            elif mat[i, j] >= 25 and mat[i, j] < 50:
                final_string = final_string + "O"
            elif mat[i, j] >= 50 and mat[i, j] < 75:
                final_string = final_string + "0"
            elif mat[i, j] >= 75 and mat[i, j] < 100:
                final_string = final_string + "H"
            elif mat[i, j] >= 100 and mat[i, j] < 125:
                final_string = final_string + "B"
            elif mat[i, j] >= 125 and mat[i, j] < 150:
                final_string = final_string + "Q"
            elif mat[i, j] >= 150 and mat[i, j] < 175:
                final_string = final_string + "G"
            elif mat[i, j] >= 175 and mat[i, j] < 200:
                final_string = final_string + "M"
            elif mat[i, j] >= 200:
                final_string = final_string + "W"
        except:
            pass
    final_string = final_string + "\n"
image.show()
screen = tk.Tk()
print(final_string)
l = tk.Text(screen)
l.config(font=("Arial", "1"))
l.insert("1.0", final_string)
l.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
screen.mainloop()