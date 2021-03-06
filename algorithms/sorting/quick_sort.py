# QuickSort

# Stage 1
# - Pick an element to be the pivot. In practice, this is usually the first or final element in the array.
# 
# Stage 2
# - Go through the array, comparing every value to the pivot.
# - Values less than the pivot should be moved before it, while values greater than the pivot should come after it. This is called the partition operation.
# - You are left with two sub-arrays: one with numbers greater than the pivot value; the other with numbers less than it.
#
# Stage 3
# - Recursively apply steps 1 and 2 to each sub-array and repeat, until you can create no further sub-arrays.
# - At that point, the sub-arrays are joined back into a single array.

def quicksort(arr):
  # If a sub-array has only 1 value, the array is sorted and can be returned
  if len(arr) <= 1:
    return arr

  # Define pivot, and create empty "left" and "right" sub-arrays
  pivot = arr[0]
  left = []
  right = []
  # Go through the array, comparing values to the pivot, and sorting them into the "left" and "right" sub-arrays
  for i in range(len(arr)):
    # Ensure pivot itself is not in left or right
    if arr[i] < pivot:
      left.append(arr[i])
    elif arr[i] > pivot:
      right.append(arr[i])
    
  # Repeat using recursion
  return quicksort(left) + [pivot] + quicksort(right)

if __name__ == '__main__':
  a = quicksort([6, 4, 8, 2, 10, 9])
  print(a)