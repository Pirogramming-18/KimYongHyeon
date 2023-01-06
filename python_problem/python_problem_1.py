import random
cur = 0
turn = True # true : player A, false : player B

def brGame(player):
    num = selectNumber(player)
    printNumber(num, player)

def selectNumber(player):
    num = 0
    if player == "computer":
        num = random.randint(1,3)
    else:
        while True:
            try:
                num = int(input("부를 숫자를 입력하세요(1,2,3만 입력 가능) : "))
                if(num == 1 or num == 2 or num == 3):
                    break
                else:
                    print("1,2,3 중 하나를 입력하세요")
            except ValueError:
                print("정수를 입력하세요")
                
    return num

def printNumber(num, turn):
    global cur
    for i in range(num):
        cur += 1
        if cur <= 31:
            print(f"{turn} : ", cur)
        
        
 #main 실행 코드       
while True:
    if turn: #computer turn
        brGame("computer")
    else:   #player B turn
        brGame("player")
    
    if(cur >= 31):  
        if(turn):
            print("player win!")
        else:
            print("computer win!")
        break
    turn = not turn


