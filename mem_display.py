import turtle
import Tkinter

#ref:https://docs.python.org/2/library/turtle.html
win = Tkinter.Tk()

canvas = turtle.ScrolledCanvas(win, width=1300, height=650)
canvas.pack()

window = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(window)
window.screensize(1300,2100)

x = 2000
text = 40
glob = 10
var = 30

t.speed(1000000)
t.penup()
t.goto(150 , x/2)
t.right(90)
t.pendown()
t.forward(x)
t.right(90)
t.forward(300)
t.right(90)
t.forward(x)
t.right(90)
t.forward(300)

z = text+glob+var
h = x/(z)

t.begin_fill()
t.fillcolor("#fddde6")
t.right(90)
t.forward(var*h)
t.right(90)
t.fd(300)
t.right(90)
t.fd(var*h)
t.right(90)
t.fd(300)
t.end_fill()

t.right(90)
t.fd(var*h)
t.left(90)
t.begin_fill()
t.fillcolor("#D0F0C0")
t.right(90)
t.forward(glob*h)
t.right(90)
t.fd(300)
t.right(90)
t.fd(glob*h)
t.right(90)
t.fd(300)
t.end_fill()

t.right(90)
t.fd(glob*h)
t.left(90)
t.begin_fill()
t.fillcolor("#A4DDED")
t.right(90)
t.forward(text*h)
t.right(90)
t.fd(300)
t.right(90)
t.fd(text*h)
t.right(90)
t.fd(300)
t.end_fill()

t.goto(150 ,x/2)

for i in  range(z/2):
    t.right(90)
    t.forward(h)
    t.right(90)
    t.forward(300)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(300)

t.penup()
t.left(90)
t.goto(-190, -1000+0.2*h)
for i in range(text+2):
    t.write(str(i), align="center", font = ("Arial", 16, "normal"))
    t.fd(h)

for i in range(glob+var-17):
    t.write(".", align="center", font = ("Arial", 16, "normal"))
    t.fd(h)

for i in range(1023+16-var, 1024):
    t.write(str(i) , align="center", font = ("Arial", 16, "normal"))
    t.fd(h)

f = open("D:/compiler_output.txt", 'r')
dic = f.readline()
lst = dic.split()

mem = {}
for i in range((len(lst)-4)/4):
    mem[lst[3+4*i]] = int(lst[5+4*i])

loop_index = {}

x=f.readline()
t.goto(0, -1000-h)
index = 0
for line in f.readlines():
    x = line.split()
    if (x[0] != "Loop" and x[0] != "Exit"):
        t.write(str(line) , align="center", font = ("Arial", 16, "normal"))
        t.fd(h)
        index = index + 1
    else:
        t.right(90)
        t.forward(180)
        t.write(str(line) , align="left", font = ("Arial", 16, "normal"))
        t.left(180)
        t.forward(180)
        t.right(90)
        loop_index[x[0]+x[1]] = index

for i in mem:
    t.goto(180, 1000-(1024-mem[i])*h)
    t.write(str(i) , align="center", font = ("Arial", 16, "normal"))

f.close()

t.penup()
t.goto(-230 ,1000)
t.right(180)
t.pendown()
t.begin_fill()
t.fillcolor("#dcdcdc")
t.forward(8*h)
t.right(90)
t.fd(300)
t.right(90)
t.fd(8*h)
t.right(90)
t.fd(300)
t.end_fill()


for i in  range(4):
    t.right(90)
    t.forward(h)
    t.right(90)
    t.forward(150)
    t.write("0" , align="center", font = ("Arial", 16, "normal"))
    t.forward(150)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(150)
    t.write("0" , align="center", font = ("Arial", 16, "normal"))
    t.forward(150)

t.penup()


t.goto(-560, 1000-h)
t.left(90)
for i in range(7):
    t.write("$s"+str(i) , align="center", font = ("Arial", 16, "normal"))
    t.backward(h)

t.write("$zero" , align="center", font = ("Arial", 16, "normal"))


t.goto(-230 , -1000+8*h)
t.right(180)
t.pendown()
t.begin_fill()
t.fillcolor("#dcdcdc")
t.forward(8*h)
t.right(90)
t.fd(300)
t.right(90)
t.fd(8*h)
t.right(90)
t.fd(300)
t.end_fill()


for i in  range(4):
    t.right(90)
    t.forward(h)
    t.right(90)
    t.forward(150)
    t.write("0" , align="center", font = ("Arial", 16, "normal"))
    t.forward(150)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(150)
    t.write("0" , align="center", font = ("Arial", 16, "normal"))
    t.forward(150)

t.penup()


t.goto(-560, -1000+7*h)
t.left(90)
for i in range(7):
    t.write("$s"+str(i) , align="center", font = ("Arial", 16, "normal"))
    t.backward(h)

t.write("$zero" , align="center", font = ("Arial", 16, "normal"))

t.goto(-230, -1000+10*h)
t.right(180)
t.pendown()
t.begin_fill()
t.fillcolor("#ffffcc")
t.forward(h)
t.right(90)
t.fd(300)
t.right(90)
t.fd(h)
t.right(90)
t.fd(300)
t.end_fill()
t.penup()

t.goto(-560, -1000+9*h)
t.left(90)
t.write("PC" , align="center", font = ("Arial", 16, "normal"))

c = 0

def PCinc(c):
    t.goto(-230, -1000+10*h)
    t.right(180)
    t.pendown()
    t.begin_fill()
    t.fillcolor("#ffffcc")
    t.forward(h)
    t.right(90)
    t.fd(300)
    t.right(90)
    t.fd(h)
    t.right(90)
    t.fd(300)
    t.end_fill()
    t.penup()

    t.goto(-380, -1000+9*h)
    t.left(90)
    t.write(str(c) , align="center", font = ("Arial", 16, "normal"))


def varval(a, val):
    t.goto(150, 1000-(a)*h)
    t.right(180)
    t.pendown()
    t.begin_fill()
    t.fillcolor("#fddde6")
    t.forward(h)
    t.right(90)
    t.fd(300)
    t.right(90)
    t.fd(h)
    t.right(90)
    t.fd(300)
    t.end_fill()
    t.penup()

    t.goto(0, 1000-(a+1)*h)
    t.left(90)
    t.write(str(val) , align="center", font = ("Arial", 16, "normal"))

def regval(a, val):
    t.penup()
    t.goto(-230 ,1000-a*(h))
    t.right(180)
    t.pendown()
    t.begin_fill()
    t.fillcolor("#dcdcdc")
    t.forward(h)
    t.right(90)
    t.fd(300)
    t.right(90)
    t.fd(h)
    t.right(90)
    t.fd(300)
    t.end_fill()
    t.penup()

    t.goto(-380, 1000-(a+1)*(h))
    t.left(90)
    t.write(str(val) , align="center", font = ("Arial", 16, "normal"))


    t.goto(-230, -1000+(8-a)*h)
    t.right(180)
    t.pendown()
    t.begin_fill()
    t.fillcolor("#dcdcdc")
    t.forward(h)
    t.right(90)
    t.fd(300)
    t.right(90)
    t.fd(h)
    t.right(90)
    t.fd(300)
    t.end_fill()
    t.penup()

    t.goto(-(380), -1000+(7-a)*h)
    t.left(90)
    t.write(str(val) , align="center", font = ("Arial", 16, "normal"))

def fun(x, y):
    global c
    global d
    global h
    t.fd(h)
    c=c+1
    if (d.get(c,-1) == -1):
        q = lst[c].split()
        if q[0] == "lw":
            t.penup()
            t.goto(170, -1010)
            t.pd()
            t.color("white")
            t.begin_fill()
            t.fillcolor("white")
            t.forward(50)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.end_fill()
            t.penup()
            t.color("black")
            t.goto(180 ,-1000)
            t.write("The value is loaded from " + str(mem[q[3][:len(q[3])-1]])+ " to register " +q[1] , align="left", font = ("Arial", 16, "normal"))
            reg_val[q[1]] = var_val[q[3][:len(q[3])-1]]
            regval(int(q[1][2]), reg_val[q[1]])
        elif q[0] == "sw":
            t.penup()
            t.goto(170, -1010)
            t.pd()
            t.color("white")
            t.begin_fill()
            t.fillcolor("white")
            t.forward(50)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.end_fill()
            t.penup()
            t.color("black")
            t.goto(180 ,-1000)
            t.write("The value from " + q[1] + " is stored to " +str(mem[q[3][:len(q[3])-1]]) , align="left", font = ("Arial", 16, "normal"))
            var_val[q[3][:len(q[3])-1]] = reg_val[q[1]]
            varval(1023-mem[q[3][:len(q[3])-1]], reg_val[q[1]])
        elif q[0] == "addi":
            t.penup()
            t.goto(170, -1010)
            t.pd()
            t.color("white")
            t.begin_fill()
            t.fillcolor("white")
            t.forward(50)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.end_fill()
            t.penup()
            t.color("black")
            t.goto(180 ,-1000)
            t.write("The value " + q[5][:len(q[5])-1] + " is added to " +q[3] +" and stored in " + q[1], align="left", font = ("Arial", 16, "normal"))
            reg_val[q[1]] = reg_val[q[3]] + int(q[5][:len(q[5])-1])
            regval(int(q[1][2]), reg_val[q[1]])
        elif q[0] == "add":
            t.penup()
            t.goto(170, -1010)
            t.pd()
            t.color("white")
            t.begin_fill()
            t.fillcolor("white")
            t.forward(50)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.end_fill()
            t.penup()
            t.color("black")
            t.goto(180 ,-1000)
            t.write("The value " + q[5][:len(q[5])-1] + " is added to " +q[3] +" and stored in " + q[1], align="left", font = ("Arial", 16, "normal"))
            reg_val[q[1]] = reg_val[q[3]] + reg_val[q[5][:len(q[5])-1]]
            regval(int(q[1][2]), reg_val[q[1]])
        elif q[0] == "mul":
            t.penup()
            t.goto(170, -1010)
            t.pd()
            t.color("white")
            t.begin_fill()
            t.fillcolor("white")
            t.forward(50)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.end_fill()
            t.penup()
            t.color("black")
            t.goto(180 ,-1000)
            t.write("The value " + q[5][:len(q[5])-1] + " is multiplied to " +q[3] +" and stored in " + q[1], align="left", font = ("Arial", 16, "normal"))
            reg_val[q[1]] = reg_val[q[3]] * reg_val[q[5][:len(q[5])-1]]
            regval(int(q[1][2]), reg_val[q[1]])
        elif q[0] == "j":
            t.penup()
            t.goto(170, -1010)
            t.pd()
            t.color("white")
            t.begin_fill()
            t.fillcolor("white")
            t.forward(50)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(600)
            t.right(90)
            t.end_fill()
            t.penup()
            t.color("black")
            t.goto(180 ,-1000)
            t.write("The program counter jumps to " + str(loop_index[q[1]+q[2][:len(q[2])-1]]), align="left", font = ("Arial", 16, "normal"))
            c = loop_index["Loop" + q[2][:len(q[2])-1]]
        elif q[0] == "beq":
            if reg_val[q[1]] == int(q[3]):
                t.penup()
                t.goto(170, -1010)
                t.pd()
                t.color("white")
                t.begin_fill()
                t.fillcolor("white")
                t.forward(50)
                t.right(90)
                t.forward(600)
                t.right(90)
                t.forward(50)
                t.right(90)
                t.forward(600)
                t.right(90)
                t.end_fill()
                t.penup()
                t.color("black")
                t.goto(180 ,-1000)
                t.write("The program counter jumps to " + str(loop_index[q[5]+q[6][:len(q[6])-1]]), align="left", font = ("Arial", 16, "normal"))
                c = loop_index["Exit" + q[6][:len(q[6])-1]]
            else:
                t.penup()
                t.goto(170, -1010)
                t.pd()
                t.color("white")
                t.begin_fill()
                t.fillcolor("white")
                t.forward(50)
                t.right(90)
                t.forward(600)
                t.right(90)
                t.forward(50)
                t.right(90)
                t.forward(600)
                t.right(90)
                t.end_fill()
                t.penup()
                t.color("black")
                t.goto(180 ,-1000)
                t.write("Condition doesn't satisfy, program continues", align="left", font = ("Arial", 16, "normal"))
    PCinc(c)
    


reg_val = {"$s0" : 0, "$s1" : 0, "$s2" : 0, "$s3" : 0, "$s4" : 0, "$s5" : 0, "$s6" : 0, "$zero" : 0}
var_val = {}
for i in mem:
    var_val[i] = 1


t.goto(180, -1000-h)
f = open("D:/compiler_output.txt", 'r')
dic = f.readline()



x = f.readline()
lst = []
lst.append(x)
for line in f.readlines():
    if line.split()[0] != "Loop" and line.split()[0] != "Exit":
        lst.append(line)

print lst 
d = {}
window.onclick(fun)
f.close()

win.mainloop()
