1. Aim To understand and implement a Bloom Filter using Python for checking whether a given item is probably present or definitely not present in a set.
2. Objectives 
3. To understand the concept of probabilistic data structures.
4. To understand the use of a bit array and hash functions in a Bloom Filter.
5. To implement insertion and membership-checking operations.
6. To identify the possibility of false-positive results.
7. To analyze the memory-efficient nature of a Bloom Filter.
8. 5. Theory
   6. 5.1 Bit Array :
       A Bloom Filter contains an array of bits. Every position initially contains 0. When an item is inserted, selected positions are changed to 1.
   5.2  Hash Functions :
       A hash function converts an item into a numeric position. This practical uses two different hash functions. Therefore, every item produces two positions in the bit array.
      5.3 Insertion Operation :
       To insert an item, calculate its positions using both hash functions and set the bits at both positions to 1. The original item is not stored.
      5.4 Membership-Checking Operation :
       To search an item, calculate the same two positions. If at least one required position contains 0, the item is definitely not present. If both positions contain 1, the item is probably present.
      5.5 False Positive :
       A false positive occurs when an item was not inserted, but all its required positions were already set to 1 by other items. The Bloom Filter then reports the item as probably present.
      5.6 False Negative :
       A standard Bloom Filter does not produce false negatives, provided that its bits are not incorrectly reset. An inserted item will continue to find its required bits set to 1.
