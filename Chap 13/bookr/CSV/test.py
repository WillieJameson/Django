def write_data(data):
    for row in range(len(data)):
        print(row)
        for col in range(len(data[row])):
            print(col)
            print(data[row][col])


if __name__ == '__main__':
    data = [['John Doe', 38],
            ['Adam Cuvver', 22],
            ['Stacy Martin', 28],
            ['Tom Harris', 42]]
    write_data(data)