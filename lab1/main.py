import matplotlib.pyplot as plt


def loadfile(file_path):
    arr = []
    f = open(file_path)
    for line in f:
        arr.append(line.split(',')[1:])
    f.close()
    return arr[1:]


def get_x_axis(arr):
    output = []
    for item in arr:
        output.append(float(item[0]))
    return output


def get_y_axis(arr):
    output = []
    for item in arr:
        float_arr = [float(i) for i in item]
        output.append(sum(float_arr[1:])/(len(float_arr) - 1))
    return output


def main():
    plt.figure(figsize=(6.7, 6.7))
    file_names = [['2cel.csv', 'purple'], ['2cel-rs.csv', 'red'], ['cel.csv', 'black'], ['rsel.csv', 'blue'], ['cel-rs.csv', 'green']]
    for file in file_names:
        arr = loadfile(file[0])
        plt.plot(get_x_axis(arr), get_y_axis(arr), label=file[0], color=file[1])
    plt.legend(loc='lower right')
    plt.xlim([0, 500000])
    plt.xlabel('Rozegranych gier')
    plt.ylabel('odsetek wygranych gier')
    plt.savefig('myplot.pdf')
    plt.show()
    plt.close()

if __name__ == '__main__':
    main()