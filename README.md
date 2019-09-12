# Data Mining Apriori
Python Apriori Implementation for mining frequent itemsets and assiciations. 

##Program Running Instructions:
The program must strictly follow the format given in the homework assignment. No modification will be accepted. Any modification will result in the failure of running the program properly. 
1. For Template 1: 
	Every none-number word must be all capital. The gene type strictly follows the format "G1_UP", etc.
	The last argument (the combination) must be in a set. For example, running the template 1 should look like:

`template1("RULE", "NONE", {"G96_DOWN", "G59_UP"}`

2. For Template 2:
	Similar instruction as Template 1.
	Example:
`template2("RULE", 3)`

3. For Template 3:
	The first argument must be a number followed by an LOWERCASE choice of (and/or). No exception will be made.
	The rest of the arguments follow the instructions of Template 1 and 2. 
	Example:
`template3("1and1", "HEAD", "ANY", "G38_DOWN", "BODY", "NONE", "G87_UP")`

Running the program will be type:
python main.py
In command line.

Due to the time restriction on this assignment, please modify the input in the source file. Doing anything in the command line will not help. We have put the sample running instructions at the end of the *main.py*.

Please modify the source code for any test/grading purpose. 
