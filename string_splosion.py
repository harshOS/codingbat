#problem
#Given a non-empty string like "Code" return a string like "CCoCodCode".
#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'


def string_splosion(str):
  temp = ''
  for i in range(len(str)+1):
    temp +=str[0:i]
  return temp

print(string_splosion('Code'))