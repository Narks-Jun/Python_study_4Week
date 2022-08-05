str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
# print(ipos)
piece = str[ipos+2:]
# print(piece)
# print(piece+42.0) This will failed because piece is string
value = float(piece)
print(value)
