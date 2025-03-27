import os
import pickle
import shutil
import gzip
from RunGrim import run_original_grim

# Step 1: Create HPF File
config_file = '../app/conf/conf.json'
run_original_grim(config_file, hap_pop_pair=True, Producehpf=True, dominant3=True)

# Generate the freq dictionary file
os.makedirs("../app/data/freqs_dicts", exist_ok=True)

freqs_files = os.listdir("data/freq_9loci/")
all_freqs = {}

for file in freqs_files:
    print(f"Reading file: {file}")
    freqs = {}
    with gzip.open(f"data/freq_9loci/{file}", 'rt') as f:
        for i, line in enumerate(f):
            if i == 0:
              continue
            hap, _, prob = line.split(",")
            hap = "~".join(sorted(hap.split("~")))
            prob == 'Freq\n'
            print(i)
            freqs[hap] = float(prob)

    pop = file.split('.')[0]
    all_freqs[pop] = freqs

with open(f"../app/data/freqs_dicts/all_freqs.pickle", "wb") as f:
    pickle.dump(all_freqs, f)
print("4. Produced Pickled Freqs: app/data/freqs_dicts/all_freqs.pickle")

# Copy pop ratio file
shutil.copy('output_new/pop_counts_file.txt', '../app/data/pop_ratio.txt')
print("5. Produced app/data/pop_ratio.txt")
