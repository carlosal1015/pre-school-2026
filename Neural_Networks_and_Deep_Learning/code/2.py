from math import exp

z = [1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0]
z_exp = [exp(i) for i in z]
sum_z_exp = sum(z_exp)
softmax = [round(i / sum_z_exp, 3) for i in z_exp]
# softmax |$\sum$|
