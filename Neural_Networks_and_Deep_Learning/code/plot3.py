from matplotlib.pyplot import axis, plot, savefig, show
from numpy import arange, exp, log

axis([-4, 4, -3, 3])

inputs = arange(-10, 10, 0.001)
outputs = list()

for x in inputs:
    y = log(1) + exp(x)

    outputs.append(y)

plot(inputs, outputs, lw=2, color="blue")
savefig("img/plot3.svg")
# show()
