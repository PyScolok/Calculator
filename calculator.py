import tkinter as tk
import re


class Calculator(tk.Frame):
    # Class variables:
    # operator_is_input - True if the operator has already been entered.
    # digit_is_input - True if the next digit is the first in the main input field.
    # formula - the string on which the calculation will be carried out.
    operator_is_input = False
    digit_is_first = True
    formula = ''

    def __init__(self, root):
        super().__init__(root)
        self.init_UI()

    def init_UI(self):
        # Creation small top label
        self.top_lbl = tk.Label(bg="#434343", fg="#CCC", font=("Calibri", 8), anchor=tk.NE,
                                height=1, relief=tk.GROOVE, bd=0)
        self.top_lbl.pack(expand=True, fill="both")

        # Creation main input label
        self.main_lbl = tk.Label(bg="#434343", fg="#CCC", font=("Calibri", 24), anchor=tk.SE,
                                height=1, relief=tk.GROOVE, bd=0, text='0')
        self.main_lbl.pack(expand=True, fill="both")

        # Creation row's for key's
        self.row_1 = tk.Frame()
        self.row_1.pack(expand=True, fill="both")
        self.row_2 = tk.Frame()
        self.row_2.pack(expand=True, fill="both")
        self.row_3 = tk.Frame()
        self.row_3.pack(expand=True, fill="both")
        self.row_4 = tk.Frame()
        self.row_4.pack(expand=True, fill="both")
        self.row_5 = tk.Frame()
        self.row_5.pack(expand=True, fill="both")

        # Creation button's in the first row
        self.btn_C = tk.Button(self.row_1, bg="#87939a", fg="#1a1a1a", text="C", font=(
            "Calibri", 22), relief=tk.GROOVE, command=self.clean_button_clicked, width=1)
        self.btn_C.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_CE = tk.Button(self.row_1, bg="#87939a", fg="#1a1a1a", text="CE", font=(
            "Calibri", 22), relief=tk.GROOVE, command=self.clean_entry_button_clicked, width=1)
        self.btn_CE.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_back = tk.Button(self.row_1, bg="#87939a", fg="#1a1a1a", text="←", font=(
            "Calibri", 22), relief=tk.GROOVE, command=self.back_button_clicked, width=1)
        self.btn_back.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_deg = tk.Button(self.row_1, bg="#cb602d", fg="#CCC", text="^", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.operator_button_clicked('^'), width=1)
        self.btn_deg.pack(side=tk.LEFT, expand=True, fill="both")

        # Creation button's in the second row
        self.btn_7 = tk.Button(self.row_2, bg="#333", fg="#CCC", text="7", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.digit_button_clicked('7'), width=1)
        self.btn_7.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_8 = tk.Button(self.row_2, bg="#333", fg="#CCC", text="8", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.digit_button_clicked('8'), width=1)
        self.btn_8.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_9 = tk.Button(self.row_2, bg="#333", fg="#CCC", text="9", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.digit_button_clicked('9'), width=1)
        self.btn_9.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_div = tk.Button(self.row_2, bg="#cb602d", fg="#CCC", text="÷", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.operator_button_clicked('÷'), width=1)
        self.btn_div.pack(side=tk.LEFT, expand=True, fill="both")

        # Creation button's in the third row
        self.btn_4 = tk.Button(self.row_3, bg="#333", fg="#CCC", text="4", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.digit_button_clicked('4'), width=1)
        self.btn_4.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_5 = tk.Button(self.row_3, bg="#333", fg="#CCC", text="5", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.digit_button_clicked('5'), width=1)
        self.btn_5.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_6 = tk.Button(self.row_3, bg="#333", fg="#CCC", text="6", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.digit_button_clicked('6'), width=1)
        self.btn_6.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_mult = tk.Button(self.row_3, bg="#cb602d", fg="#CCC", text="x", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.operator_button_clicked('*'), width=1)
        self.btn_mult.pack(side=tk.LEFT, expand=True, fill="both")

        # Creation button's in the fourth row
        self.btn_1 = tk.Button(self.row_4, bg="#333", fg="#CCC", text="1", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.digit_button_clicked('1'), width=1)
        self.btn_1.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_2 = tk.Button(self.row_4, bg="#333", fg="#CCC", text="2", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.digit_button_clicked('2'), width=1)
        self.btn_2.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_3 = tk.Button(self.row_4, bg="#333", fg="#CCC", text="3", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.digit_button_clicked('3'), width=1)
        self.btn_3.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_sub = tk.Button(self.row_4, bg="#cb602d", fg="#CCC", text="-", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.operator_button_clicked('-'), width=1)
        self.btn_sub.pack(side=tk.LEFT, expand=True, fill="both")

        # Creation button's in the fifth row
        self.btn_pnt = tk.Button(self.row_5, bg="#333", fg="#CCC", text=".", font=(
            "Calibri", 22), relief=tk.GROOVE, command=self.point_button_clicked, width=1)
        self.btn_pnt.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_0 = tk.Button(self.row_5, bg="#333", fg="#CCC", text="0", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.digit_button_clicked('0'), width=1)
        self.btn_0.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_equ = tk.Button(self.row_5, bg="#333", fg="#CCC", text="=", font=(
            "Calibri", 22), relief=tk.GROOVE, command=self.equal_button_clicked, width=1)
        self.btn_equ.pack(side=tk.LEFT, expand=True, fill="both")
        self.btn_add = tk.Button(self.row_5, bg="#cb602d", fg="#CCC", text="+", font=(
            "Calibri", 22), relief=tk.GROOVE, command=lambda: self.operator_button_clicked('+'), width=1)
        self.btn_add.pack(side=tk.LEFT, expand=True, fill="both")

    def check_events(self, event):
        """Keyboard event handler"""
        if event.keysym.isdigit():
            self.digit_button_clicked(event.keysym)
        if event.keysym == "plus":
            self.operator_button_clicked('+')
        if event.keysym == "minus":
            self.operator_button_clicked('-')
        if event.keysym == "slash":
            self.operator_button_clicked('÷')
        if event.keysym == "asterisk":
            self.operator_button_clicked('*')
        if event.keysym == "asciicircum":
            self.operator_button_clicked('^')
        if event.keysym == "period":
            self.point_button_clicked()
        if event.keysym == "Return" or event.keysym == "equal":
            self.equal_button_clicked()
        if event.keysym == "Escape":
            self.clean_button_clicked()
        if event.keysym == "Delete":
            self.clean_entry_button_clicked()
        if event.keysym == "BackSpace":
            self.back_button_clicked()

    def digit_button_clicked(self, digit):
        """Enters numbers in the main input label"""
        if len(self.main_lbl['text']) < 15 or self.digit_is_first:
            if self.digit_is_first or self.main_lbl['text'] == '0':
                self.main_lbl['text'] = digit
                self.digit_is_first = False
            else:
                self.main_lbl['text'] += digit
        else:
            pass

    def point_button_clicked(self):
        """Enters points in the main input label"""
        if len(self.main_lbl['text']) < 15 and '.' not in self.main_lbl['text']:
            self.main_lbl['text'] += '.'
        else:
            pass

    def operator_button_clicked(self, operator):
        """Enters operators in the main input label changes the operator
        if necessary, calls the calculation when you re-enter the operator
        """
        if operator not in self.formula and self.operator_is_input:
            self.change_operator(operator)
            return
        self.top_lbl['text'] += self.main_lbl['text'] + f' {operator} '
        # If the operator has already been entered, then when you press it again, the calculation will be performed:
        if self.operator_is_input:
            self.formula += self.main_lbl['text']
            self.equal_with_operator_clicked()
        self.formula = self.main_lbl['text'] + f' {operator} '
        self.operator_is_input = True
        self.digit_is_first = True

    def equal_with_operator_clicked(self):
        """Calculation when the operator is pressed again"""
        result = self.calculation()
        self.main_lbl['text'] = str(result)

    def change_operator(self, operator):
        """Change operator logic"""
        self.formula = self.formula[:-3] + f' {operator} '
        self.top_lbl['text'] = self.top_lbl['text'][:-3] + f' {operator} '

    def equal_button_clicked(self):
        """Initiates the calculation procedure"""
        self.top_lbl['text'] += self.main_lbl['text']
        self.formula += self.main_lbl['text']
        result = self.calculation()
        self.main_lbl['text'] = str(result)
        self.top_lbl['text'] = ''
        self.digit_is_first = True
        self.operator_is_input = False

    def back_button_clicked(self):
        """Removes the last item from the main input label"""
        if not self.digit_is_first:
            self.main_lbl['text'] = self.main_lbl['text'][:-1]

    def clean_button_clicked(self):
        """Clears the main input label, small label and formula"""
        self.main_lbl['text'] = '0'
        self.top_lbl['text'] = ''
        self.formula = ''
        self.digit_is_first = True
        self.operator_is_input = False

    def clean_entry_button_clicked(self):
        """Clears the main input label"""
        self.main_lbl['text'] = '0'
        self.digit_is_first = True
        self.operator_is_input = False

    def calculation(self):
        """Returns the calculation result"""
        try:
            self.format_formula()
            if self.formula[1] == '+':
                result = self.formula[0] + self.formula[2]
            elif self.formula[1] == '-':
                result = self.formula[0] - self.formula[2]
            elif self.formula[1] == '*':
                result = self.formula[0] * self.formula[2]
            elif self.formula[1] == '÷':
                result = self.formula[0] / self.formula[2]
            elif self.formula[1] == '^':
                result = self.formula[0] ** self.formula[2]
            self.formula = ''
            result = self.format_result(result)
            return result
        except ZeroDivisionError:
            return 'Error'

    def format_result(self, value):
        """Converts the result to exponential form if necessary"""
        if len(str(value)) > 15:
            return format(value, '.4e')
        else:
            return value

    def format_formula(self):
        """Converts the string representation of the formula to the appropriate types"""
        f_formula = []
        self.formula = self.formula.split(' ')
        for item in self.formula:
            if '.' in item:
                f_formula.append(float(item))
            elif re.fullmatch(r'[-+*^÷]', item):
                f_formula.append(item)
            else:
                f_formula.append(int(item))
        self.formula = f_formula


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    app.pack()
    root.title("Calculator")
    root.geometry("250x400")
    root.resizable(False, False)
    root.bind('<Key>', app.check_events)
    root.mainloop()