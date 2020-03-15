# problem link - https://codingbat.com/prob/p167246

def count_hi(str):
  count = 0
  for i in range(len(str)):
    if str[i:i+2] == 'hi':
      count += 1
  return count

print(count_hi('ABChi hi'))