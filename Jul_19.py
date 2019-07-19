#------------------------------------
# checks to see if a word is a palindrome
test1 = "maam"
test2 = "hello"

def paly(word):
  if word == word[::-1]:
    print("tis a palindrome")
  else:
    print("not a palindrome")


paly(test1)
paly(test2)


#------------------------------------
#removes the first and last element __import__
html = ['<h1>', 'Some Content', '</h1>']
html2 = ['<h1>', 'Some Content', 'more', '</h1>']

def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content


print(remove_first_and_last(html))
print(remove_first_and_last(html2))
#------------------------------------