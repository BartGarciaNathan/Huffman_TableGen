# Huffman_TableGen
Python library to generate a Huffman Table from a dictionary of Symbols and their Probability/Frequency
#### Required Libraries
+ [pygraphviz](https://pygraphviz.github.io/) - The library is used to generate an PNG file of the binary tree created from arrenging the input symbols for the Huffman Coding. 

#### Usage
Import the library and use the function `GenerateHuffmanCodeTable` . The function accepts a dictionary where the input is in the format `{ 'String.Symbol' : RealNumber }`. A second argument can be used if generating PNG image of the binary tree is desired, the argument must be a string with the filename that will be used to save the image. 

There is an example code named TestHuffman.py, to run it use ` $python TestHuffman.py`

####Example

This is the generated image from the TestHuffman.py code.
![alt text][TestResult]
[TestResult]: https://github.com/BartGarciaNathan/Huffman_TableGen/raw/master/TestTree.png "Test Code Result Image"


By [Bart Garcia Nathan] (bart.garcia.nathan+git@gmail.com)

Nov 2016
