class Node:
	"""One item in a singly linked list."""

	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:
	"""A small linked list with basic operations."""

	def __init__(self):
		self.head = None

	def append(self, value):
		"""Add value to the end of the list."""
		node = Node(value)
		if self.head is None:
			self.head = node
			return

		current = self.head
		while current.next is not None:
			current = current.next
		current.next = node

	def prepend(self, value):
		"""Add value to the beginning of the list."""
		node = Node(value)
		node.next = self.head
		self.head = node

	def find(self, value):
		"""Return True if value is present, otherwise False."""
		current = self.head
		while current is not None:
			if current.value == value:
				return True
			current = current.next
		return False

	def delete(self, value):
		"""Delete the first matching value; return whether it was found."""
		if self.head is None:
			return False
		if self.head.value == value:
			self.head = self.head.next
			return True

		current = self.head
		while current.next is not None:
			if current.next.value == value:
				current.next = current.next.next
				return True
			current = current.next
		return False

	def display(self):
		"""Print the list in order."""
		current = self.head
		values = []
		while current is not None:
			values.append(str(current.value))
			current = current.next
		print(" -> ".join(values) if values else "(empty)")


if __name__ == "__main__":
	numbers = LinkedList()
	numbers.append(10)
	numbers.append(20)
	numbers.prepend(5)

	print("List:", end=" ")
	numbers.display()  # 5 -> 10 -> 20
	print("Contains 10:", numbers.find(10))
	numbers.delete(10)
	print("After deleting 10:", end=" ")
	numbers.display()  # 5 -> 20
