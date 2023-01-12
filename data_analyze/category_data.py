# カテゴリ変数の説明変数と目的変数の関係を可視化する
# trainデータを「train_csv」で読み込み
# 2値分類のみ適用可能

# 各コンペで適当に名前を付ける
# DICT_TARGETは指定しなくてもよい。(もともとのデータのラベルがそのまま付けられる)
DICT_TARGET = {0: '0: No stroke', 1: '1: stroke'}
# TARGET_COLUMNは必ず指定
TARGET_COLUMN = 'stroke'
# 可視化したい説明変数の指定
VAL_NAME = 'gender'

def arrange_stack_bar(ax):
    #積み上げグラフの体裁を整える
    ax.set_xticklabels(labels=ax.get_xticklabels(), rotation=30, horizontalalignment="center")
    ax.grid(axis='y', linestyle='dotted')

def output_bars(df, column, index={}):
    #4(2×2)つ分のグラフの位置を確保する 
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    fig.subplots_adjust(wspace=0.5, hspace=0.5)    

    # Key-Valueラベルなしの場合
    if len(index) == 0:
        df_vc = df.groupby([column])[TARGET_COLUMN].value_counts(
            sort=False).unstack().rename(columns=DICT_TARGET)
        df[column].value_counts().plot.pie(ax=axes[0, 0], autopct="%1.1f%%")
        df_rt = df.groupby([column])[TARGET_COLUMN].value_counts(
            sort=False, normalize=True).unstack().rename(columns=DICT_TARGET)

    # Key-Valueラベルありの場合
    else:
        df_vc = df.groupby([column])[TARGET_COLUMN].value_counts(
            sort=False).unstack().rename(index=index, columns=DICT_TARGET)
        df[column].value_counts().rename(index).plot.pie(ax=axes[0, 0], autopct="%1.1f%%")
        df_rt = df.groupby([column])[TARGET_COLUMN].value_counts(
            sort=False, normalize=True).unstack().rename(index=index, columns=DICT_TARGET)
    
    df_rt.plot.bar(ax=axes[1, 1], stacked=True)

    # データラベル追加
    # ここを整備すれば多クラス分類でも行けそう
    [axes[1, 1].text(i, 1, '{:.3f}'.format(item[1]), horizontalalignment='center') 
     for i, (_, item) in enumerate(df_rt.iterrows())]

    df_vc.plot.bar(ax=axes[1, 0])

    for rect in axes[1, 0].patches:
        height = rect.get_height()

        # https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
        axes[1, 0].annotate('{:.0f}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    df_vc.plot.bar(ax=axes[0, 1], stacked=True)

    arrange_stack_bar(axes[0, 1])
    arrange_stack_bar(axes[1, 0])
    arrange_stack_bar(axes[1, 1])

    # データラベル追加
    [axes[0, 1].text(i, item.sum(), item.sum(), horizontalalignment='center') 
     for i, (_, item) in enumerate(df_vc.iterrows())]

    plt.show()

# 関数の実行
output_bars(train_csv, VAL_NAME)