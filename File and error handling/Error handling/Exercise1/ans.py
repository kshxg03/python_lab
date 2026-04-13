

def string_lowercase(text):
    try:
        new_str = ""
        for each in text:
            if each == each.lower():
                new_str += each
            
        return new_str
    except TypeError:
        return "Give valid text"
    
print(string_lowercase(11))


def density_calc(mass, volume):
    try:
        density = mass/volume
        
        return density
    except ZeroDivisionError:
        return "Volume cannot be 0"
    except TypeError:
        return "Wrong input"
    
print(density_calc(2, 0))

def get_name(dict, keyname):
   try: 
       result = dict[keyname]
       return result
   except KeyError:
       return "Key doesnot exist"
       
my_dict = {"a": 1, "b": 1, "c": 3}
print(get_name(my_dict, "d"))

def get_third_element(list):
    try:
        result = list[2]
        return result
    except IndexError:
        return "List should have more than 3 items."

my_list = [1, 2]
print(get_third_element(my_list))