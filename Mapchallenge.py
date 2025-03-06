temperatures = [32, 50, 77, 104] 

def t_to_c(temps):
    cel = {((temps[temp] - 32)*(5/9)) for temp in temps}
    print(cel)

t_to_c(temperatures)


