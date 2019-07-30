#removes the first and last element __import__

html = ['<h1>', 'Some Content', '</h1>']
html2 = ['<h1>', 'Some Content', 'more', '</h1>']

def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content


print(remove_first_and_last(html))
print(remove_first_and_last(html2))