#def primary():
#  print("Keep it logically awesome.")

  #f = open("quotes.txt")
  #quotes = f.readlines()
  #f.close()

  #print(quotes)

#if __name__== "__main__":
#  primary()

import random

f = open("quotes.txt")
quotes = f.readlines()
f.close()

last = 13
rnd = random.randint(0, last)
print(quotes[rnd])
