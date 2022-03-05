# Data Partitioner
A small project that allows you to divide up a string, list or tuple into even percentage, and return the specified segment or partition.

> **Note:** It currently doesn't handle inputting a percentage higher than 50% too well, also working on a bug where percentages are not evenly divisible cause issues.

## Installation
Simply clone from GitHub or Pypi with the following command:
```
git clone git:github.com/uxai/data-partitioner
```
```
pip install data-partitioner
```

## Usage
If you have a list of numbers, you can easily divide it into even partitions and grab a specific segment, if you only want to pass in one type:

### Arguments as single pass
The arguments of the function is as follows:
1. List / String / Tuple
2. An integer range from 1 - 100, This is the % divisible.
3. Integer or Tuple of numbers indicating the segments you want to retrieve
4. Optional `tail=` argument of boolean. Setting to true states if you want the larger groups at the tail end of the partitions or front/

For example if we have a list of 12 integers: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]` and want to partition it into 5 groups evenly, there are some 'widow indexes' that need to be accounted for:
```python
import partitioner as p

my_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(p.pal(my_data, 20, (1,2,3,4,5), tail=False))
```
```
Output:
[
    [1, 2], [3, 4], [5, 6], [7, 8, 9], [10, 11, 12]
]
```
if we give `tail=True` the result would be:
```
Output:
[
    [1, 2, 3], [4, 5, 6], [7, 8], [9, 10], [11, 12]
]
```

### Processing multiple data sets
If we want to pass multiple data points, we can do so by using a similar format above, but wrapping each inside of paranthesis.
```python
import partitioner as p

my_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_data = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(p.pal((my_data, 20, (1,2,3,4,5)), (new_data, 50, (1,2)), tail=False))
```
```
Output:
[
    [
        [1, 2, 3], [4, 5, 6], [7, 8], [9, 10], [11, 12]
    ], 
    [
        ['a', 'b', 'c', 'd'], ['e', 'f', 'g']
    ]
]
```