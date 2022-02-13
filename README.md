<h1>Sudoku Solver</h1>
This sudoku solver is solved through a backtracking algorithm, which is a brute force 
approach or algorithm. 
Here are the steps the program goes when solving a puzzle:
<ol>
<li>Pick an empty square</li>
<li>Try any available number by checking square numbers, row numbers, and column numbers</li>
<li>Go to the next empty square</li>
<li>Try another available number by checking square numbers, row numbers, and column numbers</li>
<li>If we run into a puzzle contradiction, or where we cannot place a valid value in the puzzle then
we backtrack to the last inserted number</li>
<li>Try a different number that was different from last time or iteration</li>
</ol>
To run the sudoku solver program, you will need a text file that would hold the puzzle.
A sudoku puzzle is a 9x9 puzzle. Empty cells are indicated as '0'. Here is an example below:
<pre><code>300060720
060300500
020190000
500900108
600800903
180070602
040005031
210700095
803009467</code></pre>
The program will check for any errors in your sudoku puzzle. 
To properly run this text file under this program, run this command: 
<pre><code>python sudokusolver.py *.txt</code></pre>
The * can represent the name or to the path to the text file of your sudoku puzzle. 