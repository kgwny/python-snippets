import os
import datetime
import shutil
from pathlib import Path

def collect(current_dir, txt_dates):
    for file in current_dir.glob("*.txt"):
        # get update date
        mod_ts = os.path.getmtime(str(file))
        mod_dt = datetime.datetime.fromtimestamp(mod_ts)

        # make folder
        dir_name = mod_dt.strftime("%Y_%m_%d")
        date_dir = txt_dates / dir_name
        date_dir.mkdir(exist_ok=True)

        # file copy
        shutil.copy2(str(file), str(date_dir))

def main():
    current_dir = Path(".")
    txt_dates = Path("./tmp")
    txt_dates.mkdir(exist_ok=True)
    collect(current_dir, txt_dates)

if __name__ == '__main__':
    main()
