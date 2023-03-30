from pynput.keyboard import Controller, Key
import keyboard
import time

# helping variables
k = Controller()

text =""

with open("sample.txt", "r") as f:
    text = f.readlines()

print("press f4 to start auto typing:")

while True:
    print(keyboard.read_key())
    if keyboard.read_key() == "f4":
        break

print("started")
for line in text:
    for word in line:

        if word == '\n':
            k.press(Key.enter)
            k.release(Key.enter)
        else:
            k.press(word)
            k.release(word)

        # speed controlling
        time.sleep(0.03)

print("finished")