
# Store list as ["book", "book", "pen", "pen", "pen", "pencil", "marker", "notebook"]
# Save unique items sold in stationary shop in a set as unq_items_set and display the result
# Find and display total number of unique items sold in stationary shop
# Add sticky_notes to unq_items_set set and display updated set
# Remove pen from unq_items_set set and display updated set
# Check if stapler is present in unq_items_set set and display result
# Remove eraser from unq_items_set and display result. Shouldn't give error if not present
# Assign new_items as ["highlighter", "chart_paper"]. Add all items from new_items to unq_items_set and display updated set

items = ["book", "book", "pen", "pen", "pen", "pencil", "marker", "notebook"]

unq_items_set = set(items)
print(unq_items_set)

print(len(unq_items_set))

unq_items_set.add("sticky notes")
print(unq_items_set)

unq_items_set.remove('pen')
print(unq_items_set)

print('stapler' in unq_items_set)

unq_items_set.discard("eraser")
print(unq_items_set)

new_items = ["highlighter", "chart_paper"]
unq_items_set.update(new_items)

print(unq_items_set)