from matplotlib.pyplot import axis, plot, savefig, show
from numpy import arange

axis([-4, 4, -3, 3])

inputs = arange(-10, 10, 0.001)
outputs = list()

for x in inputs:
    y = max(0, x)

    outputs.append(y)

plot(inputs, outputs, lw=2, color="blue")
savefig("img/plot2.svg")
# show()
