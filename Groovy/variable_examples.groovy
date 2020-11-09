def x = 104
println x.getClass()
x = "Guru99"
println x.getClass()

println x

2.upto(4) {println "$it"}

5.times{println "$it"}

0.step(7,2){println "$it"}

def y = ["Guru99", "is", "Best", "for", "Groovy"]
println y
y.add("Learning")
println(y.contains("is"))
println(y.get(2))
println(y.pop())
println y