#replacing all spaces with underscores.
import re
text="hai hello good morning all"

#logic
#replacing all whitespaces " " with _
output=re.sub(" ","_",text)
print(output)
