cur = 0
turn = True # true : playerA, false : playerB

def selectNumber():
    num = 0
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

def printNumber(num, player):
    global cur
    for i in range(num):
        cur += 1
        if cur <= 31:
            print(f"player{player} : ", cur)
        
        
 #main 실행 코드       
while True:
    if turn: #playerA turn
        num = selectNumber()
        printNumber(num, "A")
    else:
        num = selectNumber()
        printNumber(num, "B")
    
    if(cur >= 31):
        if(turn):
            print("player B win!")
        else:
            print("player A win!")
        break
    turn = not turn


