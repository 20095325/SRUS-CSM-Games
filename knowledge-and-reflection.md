# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A pearson hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

pearson_table = [random.randint(0, 255) for _ in range(256)]

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so.

> At its core a hash function is any function that takes an input which can be an unpredictable size and returns a value that is the same size everytime the function is run. In this case the size of an object is its bit length.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> 1. the Stupidly Simple Hash function is very bad when it comes to collision resistance security, and determinism as it will always produce the same value, however it actually excels in all other categories. the issue is that the main reasons to use hash function in the first place is to avoid collisions and to secure information.
> 2. The sum of all ASCII values is a huge improvement over the first hash function, however it still falls victim to collisions as words which are acronyms or words that add up to the same values will collide. Because so many words will either collide or be close to colliding I do not think that this function will produce uniform values. I think this hash function is efficient as it is only adding values together. This hash function is deterministic as all hash functions should produce the same output for a given input. I would say it is not very secure because it is extremely easy to reverse the algorithm.  
> 3. A pearson hash is efficient and produces uniform values due to its ability to achieve "randomness" by XORing each previous byte of the key. It is very sensitive to input changes because changing 1 bit affects each subsequent XOR and has a very low chance of collisions. It is not cryptographically strong and is vulnerable to an attacker using a pre-image attack.
> 4. The built-in hash for Python is a fast convenient function which Python uses for sets and dictionaries, It is mostly used for hash tables and shouldn't be used a cryptographic hash as it is insecure. Depending on your use case it could produce collision, but it is built is a way so that string which are similar will never collide, but they may be collisions for very large, different strings.
> 5. The SHA256 hash is considered one of the most secure hashes and is even used in blockchain technology to ensure the integrity on the blocks. Although the algorithm in computationally fast on modern hardware, older hardware may struggle. Collisions are theoretically possible but they are extremely rare. Changing one charater in you input value will give you an entirely different hash value, making it very sensitive to input changes.

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> 1. Efficient hash function
> 2. A collision strategy 
> 3. A resizing strategy
> 
> You need to have a hash function in order to use your hash map. It is very important to choose a hash function which suits your needs.
> Then you need a collision strategy to deal with collisions that will occur if you are trying to be efficient with memory. You need a way to handle collisions gracefully whether you decide to ignore collisions or store them using another method inside your hash map, they need to be dealt with.
> A resizing strategy is important because when your as your hash maps load factor increases the likelihood of collisions increases and your performance decreases. Being able to resize your hash map will help maintain a balance between memory usage and performance.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> I chose to use the hashlib module as it has easy to use functions that create hashes that are have a high collision resistance, are uniform and efficient.

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> First we import the random module.
> We then set the seed on the random instance so that it will give us the same "random" values each time we call it.
> We create our pearson table using list comprehension by looping 256 times and each time adding a random int between 0 and 255 to the list.
> We then define our pearson hash function which takes 2 parameters, a key and a size.
> We then define a local variable called hash_ and initialise it to 0.
> We then create a for loop that will iterate over each character in our key.
> In the for loop we store the int from the pearson table that is at the index equal to the previous hash_ variable XORed with the ASCII value of each subsequent character of our key
> Then we return the final hash_ value modulated to the size we require for our hash map.

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

```
# Create the player
# Get the index of the hash_map by hashing the player key
# Get the player list using the index
# Search the player list to see if the key exists
# if the key exsits update that player
# else apend the player to the list

```

## Reflection

1. What was the most challenging aspect of this task?

> The most challenging aspect was definitely trying to understand how some of the more complex hashing algorithms work

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> I probably would have just used a list inside my hash map. Lists are more memory efficient as they do not have to store the pointers to other nodes. they are also easier to work with as creating a linked list can lead to bugs as your linked list becomes more complex. 

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
