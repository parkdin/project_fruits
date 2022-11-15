def get_frutis_name(data:str)->list:
    """
    This function returns the name of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits names
    """
    row = data.split()[1:]
    name =[]
    for i in row:
        name.append(i.split(',')[0])
    return name


data = open('fruits.csv').read()

print(get_frutis_name(data))

    