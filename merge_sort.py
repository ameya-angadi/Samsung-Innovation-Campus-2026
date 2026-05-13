def divide_array(numbers, low, high):	
	if low < high:
		mid = (low+high) // 2
	divide_array(low, mid-1)
	divide_array(mid+1, high)
	merge(numbers[low:mid+1], numbers[mid+1:high])
		
def merge(array_a, array_b):
	merged_array = []
	i = j = k = 0
	while i < (len(array_a)) and j < (len(array_b)):
		if array_a[i] < array_b[j]:
			merged_array[k].append(array_a[i])
			i+=1
		else:
			merged_array[k].append(array_b[j])
			j += 1
		merged_array.extend(array_a[i:])
		merged_array.extend(array_b[j:])
		
