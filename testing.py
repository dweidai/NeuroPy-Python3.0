from NeuroPy.NeuroPy import NeuroPy
import keyboard
import serial
import time
import sys

'''
    My machine is macOS Mojave Version 10.14.3
    My python is python 3.7
    My machine is Neurosky Mindwave Mobile 2
'''
print("program started")
f = open("testfile.txt", "w")
headset = None
print(headset)
headset = NeuroPy("/dev/cu.MindWaveMobile-SerialPo", 57600)
print(headset)
print("heatset initialized")
headset.start()
print("headset started")

while True:
    att = headset.attention
    med = headset.meditation
    f.write(str(att)+"\t" + str(med) +"\n")
    time.sleep(0.1)
    print("Attention: ", att)
    print("Meditation: ", med)
    time.sleep(0.4)

    try:
        if keyboard.is_pressed('q'):
            headset.stop()
            print(headset)
            print("headset closed")
            break
        else:
            pass
    except:
        print("\t!!!!\nquit program\n\t!!!!!!\n")
        sys.exit(0)


