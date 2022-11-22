from frame import display

from logger import calculate_log,operation_log
    

def press(num):
    value = display.get()

    if value[0] == '0':
        value = value[1:]
    display.delete(0,"end")
    display.insert(0,value + num)

   

def op(o):
    value = display.get()
    if value[-1] in '-+/*':
        value = value[:-1] 
    display.delete(0,"end")
    display.insert(0,value+o)

def calculate():
    value = display.get()
    display.delete(0,"end")
    display.insert(0,eval(value))
    operation_log(value)
    calculate_log(eval(value))

def clear():
    display.delete(0,'end')
    display.insert(0,'0')
    operation_log('C')


    
    