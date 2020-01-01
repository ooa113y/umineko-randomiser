import random

print("Randomising script... (this might take a while)")
script_lines = open("0.utf", encoding="utf-8").readlines()
original_lines = [i for i in script_lines if i.startswith("langen")]
randomised_lines = original_lines[:]
random.shuffle(randomised_lines)
full_script = open("0.utf", encoding="utf-8").read()
for i, l in enumerate(original_lines):
    full_script = full_script.replace(l, randomised_lines[i])
open("0.utf", "w", encoding="utf-8").write(full_script)
