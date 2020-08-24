# inspiro
Inspiro delivers your personal inspiring and motivational quotes fresh from the oven! 

## Get started
1. Download this repository as zip or clone it locally using git
1. Add a shortcut of `inspiro.py` (with console window) or `inspiro.pyw` (without console window) to your autostart folder
    * For windows this is under: `C:\Users\<YOUR_USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
1. (optional) Make other adoptions if desired in `config.json`
1. Add your own quotes into the [quotes.csv file](quotes.csv)
    * Each row is interpreted as one Quote containing of the quote text and the Author (which is optional) seperated by a semicolon.

Now, with every login into your computer you will receive one of your configured quotes.

### Ready to use package
At [Releases](https://github.com/tfreundo/inspiro/releases) you can find ready-to-use executables fresh from the oven.
Currently there is only a **Windows executable** available.

If you're interested to use it on another platform like Linux or MAC, either build it yourself (see below) or if there is great interest I will do the cross-compiling and upload according exectuables.
Just give me a hint if you're interested in that!

## Creating your own Package
You want to package it yourself? Go ahead!
The python package is bundled with [Pyinstaller](http://www.pyinstaller.org/).

Simply execute `pyinstaller inspiro.py` or `pyinstaller --onefile --noupx inspiro.py` and the package will be generated into the `build` folder.

* For Linux builds see [here](https://pyinstaller.readthedocs.io/en/stable/bootloader-building.html#building-for-gnu-linux)
* For MAC builds see [here](https://pyinstaller.readthedocs.io/en/stable/bootloader-building.html#building-for-mac-os-x)
* For Windows builds see [here](https://pyinstaller.readthedocs.io/en/stable/bootloader-building.html#building-for-windows)