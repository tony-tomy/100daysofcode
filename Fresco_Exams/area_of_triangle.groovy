//Enter your code here. Read input from STDIN. Print output to STDOUT

BufferedReader br = new BufferedReader(new InputStreamReader(System.in))

def n = br.readLine() as Integer
def x1 = br.readLine() as Integer
def x2 = br.readLine() as Integer
def x3 = br.readLine() as Integer
def m = br.readLine() as Integer
def y1 = br.readLine() as Integer
def y2 = br.readLine() as Integer
def y3 = br.readLine() as Integer

//println n
//println x2
//println x3

def area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))/2 as Integer

println area.abs()