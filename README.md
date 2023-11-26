# Calculator
Imitates the eval function of Python but with more features such as evaluating trigonometric and logarithmic functions inside a big equation.


This calculator uses a binary tree to store an equation, where the leaves are the numbers, and in the nodes, we have the operators in order by using BODMAS. 

First, the program checks the equation and makes a dictionary storing all the brackets used in the equation and for each bracket, a key is given, and this key substitutes the bracket
e.g. 3 + ( 5 - 6) -> 3 + A
Where A is a letter given by a function that gets unique identifiers for each bracket in the  equation. For bigger equations, this would be in this way:
e.g. 3 + ((2 * 5) - 5) * (100 ^0.5)
a = 3 + (A - 5) * (100 ^0.5)
b = 3 + B * 100 ^0.5
c = 3 + B * C

and the dictionary would be:
  parenthesis = { 
      A : 2 * 5,
      B : A - 5,
      C : 100 ^ 0.5
      }

Now that this is done, the full equation is stored in the tree, where near the root, the operators of + and - would be stored, then *,  /, and finally ^, trig functions and logarithmic functions.

Finally, the tree is read in preorder traversal and the value of the equation is calculated.

To get the values of the functions, the parent class of the calculator is myMath. The functions to get sin, cos, and log are implemented to get the values for a good enough precision. More functions are implemented and I will slowly modify the calculator so all functions can be used from the calculator directly.
