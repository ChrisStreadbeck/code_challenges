#alphabetizes the characters of any string

strng = "this is a string"

def alphabetizes(strng):
  newstring = ''.join(sorted(strng))
  return newstring

print(alphabetizes(strng))