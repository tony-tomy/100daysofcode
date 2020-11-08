def x = [0, 10, 20]
def y = [0, 10, 0]

println x
println y

println x[1]

def a = (x[0] * (y[1] - y[2]) + x[1] * (y[2] - y[0]) + x[2] * (y[0] - y[1]))/2

println a.abs()

