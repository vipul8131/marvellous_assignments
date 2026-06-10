# Q1. 
myData = 119
# show value
print("myData value=", myData)
# show typw of variable
print("Type of myData=", type(myData))
# show memory address
print("Memory address of myData=", id(myData))

print("=============================================")
# Q2.
a = 10
b = 10
print("Memory Address of a=",id(a), " & Memory address of b=", id(b))

a = [10]
b = [10]
print("Memory Address of a[10]=",id(a), " & Memory address of b[10]=", id(b))

# Above first a = 10 & b = 10 both are int datatype and both are immutable so it will reuses the same Memory address.
# In 2nd a[10] & b[10] both are list datatype so List are mutable so python will consider it is different memory location.
print("=============================================")





