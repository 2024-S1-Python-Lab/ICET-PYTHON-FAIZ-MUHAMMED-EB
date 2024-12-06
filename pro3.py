s=input("enter a sentance")
print(s)
wordlist=s.split()
print(wordlist)
for i in wordlist:
     print(f"{i} occurce {wordlist.count(i)}times")
