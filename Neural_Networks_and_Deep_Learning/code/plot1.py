from matplotlib.pyplot import axis, plot, savefig, show
from numpy import arange

axis([-4, 4, -3, 3])

inputs = arange(-10, 10, 0.001)
outputs = list()

for x in inputs:
    y = x

    outputs.append(y)

plot(inputs, outputs, lw=2, color="blue")
savefig("img/plot1.svg")
# show()
