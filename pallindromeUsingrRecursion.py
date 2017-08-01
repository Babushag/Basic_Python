stringEnter=input("Enter the value")
#strnew=stringEnter[::]
def reverse(text):
  if len(text) <= 1:
    return text

  return reverse(text[1:]) + text[0]
strnew=reverse(stringEnter)
if strnew ==stringEnter:
  print("Yeah!! It is a Pallindrome")
else:
  print("oops!! It is not A Pallindrome")