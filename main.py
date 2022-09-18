from PIL import Image
import cv2
import math
import os

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', '@', ',', '.']
# ASCII_CHARS = [".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]

scale_factor = 0.25

text = open("output.txt", 'w')

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

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
            # print(ASCII_CHARS[int(percent / len(ASCII_CHARS)) - 1], end='')

            print(colored(r, g, b, ASCII_CHARS[int(percent / len(ASCII_CHARS)) - 1]), end='')
            text.write(f"{ASCII_CHARS[int(percent / len(ASCII_CHARS)) - 1]}")
        print('')
        text.write('\n')
    
    image.save("output.jpg")

filepath = input("video file path: ")
cap = cv2.VideoCapture(filepath)
input_1 = input("show video in cv2 window? (y/n): ")

while True:
    ret, frame = cap.read()
    if input_1 == 'y': cv2.imshow('frame', frame)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    gen_frame(Image.fromarray(frame_rgb))
    cv2.waitKey(1)
    os.system('cls')