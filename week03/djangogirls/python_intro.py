print("Hello, Django Girls!")
volume = 57
# volume 값을 바꿔보세요
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
    
def hi(name):
    print('Hi ' + name + '!')

hi("김용현")

girls = ['김용현', '이용현', '박용현', '최용현', '주용현']
for name in girls:
    hi(name)
    print('Next 용현')