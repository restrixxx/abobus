# Sula veikalā maksā 1.5 eiro (bez PVN) un siers 3 eiro (bez PVN). 
# Aprēķini, cik kopā tev ir jāmaksā par pirkumu ar PVN.
#21%

PVN = 0.21

sulasCena = 1.5
sulasPVN = sulasCena * PVN

sieraCena = 3
sieraPVN = sieraCena * PVN

kopaa = sulasCena + sulasPVN + sieraCena + sieraPVN

print(kopaa)