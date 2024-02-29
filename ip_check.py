import subprocess
import RPi.GPIO as GPIO
import time

# IP address to check
target_ip = "127.0.0.1" #Don't be dumb and use your own local ip.

# GPIO pin connected to the relay
relay_pin = 17

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

def is_ip_online(ip):
    # Ping the IP to check if it's online
    try:
        subprocess.check_output(["ping", "-c", "1", ip])
        return True
    except subprocess.CalledProcessError:
        return False

try:
    while True:
        if is_ip_online(target_ip):
            GPIO.output(relay_pin, GPIO.HIGH)  # Turn on relay
            print("IP is online, relay turned on")
        else:
            GPIO.output(relay_pin, GPIO.LOW)  # Turn off relay
            print("IP is offline, relay turned off")
        time.sleep(300)  # Check every 5 minutes 
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on Ctrl+C exit
