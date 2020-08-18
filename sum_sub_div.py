
def get_sum_num():
    try:
        numbers = int(input("how many number you want to add "))
        sum=0
        for i in range(0,numbers):
            n = int(input("Enter a number :"))
            sum = sum + n
        return sum
    except:
        print("enter the integer value more than 0 ")
        get_sum_num()
    
    
sum_value = get_sum_num()
print(sum_value)

def get_sub():
    try:
        first = int(input("enter the first number "))
        second = int(input("enter the second number "))
        value = abs(first - second)
        return value
    except:
        print("enter the integer value ")
        get_sub()
        
sub_value = get_sub()
print(sub_value)


def get_div():
    try:
        Dividend = int(input("enter the Dividend number "))
        Divisor = int(input("enter the Divisor number "))
        result = Dividend/Divisor
        return result
    except:
        print("enter the valid integer number ")
        get_div()
        


div_value = get_div()
print(div_value)
