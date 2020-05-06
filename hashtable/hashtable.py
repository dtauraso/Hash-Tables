class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    
    # def beforeHead(self, current, key, value):

    #     new_node = HashTableEntry(key, value)
    #     if current.next is None:
    #         current.next = new_node

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):

        self.storage = [None] * capacity
        self.population = 0
        self.capacity = capacity
    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        str_bytes = str(key).encode()
        total = 0
        
        # Loop through all the bytes
        for b in str_bytes:
            total += b
            total &= 0xffffffff  # clamp to 32 bits
            
            # To make your FNV-1 hash correct, add this as the last line of the loop:
            total &= 0xffffffffffffffff  # 64-bit (16 f's)

        return total


    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        str_bytes = str(key).encode()

        total = 0
        # Loop through all the bytes
        for b in str_bytes:
            total += b

             # To make your DJB2 hash correct, add this as the last line of the loop:
            total &= 0xffffffff  # 32-bit (8 f's)

        return total

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        '''
        get the expected index
        if no collision
            store (key, value)
        else
            go to end of linked list and append it
        '''
        location = self.hash_index(key)
        if self.storage[location] is None:
            self.storage[location] = HashTableEntry(key, value)
            self.population += 1
            if self.find_load_factor() < 0.7:
                self.down_size()

        else:
            # put in a new head
            new_node = HashTableEntry(key, value)
            new_node.next = self.storage[location]
            self.storage[location] = new_node
            self.population += 1
            if self.find_load_factor() < 0.7:
                self.down_size()


    def find_load_factor(self):
        return self.population / self.capacity
    def down_size(self):
        if self.capacity // 2 >= 128:
            self.resize(self.capacity // 2)
    def up_size(self):
        self.resize(self.capacity * 2)
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        '''
        get the expected index
        if no collision
            erase (key, value)
        else
            head = array slot
            next = first item in linked list
            delete the node
        '''
        location = self.hash_index(key)

        # at least 1 node
        # if self.storage[location] is not None:
            
        #     self.storage[location] = None
        #     self.population -= 1
        
        # Find the node to delete
        cur = self.storage[location]
        head = self.storage[location]
        # there is no key to delete
        if cur is None:
            return None

        # the head key is being deleted
        # Delete the head special case
        if cur.key == key:
            # print('this case', cur.key)
            head = head.next
            # print('head', head.key)
            # print('cur', cur.key)

            cur.next = None
            # head is not the same so must set the base location back to head
            self.storage[location] = head
            self.population -= 1
            if self.find_load_factor() < 0.2:
                self.up_size()
            # self.printList(head)
            # print()
            return cur

        # if the head is not the right key
        # maintain a prev and cur where cur is the first node
        prev = None
        # look ahead
        while cur is not None:
            if cur.key == key:
                # Found it, delete it
                prev.next = cur.next
                cur.next = None
                self.population -= 1
                if self.find_load_factor() < 0.2:
                    self.up_size()

                return cur

            prev = cur
            cur = cur.next

        return None
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        '''
        get the expected index
        if no collision
            return (key, value)
        else
            
            find in linked list and return it
        '''
        location = self.hash_index(key)
        if self.storage[location] is not None:
            if self.storage[location].next is None:
                return self.storage[location].value
            else:
                # print('colision')

                tracker = self.storage[location]
                while tracker:
                    if(tracker.key != key):
                        tracker = tracker.next
                    else:
                        return tracker.value
                # if we can't find it return None
                return None
        elif self.storage[location] is None:
            return None


    def resize(self, new_size):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

        # print(len(self.storage), self.capacity)

        self.capacity = new_size
        new_table = [None] * self.capacity
        self.population = 0
        for item in self.storage:

            if item:

                # need to visit all nodes in linked list
                tracker = item
                while tracker:

                    # self.put only operates on the old table so this way isn't ideal
                    location = self.hash_index(tracker.key)
                    if new_table[location] is None:
                        new_table[location] = HashTableEntry(tracker.key, tracker.value)
                        self.population += 1

                    else:
                        # put in a new head
                        new_node = HashTableEntry(tracker.key, tracker.value)
                        new_node.next = new_table[location]
                        new_table[location] = new_node
                        self.population += 1
                    tracker = tracker.next

                    # new_table[location] = HashTableEntry(item.key, item.value)
                
        self.storage = new_table
        # print(len(self.storage), self.capacity, 0x20000)

    def __len__(self):
        # print('special function')
        return self.capacity
    def Print(self):
        # print("here")
        for item in self.storage:
            items = []
            if item:
                tracker = item
                while tracker:
                    items.append((tracker.key, tracker.value))
                    tracker = tracker.next
            print(items)
    def printList(self, item):
        items = []
        tracker = item
        while tracker:
            items.append((tracker.key, tracker.value))
            tracker = tracker.next
        print(items)
        # [print(item.key, item.value) for item in self.storage if item is not None]


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
