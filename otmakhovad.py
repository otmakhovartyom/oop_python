import RPi.GPIO as GPIO
import time

leds = [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

def lightUp(ledNumber, period):
    GPIO.output(leds[ledNumber], 1)
    time.sleep(period)
    GPIO.output(leds[ledNumber], 0)

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        GPIO.output(leds[ledNumber], 1)
        time.sleep(blinkPeriod)
        GPIO.output(leds[ledNumber], 0)
        time.sleep(blinkPeriod)

def runningLight(count, period):
    for i in range(count):
        for k in range(8):
            GPIO.output(leds[k], 1)
            time.sleep(period)
            GPIO.output(leds[k], 0)
            
def runningDark(count, period):
    GPIO.output(leds, 1)
    time.sleep(0.1)
    for i in range(count):
        for k in range(8):
            GPIO.output(leds[k], 0)
            time.sleep(period)
            GPIO.output(leds[k], 1)

def decToBinList(decNumber):
    bin = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        bin[7 - i] = decNumber % 2
        decNumber = decNumber // 2
    return bin

def lightNumber(number):
    b = decToBinList(number)
    for i in range(8):
        GPIO.output(leds[i], b[7-i])
    time.sleep(0.5)    

def runningPattern(pattern, direction):
    b = decToBinList(pattern)
    if direction == 1:
        for k in range(20):
            for i in range(8):
                GPIO.output(leds[i], b[(i + k) % 8])
            time.sleep(0.2)
            GPIO.output(leds, 0)
            time.sleep(0.2)
    else:
        for k in range(20):
            for i in range(8):
                GPIO.output(leds[i], b[(i + 7*k) % 8])
            time.sleep(0.2)
            GPIO.output(leds, 0)
            time.sleep(0.2)

#a = input()

#lightUp(2,3)

#blink(4, 5, 1)

#runningLight(2, 0.1)

#runningDark(2, 0.3)

print decToBinList(15)

lightNumber(15)

#runningPattern(220, 1)

GPIO.output(leds, 0)
GPIO.cleanup()