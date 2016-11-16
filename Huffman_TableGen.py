"""
Generate Huffman Table Code from a dictionary of Symbols and Frequencies/Probabilities
Author: Bart Garcia Nathan bart.garcia.nathan@gmail.com
November 2016

This code is released under MIT License, so if you use it please consider sending me a Thank you mail.

"""

import pygraphviz as PG


class HuffmanNode(object):
	def __init__(self,freq,left=None, right=None, element=None):
		self.freq=freq
		if left == None:
			self.left = self
		else:
			self.left = left
		if right == None:
			self.right = self
		else:
			self.right = right
		if left == None and right == None:
			if element == None:
				self.element = ""
			else:
				self.element = element
		else:
			self.element = left.element + right.element
		self.parent = self
		self.left.parent = self
		self.right.parent = self
	def get_left(self):
		return(self.left)
	def get_right(self):
		return(self.right)
	def get_freq(self):
		return(self.freq)

#Code to use implement some Huffman Compression utilities

#Generate the Huffman Code Table from a Symbols list. The input must be a dictionary of ('symbol',freq) The code table
#Is a dictionary for ease of use, where the index is the original Symbols input and the stored value is the equivalent
# HuffmanCode Printed as characters
def GenerateHuffmanCodeTable(inputSymbols=None,printname=None):
	#Check the input data is correct
	if inputSymbols==None or not(isinstance(inputSymbols, dict)):
		print "An input dictionary of symbols and frequencies is needed."
		print " Example :"
		print "\t\t  GenerateHuffmanCodeTable({'a':14,'b':5,'c':15})"
		print "For Printing the Binary Tree to an image:"
		print "\t\t  GenerateHuffmanCodeTable({'a':14,'b':5,'c':15},'BinaryTree.png')"
		return None
	#Initialize graph if needed
	if printname!=None:
		graph = PG.AGraph(directed=True,strict=True)
	#Generate Nodes for the leafs of the binary tree
	workinglist=[]
	for symbol in inputSymbols:
		workinglist.append(HuffmanNode(inputSymbols[symbol],element=symbol))
	#Generate the binary tree based on the leaf Nodes
	while(len(workinglist)>1):
		#Sort the workinglist nodes by frequencies, starting by the  highest frequency
		workinglist.sort(key=HuffmanNode.get_freq,reverse=True)
		#Generate new node
		workinglist.append(HuffmanNode(workinglist[-1].freq+workinglist[-2].freq,workinglist[-1],workinglist[-2]))
		#Remove leafs from the root node
		workinglist.remove(workinglist[-1].left)
		workinglist.remove(workinglist[-1].right)
	#Process the tree downwards and add the code for each node 
	HuffmanCodeTable = {}
	code = ""
	known_nodes=[]
	root = workinglist[0]
	current_node = root
	while(len(HuffmanCodeTable) < len(inputSymbols)):
		#Append current node to the known nodes list
		known_nodes.append(current_node)
		#If current node has a left child and the child has not been visited, go to it
		if(current_node.left!=current_node and not(current_node.left in known_nodes)):
			code =code+'0'
			current_node=current_node.left
			if printname!=None:
				graph.add_edge(current_node.parent.element,current_node.element)
		else:
		#If current node has a right child and the child has not been visited, go to it
			if (current_node.right!= current_node and not (current_node.right in known_nodes)):
				code=code+'1'
				current_node=current_node.right
				if printname!=None:
					graph.add_edge(current_node.parent.element,current_node.element)
		#If both childs have been visited or there is no child, go to parent
			else:
				current_node=current_node.parent
				code = code[0:-1] 
		#Check if node is a leaf, in which case assign symbol and code to output dictionary
		if (current_node.left==current_node and current_node.right==current_node):
			HuffmanCodeTable[current_node.element]=code
	if printname!=None:
		graph.layout(prog='dot')
		graph.draw(printname)
	return HuffmanCodeTable
