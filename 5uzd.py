s = "hello"
print(s[1])


saraksts = [1,2,[3,4,'hello']]
saraksts[2][2] = "visu labu"
print(saraksts)


teikums = input("Uzraksti teikumu, kurā ir vismaz divi vārdi, kuri sāka ar burtu s:")

for vards in teikums.split():
  if vards[0] == 's':
    print(vards)


list = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]

def unik_list(list):
  x = []
  for a in list:
    if a not in x:
      x.append(a)
  return x

print(unik_list(list))


list = [1,2,3,4]

def multiply(numbers):
  total =1
  for x in numbers:
    total *= x
  return total

print(multiply(list))