x=open("sample.hql")
str= x.readlines()
if any(item for item in str if "drop" in item):
	print "Script review failed for sample.hql"
	exit(1)
else:
	print "Script review success for sample.hql"
	exit(0)