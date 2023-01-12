# 数値変数の説明変数と目的変数の関係を可視化する
# trainデータを「train_csv」で読み込み
# 欠損値の扱い: 除去されている

# DICT_TARGETは指定しなくてもよい。(もともとのデータのラベルがそのまま付けられる)
DICT_TARGET = {0: '0: No stroke', 1: '1: stroke'}
# TARGET_COLUMNは必ず指定
TARGET_COLUMN = 'stroke'
# 可視化したい説明変数の指定
VAL_NAME = 'gender'

def output_box_hist(column, bins=20, query=None):
    if query == None:
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    else:
        fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 12))
        train_csv.query(query)[column].hist(ax=axes[2, 0], bins=bins)
        train_csv.query(query).groupby(TARGET_COLUMN)[column].plot.hist(
        ax=axes[2, 1], bins=bins, alpha=0.5, legend=True, grid=True)
        axes[2, 1].legend(labels=[DICT_TARGET[int(float((text.get_text())))] for text in axes[2, 1].get_legend().get_texts()])

    fig.subplots_adjust(wspace=0.5, hspace=0.5)

    train_csv.boxplot(ax=axes[0, 0], column=[column])
    train_csv.boxplot(ax=axes[0, 1], column=[column], by=TARGET_COLUMN)
    axes[0, 1].set_xticklabels([DICT_TARGET[int(float(xticklabel.get_text()))] for xticklabel in axes[0, 1].get_xticklabels()])
    train_csv[column].hist(ax=axes[1, 0], bins=bins)
    train_csv.groupby(TARGET_COLUMN)[column].plot.hist(ax=axes[1, 1], bins=bins, alpha=0.5, grid=True, legend=True)
    axes[1, 1].legend(labels=[DICT_TARGET[int(float((text.get_text())))] for text in axes[1, 1].get_legend().get_texts()])

    plt.show()

output_box_hist(VAL_NAME)