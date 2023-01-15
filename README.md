# Nesting-Structure-Comparison-exercise
A function/method that returns True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

**should return True**  
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )  
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

**should return False**   
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )  
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

**should return True**    
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

**should return False**  
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
  
The exercise is on [Codewars](https://www.codewars.com/kata/520446778469526ec0000001/train/python) 
