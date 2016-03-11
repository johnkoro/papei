from bitarray import bitarray
import hashlib
 
class BloomFilter:
    
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        
    def add(self, string):
        for seed in xrange(self.hash_count):
            result = int(hashlib.sha256(string + str(seed)).hexdigest(),16) % self.size
            self.bit_array[result] = 1
            
    def lookup(self, string):
        for seed in xrange(self.hash_count):
            result = int(hashlib.sha256(string + str(seed)).hexdigest(),16) % self.size
            if self.bit_array[result] == 0:
                print "--", sentence ,"--"
                return ""
            else:
                return sentence
 
bf = BloomFilter(500000, 7)

lines = open("american-english.txt").read().splitlines()
for line in lines:
    bf.add(line)
protaseis = open("keimeno.txt", "r")
a = protaseis.readlines()
for line in lines:
    sentences = line.split()
for sentence in a :
        print (sentence)
for sentence in sentences:
    print bf.lookup(sentence)
  


