import time
from tqdm import tqdm

pbar = tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for char in pbar:
    pbar.set_description("Processing %s" % char)
    time.sleep(1)
