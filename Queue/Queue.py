class Queue:

	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)
		return item

	def dequeue(self):
		return self.items.pop(0)

	def is_empty(self):
		return len(self.items) == 0



def main():
	q1 = Queue()

	print(q1.is_empty())

	q1.enqueue(1)
	q1.enqueue(2)
	q1.enqueue(3)

	print(q1.is_empty())

	q1.dequeue()

	print(q1.is_empty())

	q1.dequeue()
	q1.dequeue()

	print(q1.is_empty())


if __name__ == "__main__":
    main()



