## Program Running Instructions:
The program must strictly follow the format given in the homework assignment. No modification will be accepted. Any modification will result in the failure of running the program properly. 
1. For Template 1: 
	Every none-number word must be all capital. The gene type strictly follows the format "G1_UP", etc.
	The last argument (the combination) must be in a set. For example, running the template 1 should look like:

	`template1("RULE", "ANY", {'G59_UP'}, 0.7, 0.5, True, transactions)`

The True here means to print out the result. The transations is just for passing values. They are required for template 1. 

2. For Template 2:
	Similar instruction as Template 1.
	Example:
	`template2("rule", 3, 0.7, 0.5, True, transactions)`

Similar explanation as Template 1. Please follow the format. 

3. For Template 3:
	The first argument must be a number followed by an LOWERCASE choice of (and/or). No exception will be made.
	The rest of the arguments follow the instructions of Template 1 and 2. 
	Example:
	`template3(transactions,0.7, 0.5, "1or1", "HEAD", "ANY", {"G10_DOWN"}, "BODY", 1, {"G59_UP"})`

Running the program will be type:
python main.py
In command line.
We have included the required examples for the homework under the *main.py*. You will be able to find the source codes of running those functions at the bottom of *main.py*.

Due to the time restriction on this assignment, please modify the input in the source file. Doing anything in the command line will not help. We have put the sample running instructions at the end of the *main.py*.

Please modify the source code for any test/grading purpose. 
