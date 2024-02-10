import turtle

# 화면 설정
wn = turtle.Screen()
wn.title("Turtle Star")
wn.bgcolor("lightgreen")

# 거북이 설정
star = turtle.Turtle()
star.color("blue")

# 별 그리기
for i in range(5):
    star.forward(150)
    star.right(144)

# 종료를 위한 클릭 대기
wn.mainloop()
