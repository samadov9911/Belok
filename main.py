import numpy as np
import matplotlib.pyplot as plt
import math

w = 1.133 * pow(10, -3)


def dx(x_, y_, Vx_, Vy_, ax_):  # k0
    return Vx_


def dVx(x_, y_, Vx_, Vy_, ax_):  # k2
    res = ax_ - 2 * w * Vy_
    return res


def dy(x_, y_, Vx_, Vy_, ax_):  # k1
    return Vy_


def dVy(x_, y_, Vx_, Vy_, ax_):  # k3
    res = 3 * (w ** 2) * y_ + 2 * w * Vx_

    return res


def dax(x_, y_, Vx_, Vy_, ax_):  # k4

    return 0

#Нахождение начальных условий
mu=396602
H=400
R0=(6371+H)
omega=math.sqrt(mu/R0**3)
V=math.sqrt(mu/R0)


k = np.zeros((5, 4))
h = 50

t = 0

#Мат.ожидание
x = 5
y = 0
Vx = 0
Vy = 2.833 * pow(10, -3)
ax = 3.518 * pow(10, -18)

#Матрица A
A=np.array([[0, 0, 1, 0, 0],
            [0, 0, 0,  1, 0],
            [0, 0, 0, -2*omega,  1],
            [0, 3*omega**2, 2*omega, 0, 0],
            [0, 0, 0, 0, 0]])

#Матрица A transpose
omega=1
AA=np.transpose([[0, 0, 1, 0, 0],
            [0, 0, 0,  1, 0],
            [0, 0, 0, -2*omega,  1],
            [0, 3*omega**2, 2*omega, 0, 0],
            [0, 0, 0, 0, 0]])



#Корреляционные коэффициенты
D1=100*10**(-6); K1=5*10**(-7); K2=2*10**(-5); K3=0; K4=0;
K5=5*10**(-7); D2=0.01*10**(-6); K6=0; K7=0; K8=0;
K9=2*10**(-5); K10=0; D3=100*10**(-6); K11=K5; K12=0;
K13=0; K14=0; K15=K5; K16=0; D4=0.01-10**(-6); K17=0;
K18=0; K19=0; K20=0; K21=0; D5=3.518*10**(19);

h = 50

x_list = list()
y_list = list()
Vx_list = list()
Vy_list = list()
ax_list = list()
t_list = list()

while t <= 5400:
    x_list.append(x)
    y_list.append(y)
    Vx_list.append(Vx)
    Vy_list.append(Vy)
    ax_list.append(ax)
    t_list.append(t)

    k[0][0] = h * dx(x, y, Vx, Vy, ax)
    k[1][0] = h * dy(x, y, Vx, Vy, ax)
    k[2][0] = h * dVx(x, y, Vx, Vy, ax)
    k[3][0] = h * dVy(x, y, Vx, Vy, ax)
    k[4][0] = h * dax(x, y, Vx, Vy, ax)

    k[0][1] = h * dx(x + k[0][0] / 2, y + k[1][0] / 2, Vx + k[2][0] / 2, Vy + k[3][0] / 2, ax + k[4][0] / 2)
    k[1][1] = h * dy(x + k[0][0] / 2, y + k[1][0] / 2, Vx + k[2][0] / 2, Vy + k[3][0] / 2, ax + k[4][0] / 2)
    k[2][1] = h * dVx(x + k[0][0] / 2, y + k[1][0] / 2, Vx + k[2][0] / 2, Vy + k[3][0] / 2, ax + k[4][0] / 2)
    k[3][1] = h * dVy(x + k[0][0] / 2, y + k[1][0] / 2, Vx + k[2][0] / 2, Vy + k[3][0] / 2, ax + k[4][0] / 2)
    k[4][1] = h * dax(x + k[0][0] / 2, y + k[1][0] / 2, Vx + k[2][0] / 2, Vy + k[3][0] / 2, ax + k[4][0] / 2)

    k[0][2] = h * dx(x + k[0][1] / 2, y + k[1][1] / 2, Vx + k[2][1] / 2, Vy + k[3][1] / 2, ax + k[4][1] / 2)
    k[1][2] = h * dy(x + k[0][1] / 2, y + k[1][1] / 2, Vx + k[2][1] / 2, Vy + k[3][1] / 2, ax + k[4][1] / 2)
    k[2][2] = h * dVx(x + k[0][1] / 2, y + k[1][1] / 2, Vx + k[2][1] / 2, Vy + k[3][1] / 2, ax + k[4][1] / 2)
    k[3][2] = h * dVy(x + k[0][1] / 2, y + k[1][1] / 2, Vx + k[2][1] / 2, Vy + k[3][1] / 2, ax + k[4][1] / 2)
    k[4][2] = h * dax(x + k[0][1] / 2, y + k[1][1] / 2, Vx + k[2][1] / 2, Vy + k[3][1] / 2, ax + k[4][1] / 2)

    k[0][3] = h * dx(x + k[0][2], y + k[1][2], Vx + k[2][2], Vy + k[3][2], ax + k[4][2])
    k[1][3] = h * dy(x + k[0][2], y + k[1][2], Vx + k[2][2], Vy + k[3][2], ax + k[4][2])
    k[2][3] = h * dVx(x + k[0][2], y + k[1][2], Vx + k[2][2], Vy + k[3][2], ax + k[4][2])
    k[3][3] = h * dVy(x + k[0][2], y + k[1][2], Vx + k[2][2], Vy + k[3][2], ax + k[4][2])
    k[4][3] = h * dax(x + k[0][2], y + k[1][2], Vx + k[2][2], Vy + k[3][2], ax + k[4][2])

    t = t + 50

    x = x + (k[0][0] + 2.0 * k[0][1] + 2.0 * k[0][2] + k[0][3]) / 6.0
    y = y + (k[1][0] + 2.0 * k[1][1] + 2.0 * k[1][2] + k[1][3]) / 6.0
    Vx = Vx + (k[2][0] + 2.0 * k[2][1] + 2.0 * k[2][2] + k[2][3]) / 6.0
    Vy = Vy + (k[3][0] + 2.0 * k[3][1] + 2.0 * k[3][2] + k[3][3]) / 6.0
    ax = ax + (k[4][0] + 2.0 * k[4][1] + 2.0 * k[4][2] + k[4][3]) / 6.0


plt.plot(x_list, y_list, label = 'Траектория относительного движения')
plt.legend(loc=4)
plt.xlabel('X, км')
plt.ylabel('Y, км')
plt.grid()
plt.show()


plt.plot(t_list, x_list, label = 'Метематическое ожидание Mx')
plt.legend()
plt.xlabel('Время (секунда)')
plt.ylabel('Mx(t), км')
plt.grid()
plt.show()

plt.plot(t_list, Vx_list, label = 'Метематическое ожидание M_Vx')
plt.grid()
plt.xlabel('Время (секунда)')
plt.ylabel('M_Vx(t), км')
plt.legend()
plt.show()


plt.plot(t_list, y_list, label = 'Метематическое ожидание My')
plt.grid()
plt.xlabel('Время (секунда)')
plt.ylabel('My (t), км')
plt.legend()
plt.show()

plt.plot(t_list, Vy_list, label = 'Метематическое ожидание M_Vy')
plt.grid()
plt.xlabel('Время (секунда)')
plt.ylabel('M_Vy(t), км')
plt.legend()
plt.show()


plt.plot(t_list, ax_list, label = 'Метематическое ожидание Max')
plt.legend()
plt.xlabel('Время (секунда)')
plt.ylabel('Max(t), км')
plt.grid()
plt.show()



Kmat=np.array([[D1, K1, K2, K3, K4],
            [K5, D2, K6,  K7, K8],
            [K9, K10, D3, K11,  K12],
            [K13, K14, K15, D4, K16],
            [K17, K18, K19, K20, D5]])

a = np.array(A)
b = np.array(K)
total1 = a.dot(b)
print(total)


KK=A*K+K*AA
print(K)
print(A)
print(AA)
print('--')
print(Kmat)

#Нахождения дисперсий методом Ранги-Кутты

h = 50




