import Queue
import Exceptions
import json 

class Queue(Queue.Queue):
    def __init__(self, name, max_size):
        self.items = []
        self.size = 0
        self.name = name
        self.max_size = max_size


    def enqueue(self, item):
        try:
            if(self.size == self.max_size):
                raise Exceptions.QueueOutOfRangeException(f'Queue max size is {self.max_size}')
        except Exceptions.QueueOutOfRangeException as error:
            print(error.msg)
        else:
            self.size += 1
            return super().enqueue(item)


    def dequeue(self):
        if self.size > 0:
            self.size -= 1
        return super().dequeue()

    
    def save(self):
        current_queue_data = {
            self.name : self.__dict__
        }
        queues_file = open("Queue/queues.json", "w") 
        json.dump(current_queue_data, queues_file, indent = 4) 
        queues_file.close() 
        return True


    def load(self):
        queues_file = open('Queue/queues.json')
        data = json.load(queues_file)
        current_queue = data[self.name]['items']
        queues_file.close()
        return current_queue



def main():

    q1 = Queue('Q1', 5)
    print(q1.is_empty())
    q1.enqueue('A')
    q1.enqueue('B')
    q1.enqueue('C')
    q1.enqueue('D')
    q1.enqueue('E')
    q1.enqueue('F')

    print(q1.dequeue())
    q1.enqueue('H')

    print(q1.__dict__)
    print(q1.__dict__)
    q1.save()
    print(q1.load())


if __name__ == "__main__":
    main()




