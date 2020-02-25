# Rectangle Area Calculator
# 2/25/20
# CTI-110 P3T1- Areas of Rectangles 
# Ethan Duenweg

# First we need to get the rectangle dimensions from the user

print("Rectangle Area Calculator")
h1 = int(input("What's the height of the rectangle 1?"))
w1 = int(input("Whats the width of rectangle 1?"))
h2 = int(input("What's the height of rectangle 2?"))
w2 = int(input("Whats the width of rectangle 2?"))

# We then need to calculate which of these rectangles would have the largest area using multiplication

area1 = (h1 * w1)
area2 = (h2 * w2)

# Now we can use 'if' functions to determine the greater number, which will be the largest area.
# We will also display the outcome to the user

if area1 > area2:
    print('Rectangle 1 has the greatest area')
else:
    if area2 > area1:
        print('Rectangle 2 has the greatest area')
    else:
        print('Both rectangles have the same area')
    
