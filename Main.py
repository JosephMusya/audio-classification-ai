import os
import sys, getopt
import signal
import time
from edge_impulse_linux.audio import AudioImpulseRunner
import twilio_notify as twilio
import led
import random as r
from upload import upload_data

led.setup()
runner = None
def signal_handler(sig, frame):
    print('Interrupted')
    if (runner):
        runner.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    count = 0
    dir_path = os.path.dirname('/home/pi/Poultra/')
    modelfile = os.path.join(dir_path, 'model.eim')

    with AudioImpulseRunner(modelfile) as runner:
        try:
            model_info = runner.init()
            labels = model_info['model_parameters']['labels']
            #Let the library choose an audio interface suitable for this model, or pass device ID parameter to manually select a specific audio interface
            selected_device_id = 2
            #if len(args) >= 2:
            #print("Device ID "+ str(selected_device_id) + " has been provided as an argument.")

            for res, audio in runner.classifier(device_id=selected_device_id):
                led.running()
                temp = str(r.randint(22,23))
                hum =  str(r.randint(78,80))
                message = 'Chickens calm'
                print('Result (%d ms.) ' % (res['timing']['dsp'] + res['timing']['classification']), end='')
                for label in labels:
                    score = res['result']['classification'][label]
                    print('%s: %.2f\t' % (label, score), end='')
                    if label == 'Unrest' and score > 0.8:
                        count = count + 1
                        print(count)
                        if count == 5:
                            message = 'Restless in chicken'
                            led.detected()
                            twilio.notify('\nATTENTION POULTRA\nDear farmer, there is unrest in your chicken flock')
                            upload_data(temp,hum,message)
                            count = 0
                            print("Sending...")
                            time.sleep(4)
                            #break
                upload_data(temp,hum,message)
                print('', flush=True)

        finally:
            if (runner):
                runner.stop()

if __name__ == '__main__':
    main()