# LINKED LIST IMPLEMENTATION

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class Linked_List:
    def __init__(self):
        self.head = None

    def append(self,data):
        """Insert at the end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def pre_append(self,data):
        """ Insert at the beginning of the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self,prev_value,data):
        """Insert after the given data in the linked list"""
        new_node = Node(data)
        cur = self.head
        while cur.next:
            if cur.data == prev_value:
                new_node.next = cur.next
                cur.next = new_node
                return
            cur = cur.next
        print(f"prev value {prev_value} not find in the linked list")

    def search(self,key):
        """"Search a value in the linked list"""
        cur = self.head
        while cur.next:
            if cur.data == key:
                print(f"{key} is present in the linked list")
                return
            cur = cur.next

        print(f"{key} is not present in the linked list")

    def delete(self,key):
        """Delete the elements of the linked list (fiest occurence)"""
        cur = self.head

        #Case1: head is the key
        if cur and cur.data == key:
            self.head = cur.next
            return

        #Case2: key is in the middle or at the end
        prev = None
        while cur and cur.data!=key:
            prev = cur
            cur = cur.next

        if cur:
            prev.next = cur.next
            print(f"Key {key} deleted")
        else:
            print(f"Key {key} not found")

    def print_list(self):
        """Print all elements of the list"""
        cur = self.head
        while cur:
            print(cur.data," -> ")
            cur = cur.next

if __name__ == "__main__":
    ll = Linked_List()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Initial list:")
    ll.print_list()
    ll.pre_append(5)
    print("After prepend 5:")
    ll.print_list()
    ll.insert_after(20, 25)
    print("After inserting 25 after 20:")
    ll.print_list()
    ll.delete(10)
    print("After deleting 10:")
    ll.print_list()
    print("Search 25:", ll.search(25))
    print("Search 100:", ll.search(100))
            
            

    
