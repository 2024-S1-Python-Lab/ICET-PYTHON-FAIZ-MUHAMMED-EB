#n=int(input("Enter a number : "))
#s=(n+11*n+111*n)
#print(f"{n}+{nn} + {nnn} = {s}")
n = int(input("Enter a number: "))
nn = 11 * n  # `nn` is 11 times `n`
nnn = 111 * n  # `nnn` is 111 times `n`
s = n + nn + nnn  # Sum of `n`, `nn`, and `nnn`
print(f"{n} + {nn} + {nnn} = {s}")
