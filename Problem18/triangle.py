#! /bin/env python

ct = 0
class Node:
	def __init__(self,value, left_node,right_node):
		self.left_node = left_node
		self.right_node = right_node
		self.value = value
		self.known_max = False
		self.max = value

	def max_sum(self):
		global ct
		ct += 1
		if self.known_max:
			return self.max
		if self.left_node and self.right_node:
			self.max =  max(self.left_node.max_sum(), self.right_node.max_sum()) + self.value
			self.known_max = True
		return self.max

def load_file(filename):
	f = open(filename, 'r')
	lines = f.readlines()
	head = []
	counter = -1
	for i in range(len(lines)-1,-1,-1):
		tail = []
		line = lines[i][:-1].split()
		if i == len(lines)-1:
			for j in range(0,len(line)):
				tail.append(Node(int(line[j]),None,None))
		else:
			for j in range(0,len(line)):
				tail.append(Node(int(line[j]),head[counter][j],head[counter][j+1]))
		head.append(tail)
		counter += 1
	return head[-1][0]

def main():
	# head = load_file('data.in')
	head = load_file('p067_triangle.txt')

	print head.max_sum()
	print "CT",ct

if __name__ == '__main__':
 	main() 