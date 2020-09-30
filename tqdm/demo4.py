from tqdm import tqdm
import time

# totalは合計値
bar = tqdm(total = 1000)

for i in range(100):
    # 進捗の設定
    bar.update(10)
    time.sleep(1)
