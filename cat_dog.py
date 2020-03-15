# problem link - https://codingbat.com/prob/p164876

def cat_dog(str):
  cat_count = 0
  dog_count = 0
  for i in range (len(str)):
    if str[i:i+3] == 'cat' : cat_count += 1
    if str[i:i+3] == 'dog' : dog_count += 1
  if cat_count == dog_count : return True
  return False
print(cat_dog('1cat1cadodog'))