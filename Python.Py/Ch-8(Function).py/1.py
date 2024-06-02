def percent (marks):
    p=(sum(marks)/400)*100
    return p

marks1=[98,98,97,99]
percentage1=percent(marks1)

marks2=[99,99,98,99]
percentage2=percent(marks2)

print(percentage1,percentage2)