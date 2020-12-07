# Python3 implementation of above approach 

# Function to check if n is palindrome 
def isPalindrome(n) : 
	
	# Find the appropriate divisor 
	# to extract the leading digit 
	divisor = 1
	
	while (n / divisor >= 10) : 
		divisor *= 10

	while (n != 0) : 
		
		leading = n // divisor 
		trailing = n % 10

		# If first and last digits are 
		# not same then return false 
		if (leading != trailing) : 
			return False

		# Removing the leading and trailing 
		# digits from the number 
		n = (n % divisor) // 10

		# Reducing divisor by a factor 
		# of 2 as 2 digits are dropped 
		divisor = divisor // 100
	
	return True

# Function to find the largest 
# palindromic number 
def largestPalindrome(A, n) : 

	# Sort the array 
	A.sort() 

	for i in range(n - 1, -1, -1) : 

		# If number is palindrome 
		if (isPalindrome(A[i])) : 
			return A[i] 
	
	# If no palindromic number found 
	return -1

def make_palindrome(A):


# Driver Code 
if __name__ == "__main__" : 

	A = [937, 113] 
	n = len(A) 

	# print required answer 
	print(largestPalindrome(A, n)) 

# This code is contributed by Ryuga 


# p = largestPalindrome([937, 113], 2)
# print(p)

mport functools
import operator

def product(seq):
    """Product of a sequence."""
    return functools.reduce(operator.mul, seq, 1)