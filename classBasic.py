class Employee:
    pass
e=Employee
e.eid=101
e.ename="abc"
e.salary=1000
print(e.eid,'\t',e.ename,'\t',e.salary)

e2=Employee
e2.eid=202
e2.ename = "xyz"
e2.salary = 2000
e2.bonus=1000

print(e.eid,'\t',e.ename,'\t',e.salary)
print(e2.eid,'\t',e2.ename,'\t',e2.salary,'\t',e2.bonus)

e3 = Employee
e3.id=20
print(e3.id)
print(e2.eid,'\t',e2.ename,'\t',e2.salary,'\t',e2.bonus)
