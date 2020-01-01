import os
import shutil
import random
import glob

if not os.path.exists('bmp'):
    print('First run -- extracting resources...')
    for i in glob.glob('*.nsa'):
        os.system(f"nsadec {i}")
random_dirs = [
    'big/bmp/tati/**/*.png',
    'bmp/tati/**/*.png',
    'BGM/*.ogg',
    'bmp/background/**/*.png',
    'bmp/background/**/*.bmp'
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
