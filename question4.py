list = ["palindrome", "madamimadam", "idolize", "jahaj"]
newlist = []
for i in list:
    if i == i[::-1]:
        newlist.append("Palindrome!")
    else:
        newlist.append("Not a palindrome!")

print(newlist)