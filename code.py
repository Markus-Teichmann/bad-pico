from payload import run
import digitalio
from board import *
from time import sleep

import supervisor
supervisor.runtime.autoreload = False

run()
