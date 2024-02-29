import subprocess
import RPi.GPIO as GPIO
import time

# IP address to check
target_ip = "127.0.0.1" #Don't be dumb and use your own local IP.

# GPIO pin connected to the relay
relay_pin = 17

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# Flag to track relay state
relay_state = False

def is_ip_online(ip):
    # Ping the IP to check if it's online
    try:
        subprocess.check_output(["ping", "-c", "1", ip])
        return True
    except subprocess.CalledProcessError:
        return False
    #time.sleep(5) #if needed
try:
    while True:
        if is_ip_online(target_ip):
            if not relay_state:
                GPIO.setmode(GPIO.BCM) # Reinitialize 
                GPIO.setup(relay_pin, GPIO.OUT) # Reinitialize
                GPIO.output(relay_pin, GPIO.HIGH)  # Turn on relay
                relay_state = True
        else:
            if relay_state:
                GPIO.output(relay_pin, GPIO.LOW)  # Turn off relay
                relay_state = False
                GPIO.cleanup()
        time.sleep(30)  # Check every 30 seconds
except KeyboardInterrupt:
    print ("loop ending")

finally:
    print ("cleaning up")
    GPIO.cleanup() #Damn GPIO's always used by something.
