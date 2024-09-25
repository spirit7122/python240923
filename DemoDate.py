#DemoDate.py
from datetime import *

d1= date(2024,9,1)
print(d1)
d2 = date.today()
print(d2)
d3 = datetime.now()
print(d3)
d4 = timedelta(days=100)
print("주문받고 100일후:",d2+d4)


import random
print(random.random())
print(random.random())
print(random.uniform(2.0, 5.0))
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20),10))
print(random.sample(range(20),10))

print(random.sample(range(1,46),5))

#파일명 다루기
from os.path import *
from os import *

print(abspath("pythoin.exe"))

print(basename("c:\\수업자료\\work\\python.exe"))

fName= "c:\python310\\python.exe"
if exists(fName):
    print("파일크기", getsize(fName))
else:
    print("파일없음")

print(name)
print(environ)

import glob
print(glob.glob("c:\\수업자료\\work\\*.py"))