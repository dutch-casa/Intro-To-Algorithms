'''
COMP 3270 Intro to Algorithms Homework 1: Introduction to Python
install python (google it) and make sure you have python version 3.6+ 
'''
import random
import time

'''
Problem 1: Make your own hashmap class from scratch (using only python lists). dicts not allowed. This problem will be 75% of this homework
Implement chaining in case of collisions. 
Use any hash function you like (such as those in the lecture notes). 
The underlying list may be fixed length. You do not have to account for the need to double its size when it is near capacity. Set it to 1024
Allow for types int and str (to convert an arbitrary str to a number you can use number = int.from_bytes(mystring.encode('utf-8'), 'little') and to recover the str you can use recoveredstring = number.to_bytes((number.bit_length() + 7) // 8, 'little').decode('utf-8').
For each key, there should be an associated value.
Implement insert(self, key, value), delete(self, key), get(self, key), and iter(self) which only loops through non-empty key, value pairs.
See https://www.w3schools.com/python/python_iterators.asp for how to implement an iterator in python
'''
# your code here
class HashMap:
    def __init__(self, size=1024):
        self.size = size
        # Each bucket is a list to handle collisions via chaining.
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def insert(self, key, value):
        index = hash(key) % self.size
        bucket = self.table[index]
        # Check if the key already exists in the bucket.
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Update the value if key exists.
                bucket[i] = (key, value)
                return
        # Key does not exist, so append it.
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        index = hash(key) % self.size
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = hash(key) % self.size
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return

    def __iter__(self):
        # Yield only non-empty key, value pairs.
        for bucket in self.table:
            for pair in bucket:
                yield pair



'''
Problem 2: Use your hashmap class to count the number of each substring of length k in a DNA sequence. 
Print out the repeated items and the number of times they were repeated
run it on string "ATCTTGGTTATTGCGTGGTTATTCTTGC" with k=4
'''
#your code here
def count_substrings(sequence, k):
    map = HashMap()
    for i in range(len(sequence) - k + 1):
        substring = sequence[i:i+k]
        if map.get(substring) is not None:
            map.insert(substring, map.get(substring) + 1)
        else:
            map.insert(substring, 1)
    for key, value in map:
        if value > 1:
            print(key, value)

count_substrings("ATCTTGGTTATTGCGTGGTTATTCTTGC", 4)


'''
Problem 3: Two sum. This time just use the python dict or set. 
Given an array, find two numbers that sum to a target number (don't worry about not reusing the same index this time). 
Code this two ways. Once brute force with nested for loops. And once using hashing. 
Use the input below. Bonus to code the sorting/binary search method. Feel free to use sort() or sorted() but code binary search yourself.
Compare the time taken between the implementations using the time package imported above.
'''
A = [random.randint(0,10000) for i in range(10000)]
target = A[random.randint(0, len(A)-1)] + A[random.randint(0,len(A)-1)]


def brute_force(A, target):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                return A[i], A[j]
    return None

def hash_method(A, target):
    map = {}
    for i in range(len(A)):
        complement = target - A[i]
        if complement in map:
            return complement, A[i]
        else:
            map[A[i]] = i
    return None

print(target)
print(brute_force(A, target))
print(hash_method(A, target))