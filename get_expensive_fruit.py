def get_expensive_fruit(data:str)->str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
    """
    # your code here
    row = data.split()[1:]
    max = 0
    exp_name = []
    for i in row:
        price = float(i.split(',')[1])
        name = i.split(',')[0]
        if price > max:
            max = price
            exp_name = name
    return exp_name
data = open('fruits.csv').read()
print(get_expensive_fruit(data))

