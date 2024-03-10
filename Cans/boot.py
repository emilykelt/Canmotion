import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.GP15)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# If the GP15 is connected to ground with a wire
# CircuitPython can write to the drive (not USB)
storage.remount("/", readonly=switch.value)
