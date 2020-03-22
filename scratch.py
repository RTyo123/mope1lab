import random

A0 = 2
A1 = 3
A2 = 4
A3 = 5

N = 8  # number of experiments


def f(x1, x2, x3):
    return A0 + A1 * x1 + A2 * x2 + A3 * x3


def generate_x(start=0, stop=20):
    return [random.randint(start, stop) for _ in range(N)]


def count_x0i(x_results) -> int:
    return (max(x_results) + min(x_results)) / 2


def count_dxi(x0i, x_results) -> int:
    return x0i - min(x_results)


def count_xni(x0i, dxi, x_results) -> list:
    return [(i - x0i) / dxi for i in x_results]


def get_opt_y(Y):
    return max(Y)


X1, X2, X3 = [generate_x() for i in range(3)]
Y = [f(X1[i], X2[i], X3[i]) for i in range(8)]

X01 = count_x0i(X1)
X02 = count_x0i(X2)
X03 = count_x0i(X3)

dX1 = count_dxi(X01, X1)
dX2 = count_dxi(X02, X2)
dX3 = count_dxi(X03, X3)

X1n = count_xni(X01, dX1, X1)
X2n = count_xni(X02, dX2, X2)
X3n = count_xni(X03, dX3, X3)

Yet = f(X01, X02, X03)

OPT_Y = get_opt_y(Y)
index = Y.index(OPT_Y)
OPT_POINT = [X1[index], X2[index], X3[index]]

print("N   X1   X2   X3     Y3       XH1    XH2    XH3")
for i in range(N):
    print(f"{i+1:^1} |{X1[i]:^4} {X2[i]:^4} {X3[i]:^4} |"
          f" {Y[i]:^5} || {'%.2f' %X1n[i]:^5}  {'%.2f' %X2n[i]:^5}  {'%.2f' %X3n[i]:^5} |")

print(f"\nX0| {X01:^4} {X02:^4} {X03:^4}|")
print(f"dx| {dX1:^4} {dX2:^4} {dX3:^4}|")
print(f"Function: y = {A0} + {A1}x1 + {A2}x2 + {A3}x3")
print("Yет =", Yet)
print("Optimal point (max(Y)):  Y({0}, {1}, {2}) = {3}".format(*OPT_POINT, "%.1f" % OPT_Y))
