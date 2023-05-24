import alsaaudio
import time
from gpiozero import LED

# Deschide mixerul pentru redare
mixer = alsaaudio.Mixer()

# Inițializează ledurile
led_green = LED(7)  # Pinul GPIO pentru ledul verde
led_yellow = LED(8)  # Pinul GPIO pentru ledul galben
led_red = LED(25)  # Pinul GPIO pentru ledul roșu

# Continuu monitorizează volumul

    # Obține nivelul volumului
volume = mixer.getvolume()[0]

    # Printează nivelul volumului
print("Current volume:", volume)

    # Controlează ledurile în funcție de nivelul volumului
if volume < 75:
    led_green.on()
    led_yellow.off()
    led_red.off()
elif 75 <= volume <= 90:
    led_green.off()
    led_yellow.on()
    led_red.off()
else:
    led_green.off()
    led_yellow.off()
    led_red.on()

time.sleep(1)
