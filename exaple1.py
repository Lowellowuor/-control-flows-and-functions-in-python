grade = [91,85,78,69,74] # Example grade value
for grade in grade:
	if grade >= 90:
		print("A")
	elif grade >= 80:
		print("B")
	elif grade >= 70:
		print("C")
	elif grade >= 60:
		print("D")
	elif grade >= 50:
		print("E")
	else:
		print("FAIL")