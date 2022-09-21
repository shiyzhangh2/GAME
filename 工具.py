#模块导入
from random import *
from os import *
from calendar import *
from time import *
from tkinter import *

#函数定义
def echo(guess_number,x):
    if x > guess_number:
        return 1
    elif x < guess_number:
        return -1
    else:
        return 0

def button1():
    label_1.config(text = '计算机 和 差 积 前面可以加上……')
    label_2.config(text = '面积 可以加上 三角形 圆形……')
    label_3.config(text = '打开软件 可以加上其他软件 如：system(软件英文名)')
    label_4.config(text = '工作计时器 时间到的时候加上音乐')
    label_5.config(text = '其他功能也可加强，也可以自己做')
    button_2 = Button(root,text = '退出',fg = 'red',command = button2)
    button_3 = Button(root,text = '小游戏',fg = 'orange',command = button3)
    button_2.pack()
    button_3.pack()

def button2():
    root.quit()

def button3():
    system("猜数游戏.py")
                      

print('欢迎您的到来！')
while True:
    print('构个三角形（1）计算机（2）面积（3）几位数（4）鸡兔同笼（5）九九乘法表（6）自定义乘法表（7）随便打字（8）华氏度转摄氏度 或 摄氏度转华氏度（9）周长（10）猜数（11）打开软件（12）工作计时器（13）自己改一改（GUI）')
    yao = input()
    if yao == '1':
        print('三角形')
        A = input()
        B = input()
        C = input()
        if A + B > C and A + C > B and B + C > A:
            print('能构出三角形')
        else:
            print('不能构出三角形')
    elif yao == '2':
        print('计算机')
        print('要计算小数（1）还是普通数（2）')
        S = input()
        print('输入数字')
        a = input()
        b = input()
        if S == '1':
            a = float(a)
            b = float(b)
        elif S == '2':
            a = int(a)
            b = int(b)
        else:
            print('请输入1或2!')
        print(a + b)
        print(a - b)
        print(a * b)
        a1 = a // b
        b2 = a % b
        a1 = str(a1)
        b2 = str(b2)
        print('商是' + a1)
        print('余数是' + b2)
        if a % 2 == 1:
            print('第一个数是单数')
        else:
            print('第一个数是双数')
        if b % 2 == 1:
            print('第二个数是单数')
        else:
            print('第二个数是双数')
        if a > b:
            print('第一个数最大')
        elif a < b:
            print('第二个数最大')
        elif a == b:
            print('两个数一样大')
    elif yao == '3':
        print('面积（正方形或长方形）（先写长，再写宽）')
        Bian_Chang = input()
        Bian_Kuan = input()
        Bian_Chang = int(Bian_Chang)
        Bian_Kuan = int(Bian_Kuan)
        print(Bian_Chang * Bian_Kuan)
    elif yao == '4':
        print('几位数（输入一个多位数吧！)')
        Shu = input()
        Wei_Shu = len(Shu)
        Wei_Shu = str(Wei_Shu)
        print(Wei_Shu + '位数')
    elif yao == '5':
        print('鸡兔同笼（先头再脚）（没回答就是题目不成立）')
        heads = input()
        legs = input()
        heads = int(heads)
        legs = int(legs)
        for i in range(1,heads + 1):
            if i * 2 + (heads - i) * 4 == legs:
                print("chickens:",i)
                print("rabit:",heads - i)
    elif yao == '6':
        for i in range(1,10):
            for j in range(1,10):
                print("%d*%d =%2d"%(i,j,i * j),end = " ")
        print(" ")
    elif yao == '7':
        num = int(input("请输入要显示乘法表的数："))
        j = int(input("请输入要乘的最大数："))
        print(num,"对应的乘法表为：")
        for i in range(1,j + 1):
            print(num,"*",i,"=",num * i)
    elif yao == '8':
        print('随便打字（输入 quit 退出！）')
        while True:
            Da_Zi = input()
            if Da_Zi == 'quit':
                break
    elif yao == '9':
        print('转换温度')
        print('你要转摄氏度（1）还是华氏度（其他按键）')
        Wen_Xuan = input()
        if Wen_Xuan == '1':
            C = float(input("请输入要转换的摄氏温度值："))
            F = 1.8 * C + 32
            print("对应的华氏温度为：",F)
        else:
            F = float(input("请输入要转换的华氏温度值："))
            C = (F - 32) / 1.8
            print("对应的摄氏温度为：",C)
    elif yao == '10':
        print('周长（正方形或长方形）')
        Chang = int(input("请输入长："))
        Kuan = int(input("请输入宽："))
        Zhou_Chang = (Chang + Kuan) * 2
        print(Zhou_Chang)
    elif yao == '11':
        print('两人猜数（1）一人猜数（2）')
        C_XZ = input()
        if C_XZ == '1':
            print('一人写数一人猜')    
            print('无限猜数（猜到全对为止）（1）')
            print('限次猜数（只有*次猜数机会）（推荐）（2）')
            C_M = input()
            if C_M == '1':
                print('无限猜数')
                print('写数人请写数（猜数人不要看哦！！！）')
                C_SHU1 = input()
                print('你的提示是：')
                C_T = input()
                for i in range(50):
                    print('不能翻上面！！！')
                print('开始猜数！！！')
                print(C_T)
                while True:
                    C_C = input()
                    if C_C  == C_SHU1:
                        print('答对了！！！')
                        break
                    if C_C > C_SHU1:
                        print('大了')
                        continue
                    if C_C < C_SHU1:
                        print('小了')
                        continue
            elif C_M == '2':
                print('限次猜数')
                print('写数人请写数（猜数人不要看哦！！！）')
                C_SHU1 = input()
                print('你给猜数人几次机会？')
                C_J = input()
                C_J = int(C_J)
                print('你的提示是：')
                C_T = input()
                for i in range(50):
                    print('不能翻上面！！！')
                print('你的机会有：')
                print(C_J)
                print('开始猜数！！！')
                print(C_T)
                for j in range(C_J):
                    C_C = input()
                    if C_C  == C_SHU1:
                        print('答对了！！！')
                        break
                    if C_C > C_SHU1:
                        print('大了')
                        continue
                    if C_C < C_SHU1:
                        print('小了')
                        continue
        elif C_XZ == '2':
            print('10次机会')
            x = randint(1,1000)
            count = 1
            while count <= 10:
                gn = int(input("请猜数（第%d次）："%count))
                check = echo(gn,x)
                if check == 0:
                    break
                elif check > 0:
                    print("猜小了！")
                else:
                    print("猜大了！")
                count = count + 1
            if count > 10:
                print("游戏结束，你失败了！")
            else:
                print("恭喜你猜对了，共猜了%d次"%count)
        print('GAME OVER')
    elif yao == '12':
        print('打开记事本（1）放大镜（2）计算机（3）画图（4）')
        RJ = input()
        if RJ == '1':
            system("notepad")
        elif RJ == '2':
            system("magnify")
        elif RJ == '3':
            system("calc")
        elif RJ == '4':
            system("mspaint")
    elif yao == '13':
        print('此功能只支持一直在电脑面前的人计时，长时间离开电脑屏幕的人不支持使用')
        JSQ = int(input('请输入计时的秒数（建议300秒内）：'))
        print('正在计时中ing……')
        sleep(JSQ)
        for i in range(10):
            print('时间到！！！')            


    elif yao == 'GUI':
        print('看任务栏')
        root = Tk(className = '自己改教程')
        label_1 = Label(root,text = '点击按钮开始改一改教程',height = 2,width = 40,fg = 'blue')
        label_2 = Label(root,text = '',fg = 'blue')
        label_3 = Label(root,text = '',fg = 'blue')
        label_4 = Label(root,text = '',fg = 'blue')
        label_5 = Label(root,text = '',fg = 'blue')
        button_1 = Button(root,text = '开始教程',command = button1)
        label_1.pack()
        label_2.pack()
        label_3.pack()
        label_4.pack()
        label_4.pack()
        label_5.pack()
        button_1.pack()
        root.mainloop()
            
    print('你要再来一次吗?（1 = 来）（其他按键 = 不来）')
    yao_ma = input()
    if yao_ma == '1':
        print('继续开始喽！')
        continue
    else:
        print('已退出！')
        break
