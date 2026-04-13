
# Daaraz found that their top electronic gadget buyer's are ram, shyam, sita, hari. Cosmetic buyers are hari, sita, gita, rita. Top grocery buyer's are ram, hari, gita and rabi. Find:
# Customers are top buyers of all electronics, cosmetics and groceries
# Customers who are top buyer of single category only
# Customers who are top buyers of exactly two categories
# All unique customers who are top buyers of at least one category
# Customers who are top buyers of electronics but not cosmetics

top_gadget_buyers = {"ram", "shyam", "sita", "hari"}

top_cosmetic_buyers = {"rita", "gita", "sita", "hari"}

top_grocery_buyers = {"ram", "gita", "rabi", "hari"}

# Customers are top buyers of all electronics, cosmetics and groceries
top_customers_all = top_gadget_buyers & top_cosmetic_buyers & top_grocery_buyers
print(top_customers_all)

# Customers who are top buyer of single category only
only_gadget_buyers = top_gadget_buyers - (top_cosmetic_buyers | top_grocery_buyers)
print(only_gadget_buyers)

only_cosmetic_buyers = top_cosmetic_buyers - (top_gadget_buyers | top_grocery_buyers)
print(only_cosmetic_buyers)

only_grocery_buyers = top_grocery_buyers - (top_gadget_buyers | top_cosmetic_buyers)
print(only_grocery_buyers)


# Customers who are top buyers of exactly two categories
gadget_cosmetic_buyers = (top_gadget_buyers & top_cosmetic_buyers) - top_grocery_buyers
print(gadget_cosmetic_buyers)

cosmetic_grocery_buyers = (top_cosmetic_buyers & top_grocery_buyers) - top_gadget_buyers
print(cosmetic_grocery_buyers)

gadget_grocery_buyers = (top_gadget_buyers & top_grocery_buyers) - top_cosmetic_buyers
print(gadget_grocery_buyers)

# All unique customers who are top buyers of at least one category
unique_one_category = top_gadget_buyers | top_cosmetic_buyers | top_grocery_buyers
print(unique_one_category)

# Customers who are top buyers of electronics but not cosmetics
electronics_but_not_cosmetics = top_gadget_buyers - top_cosmetic_buyers
print(electronics_but_not_cosmetics)
