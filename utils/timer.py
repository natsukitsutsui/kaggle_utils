#計算時間の測定
def timer(start_time=None):
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        tmin, tsec = divmod((datetime.now() - start_time).total_seconds(), 60)
        print(" 計算時間: %i 分 %s 秒." % (tmin, round(tsec, 2)))