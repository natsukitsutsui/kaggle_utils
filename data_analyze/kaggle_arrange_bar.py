#クラス分類問題で目的変数の特徴を図にして出力する
#trainデータを「train_csv」で読み込み

#各コンペで適当に名前を付ける
DICT_TARGET = {0: '0: No stroke', 1: '1: stroke '}
TARGET_COLUMN = 'stroke'

def arrange_bar(ax, sr):
    #棒グラフの体裁を整える
    ax.set_xticklabels(labels=ax.get_xticklabels(), rotation=30, horizontalalignment="center")
    ax.grid(axis='y', linestyle='dotted')
    [ax.text(i, count, count, horizontalalignment='center') for i, count in enumerate(sr)]

#value_counts()で要素の数をカウント
#renameで分かりやすい名前に変更
sr_target = train_csv[TARGET_COLUMN].value_counts().rename(DICT_TARGET)

#グラフ2つ分の位置を用意
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 3))
fig.subplots_adjust(wspace=0.5, hspace=0.5)
sr_target.plot.pie(autopct="%1.1f%%", ax=axes[0])
sr_target.plot.bar(ax=axes[1])

arrange_bar(axes[1], sr_target)

plt.show()