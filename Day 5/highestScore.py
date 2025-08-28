student_scores= [150,142,185,120,171,184,149,24,59,68,199,78,65,89]

sum1=0

total_exam_score=sum(student_scores)

for score in student_scores:
    sum1+=score
print(total_exam_score)
print(sum1)


print(max(student_scores))
max_score=0

for a in student_scores:
    if a>max_score:
        max_score=a

print(max_score)