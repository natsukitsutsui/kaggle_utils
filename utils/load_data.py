#データの読み込み
def load_data(id_=ID, target_col=TARGET_COL, path_train=DATA_TRAIN_PATH, path_test=DATA_TEST_PATH):
    """
    データの読み込みを行う関数
    Parameters
    ----------
    id: str
        データのid
    target_col: str
        目的変数の列名
    path_train: str
        訓練データのパス
    path_test: str
        テストデータのパス

    Returns
    ----------
    train: DataFrame
        訓練データ(idと目的変数を除いたもの)
    train_labels: DataFrame
        訓練データの目的変数
    train_ids: DataFrame
        訓練データのid
    features: list
        trainの列一覧
    test: DataFrame
        テストデータ(提出する用のデータ)
    test_ids: DataFrame
        テストデータのid(最後に予測結果とconcatして提出)
    """
    train_loader = pd.read_csv(path_train)
    train = train_loader.drop([target_col, id_], axis=1)
    features = train.columns.tolist()
    print("\n 訓練データの大きさ:", train.shape)
    train_labels = train_loader[target_col]
    train_ids = train_loader[id_]

    test_loader = pd.read_csv(path_test)
    test = test_loader[features]
    print(" テストデータの大きさ:", test.shape)
    test_ids = test_loader[id_]

    return train, train_labels, train_ids, features, test, test_ids