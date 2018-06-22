var=raw_input("enter:")
def distance_from_zero(a):
  if int(a) or float(a):
    print abs(a)
  else:
    print "nope"
distance_from_zero(int(var)) 
