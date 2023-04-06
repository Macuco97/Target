sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
others = 19849.53

total = sp + rj + mg + es + others
sp = 100 * sp / total
rj = 100 * rj / total
mg = 100 * mg / total
es = 100 * es / total
others = 100 * others / total

print(f"SP: {sp:.2f}%")
print(f"RJ: {rj:.2f}%")
print(f"MG: {mg:.2f}%")
print(f"ES: {es:.2f}%")
print(f"Others: {others:.2f}%")
