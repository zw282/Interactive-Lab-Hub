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
driving_speed = 17600

# This is the average driving time in seconds
#average_time = main_distance / driving_speed * 3600

# This is the default direction
dirlist = ["EAST", "WEST", "SOUTH", "NORTH"]

# main, dir_selection
screen = "main"
dir_index = 0
start = 0
end = 0
directions = [Direction.EAST, Direction.WEST, Direction.SOUTH, Direction.NORTH]


# set up rocket image
rocket = Image.open("rocket1.jpg")
red = Image.open("red.jpg")

def display_main_screen():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((0, 0), "ROCKET TRAVELLER", font=font, fill="#F9AD43")
    draw.text((0, 20), "Press Top", font=font, fill="#F9AD43")
    draw.text((0, 40), "To choose your direction", font=font, fill="#F9AD43")
    draw.text((0, 60), "Press Bottom", font=font, fill="#F9AD43")
    draw.text((0, 80), "To confirm", font=font, fill="#F9AD43")
   
def display_dir_selection_screen(i):
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    dirr = dirlist[i]
    draw.text((0,0), str(dirr), font=font, fill ="#F9AD43")
    disp.image(image, rotation)
    time.sleep(0.5)
    
    
def display_dir_confirm(i):
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    dirr = dirlist[i]
    draw.text((0, 0), "you are travelling " + str(dirr), font=font, fill="#F9AD43")
    draw.text((0, 20), "from TATA " + str(dirr), font=font, fill="#F9AD43")
    draw.text((0, 40), "press top to start ", font=font, fill="#F9AD43")
    disp.image(image, rotation)            
    time.sleep(1)   
    
def display_walk_screen():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    #dirr = dirlist[i]
    #dirr = str(dirr) 
    disp.image(rocket, rotation)
    time.sleep(1)
    disp.image(red, rotation)
    time.sleep(1)

    
def display_walk_done_screen(start, i):
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    driving_time = end - start
    distance = (driving_speed * driving_time) / 3600
    current_co = inverse_haversine(tata, distance, directions[i], unit = Unit.MILES)
    current_co = (round(current_co[0],3),round(current_co[1],3))
    distance = round(distance,3)
    draw.text((0, 0), "You have travelled", font=font, fill="#F9AD43")
    draw.text((0, 20), str(distance) + "miles", font=font, fill="#F9AD43")
    draw.text((0, 40), "Your coordinates are", font=font, fill="#F9AD43")
    draw.text((0, 60), str(current_co), font=font, fill="#F9AD43")
    draw.text((0, 80), "Check where you are!", font=font, fill="#F9AD43")
    disp.image(image, rotation)
    time.sleep(10)
    
    
def button_a_pressed():
    return buttonB.value and not buttonA.value

def button_b_pressed():
    return buttonA.value and not buttonB.value

while True:
    # transition from screen to screen
    if screen == "main" and button_a_pressed():
        screen = "dir_selection"
        time.sleep(1)
        
    if screen == "dir_selection" and button_a_pressed():
        if dir_index == 3:
            dir_index = 0
        else:
            dir_index += 1
        
    if screen == "dir_selection" and button_b_pressed():
        screen = "dir_confirm"
        print("selection")
        time.sleep(1)
        
    if screen == "dir_confirm" and (button_a_pressed() or button_b_pressed()):
        screen = "walk"
        print("confirmed - go to walk")
        time.sleep(1)
    
    if screen == "walk" and button_a_pressed():
        print("start calculating time")
        start = time.time()
        disp.image(rocket, rotation)
        time.sleep(1)
        
    if screen == "walk" and button_b_pressed():
        end = time.time()
        print("calculated time")
        screen = "walk_done"
        print("done")
        time.sleep(1)
    


        
        
        
        
    
    # display screen
    if screen == "main":
        display_main_screen()
    elif screen == "dir_selection":
        display_dir_selection_screen(dir_index)
    elif screen == "dir_confirm":
        display_dir_confirm(dir_index)
    elif screen == "walk":
        display_walk_screen()
    elif screen == "walk_done":
        display_walk_done_screen(start, dir_index)

    disp.image(image, rotation)
    
    # end = None
    
    # if buttonB.value and not buttonA.value:
    #     draw.rectangle((0, 0, width, height), outline=0, fill=0)
    #     start = time.time()
    #     START = 'Start traveling'
    #     draw.text((0, 20), START, font=font, fill="#F9AD43")
    #     disp.image(image, rotation)
    #     time.sleep(0.5)
        
    #     while end == None:
    #         if buttonB.value and not buttonA.value:
    #             end = time.time()
        
    #     draw.rectangle((0, 0, width, height), outline=0, fill=0)
    #     driving_time = end - start
    #     distance = (driving_speed * driving_time) / 3600
    #     current_co = inverse_haversine(tata, distance, Direction.EAST, unit = Unit.MILES)
    #     current_co = (round(current_co[0],3),round(current_co[1],3))
    #     distance = round(distance,3)
    #     draw.text((0, 0), "You have travelled", font=font, fill="#F9AD43")
    #     draw.text((0, 20), str(distance) + "miles", font=font, fill="#F9AD43")
    #     draw.text((0, 40), "Your coordinates are", font=font, fill="#F9AD43")
    #     draw.text((0, 60), str(current_co), font=font, fill="#F9AD43")

    #     draw.text((0, 80), "Check where you are!", font=font, fill="#F9AD43")

#         disp.image(image, rotation)
    #     time.sleep(10)
      

