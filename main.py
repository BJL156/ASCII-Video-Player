from PIL import Image
import cv2
import math
import os

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', '@', ',', '.']
# ASCII_CHARS = [".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]

scale_factor = 0.1

text = open("output.txt", 'w')

def gen_frame(image):
    width, height = image.size
    image = image.resize((int(scale_factor*width), int(scale_factor*height)), Image.NEAREST)
    width, height = image.size
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            gray = int(r / 3 + g / 3 + b / 3)
            pixels[x, y] = (gray, gray, gray)

            percent = (gray / 255 * 100)
            print(ASCII_CHARS[int(percent / len(ASCII_CHARS)) - 1], end='')
            text.write(f"{ASCII_CHARS[int(percent / len(ASCII_CHARS)) - 1]}")
        print('')
        text.write('\n')

cap = cv2.VideoCapture("videos/video.mp4")

while True:
    ret, frame = cap.read()
    gen_frame(Image.fromarray(frame))
    cv2.waitKey(10)
    os.system('cls')


# frame = Image.open("cameron.jpg")
# gen_frame(image)
