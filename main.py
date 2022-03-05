# Sample
import random
import src.partitioner as p

my_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_data = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(p.pal(my_data, 25, (1,2,3), tail=False))