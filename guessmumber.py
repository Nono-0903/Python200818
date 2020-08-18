import random
no = random.randint(1,20)
i=0
while i<5:
    ans = int(input("請輸入數字:"))
    if ans == no :
        print("恭喜答對!!")
        print('你總共猜了',i+1,'次')
        break
    else :
        if no < ans:
            print("太大了")
        else:
            print("太小了")
    i=i+1
