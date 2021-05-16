#!/usr/bin/env python

import pycom
from _pybytes import Pybytes
from _pybytes_config import PybytesConfig

pycom.heartbeat(False)
# Orange: Booting
pycom.rgbled(0x221000)

conf = PybytesConfig().read_config()
pybytes = Pybytes(conf)
