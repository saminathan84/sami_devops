#x=open("D:\\525419\\devops_poc\\sample.hql")
x=open("sample.hql")
str= x.readlines()
if any(item for item in str if "drop" in item):
	print "failed"
	exit(1)
else:
	print "pass"
	exit(0)