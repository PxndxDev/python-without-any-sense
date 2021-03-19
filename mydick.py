import matplotlib.pyplot as plt

x1 = [-2, -2, -1, 0, 1, 2, 2]
y1 = [-1, 5, 6, 6.5, 6, 5, -1]

plt.plot(x1, y1, label="testicules")

x2 = [-2, -3, -3,     -3,   -2.5,   -1.5, -0.5,   0,     0.5,  1.5, 2.5,  3,    3,     3, 2]
y2 = [-1, -2, -2.5,   -3.5, -4.5,   -5,   -4.5,   -3.5,  -4.5, -5,  -4.5, -3.5, -2.5, -2, -1]

plt.plot(x2, y2, label="verge")

plt.xlabel('dimensions x')

plt.ylabel('dimensions y')

plt.title('C\'est ma queue !')

plt.legend()

plt.show()
