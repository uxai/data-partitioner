# Sample data with output split 50/50 and retrieving both
import random
import src.partitioner as p

my_data = [random.uniform(0, 1) for _ in range(0, 10)]

print(p.pal(my_data, 50, tail=False))