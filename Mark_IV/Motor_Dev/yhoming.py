#prod ready
import RPi.GPIO as GPIO
from time import sleep
from Limit_Switches import limitSwitches

'''
Moves both motor 3 and motor 4 of the Y axis. Currently CWW || 1 moves the y axis toward home (limitswitches)
'''

ls = limitSwitches()

def yHoming():
    # Direction pin from controller
    GPIO.cleanup()
    DIR_1 = 19 #DIR+
    # Step pin from controller
    STEP_1 = 20 #PULL+
    # 0/1 used to signify clockwise or counterclockwise.
    CW = 0
    CCW = 1
    MAX = 10000
    motor1_flag = 0
    motor2_flag = 0

    GPIO.setmode(GPIO.BCM)
    motor1_switch=18
    motor2_switch=12
    GPIO.setup(motor1_switch,GPIO.IN,pull_up_down=GPIO.PUD_UP)    
    GPIO.setup(motor2_switch,GPIO.IN,pull_up_down=GPIO.PUD_UP)

    # Setup pin layout on PI
    GPIO.setmode(GPIO.BCM)

    # Establish Pins in software
    GPIO.setup(DIR_1, GPIO.OUT)
    GPIO.setup(STEP_1, GPIO.OUT)
   # GPIO.setup(DIR_2, GPIO.OUT)
   # GPIO.setup(STEP_2, GPIO.OUT)

    # Set the first direction you want it to spin
    GPIO.output(DIR_1, CCW)
   # GPIO.output(DIR_2, CCW)
    try:
        # Run forever.
        while(1):

            # Run for 200 steps. This will change based on how you set you controller
            for x in range(MAX):

                # Set one coil winding to high
                GPIO.output(STEP_1,GPIO.HIGH)
    #            GPIO.output(STEP_2,GPIO.HIGH)
                # Allow it to get there.
                #.5 == super slow
                # .00005 == breaking
                sleep(.005) # Dictates how fast stepper motor will run
                # Set coil winding to low
                GPIO.output(STEP_1,GPIO.LOW)
     #           GPIO.output(STEP_2,GPIO.LOW)
                sleep(.005) # Dictates how fast stepper motor will run

          
                if GPIO.input(motor2_switch) == 0:
                    motor2_flag += 1
                elif GPIO.input(motor1_switch) == 0:
                    motor1_flag +=1
                else:
                    motor2_flag = 0
                    motor1_flag = 0

                if motor2_flag >= 5:
                    print('Y Homing')
                    sleep(1)
                    return

                elif motor1_flag >= 5:
                    print('Y Homing')
                    sleep(1)
                    return
                
                    
    # Once finished clean everything up
    except KeyboardInterrupt:
        print("cleanup")
        GPIO.cleanup()



def main():
    yHoming()


if __name__ == '__main__':
    main()