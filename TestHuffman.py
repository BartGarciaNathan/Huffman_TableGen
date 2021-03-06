"""
Huffman table Generator example using frequency of letters and saving the binary tree to a PNG file
Author: Bart Garcia Nathan bart.garcia.nathan@gmail.com
Nov 2016
"""

import Huffman_TableGen as Huff

freq = {
      'a':8.167,  'b':1.492,  'c':2.782 ,  'd':4.253 ,
     'e':12.702 ,  'f':2.228,  'g':2.015 ,  'h':6.094 ,
     'i':6.966 ,  'j':0.153 ,  'k':0.747 ,  'l':4.025 ,
     'm':2.406 ,  'n':6.749 ,  'o':7.507 ,  'p':1.929 , 
     'q':0.095 ,  'r':5.987 ,  's':6.327 ,  't':9.056 , 
     'u':2.758 ,  'v':1.037 ,  'w':2.365 ,  'x':0.150 ,
     'y':1.974 ,  'z':0.074  }

HuffmanTable_dic=Huff.GenerateHuffmanCodeTable(freq,'TestTree.png')
print HuffmanTable_dic
