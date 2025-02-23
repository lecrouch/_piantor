import board
from kb import KMKKeyboard, isRight
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.tapdance import TapDance
from kmk.modules.holdtap import HoldTap
from kmk.modules.combos import Combos, Chord

print(f"LOADING PIANTOR {'RIGHT' if isRight else 'LEFT'}...")

'''

 I N I T I A L I Z E  K E E B
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
'''
keyboard = KMKKeyboard()
keyboard.tap_time = 100
keyboard.extensions.append(MediaKeys())
'''
'''
'''
'''
'''

 S P L I T  S E T U P
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
'''
split_side = SplitSide.RIGHT if isRight else SplitSide.LEFT
uart_flip = False if isRight else True

data_pin = board.GP1  #RX
data_pin2 = board.GP0 #TX

split = Split(
    split_flip=False,
    split_side=split_side,
    split_type=SplitType.UART,
    split_target_left=True,
    data_pin=data_pin,
    data_pin2=data_pin2,
    uart_flip=uart_flip,
    use_pio=True
)
keyboard.modules.append(split)
'''
'''
'''
'''
'''

 H O L D  T A P
‾‾‾‾‾‾‾‾‾‾‾‾‾‾
'''
holdtap = HoldTap()
keyboard.modules.append(holdtap)
LSFT_P   = KC.HT(KC.LPRN, KC.LSFT,                          prefer_hold=False, tap_interrupted=False, tap_time=70)
RSFT_P   = KC.HT(KC.RPRN, KC.RSFT,                          prefer_hold=False, tap_interrupted=False, tap_time=80)
RSFT_MEH = KC.HT(KC.RPRN, KC.LCTRL(KC.LSFT(KC.LALT)),       prefer_hold=False, tap_interrupted=False, tap_time=90)
G_OP     = KC.HT(KC.G,    KC.LALT,                          prefer_hold=False, tap_interrupted=False, tap_time=90)
'''
'''
'''
'''
'''

 L A Y E R S
‾‾‾‾‾‾‾‾‾‾‾‾‾
'''
layers = Layers()
keyboard.modules.append(layers)
A_LT_1      = KC.LT(1, KC.A,        prefer_hold=False, tap_interrupted=False, tap_time=110)
B_LT_2      = KC.LT(2, KC.B,        prefer_hold=False, tap_interrupted=False, tap_time=100)
N_LT_2      = KC.LT(2, KC.N,        prefer_hold=False, tap_interrupted=False, tap_time=100)
SPC_LT_3    = KC.LT(3, KC.SPC,      prefer_hold=False, tap_interrupted=False, tap_time=110)
Z_LT_3      = KC.LT(3, KC.Z,        prefer_hold=False, tap_interrupted=False, tap_time=110)

LAY_1 = KC.MO(1)
LAY_0 = KC.TO(0)
'''
'''
'''
'''
'''

 T A P  D A N C E
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
//  TAP DANCE - START
'''
tapdance = TapDance()
tapdance.tap_time = 180
keyboard.modules.append(tapdance)
L_CAR = KC.TD(
    # Tap once for "t"
    KC.T,
    # Tap twice for "<"
    KC.LABK,
)

R_CAR = KC.TD(
    # Tap once for "y"
    KC.y,
    # Tap twice for ">"
    KC.RABK,
)

Q_GRAV = KC.TD(
    # Tap once for "q"
    KC.Q,
    # Tap twice for "`"
    KC.GRV,
    tap_time=200
)

B_TD = KC.TD(
    # Tap once for "b", press & hold for KC.MO(2)
    KC.HT(
        KC.B,
        KC.MO(2),
        prefer_hold=True,
        tap_interrupted=True,
    ),
    # Tap twice for "-"
    KC.MINS
    ,
    # Tap three times for "_"
    KC.UNDS
)

CMD_OPT = KC.TD(
    # Tap Once for LGUI
    KC.LGUI,
    # Tap Twice for LALT
    KC.LALT,
    # Tap Three Times for LGUI + LALT
    KC.LGUI(KC.LALT),
    tap_time=80
)
'''
'''
'''
'''
'''
//  TAP DANCE - END

 C O M B O S
‾‾‾‾‾‾‾‾‾‾‾‾‾
'''
combos = Combos()
keyboard.modules.append(combos)
combos.combos = [
    # ROW 1 - LEFT HAND                                    # ROW 1 - RIGHT HAND
    # ( Q + W = ESCAPE ),                                  # ( I + O = BACKSPACE )
    Chord((Q_GRAV, KC.W), KC.ESCAPE, timeout=50),          Chord((KC.I, KC.O), KC.BSPC, timeout=50),
    # ( W + E = TAB )                                      # ( O + P = DELETE )
    Chord((KC.W, KC.E), KC.TAB, timeout=40),               Chord((KC.O, KC.P), KC.DEL, timeout=50),
    #
    #
    # ROW 2 - LEFT HAND                                    # ROW 2 - RIGHT HAND
    # ( S + D = LAYER 1 )                                  # ( H + J = "]" )
    Chord((KC.S, KC.D), LAY_1),                            Chord((KC.H, KC.J), KC.RBRC),
    # ( D + F = "SPACE" )                                  # ( K + L = ENTER )
    Chord((KC.D, KC.F), KC.SPC),                           Chord((KC.K, KC.L), KC.ENT, timeout=50),
    #
    #
    # ROW 3 - LEFT HAND                                    # ROW 3 - RIGHT HAND
    # ( X + C = LAYER 1),                                  # ( N + M = "=" )
    Chord((KC.X, KC.C), LAY_1),                            Chord((N_LT_2, KC.M), KC.EQL),
    # ( V + B = "-" )                                      # ( `,` + `.` = LAYER 1 )
    Chord((KC.V, B_LT_2), KC.MINS),                        Chord((KC.COMM, KC.DOT), LAY_1),
]
'''
'''
'''
'''
'''

 C L E A N  K E Y  N A M E S
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
'''
XXXXXXX = KC.NO
_______ = KC.TRNS
KC_MEH  = KC.LCTRL(KC.LSFT(KC.LALT))
'''
'''
'''
'''
'''

 K E Y M A P
‾‾‾‾‾‾‾‾‾‾‾‾‾
'''
keyboard.keymap = [
    # LAYER 0 - BASE #########################################################################################################################################
    #
    #       VISUALIZATION - LAYER 0
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │   TAB   │ Q_GRAV  │    W    │    E    │    R    │    T    │                           │    Y    │    U    │    I    │    O    │    P    │  BCKSPC │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │ LAY_1   │    A    │    S    │    D    │    F    │  G_OP   │                           │    H    │    J    │    K    │    L    │    ;    │  ENTER  │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │ KC.LALT │ Z_LT_3  │    X    │    C    │    V    │ B_LT_2  │                           │ N_LT_2  │    M    │    ,    │    .    │    /    │  RSFT   │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #                                           ┌─────────┬─────────┬─────────┐       ┌─────────┬─────────┬─────────┐
    #                                           │  LCTRL  │  LSFT   │   LGUI  │       │SPC_LT_3 │   MEH   │  QUOT   │
    #                                           └─────────┴─────────┴─────────┘       └─────────┴─────────┴─────────┘
    [ #     KEYMAP - LAYER 0
        #
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        KC.TAB,  Q_GRAV,  KC.W,    KC.E,    KC.R,    KC.T,                                              KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.BSPC,
        LAY_1,   KC.A,    KC.S,    KC.D,    KC.F,    G_OP,                                              KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.ENT,
        KC.LALT, Z_LT_3,  KC.X,    KC.C,    KC.V,    B_LT_2,                                            N_LT_2,  KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,
        KC.LCTL, KC.LSFT, KC.LGUI,                        SPC_LT_3, KC_MEH,  KC.QUOT,
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                                                                              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #                                       ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    ],
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # LAYER 1 - FUNCS ########################################################################################################################################
    #
    #       VISUALIZATION - LAYER 1
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │    `    │    F1   │    F2   │    F3   │    F4   │    F5   │                           │    F6   │    F7   │    F8   │    F9   │   F10   │ DELETE  │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │         │         │         │         │         │  ENTER  │                           │ PGE UP  │  LEFT   │  DOWN   │   UP    │  DOWN   │         │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │  SPACE  │         │         │         │  SPACE  │ BCKSPC  │                           │ PGE DWN │         │   PREV  │  PLAY   │  NEXT   │         │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #                                           ┌─────────┬─────────┬─────────┐       ┌─────────┬─────────┬─────────┐
    #                                           │         │         │         │       │         │   F11   │   F12   │
    #                                           └─────────┴─────────┴─────────┘       └─────────┴─────────┴─────────┘
    [ #     KEYMAP - LAYER 1
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        KC.GRV,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,                                             KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.DEL,
        _______, _______, _______, _______, _______, KC.ENT,                                            KC.PGUP, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, _______,
        KC.SPC,  _______, _______, _______, LAY_0,   KC.BSPC,                                           KC.PGDN, _______, KC.MRWD, KC.MPLY, KC.MFFD, _______,
        _______, _______, _______,                         _______,  KC.F11,  KC.F12,
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                                                                              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #                                       ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    ],
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # LAYER 2 - LAY_2 - (NUMS + SHIFTED NUMS) #################################################################################################################
    #
    #       VISUALIZATION - LAYER 2
    #
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │         │    1    │    2    │    3    │    4    │    5    │                           │    6    │    7    │    8    │    9    │    0    │         │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │         │    !    │    @    │    #    │    $    │    %    │                           │    ^    │    &    │    *    │    `    │    \    │         │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │         │         │         │         │         │         │                           │         │         │         │         │         │         │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #                                           ┌─────────┬─────────┬─────────┐       ┌─────────┬─────────┬─────────┐
    #                                           │         │         │         │       │         │         │         │
    #                                           └─────────┴─────────┴─────────┘       └─────────┴─────────┴─────────┘
    [ #     KEYMAP - LAYER 2
        #
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        _______, KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                                             KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   _______,
        _______, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC,                                           KC.CIRC, KC.AMPR, KC.ASTR, KC.GRV,  KC.BSLS, _______,
        _______, _______, _______, _______, _______, _______,                                           _______, _______, _______, _______, _______, _______,
        _______, _______, _______,                         _______, _______, _______,
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                                                                              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #                                       ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    ],
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # LAYER 3 - LAY_3 - (SYMBOLS) ############################################################################################################################
    #
    #       VISUALIZATION - LAYER 3
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │    ~    │         │         │         │    (    │    <    │                           │    >    │    )    │         │         │         │         │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │         │         │         │         │    {    │    [    │                           │    ]    │    }    │         │         │         │    \    │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │         │         │         │         │    _    │    -    │                           │    =    │    +    │         │         │         │  LAY_0  │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #                                           ┌─────────┬─────────┬─────────┐       ┌─────────┬─────────┬─────────┐
    #                                           │         │         │         │       │         │         │         │
    #                                           └─────────┴─────────┴─────────┘       └─────────┴─────────┴─────────┘
    [ #     KEYMAP - LAYER 3
        #
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        KC.TILD, _______, _______, _______, KC.LPRN, KC.LABK,                                           KC.RABK, KC.RPRN, _______, _______, _______, _______,
        _______, _______, _______, _______, KC.LCBR, KC.LBRC,                                           KC.RBRC, KC.RCBR, _______, _______, _______, KC.BSLS,
        _______, _______, _______, _______, KC.UNDS, KC.MINS,                                           KC.EQL,  KC.PLUS, _______, _______, _______, LAY_0,
        _______, _______, _______,                         _______, _______, _______,
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                                                                              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #                                       ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    ],
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # LAYER 4 - TRANS ########################################################################################################################################
    #
    #       VISUALIZATION - LAYER 4
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │         │         │         │         │         │         │                           │         │         │         │         │         │         │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │         │         │         │         │         │         │                           │         │         │         │         │         │         │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │         │         │         │         │         │         │                           │         │         │         │         │         │         │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #                                           ┌─────────┬─────────┬─────────┐       ┌─────────┬─────────┬─────────┐
    #                                           │         │         │         │       │         │         │         │
    #                                           └─────────┴─────────┴─────────┘       └─────────┴─────────┴─────────┘
    [ #     KEYMAP - LAYER 4
        #
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        _______, _______, _______, _______, _______, _______,                                           _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______,                                           _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______,                                           _______, _______, _______, _______, _______, _______,
        _______, _______, _______,                         _______, _______, _______,
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                                                                              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #                                       ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    ],
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # LAYER 5 - EMPTY ########################################################################################################################################
    #
    #       VISUALIZATION - LAYER 5
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │                           │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │                           │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐                           ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
    #   │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │                           │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │  KC.NO  │
    #   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘                           └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
    #                                           ┌─────────┬─────────┬─────────┐       ┌─────────┬─────────┬─────────┐
    #                                           │  KC.NO  │  KC.NO  │  KC.NO  │       │  KC.NO  │  KC.NO  │  KC.NO  │
    #                                           └─────────┴─────────┴─────────┘       └─────────┴─────────┴─────────┘
    [ #     KEYMAP - LAYER 5
        #
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                           XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                           XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                           XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX,                         XXXXXXX, XXXXXXX, XXXXXXX,
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                                                                              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #                                       ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾                        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    ]
]

if __name__ == '__main__':
    keyboard.go()
