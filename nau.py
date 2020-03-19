def out_red(text):
    print("\033[31m {}".format(text))


def out_yellow(text):
    print("\033[33m {}".format(text))


def out_blue(text):
    print("\033[34m {}".format(text))


def generate_matrix():
    from random import randrange
    matrix_with_y = [[randrange(y_min, y_max) for y in range(m)] for x in range(3)]
    return matrix_with_y


def sum_y(matrix_with_y):
    sum_y1, sum_y2, sum_y3 = 0, 0, 0
    for j in range(m):
        sum_y1 += matrix_with_y[0][j]
        sum_y2 += matrix_with_y[1][j]
        sum_y3 += matrix_with_y[2][j]
    return sum_y1, sum_y2, sum_y3


def find_average_y(sum_of_y):
    average_y1 = sum_of_y[0] / m
    average_y2 = sum_of_y[1] / m
    average_y3 = sum_of_y[2] / m
    return average_y1, average_y2, average_y3


def find_dispersion(lst_y, average_y):
    dispersion_y1, dispersion_y2, dispersion_y3 = 0, 0, 0
    for k in range(m):
        dispersion_y1 += (lst_y[0][k] - average_y[0]) ** 2
        dispersion_y2 += (lst_y[1][k] - average_y[1]) ** 2
        dispersion_y3 += (lst_y[2][k] - average_y[2]) ** 2

    dispersion_y1 = dispersion_y1 / (m - 1)
    dispersion_y2 = dispersion_y2 / (m - 1)
    dispersion_y3 = dispersion_y3 / (m - 1)
    return dispersion_y1, dispersion_y2, dispersion_y3


def find_deviation():
    from math import sqrt
    deviation_1 = sqrt((2 * (2 * m - 2)) / (m * (m - 4)))
    return deviation_1


def find_Fuv(lst_with_dispersion):
    Fuv1 = lst_with_dispersion[0] / lst_with_dispersion[1]
    Fuv2 = lst_with_dispersion[2] / lst_with_dispersion[0]
    Fuv3 = lst_with_dispersion[2] / lst_with_dispersion[1]
    return Fuv1, Fuv2, Fuv3


def find_dispersion_uv(lst_with_f):
    dispersion_uv1 = (1 - 2 / m) * lst_with_f[0]
    dispersion_uv2 = (1 - 2 / m) * lst_with_f[1]
    dispersion_uv3 = (1 - 2 / m) * lst_with_f[2]
    return dispersion_uv1, dispersion_uv2, dispersion_uv3


def find_Ruv(lst_with_dispersion_uv, deviation_1):
    from math import fabs
    Ruv1 = fabs(lst_with_dispersion_uv[0] - 1) / deviation_1
    Ruv2 = fabs(lst_with_dispersion_uv[1] - 1) / deviation_1
    Ruv3 = fabs(lst_with_dispersion_uv[2] - 1) / deviation_1
    return Ruv1, Ruv2, Ruv3


def find_Rkr(dictionary):
    lst_with_keys = list(dictionary.keys())
    lst_with_keys.append(m)
    if lst_with_keys.count(m) == 1:
        lst_with_keys.sort()
        index_m = lst_with_keys.index(m)
        if m == lst_with_keys[-1]:
            need_key = lst_with_keys[index_m - 1]
        else:
            need_key = lst_with_keys[index_m + 1]
    else:
        need_key = m
    return dictionary.get(need_key)

def det(a):
    from numpy.linalg import det
    return det(a)


def delta_x(min_x, max_x):
    from math import fabs
    return fabs(max_x - min_x) / 2
m = 5
dict_p99 = {2: 1.73, 6: 2.16, 8: 2.43, 10: 2.62, 12: 2.75, 15: 2.9, 20: 3.08}
dict_p98 = {2: 1.72, 6: 2.13, 8: 2.37, 10: 2.54, 12: 2.66, 15: 2.8, 20: 2.96}
dict_p95 = {2: 1.71, 6: 2.10, 8: 2.27, 10: 2.41, 12: 2.52, 15: 2.64, 20: 2.78}
dict_p90 = {2: 1.69, 6: 2, 8: 2.17, 10: 2.29, 12: 2.39, 15: 2.49, 20: 2.62}
print("-" * 40)
x1_min = -15
x1_max = 30
x2_min = -35
x2_max = 15
p = float(input("Введіть довірчу імовірність: "))
print("-" * 40)

y_max = (30 - 13) * 10
y_min = (20 - 13) * 10

while True:
    matrix = generate_matrix()
    sum_y = sum_y(matrix)
    average = find_average_y(sum_y)
    dispersion = find_dispersion(matrix, average)
    deviation = find_deviation()
    Fuv = find_Fuv(dispersion)
    dispersion_uv = find_dispersion_uv(Fuv)
    Ruv = find_Ruv(dispersion_uv, deviation)
    if p == 0.9:
        Rkr = find_Rkr(dict_p90)
    elif p == 0.95:
        Rkr = find_Rkr(dict_p95)
    elif p == 0.98:
        Rkr = find_Rkr(dict_p98)
    else:
        Rkr = find_Rkr(dict_p99)
    if Ruv[0] < Rkr and Ruv[1] < Rkr and Ruv[2] < Rkr:
        break
    else:
        m += 1

matrix_x = [[-1, -1], [1, -1], [-1, 1]]
mx_1, mx_2, a1, a2, a3, a11, a22 = 0, 0, 0, 0, 0, 0, 0
for i in range(len(matrix_x)):
    mx_1 += matrix_x[i][0]
    mx_2 += matrix_x[i][1]
    a1 += matrix_x[i][0] ** 2
    a2 += matrix_x[i][0] * matrix_x[i][1]
    a3 += matrix_x[i][1] ** 2
    a11 += matrix_x[i][0] * average[i]

a22 += matrix_x[i][1] * average[i]

mx_1 = mx_1 / len(matrix_x)
mx_2 = mx_2 / len(matrix_x)
a1 = a1 / len(matrix_x)
a2 = a2 / len(matrix_x)
a3 = a3 / len(matrix_x)
a11 = a11 / len(matrix_x)
a22 = a22 / len(matrix_x)
my = sum(average) / len(average)

b0_numerator = [[my, mx_1, mx_2], [a11, a1, a2], [a22, a2, a3]]
b012_denominator = [[1, mx_1, mx_2], [mx_1, a1, a2], [mx_2, a2, a3]]
b1_numerator = [[1, my, mx_2], [mx_1, a11, a2], [mx_2, a22, a3]]
b2_numerator = [[1, mx_1, my], [mx_1, a1, a11], [mx_2, a2, a22]]

b0 = det(b0_numerator) / det(b012_denominator)
b1 = det(b1_numerator) / det(b012_denominator)
b2 = det(b2_numerator) / det(b012_denominator)

delta_x1 = delta_x(x1_min, x1_max)
delta_x2 = delta_x(x2_min, x2_max)
x10 = (x1_max + x1_min) / 2
x20 = (x2_max + x2_min) / 2

a0 = b0 - b1 * (x10 / delta_x1) - b2 * (x20 / delta_x2)
a1 = b1 / delta_x1
a2 = b2 / delta_x2

out_red("\tМатриця з у-ків")
for i in range(len(matrix)):
    print("|", end=" ")
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print("|")
out_blue("-" * 40)
out_red("\tСередні значення ȳi:")
out_yellow(" ȳ1 = {:.3f}".format(average[0]))
out_yellow(" ȳ2 = {:.3f}".format(average[1]))
out_yellow(" ȳ3 = {:.3f}".format(average[2]))
out_blue("-" * 40)
out_red("\tДисперсії по рядках:")
out_yellow(" σ{y1} =" + " {:.3f}".format(dispersion[0]))
out_yellow(" σ{y2} =" + " {:.3f}".format(dispersion[1]))
out_yellow(" σ{y3} =" + " {:.3f}".format(dispersion[2]))
out_blue("-" * 40)
out_red("\t Ruv:")
out_yellow(" Ruv1 = {:.3f}".format(Ruv[0]))
out_yellow(" Ruv2 = {:.3f}".format(Ruv[1]))
out_yellow(" Ruv3 = {:.3f}".format(Ruv[2]))
out_blue("-" * 40)
out_red("\tОтже нормоване рівняння регресії:\\n ŷ = {:.3f} + {:.3f}*X1 + {:.3f}*X2".format(b0, b1, b2))
out_yellow("\tПеревірка:\n {:.3f} - {:.3f} - {:.3f} = {:.3f}".format(b0, b1, b2, average[0]))
out_yellow(" {:.3f} + {:.3f} - {:.3f} = {:.3f}".format(b0, b1, b2, average[1]))
out_yellow(" {:.3f} - {:.3f} + {:.3f} = {:.3f}".format(b0, b1, b2, average[2]))
out_yellow("Результат збігається  середніми значеннями ȳi.")
out_blue("-" * 40)
out_yellow("\tНатуралізоване рівняння регресії:\n ŷ = {:.3f} + {:.3f}*X1 + {:.3f}*X2".format(a0, a1, a2))
out_yellow("\tЗробимо перевірку по рядкам:\n "
           "{:.3f} + {:.3f}*{:.3f} + {:.3f}*{:.3f} = ""{:.3f}".format
           (a0, a1, x1_min, a2, x2_max, a0 + a1 * x1_min + a2 * x2_min))
out_yellow(" {:.3f} + {:.3f}*{:.3f} + {:.3f}*{:.3f} = {:.3f}".format(
    a0, a1, x1_max, a2, x2_min, a0 + a1 * x1_max + a2 * x2_min))
out_yellow(" {:.3f} + {:.3f}*{:.3f} + {:.3f}*{:.3f} = {:.3f}".format(
    a0, a1, x1_min, a2, x2_max, a0 + a1 * x1_min + a2 * x2_max))
out_yellow("Отже, коефіцієнти натуралізованого рівняння регресії вірні.")
out_blue("-" * 40)

if m > 20:
    print(f"m = {m} > 20 does not work correctly")
else:
    print(f"m = {m} < 20 program successful")
