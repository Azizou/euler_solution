import unittest
from  triangle import Node
class TestNodeMethods(unittest.TestCase):

	def setUp(self):
		self.a = Node(8,None,None)
		self.b = Node(5,None,None)
		self.c = Node(9,None,None)
		self.d = Node(3,None,None)
		self.e = Node(2,self.a,self.b)
		self.f = Node(4,self.b,self.c)
		self.g = Node(6,self.c,self.d)
		self.h = Node(7,self.e,self.f)
		self.i = Node(4,self.f,self.g)
		self.j = Node(3,self.h,self.i)
		# self.k = Node(5,None,None)
		# self.l = Node(9,None,None)
		# self.m = Node(6,n,p)
		# self.q = Node()

	def test_create(self):
		"""Test the construction of node instances"""
		self.assertEqual(None,self.a.left_node)
		self.assertEqual(None,self.a.right_node)
		self.assertEqual(8,self.a.value)

		self.assertEqual(2,self.e.value)
		self.assertEqual(self.b, self.e.right_node)

	def test_max_sum(self):
		"""Test the max sum method of a Node"""

		self.assertEqual(8, self.a.max_sum())
		self.assertEqual(10, self.e.max_sum())
		self.assertEqual(13, self.f.max_sum())
		print self.j.max_sum()

if __name__ == '__main__':
	unittest.main()