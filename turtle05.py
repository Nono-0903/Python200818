import turtle
m = int(input("請輸入你要的正多邊形邊數:"))
for i in range(m):
    turtle.forward(1)
    turtle.right(360/m)
turtle.done()