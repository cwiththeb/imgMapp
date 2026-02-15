from PIL import Image
from tkinter import Tk, filedialog

def imgMapp(path, scale):
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^'. "

    img = Image.open(path)
    w, h = img.size
    img = img.resize((int(w*scale), int(h*scale*0.55)))
    img = img.convert("L")

    pixels = img.getdata()
    width = img.width

    result = ""
    for y in range(img.height):
        line = ""
        for x in range(img.width):
            p = img.getpixel((x, y))
            index = p * (len(chars)-1) // 255
            line += chars[index]
        result += line + "\n"

    return result

art = imgMapp("/storage/emulated/0/Download/300px-Thumbs_Up_Crying_Cat.jpg", 0.5)

with open("/storage/emulated/0/Download/ascii.txt", "w") as f:
    f.write(art)


# Desktop File Picker logic (Windows / Mac / Linux)
# from tkinter import Tk, filedialog
#
# root = Tk()
# root.withdraw()  # Hide the empty root window
#
# file_path = filedialog.askopenfilename(
#     title="Select an Image",
#     filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
# )
#
# if file_path:
#     print(imgMapp(file_path, 0.2))
# else:
#     print("No file selected.")