#!/usr/bin/python3

from os import listdir, rename, chdir
from PIL import Image

def get_numbers(image):
    left = [103, 124, 145, 166, 186, 207, 228, 249, 269, 290, 311, 332]
    top = 74
    bottom = 104
    numbers = []
    for i in range(11):
        numbers.append(image.crop((left[i], top, left[i+1], bottom)))
        n = numbers[-1]
        for x in range(n.width):
            for y in range(n.height):
                if sum(n.getpixel((x, y))) > 128*3:
                    n.putpixel((x, y), (255, 255, 255))
                else:
                    n.putpixel((x, y), (0, 0, 0))
    return numbers

stddigit = list(map(Image.open, map(lambda i:'%d.bmp'%i, range(10))))    
def getdigit(digit):
    scores = []
    for d in stddigit:
        score = 0
        for x in range(20):
            for y in range(30):
                if d.getpixel((x, y)) == digit.getpixel((x, y)):
                    score += 1
        scores.append(score)
    return scores.index(max(scores))

def process(image):
    result = ''
    for d in get_numbers(image):
        result += str(getdigit(d))
    return result

def main():
    chdir(input('enter the directory name: '))
    names = {}
    for f in listdir():
        rename(f, 'processing '+f)
    for f in listdir():
        n = process(Image.open(f).resize((720, 1080)))
        if n in names:
            names[n] += 1
            n += ' (%d)' % names[n]
        else:
            names[n] = 1
        rename(f, n + '.' + f.rpartition('.')[2])

if __name__ == '__main__':
    main()

