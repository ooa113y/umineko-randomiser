This is a set of Python scripts to randomise the content of Umineko no Naku Koro ni.

## SPOILER WARNING
Using this is bound to get you spoiled on sprites, music and backgrounds you haven't seen, as well as lines of text you haven't read. Do not use this unless you have finished reading Umineko.

## How to use:
1. Download and install the latest version of [Python](https://python.org) on your computer. You'll need this to run the scripts.
2. Download the [randomiser itself](../../archive/master.zip) and extract it to your game directory.
3. On Linux or OS X, put a copy of `nsadec` somewhere in your `$PATH`, or extract the `arc*.nsa` archives yourself. On Windows, the program will handle this for you.
4. Run the program. On Windows, this can be done by double-clicking the `randomise_resources.py` or `randomise_script.py` files (for resources and scripts, respectively). On Linux/OS X, pass those scripts to your Python interpreter via the command line.

## What is randomised?
- Music
- Backgrounds
- Sprites
- The English script (optional)

## What versions of Umineko are supported?
The Steam version of both the [Question](https://store.steampowered.com/app/406550/) and [Answer](https://store.steampowered.com/app/639490/) arcs should work. Fan modifications such as 07th-Mod, as well as the original physical release, are not supported.

## How to undo the randomisation?
Delete the "bmp", "big", "bgm" folders and the "0.utf" file. [Ask Steam to redownload those for you.](https://support.steampowered.com/kb_article.php?ref=2037-QEUH-3335) You don't have to do this if you just want to run the randomiser again, simply run it and you'll be fine.

## Known issues
- The script randomisation takes a *long* time (10+ minutes).
- Lines may run off screen sometimes.
- The chapter jump is slightly glitched (it works, but the text before it will be nonsensical).
- Nothing makes sense. It's a visual novel, what do you expect to get from randomising it?
