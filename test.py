import matplotlib.pyplot as plt #ヒストグラムの表示用

list = []# 空のリスト作成
count =0 #while文の繰り返しでのカウント数
num = 101#100は偶数であるため考える必要がないため

def isPrime(n):         #素数判定関数
    a = n**(1/2)        #入力値の平方根を取っている
    i = 2               #繰り返し処理の初期値を2としている
    if n <= 2:          #入力値が２以下の時は処理しない
        return False
    else:                      #入力値が2より大きいときの処理
        while i <= a:          #素数かどうかを平方根の値まで素数から割る処理
            if n % i == 0:     #割り切れるとその数で約数を持つため素数ではない
                return False
            i += 1
        return True            #１とその数のみが割り切れる数なので素数

def addPrime(s):               #与えられた数が素数ならリストに加える関数
    if isPrime(s) == True:     #isPrime関数の値がTrueの時の処理
        list.append(s)         #listに値を加える

while len(list) < 20:          #listの中の要素数が20になるまで処理を続ける
    num -= 2*count*(-1)**count #工夫したポイントcountの値をうまく組み合わせることで記述のダブりのカット
    addPrime(num)              #addPrime関数の実行
    count += 1                 #このタイミングでcountを+1することでcount=0を生かした処理にする


print(sorted(list, reverse=True))            #素数を大きい順で表示

n,bins, patches=plt.hist(list,bins = 40)     #ヒストグラム表示準備
plt.xlabel("values")                         #x軸のラベル決め
plt.ylabel("frequency")                      #y軸のラベル決め
plt.title("histogram")                       #ヒストグラムのタイトル決め
plt.show()                                   #ヒストグラムの表示