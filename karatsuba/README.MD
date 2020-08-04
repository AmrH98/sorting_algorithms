# Sorting Algorithms Implementation

### Karatsuba


##### General Treatment

- X and Y n-digit string in base B
- m < n
  example: x = x1 B^m + x0
- x0 and y0 less than B^m
- z2 = x1y1
- z1 = x1y0 + x0y1
- z0 = x0y0
- result = z2 B^2m + z1B^m + z0
