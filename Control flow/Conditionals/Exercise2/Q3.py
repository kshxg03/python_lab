
# Ask user for three sides of a triangle and display type of triangle in format: This is an isosceles triangle. 
# (Rule: All sides equal => Equilateral, Two sides equal => Isosceles, No sides equal => Scalene)

first_side = (input("give me first side of the triangle: "))
second_side = (input("give me second side of the triangle: "))
third_side = (input("give me third side of the triangle: "))

if first_side == second_side == third_side:
    print("The triangle is an equilateral triangle.")
elif (
    first_side == second_side or 
    first_side == third_side or 
    second_side == third_side
):
    print("The triangle is an isosceles triangle.")
elif first_side != second_side != third_side:
    print("The traingle is an scalene triangle.")



