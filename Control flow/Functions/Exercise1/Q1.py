
# Write a function get_simple_interest(principal, rate, time) to calculate and return simple interest based on given principal, rate and time.


def get_simple_interest(principal, rate, time):
    simple_interest = (principal*rate*time)/100
    return simple_interest

print(get_simple_interest(1000, 4, 3))