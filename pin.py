# Ez egy egyszerű pinkódos rendszer lesz :)
# Pin = 1496, de ezt persze te változtathatod!
import time

pin = input("Írd be a pinkódot:")


if pin == "1496":
    time.sleep(1)
    print("Sikeres Bejelentkezés!")
else:
    print("Sikertelen Bejelentkezés!")
    exit()
