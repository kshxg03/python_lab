

# Write a function get_rectangle_area_perimeter(length, width) to calculate and return area and perimeter of a rectangle based on length and width.

def get_rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2*(length + width)
    return area, perimeter

area, perimeter = get_rectangle_area_perimeter(2, 3)
print(f"Area: {area} and perimeter: {perimeter}")