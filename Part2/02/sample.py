def main():                                     # メインという関数を定義
    """
    サンプルプログラムのメイン関数
    """

    for i in range(1, 6):                       # 1 から 5 までのループ処理
        if i % 2 == 0:                          # 偶数かどうかのチェック
            print("%sは偶数です。" % i)           # 偶数の場合に出力
        else:
            print("%sは奇数です。" % i)           # 奇数の場合に出力

if __name__ == "__main__":                      # コマンドラインからの実行かどうかの制御
    main()                                      # main() 関数を呼び出す
