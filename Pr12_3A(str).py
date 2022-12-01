#3_A(str)
#Reverse number

def reverse(n):
    if len(n) != 0:
        return reverse(n[1:]) + n[0]
    else:
        return(n)

n = input("Enter number: ")
print("Reverse number: %s" % reverse(n))


