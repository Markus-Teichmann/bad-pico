special = {
    'backspace':    0x2a,
    'del':          0x4c,
    'downarrow':    0x51,
    'end':          0x4d,
    'enter':        0x28,
    'esc':          0x29,
    'home':         0x4a,
    'insert':       0x49,
    'lalt':         0xe2,
    'lcontrol':     0xe0,
    'leftarrow':    0x50,
    'lgui':         0xe3, # Windows Key
    'lshift':       0xe1,
    'pagedown':     0x4e,
    'pageup':       0x4b,
    'pause':        0x48,
    'prtscr':       0x46,
    'ralt':         0xe6,
    'rcontrol':     0xe4,
    'rgui':         0xe7,
    'rightarrow':   0x4f,
    'rshift':       0xe5,
    'space':        0x2c,
    'tab':          0x2b,
    'uparrow':      0x52 
}

ENTER = [[special['enter']]]
ESC = [[special['esc']]]
BACKSPACE = [[special['backspace']]]
TAB = [[special['tab']]]
SPACE = [[special['space']]]
PRTSCR = [[special['prtscr']]]
PAUSE = [[special['pause']]]
INSERT = [[special['insert']]]
HOME = [[special['home']]]
PAGEUP = [[special['pageup']]]
PAGEDOWN = [[special['pagedown']]]
DEL = [[special['del']]]
END = [[special['end']]]
RIGHT_ARROW = [[special['rightarrow']]]
LEFT_ARROW = [[special['leftarrow']]]
UP_ARROW = [[special['uparrow']]]
DOWN_ARROW = [[special['downarrow']]]
LEFT_SHIFT = [[special['lshift']]]
LEFT_CONTROL = [[special['lcontrol']]]
LEFT_ALT = [[special['lalt']]]
LEFT_GUI = [[special['lgui']]]
RIGHT_SHIFT = [[special['rshift']]]
RIGHT_CONTROL = [[special['rcontrol']]]
RIGHT_ALT = [[special['ralt']]]
RIGHT_GUI = [[special['rgui']]]
WIN = LEFT_GUI
SHIFT = LEFT_SHIFT
ALT = LEFT_ALT
CTRL = LEFT_CONTROL
COMMAND = LEFT_GUI
OPTION = LEFT_ALT

CTRLALTDEL = [[special['lcontrol'], special['lalt'], special['del']]]
RUN = [[special['lgui'], 0x15]] #Win + r
SPOTLIGHT = [[special['lgui'], special['space']]]
CLOSE = [[special['lalt'], 0x3d]] #Alt + F4