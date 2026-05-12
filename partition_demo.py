import sys
import partition

input_num = [int(value) for value in sys.argv[1:]]


print("Input numbers:", input_num)
print("Partitioned numbers: ", partition.partition_array(input_num))