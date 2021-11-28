import os
from global_settings import LOG_PATH
from global_settings import FIG_PATH
from global_settings import CLEAN_PATH
from global_settings import RICH_PATH
from global_settings import WORD_PATH


# Create directories
if not os.path.isdir(CLEAN_PATH):
    os.mkdir(CLEAN_PATH)

if not os.path.isdir(RICH_PATH):
    os.mkdir(RICH_PATH)

if not os.path.isdir(WORD_PATH):
    os.mkdir(WORD_PATH)

if not os.path.isdir(LOG_PATH):
    os.mkdir(LOG_PATH)

if not os.path.isdir(FIG_PATH):
    os.mkdir(FIG_PATH)


if __name__ == "__main__":
    from main import run_data_prep
    from main import run_word_sps
    from main import run_experiment
    from main import run_backtest
    from experiments.params import perc_ls

    # run_data_prep()
    # run_word_sps()
    # model_name = "ssestm"
    model_name = "doc2vec"
    # run_experiment(model_name, perc_ls)

    # run_experiment(model_name, perc_ls)
    run_backtest(model_name)
