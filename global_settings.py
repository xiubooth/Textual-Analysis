import os
import json
import numpy as np
import pandas as pd
from pathlib import Path

# desktop path
DESKTOP_PATH = str(Path(os.getcwd()).parent.absolute())

# data path
DATA_PATH = os.path.join(DESKTOP_PATH, "data")
CLEAN_PATH = os.path.join(DATA_PATH, "cleaned")
RICH_PATH = os.path.join(DATA_PATH, "enriched")
WORD_PATH = os.path.join(DATA_PATH, "word")

# output path
OUTPUT_PATH = os.path.join(DESKTOP_PATH, "output")
LOG_PATH = os.path.join(OUTPUT_PATH, "log")
FIG_PATH = os.path.join(OUTPUT_PATH, "fig")

# stkcd & trddt
stkcd_all = list(np.load(os.path.join(DATA_PATH, "stkcd_all.npy")))
dalym = pd.read_csv(os.path.join(DATA_PATH, "dalym.csv"))
trddt_all = np.array(sorted(set(dalym["Trddt"])))
date0_min = "2015-01-07"
date0_max = "2019-07-30"

# risklab server
user = "risklab_user"
host = "128.135.196.208"
PASS_PATH = os.path.join(DATA_PATH, "password")
with open(os.path.join(PASS_PATH, "password.json"), "r") as f:
    pass_file = json.load(f)
    password = pass_file["password"]

# dictionary
# https://github.com/MengLingchao/Chinese_financial_sentiment_dictionary
xlsx_dict = pd.ExcelFile(os.path.join(DATA_PATH, "Chinese_Dict.xlsx"))
pos_dict = [_.strip() for _ in xlsx_dict.parse("positive").iloc[:, 0]]
neg_dict = [_.strip() for _ in xlsx_dict.parse("negative").iloc[:, 0]]
full_dict = pos_dict + neg_dict
