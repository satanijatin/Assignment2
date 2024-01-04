def isPalindrome(s):
	return s == s[::-1]

s = str(input("Enter String : "))
ans = isPalindrome(s)

if ans:
	print("String is Palindrom")
else:
	print("String is Not Palindrom")
