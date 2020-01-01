import random
import os
import shutil
import glob

print("Randomising script... (this might take a while)")
script_file = "0.u" if os.path.exists("0.u") else "0.utf"
script_lines = open(script_file, encoding="utf-8").readlines()
original_lines = [i for i in script_lines if i.startswith("langen")]
randomised_lines = original_lines[:]
random.shuffle(randomised_lines)
full_script = open(script_file, encoding="utf-8").read()
for i, l in enumerate(original_lines):
    full_script = full_script.replace(l, randomised_lines[i])
# ADV mode hack for Nocturne to make it at least somewhat usable
if all(x in full_script for x in ["umineko8final", "advsetwindow"]):
    full_script = full_script.replace("^@", "^\\")
# Replace ADV-mode textboxes with ones without nametags
# (the nametags would be incorrect after randomisation)
textbox_locations = [
    "textbox/black",
    "textbox/clean",
    "textbox/normal",
    "textbox",
    "textbox_black",
    "textbox_clean",
]
for textbox_location in textbox_locations:
    normal_box = f"{textbox_location}/-1.png"
    if os.path.exists(normal_box):
        for i in glob.glob(f"{textbox_location}/*.png"):
            try:
                shutil.copy(normal_box, i)
            except shutil.SameFileError:
                pass
open(script_file, "w", encoding="utf-8").write(full_script)
