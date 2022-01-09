perc_ls = 0.05
subset_size = 0.1

window_dict = {
    "train_win": 12,
    "valid_win": 12 + 6,
    "test_win": 12 + 6 + 1
}

proc_dict = {
    "ssestm": 37,
    "doc2vec": 13,
    "bert": 5,
}

params_dict = {
    "ssestm": {"pen": [0.0]},
    "doc2vec": {"window": [5, 10, 20], "vec_size": [5, 20, 50], "epochs": [10, 20],
                "num_bins": [20], "cls_type": ["lr"]},
    "bert": {"input_shape": [64, 128, 256]},
    "dnn": {"hidden": [60]},
}
