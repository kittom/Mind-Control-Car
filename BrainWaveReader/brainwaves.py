from NeuroPy import NeuroPy
from time import sleep

neuropy = NeuroPy.NeuroPy("/dev/tty.MindWaveMobile-SerialPo")

def attention_callback(attention_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of attention is: ", attention_value)
    return None

neuropy.setCallBack("attention", attention_callback)
neuropy.start()

try:
    while True:
        sleep(0.2)
finally:
    neuropy.stop()