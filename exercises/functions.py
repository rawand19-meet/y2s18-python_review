# Write your solution for 1.4 here!

def is_prime(x):
    prime = true
    for i in range(2,x):
        if x % i==0:
            return False
        else:
		    return True
print (is_prime(21))
