
class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bit_array = [0] * size

    def hash1(self, item):
        total = 0
        for character in item:
            total = total + ord(character)
        return total % self.size

    def hash2(self, item):
        total = 0
        for index, character in enumerate(item):
            total = total + (index + 1) * ord(character)
        return total % self.size

    def add(self, item):
        position1 = self.hash1(item)
        position2 = self.hash2(item)

        self.bit_array[position1] = 1
        self.bit_array[position2] = 1

        print(item, "added at positions", position1, "and", position2)

    def check(self, item):
        position1 = self.hash1(item)
        position2 = self.hash2(item)

        if (self.bit_array[position1] == 1 and
                self.bit_array[position2] == 1):
            return "Probably Present"
        else:
            return "Definitely Not Present"


bloom_filter = BloomFilter(20)

bloom_filter.add("pooja")
bloom_filter.add("rahul")
bloom_filter.add("priya")
bloom_filter.add("amit")

print("\nBloom Filter Bit Array:")
print(bloom_filter.bit_array)

print("\nSearch Results:")
print("pooja :", bloom_filter.check("pooja"))
print("rahul :", bloom_filter.check("rahul"))
print("neha  :", bloom_filter.check("neha"))
print("rohan :", bloom_filter.check("rohan"))

