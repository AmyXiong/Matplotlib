import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)

# ------- First subplot ----------

ylin = x
yqua = x ** 2
ycub = x ** 3

plt.subplot(1,2,1)

plt.xlim([-11, 11])
plt.ylim([-10, 10])

plt.plot(x, ylin, 'r', label = "linear")
plt.plot(x, yqua, 'g', label = "quadratic")
plt.plot(x, ycub, 'y', label = "cubic")

plt.xlabel("x")
plt.ylabel("y")

plt.legend(loc = "lower right")

plt.title("Rectangular Coordinate")

# -------- Second subplot -----------

plt.subplot(1, 2, 2, polar = True)

ylin = x
yqua = x ** 2
ycub = x ** 3

plt.plot(x, ylin, 'r', label = "linear")
plt.plot(x, yqua, 'g', label = "quadratic")
plt.plot(x, ycub, 'y', label = "cubic")

plt.legend(loc = "lower center")

plt.title("Polar Coordinate")

# --------- Final step ------------

plt.savefig("Polynomials.pdf")