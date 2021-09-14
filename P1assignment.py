#TatiyanaHicks
#Course:151, Prof.Mehri
#Date 9/29/2021
#Programming Assignment
#Program inputs(length,width,height)
#Program outputs  (total area of the room in need of paint, # of primer gallons needed painting, # of paint needed for painting)

#ask user for room dimensions (convert inputs to a float)
print("Enter the dimensions")
W = float(input("w"))
H = float(input("h"))
L = float(input("l"))
#calculate the total area of the room in need of paint
area = ((L * H * 2) + (W * H * 2 ) + (L * W ))
#calculate the # of primer gallons needed for painting, # of paint needed for painting
primer = area / 200
paint = area / 350
#print program outputs
print("the total area of the room in need if paint is", area, "sqft")
print("the # of primer gallons needed for painting is" , primer, "gallons")
print("the # of paint needed for painting is" , paint, "gallaons")



