import os
import shutil
import random
import glob

if not os.path.exists("bmp"):
    print("First run -- extracting resources...")
    for i in glob.glob("*.nsa"):
        os.system(f"nsadec {i}")
random_dirs = [
    "big/bmp/tati/**/*.png",  # Base game Steam sprites/07th-Mod Rondo sprites
    "bmp/tati/**/*.png",  # Base game potato sprites
    "BGM/*.ogg",  # Music
    "BGM2/*.ogg",  # Chiru music
    "BGM3/*.ogg",  # Chiru music
    "BGM4/*.ogg",  # Chiru music
    "bmp/background/**/*.png",  # Base game backgrounds (PNG)
    "bmp/background/**/*.bmp",  # Base game backgrounds (BMP)
    "sprites/**/*.png",  # 07th-Mod Nocturne sprites
    "bg/*.png",  # 07th-Mod Nocturne backgrounds
]
for random_dir in random_dirs:
    print(f"Randomising {random_dir}...")
    original = glob.glob(random_dir, recursive=True)
    randomised = original[:]
    random.shuffle(randomised)
    for i, f in enumerate(original):
        try:
            shutil.copy(randomised[i], f)
        except shutil.SameFileError:
            pass
        print(f"{f} -> {randomised[i]}")
