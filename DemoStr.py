#DemoStr.py

strA = "파이썬은 강력해"
strB = "python is very powerful"

print(len(strA))
print(strB.capitalize())
print(strB.count("p"))
print("MBC2580".isalnum())
print("2580".isdecimal())


data = "<<< spam and ham >>>"
result = data.strip("<> ")
print(data)
print(result)
result = result.replace("spam","sapm egg")
print(result)
lst = result.split()
print(lst)
print(":)".join(lst))

import re
#result = re.search()

result=re.search("apple", "this is apple")
print(result.group())

result=re.search("\d{4}", "올해는 2024년입니다.")
print(result.group())

result=re.search("\d{5}", "우리 동네는 52100입니다.")
print(result.group())
