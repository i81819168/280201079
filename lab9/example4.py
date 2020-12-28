import time
def timer(t):
  if t == 0:
    print("end")
    return None
    
  print("remaining time:" + str(t))
  time.sleep(1)
  return timer(t-1)

s = 5
timer(s)