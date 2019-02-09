#!/usr/bin/env python3
#
# By TheDoudou
#

import sys
import os

from gi.repository import Gdk

window = Gdk.get_default_root_window()
x, y, width, height = window.get_geometry()

pb = Gdk.pixbuf_get_from_window(window, 130, 405, 200, 300)

pb.savev("screenshot.png", "png", (), ())

src =  "screenshot.png"

sys.stdout.write("Content-Type: image/png\n")
sys.stdout.write("Content-Length: " + str(os.stat(src).st_size) + "\n")
sys.stdout.write("\n")
sys.stdout.flush()
sys.stdout.buffer.write(open(src, "rb").read())