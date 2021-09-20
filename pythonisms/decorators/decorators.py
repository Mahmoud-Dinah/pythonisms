from functools import wraps
from time import sleep

def timeFunc(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)

    return wrapper

def original(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Original Value -- {orig_val}'

    return wrapper

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value='null'):
        try:
          node = Node(value)
          if not self.head:
              self.head = node
          else:
              current = self.head
              self.head= node
              self.head.next=current
        except Exception as e:
          raise Exception(f"error happend : {e}")

    def includes(self,num):
        try:
          x=False

          current = self.head
          while current:
              if current.value==num:

                  x=True
                  break
              current=current.next
          return x
        except Exception as e:
          raise Exception(f"error happend : {e}")


    @timeFunc
    @original
    def __str__(self):
        output = ""
        current = self.head
        while current:
            value = current.value
            if current.next is None:
                output += f"( {value} ) -> NULL"
                break
            output += f"( {value} ) -> "
            current=current.next
        return output

if __name__ == "__main__":
    print('test run')
    print('test run 2')
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    print(str(ll))