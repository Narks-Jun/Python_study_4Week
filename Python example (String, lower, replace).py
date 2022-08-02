words = 'Connect Foundation'

if 'F' in words :
    low = words.lower()
    print(words[7])
    high = low.replace(low[7],'&')
else :
    print(words)
print(high)

print
