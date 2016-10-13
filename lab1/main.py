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
        output.append(sum(float_arr[1:])/len(float_arr) - 1)
    return output


def main():
    file_names = ['2cel.csv', '2cel-rs.csv', 'cel.csv', 'rsel.csv']
    for file in file_names:
        arr = loadfile(file)
        plt.plot(get_x_axis(arr), get_y_axis(arr), label=file)
    plt.legend()
    plt.savefig('myplot.pdf')
    plt.close()

if __name__ == '__main__':
    main()