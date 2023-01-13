# target_encoding
"""
target encodingを行うスクリプト
testデータには、trainデータ全体の平均値を置換
trainデータは, out-of-foldを用いてfoldの数だけtarget encodingを行う

train: DataFrame
    訓練データ(idと目的変数を除いたもの)
train_labels: ndarray
    訓練データの目的変数
test: DataFrame
    テストデータ(提出する用のデータ)
"""

# KFoldをimport
from sklearn.model_selection import KFold

# target encodingを行うカテゴリ変数
cat_cols = ['hypertension','heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']

for c in cat_cols:
    # 学習データ全体で各カテゴリにおけるtargetの平均値を計算
    data_tmp = pd.DataFrame({c:train[c], 'target': train_labels})
    target_mean = data_tmp.groupby(c)['target'].mean()
    # テストデータのカテゴリを平均値で置換
    test[c] = test[c].map(target_mean)
    
    # 学習データの返還後の値を格納する配列を作成
    tmp = np.repeat(np.nan, train.shape[0])
    
    # 学習データを分割(分割数は適宣指定する)
    kf = KFold(n_splits=4, shuffle=True, random_state=0)
    for idx_1, idx_2 in kf.split(train):
        # out-of-foldで各カテゴリにおける目的変数の平均値を計算
        target_mean = data_tmp.iloc[idx_1].groupby(c)['target'].mean()
        # 変換後の値を一時配列に格納
        tmp[idx_2] = train[c].iloc[idx_2].map(target_mean)
    
    #返還後のデータで元の変数を置換
    train[c] = tmp