import sys
game_on = True
sqr = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
#fzr melhor menu inicial e colocar menu final e pve
def game_init():# se o x ganhar n faz print do jogo no fim
    print("Welcome!")
    print("Choose a game mode: ")
    print(" ")
    print("1.pvp")
    print("2.pve")#primeiro random, e se encontrar 2 em linha tentar por o 3
    print("3.quit")
    print(" ")
    x = int(input())
    print(" ")
    if x == 1:
        run_pvp()
    elif x == 2:
        run_pve()
    elif x == 3:
        sys.exit()
    else:
        print("Invalid option!")
        game_init()    

def run_pve():
    print("Game mode Unavailable")
    print(" ")
    game_init()

def run_pvp():
    while game_on:#fzr for aqui
        check_end('X')
        draw_board()
        get_sqr('O')
        draw_board()
        check_end('O')
        get_sqr('X')

def draw_board():
    print("   1     2     3  x")
    print("      |     |     ")
    print("1  "+sqr[0][0]+"  |  "+sqr[0][1]+"  |  "+sqr[0][2]+"  ")
    print(" _____|_____|_____")
    print("      |     |    ")
    print("2  "+sqr[1][0]+"  |  "+sqr[1][1]+"  |  "+sqr[1][2]+"  ")
    print(" _____|_____|_____")
    print("      |     |     ")
    print("3  "+sqr[2][0]+"  |  "+sqr[2][1]+"  |  "+sqr[2][2]+"  ")
    print("      |     |     ")
    print('y')
    print(" ")

def get_sqr(player):
    sqrx = 5
    sqry = 5
    try:
        sqrx = int(input("x coordinate: "))
        sqry = int(input("y coordinate: "))
        if (sqrx > 0 and sqrx < 4 and sqry > 0 and sqry < 4) and sqr[sqrx-1][sqry-1] == " ":
            sqr[sqry-1][sqrx-1] = player
        else:
            q = input("Invalid coordenates!\nDo u wanna quit?(y/n) ")
            if q.upper() == "Y":
                sys.exit()
            else:
                get_sqr(player)
    except:
        q = input("Invalid coordenates!\nDo u wanna quit?(y/n) ")
        if q.upper() == "Y":
            sys.exit()
        else:
            get_sqr(player)

def check_end(player):#fzr com for
    i = 0
    while i < 3:
        if sqr[0][i] == sqr[1][i] and sqr[1][i] == sqr[2][i] and sqr[0][i] != " ":
            print(player + " win!")
            sys.exit()
        i += 1    
    while i < 3:
        if sqr[i][0] == sqr[i][1] and sqr[i][1] == sqr[i][2] and sqr[i][0] != " ":
            print(player + " win!")
            sys.exit()
        i += 1 
    if sqr[0][0] == sqr[1][1] and sqr[1][1] == sqr[2][2] and sqr[0][0] != " ":
        print(player + " win!")
        sys.exit()  
    if sqr[0][2] == sqr[1][1] and sqr[1][1] == sqr[2][0] and sqr[2][0] != " ":
        print(player + " win!")
        sys.exit() 
game_init()
#trocar sistema de desenho e de coordenadas de forma a que o desenho seja automatico, a decalração de cooredenadas tambem e por fim que e para receber as duas coordenadas de uma vez