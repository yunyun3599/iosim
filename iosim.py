#!/usr/bin/python3

import logger
import conf

def __usage_iosim():
    print("""\
Usage: iosim.py [<options>] <path>
  <options>
   -h: help(this message)
   -c <size in blks>
""")

if __name__ == "__main__":
    from sim import Simulator

    logger.init("iosim")

    sim = Simulator()

    conf.parse(__usage_iosim)
    sim.run()
