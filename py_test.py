def check_fermat(a, b, c, n):
    if n > 2 and (a ** n) + ( b ** n) == c ** n:
      print "Holy smokes, Fermat was wrong!"
    else:
      print "No, that does not work."
      
def prompt_vals():
    a = int(raw_input("Set a value:"))
    b = int(raw_input("Set b value:"))
    c = int(raw_input("Set c value:"))
    n = int(raw_input("Set n value:")) 
    
    check_fermat(a, b, c, n)
              
def factorial(n):
    print n
    if n == 0:
      return 1
    else:
      recurse = factorial(n-1)
      result = n * recurse
      return result

def openfile(fname):
    count = 0
    f = open(fname, "r+")
    string = f.read()
    print string
    
    for s in string:
      count += 1

    return count
    
print openfile("py_test.py")      
    
