from functools import lru_cache
import os
from subprocess import call, DEVNULL
from time import sleep

# Only available on MacOS
try:
    from AppKit import NSScreen
except ImportError:
    raise ImportError("PyObjC does not seem to be installed. Install it with `pip install -U pyobjc`")

from . import BaseSystem


class System(BaseSystem):

    @property
    def browser_path(self):
        return os.path.join('/', 'Applications', 'Google Chrome.app', 'Contents', 'MacOS', 'Google Chrome')

    def close_existing_browsers(self):
        result = call(['killall', 'Google Chrome'], stdout=DEVNULL, stderr=DEVNULL)
        # Give some time to shut down
        sleep(2)
        return result

    @property
    @lru_cache()
    def displays(self):
        screens = NSScreen.screens()
        connected = []
        for idx, screen in enumerate(screens):
            screen = screen.frame()
            origin_y = screen.origin.y
            # Flip coordinate space because Apple is weird
            # https://developer.apple.com/documentation/coregraphics/cgrect
            if len(connected) > 0:
                origin_y = -screen.size.height - (origin_y - connected[0]["y"])
            connected.append({
                "id": idx,
                "width": int(screen.size.width),
                "height": int(screen.size.height),
                "x": int(screen.origin.x),
                "y": int(origin_y)
            })
        return connected
