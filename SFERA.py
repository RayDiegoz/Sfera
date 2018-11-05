import math

def volume(r):
  v=(4.0/3.0*math.pi)*r**3
  return v



r= input ("Inserire il raggio della sfera:")
r= int(r)
ris=volume(r)
print (ris)