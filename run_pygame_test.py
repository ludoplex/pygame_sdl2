#!/usr/bin/env python
"""
Wrapper script to use pygame_sdl2 to run tests from the pygame test suite.
"""


import pygame_sdl2, sys
pygame_sdl2.import_as_pygame()

if len(sys.argv) < 2:
    print(f"usage: {sys.argv[0]} <path-to-script>")
    sys.exit(1)

import sys
sys.argv = sys.argv[1:]
__file__ = sys.argv[0]

code = compile(open(__file__).read(), __file__, 'exec')
exec(code)
