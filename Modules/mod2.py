

sum = 0

def display_from_mod2(ele_list):
     global sum
     for ele in ele_list:
        sum += ele
        print(ele,end=' ')


def get_sum():
    return sum

