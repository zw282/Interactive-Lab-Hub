import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
from datetime import datetime
import haversine
from haversine import inverse_haversine, Direction, Unit
from math import pi

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Setup the code for our buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

button = digitalio.DigitalInOut(board.D23)
button.switch_to_input()

# This is the coordinates of Tata Innovation Center 
tata = (40.7578325,-73.9559878) #(lat, lon)

# This is the average driving speed mph
driving_speed = 10000

# This is the average driving time in seconds
#average_time = main_distance / driving_speed * 3600

# This is the default direction
dirlist = ["EAST", "WEST", "SOUTH", "NORTH"]

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 0), "Press Top", font=font, fill="#F9AD43")
    draw.text((0, 20), "To choose your direction", font=font, fill="#F9AD43")
    draw.text((0, 40), "Press Bottom", font=font, fill="#F9AD43")
    draw.text((0, 60), "To confirm", font=font, fill="#F9AD43")

    disp.image(image, rotation)
    
    confirm = False
    
    #direction loop from dir[0]
    i = -1
    if buttonB.value and not buttonA.value:            
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        i = i+1
        if i > 3 :
            i = i % 4 - 1   
        dirr = dirlist[i]
        draw.text((0,0), str(dirr), font=font, fill ="#F9AD43")
        disp.image(image, rotation)
        time.sleep(1)
        
        if buttonA.value and not buttonB.value:
            confirm = True 
            continue
            
    if confirm == True:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((0, 0), "you are travelling " + str(dirr), font=font, fill="#F9AD43")
        disp.image(image, rotation)            
        time.sleep(1)   
    
    end = None
    
    if buttonB.value and not buttonA.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        start = time.time()
        START = 'Start traveling'
        draw.text((0, 20), START, font=font, fill="#F9AD43")
        disp.image(image, rotation)
        time.sleep(0.5)
        
        while end == None:
            if buttonB.value and not buttonA.value:
                end = time.time()
        
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        driving_time = end - start
        distance = (driving_speed * driving_time) / 3600
        current_co = inverse_haversine(tata, distance, Direction.dirr, unit = Unit.MILES)
        current_co = (round(current_co[0],3),round(current_co[1],3))
        distance = round(distance,3)
        draw.text((0, 0), "You have travelled", font=font, fill="#F9AD43")
        draw.text((0, 20), str(distance) + "miles", font=font, fill="#F9AD43")
        draw.text((0, 40), "Your coordinates are", font=font, fill="#F9AD43")
        draw.text((0, 60), str(current_co), font=font, fill="#F9AD43")

        draw.text((0, 80), "Check where you are!", font=font, fill="#F9AD43")

        disp.image(image, rotation)
        time.sleep(10)
