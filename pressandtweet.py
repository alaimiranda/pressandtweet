import sys,random
from twython import Twython
from picamera import PiCamera
from time import sleep
from gpiozero import Button
from gpiozero import LED

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

random.seed()
f = open("/home/pi/Camera/eff_large_wordlist.txt")
las7776 = f.readlines()
camera = PiCamera()
button = Button(18)
red = LED(23)

def main():
        parasiempre = 1
        while(parasiempre):
            if button.is_pressed:
                linea = random.randint(0, 7775) 
                message = las7776[linea].strip("\n")
                message2tweet = message.replace("\t", " ")
                camera.start_preview()
		red.on()
                sleep(3)
                camera.capture('/home/pi/Camera/image.jpg')
                red.off()
		camera.stop_preview()
                with open('/home/pi/Camera/image.jpg', 'rb') as photo:
                    twitter.update_status_with_media(status=message2tweet, media=photo)

if __name__=='__main__':
        main()
