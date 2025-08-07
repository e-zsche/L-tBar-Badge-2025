import time
from machine import Pin
import neopixel

from ir_tx.nec import NEC as IR_TX

np = neopixel.NeoPixel(Pin(16), 3)

ir_tx_pin = Pin(14, Pin.OUT, value=0)
ir_rx_pin = Pin(15, Pin.IN)

ir_tx = IR_TX(ir_tx_pin, freq=38000)

data = 0x17
count = 0
while 1:
    print("transmit: ", end="")
    print(count, data)
    ir_tx.transmit(0x6969, data)
    count += 1
    time.sleep(0.25)
