Multibrowse: Multi-Monitor Kiosk Mode
=====================================

Simple python script to open several full-screen browser windows onto multiple monitor setups.

Browser is currently set to Google Chrome, but can be adapted to use any browser.

Supported platforms: Windows(7/8/10)/Linux/MacOS

Usage
-----

Open `http://ivo.la` on display 1 and `http://bbc.com` on display 2

```
multibrowse http://ivo.la http://bbc.com
```

Open `http://ivo.la` on display 1 and `http://bbc.com` on display 3

```
multibrowse http://ivo.la - http://bbc.com
```

To exit windows opened in fullscreen, use:
 * Mac: ⌘-Q
 * Windows: Alt-F4

### Displays Ordering

Displays are ordered according to their x/y position from left to right, then top to bottom. Top-left display is always display #1.

Installation
------------

Binaries can be found on the [releases page](https://github.com/foxxyz/multibrowse/releases). To build yourself, see below.

Development Requirements
------------------------

 * Python 3

### Linux

 * xdotool
  * Install with Apt: `sudo apt-get install xdotool`
  * Install with Pacman: `sudo pacman -S xdotool`

### MacOS

 * PyObjC
  * Install with pip: `pip install pyobjc`


Building
--------

Multibrowse can be built into a single contained .exe file using [pyinstaller](http://www.pyinstaller.org/). Pyinstaller can be installed using `pip install pyinstaller`. The old way using `py2exe` is no longer recommended due to Python 3 compatibility issues.

The following command should produce a single self-contained exe file in `/dist`:

```
pyinstaller --onefile multibrowse.py
```

License
-------

MIT