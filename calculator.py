from tkinter import *
from decimal import Decimal

# Variables
val = ""
A = 0
B = 0
C = 0
operator = ""
valS = ""


# Functions
def check_events(event):
    if event.keysym == "0":
        btn0_clicked()
    if event.keysym == "1":
        btn1_clicked()
    if event.keysym == "2":
        btn2_clicked()
    if event.keysym == "3":
        btn3_clicked()
    if event.keysym == "4":
        btn4_clicked()
    if event.keysym == "5":
        btn5_clicked()
    if event.keysym == "6":
        btn6_clicked()
    if event.keysym == "7":
        btn7_clicked()
    if event.keysym == "8":
        btn8_clicked()
    if event.keysym == "9":
        btn9_clicked()
    if event.keysym == "plus":
        btn_plus_clicked()
    if event.keysym == "minus":
        btn_minus_clicked()
    if event.keysym == "slash":
        btn_div_clicked()
    if event.keysym == "asterisk":
        btn_mult_clicked()
    if event.keysym == "asciicircum":
        btn_deg_clicked()
    if event.keysym == "period":
        btn_point_clicked()
    if event.keysym == "Return" or event.keysym == "equal":
        btn_equ_clicked()
    if event.keysym == "Escape":
        btn_c_clicked()
    if event.keysym == "Delete":
        btn_ce_clicked()
    if event.keysym == "BackSpace":
        btn_back_clicked()


def btn_point_clicked():
    global val
    if len(val) < 15 and "." not in val and val != "":
        val += "."
        data.set(val)
    else:
        pass


def btn0_clicked():
    global val
    if len(val) < 15 and val != "0":
        val += "0"
        data.set(val)
    else:
        pass


def btn1_clicked():
    global val
    if len(val) < 15:
        val += "1"
        data.set(val)
    else:
        pass


def btn2_clicked():
    global val
    if len(val) < 15:
        val += "2"
        data.set(val)
    else:
        pass


def btn3_clicked():
    global val
    if len(val) < 15:
        val += "3"
        data.set(val)
    else:
        pass


def btn4_clicked():
    global val
    if len(val) < 15:
        val += "4"
        data.set(val)
    else:
        pass


def btn5_clicked():
    global val
    if len(val) < 15:
        val += "5"
        data.set(val)
    else:
        pass


def btn6_clicked():
    global val
    if len(val) < 15:
        val += "6"
        data.set(val)
    else:
        pass


def btn7_clicked():
    global val
    if len(val) < 15:
        val += "7"
        data.set(val)
    else:
        pass


def btn8_clicked():
    global val
    if len(val) < 15:
        val += "8"
        data.set(val)
    else:
        pass


def btn9_clicked():
    global val
    if len(val) < 15:
        val += "9"
        data.set(val)
    else:
        pass


def btn_plus_clicked():
    global val, A, operator, valS
    if len(val) < 16:
        operator_check("+")
    else:
        pass


def btn_minus_clicked():
    global val, A, operator, valS
    if len(val) < 16:
        operator_check("-")
    else:
        pass


def btn_mult_clicked():
    global val, A, operator, valS
    if len(val) < 16:
        operator_check("x")
    else:
        pass


def btn_div_clicked():
    global val, A, operator, valS
    if len(val) < 16:
        operator_check("/")
    else:
        pass


def btn_deg_clicked():
    global val, A, operator, valS
    if len(val) < 16:
        operator_check("^")
    else:
        pass

    
def operator_check(op):
    global val, A, operator, valS
    if operator == "" or operator == op:
        try:
            if "." in val:
                A = float(val)
            else:
                A = int(val)
            operator_set(op)
        except ValueError:
            pass
    else:
        operator_change(op)


def operator_set(op):
    global val, valS, operator
    valS = val + op
    val = ""
    data.set(val)
    dataS.set(valS)
    operator = op


def operator_change(op):
    global valS, operator
    x = []
    for i in valS:
        x.append(i)
    x.pop()
    valS = "".join(x)
    valS += op
    dataS.set(valS)
    operator = op


def btn_c_clicked():
    global val, A, B, operator, valS
    A = 0
    B = 0
    operator = ""
    valS = ""
    dataS.set(valS)
    val = ""
    data.set(val)


def btn_ce_clicked():
    global val, A, B, operator
    if A != 0:
        val = ""
        data.set(val)
    if A == 0:
        val = ""
        operator = ""
        data.set(val)


def btn_back_clicked():
    global val
    x = []
    try:
        for i in val:
            x.append(i)
        x.pop()
        val = "".join(x)
        data.set(val)
    except IndexError:
        pass


def btn_equ_clicked():
    global val, A, B, operator, valS
    try:
        valS = ""
        dataS.set(valS)
        if "." in val:
            B = float(val)
        else:
            B = int(val)
        if operator == "-":
            val = str(A - B)
            point_check()
        elif operator == "+":
            val = str(A + B)
            point_check()
        elif operator == "/":
            val = str(round(A / B, 10))
            point_check()
        elif operator == "x":
            val = str(A * B)
            point_check()
        elif operator == "^":
            val = str(round(A ** B, 10))
            point_check()
        operator = ""
    except ZeroDivisionError:
        data.set("Err")
    except OverflowError:
        data.set("Err")


def point_check():
    global val, C
    if "." in val:
        x = val.split(".")
        if x[1] == "0":
            val = x[0]
            e_format()
        elif 3 < len(x[0]) < 13:
            C = len(x[0])
            val = str(round(float(val), (14 - C)))
            e_format()
        elif len(x[0]) >= 13:
            val = x[0]
            data.set(val)
        else:
            e_format()
    else:
        e_format()


def e_format():
    global val
    if len(val) < 16:
        data.set(val)
    else:
        val = Decimal(float(val))
        val = format(val, ".4e")
        data.set(val)


# Creation window
window = Tk()
window.title("Калькулятор")
window.geometry("250x400")
window.resizable(0, 0)

# Creation small label
dataS = StringVar()
lblS = Label(window, bg="#434343", fg="#CCC", font=("Calibri", 18), anchor=NE,
             height=1, relief=GROOVE, textvariable=dataS)
lblS.pack(expand=True, fill="both")

# Creation label for input
data = StringVar()
lbl = Label(window, bg="#434343", fg="#CCC", font=("Calibri", 24), anchor=SE,
            height=1, relief=GROOVE, textvariable=data)
lbl.pack(expand=True, fill="both")

# Creation row's for key's
row1 = Frame(window)
row1.pack(expand=True, fill="both")
row2 = Frame(window)
row2.pack(expand=True, fill="both")
row3 = Frame(window)
row3.pack(expand=True, fill="both")
row4 = Frame(window)
row4.pack(expand=True, fill="both")
row5 = Frame(window)
row5.pack(expand=True, fill="both")

# Creation button's in the first row
btnC = Button(row1, bg="#87939a", fg="#1a1a1a", text="C", font=("Calibri", 22),
              relief=GROOVE, command=btn_c_clicked, width=1)
btnC.pack(side=LEFT, expand=True, fill="both")
btnCE = Button(row1, bg="#87939a", fg="#1a1a1a", text="CE", font=("Calibri", 22),
               relief=GROOVE, command=btn_ce_clicked, width=1)
btnCE.pack(side=LEFT, expand=True, fill="both")
btnBack = Button(row1, bg="#87939a", fg="#1a1a1a", text="←", font=("Calibri", 22),
                 relief=GROOVE, command=btn_back_clicked, width=1)
btnBack.pack(side=LEFT, expand=True, fill="both")
btnDeg = Button(row1, bg="#cb602d", fg="#CCC", text="^", font=("Calibri", 22),
                relief=GROOVE, command=btn_deg_clicked, width=1)
btnDeg.pack(side=LEFT, expand=True, fill="both")

# Creation button's in the second row
btn7 = Button(row2, bg="#333", fg="#CCC", text="7", font=("Calibri", 22),
              relief=GROOVE, command=btn7_clicked, width=1)
btn7.pack(side=LEFT, expand=True, fill="both")
btn8 = Button(row2, bg="#333", fg="#CCC", text="8", font=("Calibri", 22),
              relief=GROOVE, command=btn8_clicked, width=1)
btn8.pack(side=LEFT, expand=True, fill="both")
btn9 = Button(row2, bg="#333", fg="#CCC", text="9", font=("Calibri", 22),
              relief=GROOVE, command=btn9_clicked, width=1)
btn9.pack(side=LEFT, expand=True, fill="both")
btnDiv = Button(row2, bg="#cb602d", fg="#CCC", text="/", font=("Calibri", 22),
                relief=GROOVE, command=btn_div_clicked, width=1)
btnDiv.pack(side=LEFT, expand=True, fill="both")

# Creation button's in the third row
btn4 = Button(row3, bg="#333", fg="#CCC", text="4", font=("Calibri", 22),
              relief=GROOVE, command=btn4_clicked, width=1)
btn4.pack(side=LEFT, expand=True, fill="both")
btn5 = Button(row3, bg="#333", fg="#CCC", text="5", font=("Calibri", 22),
              relief=GROOVE, command=btn5_clicked, width=1)
btn5.pack(side=LEFT, expand=True, fill="both")
btn6 = Button(row3, bg="#333", fg="#CCC", text="6", font=("Calibri", 22),
              relief=GROOVE, command=btn6_clicked, width=1)
btn6.pack(side=LEFT, expand=True, fill="both")
btnMult = Button(row3, bg="#cb602d", fg="#CCC", text="x", font=("Calibri", 22),
                 relief=GROOVE, command=btn_mult_clicked, width=1)
btnMult.pack(side=LEFT, expand=True, fill="both")

# Creation button's in the fourth row
btn1 = Button(row4, bg="#333", fg="#CCC", text="1", font=("Calibri", 22),
              relief=GROOVE, command=btn1_clicked, width=1)
btn1.pack(side=LEFT, expand=True, fill="both")
btn2 = Button(row4, bg="#333", fg="#CCC", text="2", font=("Calibri", 22),
              relief=GROOVE, command=btn2_clicked, width=1)
btn2.pack(side=LEFT, expand=True, fill="both")
btn3 = Button(row4, bg="#333", fg="#CCC", text="3", font=("Calibri", 22),
              relief=GROOVE, command=btn3_clicked, width=1)
btn3.pack(side=LEFT, expand=True, fill="both")
btnMinus = Button(row4, bg="#cb602d", fg="#CCC", text="-", font=("Calibri", 22),
                  relief=GROOVE, command=btn_minus_clicked, width=1)
btnMinus.pack(side=LEFT, expand=True, fill="both")

# Creation button's in the fifth row
btnPoint = Button(row5, bg="#333", fg="#CCC", text=".", font=("Calibri", 22),
                  relief=GROOVE, command=btn_point_clicked, width=1)
btnPoint.pack(side=LEFT, expand=True, fill="both")
btn0 = Button(row5, bg="#333", fg="#CCC", text="0", font=("Calibri", 22),
              relief=GROOVE, command=btn0_clicked, width=1)
btn0.pack(side=LEFT, expand=True, fill="both")
btnEqu = Button(row5, bg="#333", fg="#CCC", text="=", font=("Calibri", 22),
                relief=GROOVE, command=btn_equ_clicked, width=1)
btnEqu.pack(side=LEFT, expand=True, fill="both")
btnPlus = Button(row5, bg="#cb602d", fg="#CCC", text="+", font=("Calibri", 22),
                 relief=GROOVE, command=btn_plus_clicked, width=1)
btnPlus.pack(side=LEFT, expand=True, fill="both")

window.bind("<Key>", check_events)

window.mainloop()
