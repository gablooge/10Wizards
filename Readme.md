# There are 10 people at a wizard meetup. 
# Each wizard has levels 0 - 9 (the index of the input) and 
# knows a few other wizards there. 
# Your job is to find the cheapest way for wizard 0 to meet wizard 9.
# Introductions have a cost that equals the square of the difference in levels. 

# Goal: Level 0 wizard wants to meet level 9 using the fewest possible magic points.
# Cost: square of difference of levels
# The index of the array represents the level (0-9)
# the value is an array with the index of the other people each person knows. 
# Note that relationships are one directional (e.g. 2 can introduce you to 3 but not vice versa)
# e.g. Min cost: 23 Min path: [0, 1, 4, 6, 9]


# $ python solution.py < input.txt > output.txt
