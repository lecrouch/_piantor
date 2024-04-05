import board
from kb import KMKKeyboard, isRight
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType

print("LOADING PIANTOR LEFT...")

keyboard = KMKKeyboard()
keyboard.tap_time = 100

keyboard.debug_enabled = True

split_side = SplitSide.RIGHT if isRight else SplitSide.LEFT

data_pin = board.GP1  #RX
data_pin2 = board.GP0 #TX

split = Split(
    split_flip=False,
    split_side=split_side,
    split_type=SplitType.UART,
    split_target_left=True,
    data_pin=data_pin,
    data_pin2=data_pin2,
    uart_flip=True,
    use_pio=True
)
keyboard.modules.append(split)

layers = Layers()
keyboard.modules.append(layers)

keyboard.keymap = [
    [  # L / R Test
        KC.A, KC.A, KC.A, KC.A, KC.A, KC.A,                                             KC.B, KC.B, KC.B, KC.B, KC.B, KC.B,
        KC.A, KC.A, KC.A, KC.A, KC.A, KC.A,                                             KC.B, KC.B, KC.B, KC.B, KC.B, KC.B,
        KC.A, KC.A, KC.A, KC.A, KC.A, KC.A,                                             KC.B, KC.B, KC.B, KC.B, KC.B, KC.B,
                                KC.A, KC.A, KC.A,                                 KC.B, KC.B, KC.B,
    ]
]

if __name__ == '__main__':
    keyboard.go()
