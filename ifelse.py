#ifelse.py

score=int(input("점수입력바람:"))

if 90 <= score <=100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
else:
    grade = 'D'

print("등급",grade)