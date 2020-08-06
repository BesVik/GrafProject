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

brushColor(255, 255, 255)
circle(300, 70, 20)
circle(280, 70, 20)
circle(260, 70, 20)
circle(240, 70, 20)
circle(220, 70, 20)
circle(240, 55, 20)
circle(260, 55, 20)
circle(280, 55, 20)

run()
