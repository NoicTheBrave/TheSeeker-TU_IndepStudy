from pynput import keyboard
import serial 
import time 


def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['down', 'up', 'left', 'right', 'space']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        print('Key pressed: ' + k)
        #return False  # stop listener; remove this if want more keys
        
        #Ghetto "Switch Statemetn" (Currently believe to be running Python3.6.X, Switch statements [i dont believe] are in this ver.)
        if k == 'up': #FORWARDS
            msg = "S170\n" #S = Speed, Number = PWM Fed to the ESC, starting @ ~150 -> 255
            serial1.write(msg.encode())
            print("FORWARD")
        elif k == 'down':#BACKWARDS - WORK IN PROGRESS (Believed you have to "hit back twice", aka back once, hit neutural, then hit back again (we arent sure)) 
            msg =  "S150\n" #PLACE HOLDER          
            serial1.write(msg.encode()) #May need to rapidly do several commands here to get it to go in reverse, with a time delay 
            print("BACKWARD")
        elif k == 'left': #TURN LEFT 
            msg =  "T50\n"           #T = Turn, Number = Angle (0->180, however ~50 -> ~130 might be best USEFUL range...?)
            serial1.write(msg.encode())
            print("LEFT") 
        elif k == 'right': #TURN RIGHT
            msg =  "T130\n" #PLACE HOLDER          
            serial1.write(msg.encode())
            print("RIGHT")
        elif k == 'space': #RESET EVERYTHING (might break, might just kill motor, Depends on the ESC Configuration)
            #msg = "S150"
            #serial1.write(msg.encode())
            #time.sleep(1)
            #---Suppose to ALSO straighten out the car but we see how well thats working out -_- AND put it to a complete stop. its not -_-
            msg = "T90\n"
            serial1.write(msg.encode())
            print("space")


listener = keyboard.Listener(on_press=on_press)

serial1 = serial.Serial("/dev/ttyACM0", 9600)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
