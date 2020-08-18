import random
no = random.randint(1,10)
ans = int(input("請輸入整數數字1-10:"))
    
if no == ans :
        print("恭喜答對!!")
else :
        print("錯了哈哈!!")
        print("答案是",no)
