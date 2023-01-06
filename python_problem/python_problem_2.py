data = {}   # key : name / value [name, mid, final, grade]

#메뉴 2번에서 사용
#점수 2개를 입력 받아 점수에 맞는 등급 반환
def calGrade(score1, score2):
    ev = (score1 + score2) / 2
    if(ev >= 90):
        return 'A'
    elif(ev >= 80):
        return 'B'
    elif(ev >= 70):
        return 'C'
    else:
        return 'D'

#메뉴 3번에서 사용
#data에 저장된 학생 정보를 형식에 맞게 출력
def showInfo():
    print("-" * 30)
    print("name   mid   final   grade")
    print("-" * 30)
    for li in list(data.values()):       
        print(f"{li[0]}     {li[1]}      {li[2]}       {li[3]}")

##############  menu 1
def menu1(name, score1, score2) :
    data[name] = [name, score1, score2, ""]

##############  menu 2
def menu2() :
    for target in list(data.values()):        
        if(target[3] == ""):
            target[3] = calGrade(target[1], target[2])
        
##############  menu 3
def menu3() :
    showInfo()
    
##############  menu 4
def menu4(name):
    data.pop(name, None)
    print(f"{name} student information is deleted")
    

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    try:
        choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    except ValueError:
        print("Wrong number. Choose again.")
        
    if choice == "1":
        info = input("Enter name mid-score final-score : ").split()
        
        #데이터 개수 검증
        if(len(info) != 3): 
            print("Num of data is not 3!")
            continue
        
        name = info[0]
        
        #이름 중복 검증            
        if(name in data.keys()):
            print("Already exist name!")
            break
        
        mid = -1; final = -1
        try:
            mid = int(info[1]); final = int(info[2])
        except ValueError:
            print("Score is not a positive integer!")
            continue
        
        #점수 값 양의 정수 검증
        if(mid < 0 or final < 0):
            print("Score is not a positive integer!")
            continue
        
        menu1(name, mid, final)
        
        
    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if(len(data) == 0):
            print("No student data!")
            continue
        
        menu2()
        print("Grading to all students.")
        
    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if(len(data) == 0):
            print("No student data!")
            continue
        
        #학점이 부여되지 않은 학생이 있는 경우 에외 처리
        try:
            for target in list(data.values()):                
                if(target[3] == ""):
                    raise Exception
        except:
            print("There is a student who didn't get grade")
            continue
        
        menu3()
            
            
    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if(len(data) == 0):
            print("No student data!")
            continue
        
        target = input("Enter the name to delete : ")  
        #데이터에 존재하지 않는 학생인 경우 예외처리      
        if(target not in data.keys()):
            print("Not exist name!")
            continue
        
        menu4(target)
        
        
    elif choice == "5" :        
        print("Exit Program!")
        break
        
    else :         
        #정수이나 1~5 값이 아닐 경우 예외처리
        print("Wrong number. Choose again.")               
    