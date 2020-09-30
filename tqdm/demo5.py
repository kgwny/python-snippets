from tqdm import tqdm
import time

# totalは合計値
bar = tqdm(total = 1000)

# 説明の設定
bar.set_description('Progress rate')

for i in range(100):
    bar.update(10)
    time.sleep(0.1)
