print("kółko i krzyrzyk")
print("jest to gra dla dwóch graczy")
empty = "_"
board = [empty, empty, empty, empty, empty, empty, empty, empty, empty]
def print_board(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

def dostepne_pola(board):
    dostepne = []
    if board[0] == empty:
        dostepne.append(1)
    if board[1] == empty:
        dostepne.append(2)
    if board[2] == empty:
        dostepne.append(3)
    if board[3] == empty:
        dostepne.append(4)
    if board[4] == empty:
        dostepne.append(5)
    if board[5] == empty:
        dostepne.append(6)
    if board[6] == empty:
        dostepne.append(7)
    if board[7] == empty:
        dostepne.append(8)
    if board[8] == empty:
        dostepne.append(9)
    return dostepne

def wybor_gracza(gracz, board, dostepne):
    wybor = int(input("wpisz swój wybór (musi być w dostępnych): "))
    while wybor not in dostepne:
        wybor = int(input("wpisz swój wybór (musi być w dostępnych): "))
    else:
        print("")
    empty = "_"
    if gracz == "x":
        board[wybor - 1] = "x"
    else:
        board[wybor - 1] = "o"
    return board


def bot(board, tura):
    choice = 4
    packs = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]] # all the winning combinations
    if tura == 2:
        if board[4] == empty:
            choice = 4
        else:
            choice = 0
    is_winning = False
    pom1 = []
    pom_o = []
    if tura == 4:
        for pack in packs:
            for i in pack:
                if board[i] == "x":
                    pom1.append(i)
            if len(pom1) == 2:
                pom = pack
                choice_list = [x for x in pom if (x not in pom1)]
                if not board[choice_list[0]] == empty:
                    print("soup")
                    break
                print(choice_list[0])
                return choice_list[0]
            pom1 = []
        if board[1] == empty and board[7] != "x":
            return 1
        if board[7] == empty and board[1] != "x":
            return 7
        if board[5] == empty and board[3] != "x":
            return 5
        if board[3] == empty and board[5] != "x":
            return 3
        if board[0] == empty and board[8] != "x":
            return 0
        if board[2] == empty and board[6] != "x":
            return 2
        if board[6] == empty and board[2] != "x":
            return 6
        if board[8] == empty and board[0] != "x":
            return 8

    if tura == 6:
        for pack in packs:
            for i in pack:
                if board[i] == "o":
                    pom_o.append(i)
                if board[i] == "x":
                    pom1.append(i)
            if len(pom_o) == 2:
                pom = pack
                choice_list = [o for o in pom if (o not in pom_o)]
                if not board[choice_list[0]] == empty:
                    break
                print("soup", choice_list[0])
                return choice_list[0]
            if len(pom1) == 2:
                pom = pack
                choice_list = [x for x in pom if (x not in pom1)]
                if not board[choice_list[0]] == empty:
                    break
                print("soupx", choice_list[0])
                return choice_list[0]
            pom1 = []
            pom_o = []
    return choice







def check_win(board):
    zwyciezca = "nikt"
    if board[2] == board[5] == board[8] and board[8] != "_" or board[6] == board[7] == board[8] and board[8] != "_":
        zwyciezca = board[8]
    if board[0] == board[3] == board[6] and board[0] != "_" or board[0] == board[4] == board[8] and board[0] != "_" or board[0] == board[1] == board[2] and board[0] != "_":
        zwyciezca = board[0]
    if board[1] == board[4] == board[7] and board[4] != "_" or board[3] == board[4] == board[5] and board[4] != "_" or board[2] == board[4] == board[6] and board[4] != "_":
        zwyciezca = board[4]
    return zwyciezca
gracz = "x"
tura = 0

play = input("chcesz grać? Wpisz 2 by grać w 2 osoby albo 1 by grać z botem: ")
while play == "2" or play == "1":
    tura += 1
    print_board(board)
    print("tura nr. ", str(tura)," gracza ", gracz)
    dostepne = dostepne_pola(board)
    if play =="2":
        print("wybierz pole, w którym chcesz postawić ", gracz)
        print("dostępne pola:")
        print(dostepne)
        board = wybor_gracza(gracz, board, dostepne)
    else:
        if gracz == "o":
            board[bot(board, tura)] = "o"
        else:
            print("wybierz pole, w którym chcesz postawić ", gracz)
            print("dostępne pola:")
            print(dostepne)
            board = wybor_gracza(gracz, board, dostepne)


    zwyciezca = check_win(board)
    if zwyciezca == "nikt":
        if dostepne_pola(board) == []:
            print("Niestety, po ", tura, " turze był remis.")
            print_board(board)
            board = [empty, empty, empty, empty, empty, empty, empty, empty, empty]
            tura = 0
            play = input("Chcesz dalej grać? Wpisz 2 by grać w 2 osoby: ")
            gracz = "x"
        else:
            if gracz == "x":
                gracz = "o"
            else:

                gracz = "x"

    elif zwyciezca != "nikt":
        print("Gratulacje. Po ", tura, " turze wygrał gracz ", gracz)
        print_board(board)
        board = [empty, empty, empty, empty, empty, empty, empty, empty, empty]
        tura = 0
        play = input("Chcesz dalej grać? Wpisz 2 by grać w 2 osoby: ")
        gracz = "x"

#https://youtu.be/WeELPnZqhow?list=TLPQMTExMjIwMjHP94udPzkpww