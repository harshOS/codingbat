#problem link - https://codingbat.com/prob/p174314

def end_other(a, b):
  if len(a) > len(b) :
    end = b.lower()
    big = a.lower()
  else :
    end = a.lower()
    big = b.lower()
  if end == big [len(big)-len(end):]:
    return True
  return False

print(end_other('abc', 'abXabc'))