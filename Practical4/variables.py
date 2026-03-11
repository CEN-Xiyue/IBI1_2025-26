a = 5.08
b = 5.33
c = 5.55
d = b-a
e = c-b
print("d=",d)
print("e=",e)
if d > e:
    comparison = "The population growth rate slowed down (d > e)"
elif d < e:
    comparison = "The population growth rate accelerated (d < e)"
else:
    comparison = "The population growth rate remained the same (d = e)"
print("In conclusion:", comparison)
# Explanation: d=0.25, e=0.22, so d>e, Scotland's population growth decelerated

#Truth tables are as follows:
X = True
Y = False
W = X or Y
#X true, Y true: W true
#X true, Y false: W true
#X false, Y true: W true
#X false, Y false: W false