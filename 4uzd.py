saroksts = 
saroksts = {int(sk) for sk in input("Ivodi skaitļus, otdolūt tūs ar atstorpi:").split()}
for i in range(len(saroksts)):
  if saroksts[i] == saroksts[i+1]: