#### SET IMPLEMENTATION BY OWN

class My_Set:
    def __init__(self,capacity=10):
        self.capacity = 10
        self.table = [[] for _ in range(capacity)]
        self.size = 0

    def _hash(self,element):
        """ Hash Function """
        return hash(element)%self.capacity

    def add(self,element):
        """ Add Element (No Duplicates)"""
        index = self._hash(element)
        bucket = self.table[index]

        for item in bucket:
            if item == element:
                return

        bucket.append(element)
        self.size += 1


    def remove(self,element):
        """Remove Element if exits"""
        index = self._hash(element)
        bucket = self.table[index]

        for i,item in enumerate(bucket):
            if item == element:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def contains(self,element):
        """Check if the element is in hash Table"""
        index = self._hash(element)
        bucket = self.table[index]
        return element in bucket

    def union(self,other_set):
        """Make union of two sets"""
        result = My_Set(self.capacity+other_set.capacity)
        for bucket in self.table:
            for item in bucket:
                result.add(item)

        for bucket in other_set.table:
            for item in bucket:
                result.add(item)

        return result

    def intersection(self,other_set):
        """Make intersection of two sets"""
        result = My_Set(min(self.capacity,other_set.capacity))
        for bucket in self.table:
            for item in bucket:
                if other_set.contains(item):
                    result.add(item)

        return result

    def difference(self,other_set):
        """Return new set with elements in self but not in other"""
        result = My_Set(self.capacity)
        for bucket in self.table:
            for item in bucket:
                if not other_set.contains(item):
                    result.add(item)

        return result

    def __repr__(self):
        elements = []
        for bucket in self.table:
            elements.extend(bucket)
        return "{" +  ",".join(map(str,elements))+"}"


if __name__ == "__main__":
    s1 = My_Set()
    s1.add(1)
    s1.add(2)
    s1.add(3)

    s2 = My_Set()
    s2.add(3)
    s2.add(4)
    s2.add(5)

    print("Set 1:", s1)
    print("Set 2:", s2)

    print("Union:", s1.union(s2))
    print("Intersection:", s1.intersection(s2))
    print("Difference (s1 - s2):", s1.difference(s2))

    print("Contains 2?", s1.contains(2))
    print("Remove 2:", s1.remove(2))
    print("After removing 2:", s1)
