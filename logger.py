from datetime import datetime as dt

def operation_log(data):
    time = dt.now().strftime('%H:%M')
    with open('logs.csv', 'a') as file:
        file.write(f'{time};operation;{data};')
    

def calculate_log(data):
    with open('logs.csv', 'a') as file:
        file.write(f'result;{data};\n')

