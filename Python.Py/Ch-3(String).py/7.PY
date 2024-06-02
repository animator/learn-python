s="This is a string with double space  and we need to place it with single space"

doublespace=s.find("  ")
print(doublespace)

s=s.replace("  "," ")
print(s)