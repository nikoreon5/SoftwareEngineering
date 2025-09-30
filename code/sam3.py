from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
maxSemiPerimeter = (max(one) + max(two) + max(three)) / 2
minSemiPerimeter = (min(one) + min(two) + min(three)) / 2
minSquare = sqrt(minSemiPerimeter * (minSemiPerimeter - min(one)) * (minSemiPerimeter - min(two)) * (minSemiPerimeter - min(three)))
maxSquare = sqrt(maxSemiPerimeter * (maxSemiPerimeter - max(one)) * (maxSemiPerimeter - max(two)) * (maxSemiPerimeter - max(three)))
print(minSquare)
print(maxSquare)