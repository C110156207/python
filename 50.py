# 找出班上成績問題
student = set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
eng = set(['John','Mary','Fiona','Claire','Ben','Bill'])
math = set(['Mary','Fiona','Claire','Eva','Ben'])
print('英文與數學都及格',eng&math)
print('數學不及格',math^student)
print('英文及格且數學不及格',eng&(math^student))