from graph import *

windowSize(500, 600)

brushColor(175, 238, 238)  # цвет неба
rectangle(0, 0, 500, 300)  # небо
brushColor(0, 255, 0)  # цвет земли
rectangle(0, 300, 500, 600)  # земля

brushColor(178, 34, 34)
rectangle(75, 250, 250, 400)  # стены

brushColor(0, 206, 209)
rectangle(125, 275, 200, 325)  # окно

brushColor(255, 0, 0)
polygon([(55, 250), (160, 200), (270, 250), (55, 250)])  # крыша

brushColor(139, 0, 0)
rectangle(400, 250, 420, 430)  # ствол дерева

brushColor(0, 200, 0)
penSize(2)
circle(400, 250, 30)
circle(420, 250, 30)
circle(430, 220, 30)
circle(380, 220, 30)
circle(400, 200, 40)  # крона дерева

brushColor(255, 255, 0)
circle(420, 70, 50)  # солнце

x = 300

brushColor(255, 255, 255)
obj = circle(x, 70, 20)
if x == 380:
    brushColor(70, 130, 180)
    rectangle(0, 0, 500, 300)
    brushColor(50, 205, 50)
    rectangle(0, 300, 500, 600)
obj1 = circle(280, 70, 20)
obj2 = circle(260, 70, 20)
obj3 = circle(240, 70, 20)
obj4 = circle(220, 70, 20)
obj5 = circle(240, 55, 20)
obj6 = circle(260, 55, 20)
obj7 = circle(280, 55, 20)



def keyPressed(event):
    if event.keycode == VK_RIGHT:
        moveObjectBy(obj, 2, 0)
        moveObjectBy(obj1, 2, 0)
        moveObjectBy(obj2, 2, 0)
        moveObjectBy(obj3, 2, 0)
        moveObjectBy(obj4, 2, 0)
        moveObjectBy(obj5, 2, 0)
        moveObjectBy(obj6, 2, 0)
        moveObjectBy(obj7, 2, 0)
    elif event.keycode == VK_LEFT:
        moveObjectBy(obj, -2, 0)
        moveObjectBy(obj1, -2, 0)
        moveObjectBy(obj2, -2, 0)
        moveObjectBy(obj3, -2, 0)
        moveObjectBy(obj4, -2, 0)
        moveObjectBy(obj5, -2, 0)
        moveObjectBy(obj6, -2, 0)
        moveObjectBy(obj7, -2, 0)


onKey(keyPressed)



run()
