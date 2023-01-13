# target_encoding_cross_validation
"""
cross validationを行いつつ,target encodingを行うスクリプト

train: DataFrame
    訓練データ(idと目的変数を除いたもの)
train_labels: ndarray
    訓練データの目的変数
test: DataFrame
    テストデータ(提出する用のデータ)
"""

# KFoldをimport
from sklearn.model_selection import KFold

# クロスバリデーションのfoldごとにtarget encodingをやり直す
kf = KFold(n_splits=4, shuffle=True, random_state=0)

# target encodingを行うカテゴリ変数
cat_cols = ['gender','hypertension','heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']

train_y = pd.DataFrame(train_labels, columns=['target'])

for i, (tr_idx, va_idx) in enumerate(kf.split(train)):

    # 学習データからバリデーションデータを分ける
    tr_x, va_x = train.iloc[tr_idx].copy(), train.iloc[va_idx].copy()
    tr_y, va_y = train_y.iloc[tr_idx], train_y.iloc[va_idx]
    
    # 変数をループしてtarget encoding
    for c in cat_cols:
        #tr_xの型を整える
        tr_x_c = pd.DataFrame(tr_x[c].tolist(), columns=[c])
        
        # 学習データ全体で各カテゴリにおけるtargetの平均値を計算
        data_tmp = pd.concat([tr_x_c, tr_y], axis=1)
        target_mean = data_tmp.groupby(c)['target'].mean()
        
        #バリデーションデータのカテゴリを置換
        va_x.loc[:, c] = va_x[c].map(target_mean)
        
        #学習データの変換後の値を格納する配列を準備
        tmp = np.repeat(np.nan, tr_x.shape[0])
        kf_encoding = KFold(n_splits=4, shuffle=True, random_state=0)
        for idx_1, idx_2 in kf_encoding.split(tr_x):
            #out-of-foldで各カテゴリにおける目的変数の平均を計算
            target_mean = data_tmp.iloc[idx_1].groupby(c)['target'].mean()
            #変換後の値を一時配列に格納
            tmp[idx_2] = tr_x[c].iloc[idx_2].map(target_mean)
        tr_x.loc[:, c] = tmp
    #必要に応じてencodeされた特徴量を保存し, あとで読み込めるようにしておく。