# problem link - https://codingbat.com/prob/p170842

def double_char(str):
  str2 = ''
  for i in range(len(str)):
    str2 += 2*str[i]
  return str2

print(double_char('Hi-There'))