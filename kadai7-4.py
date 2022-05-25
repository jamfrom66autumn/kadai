tic_tac_toe = [["　","〇","×"],["｜","＋","－"]] #二次元配列を用意する、一つ目のリストに␣、〇、×を含め二つ目のリストに区切りとナル記号を挿入

for p in [0,1,0,1,2]:#pの場合分けによって表示させる内容を変化させる
    if p == 0:#pが0の時に×｜〇｜　を表示させる
        print(tic_tac_toe[p][2],tic_tac_toe[p+1][0],tic_tac_toe[p][1],tic_tac_toe[p+1][0],tic_tac_toe[p][0])
    elif p == 1:#pが1の時に－＋－＋－を表示させる
        print(tic_tac_toe[p][2],tic_tac_toe[p][1],tic_tac_toe[p][2],tic_tac_toe[p][1],tic_tac_toe[p][2])
    elif p == 2:#pが2のときに〇｜　｜　を表示させる
        print(tic_tac_toe[p-2][1],tic_tac_toe[p-1][0],tic_tac_toe[p-2][0],tic_tac_toe[p-1][0],tic_tac_toe[p-2][0])
