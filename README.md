# inspiro
Inspiro delivers your personal inspiring and motivational quotes fresh from the oven!
![inspiro.png](inspiro.png)

## Get started 

### Rready to use packages
At [Releases](https://github.com/tfreundo/inspiro/releases) you can find ready-to-use executables.
Currently there is only a **Windows executable** available.
Just:
1. **download the zip file** and place it anywhere you like
1. (optional) Configure the `config.json` if you want to
1. Add your own quotes into the [quotes.csv file](quotes.csv)
    * Each row is interpreted as one Quote containing of the quote text and the Author (which is optional) seperated by a semicolon.
1. (optional) Add the `inspiro.exe` to your autostart
    * For windows this is under: `C:\Users\<YOUR_USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

If you're interested to use it on another platform like Linux or MAC, either build it yourself (see below) or if there is great interest I will do the cross-compiling and upload according exectuables.
Just give me a hint if you're interested in that!

### Python code
1. Download this repository as zip or clone it locally using git
1. (optional) Create a venv using `pip -m venv my-venv`
1. Install the required packages using `pip install -r requirements.txt` in the root folder
1. Add a shortcut of `inspiro.py` (with console window) or `inspiro.pyw` (without console window) to your autostart folder
    * For windows this is under: `C:\Users\<YOUR_USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
1. (optional) Make other adoptions if desired in `config.json`
1. Add your own quotes into the [quotes.csv file](quotes.csv)
    * Each row is interpreted as one Quote containing of the quote text and the Author (which is optional) seperated by a semicolon.

Now, with every login into your computer you will receive one of your configured quotes.

## Creating your own Package
You want to package it yourself? Go ahead!
The python package is bundled with [Pyinstaller](http://www.pyinstaller.org/).

Simply use the [dist.py](dist.py) and adapt it accordingly.
You will find the generated executables in the `dist` folder.

* For Linux builds see [here](https://pyinstaller.readthedocs.io/en/stable/bootloader-building.html#building-for-gnu-linux)
* For MAC builds see [here](https://pyinstaller.readthedocs.io/en/stable/bootloader-building.html#building-for-mac-os-x)
* For Windows builds see [here](https://pyinstaller.readthedocs.io/en/stable/bootloader-building.html#building-for-windows)