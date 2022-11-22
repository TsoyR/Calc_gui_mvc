from frame import *

from click_button import *




def create():
    def make(num):
        return Button(win,text=num,bd=6,command= lambda :press(num))
    def make_o(operation):
        return Button(win,text=operation,bd=6,command= lambda :op(operation),fg = 'red',bg='blue')
    def make_equal(operation):
        return Button(win,text=operation,bd=6,command=calculate,fg = 'red',bg='blue')  
    def make_clear(operation):
        return Button(win,text=operation,bd=6,command=clear,fg = 'red',bg='blue')  

        
    make('1').grid(row=1,column=0,stick="wens",padx=6,pady=6)
    make('2').grid(row=1,column=1,stick="wens",padx=6,pady=6)
    make('3').grid(row=1,column=2,stick="wens",padx=6,pady=6)
    make('4').grid(row=2,column=0,stick="wens",padx=6,pady=6)
    make('5').grid(row=2,column=1,stick="wens",padx=6,pady=6)
    make('6').grid(row=2,column=2,stick="wens",padx=6,pady=6)
    make('7').grid(row=3,column=0,stick="wens",padx=6,pady=6)
    make('8').grid(row=3,column=1,stick="wens",padx=6,pady=6)
    make('9').grid(row=3,column=2,stick="wens",padx=6,pady=6)
    make('0').grid(row=4,column=0,stick="wens",padx=6,pady=6)
    make_o('+').grid(row=1,column=3,stick="wens",padx=6,pady=6)
    make_o('-').grid(row=2,column=3,stick="wens",padx=6,pady=6)
    make_o('/').grid(row=3,column=3,stick="wens",padx=6,pady=6)
    make_o('*').grid(row=4,column=3,stick="wens",padx=6,pady=6)
    make_equal('=').grid(row=4,column=1,stick="wens",padx=6,pady=6)
    make('j').grid(row=4,column=2,stick="wens",padx=6,pady=6)
    make_clear('C').grid(row=5,column=3,stick="wens",padx=6,pady=6)
    make('(').grid(row=5,column=1,stick="wens",padx=6,pady=6)
    make(')').grid(row=5,column=2,stick="wens",padx=6,pady=6)

    win.mainloop()


        




