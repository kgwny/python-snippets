import time
from tqdm import tqdm

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    pbar.set_description("Processing %s" % char)
    time.sleep(1)
