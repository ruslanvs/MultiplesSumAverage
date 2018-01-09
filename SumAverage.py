# 1) Prints the sum of all the values in the list
a = [1, 2, 5, 10, 255, 3]
print "List", a
total = 0

# iterate through the list and add up every value, then print the total
for i in range (0, len(a)):
    total += a[i]

print "total via loop", total

# sum and print the list values using built-in sum function
print "total via built-in sum", sum(a)


# 2) Prints the average of the values in same list.
for i in range (0, len(a)):
    total += a[i]

print total, float( len(a) )
print "Average via loop:", av, "No built-in function identified. Do not forget to include the float type"