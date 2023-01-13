from sklearn.model_selection import KFold
"""
cross validationを行うスクリプト

train: DataFrame
    訓練データ(idと目的変数を除いたもの)
train_labels: DataFrame
    訓練データの目的変数
"""

scores = []

#KFoldクラスを用いてクロスバリデーションの分割を行う
kf = KFold(n_splits=4, shuffle=True, random_state=0)
# modelを作成(各コンペでモデルを選択する)
model = Model()

for tr_idx, va_idx in kf.split(train):
    # データを分割
    tr_x = train.iloc[tr_idx]
    va_x = train.iloc[va_idx]
    tr_y = train_labels.iloc[tr_idx]
    va_y = train_labels.iloc[va_idx]
    # 学習
    model.fit(tr_x, tr_y)
    # 予測
    va_pred = model.predict(va_x)
    # roc_auc_scoreを算出(今回の評価指標)
    score = model.score(va_x, va_y)
    # scoreをまとめる
    scores.append(score)

# 各foldで得られたscoreを平均して評価指標とする
print('score: ' + str(np.mean(scores)))