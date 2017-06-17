## INTRODUCTION ##
This document provides a brief description of the project, assumptions, implementation details and architecture, as well as detailed instructions on how to run the program.

The programming language used was Python version 2.7.10.

## ASSUMPTIONS ##
The assumptions explained below have guided the implementation of the algorithm.

- The input must be passed through the standard input and formatted correctly (as indicated in the specification example).
	- The accepted format is based on the *regex* `[a-zA-Z]{2}\d+((,){1}( )*[a-zA-Z]{2}\d+)*`. Each vertex is represented by a letter of the alphabet and the distance is an integer. Example: AB7 means an edge with origin in vertex A and destination in vertex B with weight equal to 7.
- The output of the algorithm is based on the tests passed in the specification. So, if the input is equals to the specification's input, the result will be the same of the specification's output.
	- The `src/main/main.py` file contains the test results. If you want to run tests for other edge sets, you need to change it.
	- Each type of test problem is connected to a corresponding function that solves it.
	- As there is a correspondence between the types of tests and the functions implemented, an user interface could have been implemented through the command line where the user chooses which type of problem (based on the tests) she/he would like to solve. However, for the sake of simplicity of the solution, this functionality has not been implemented.
	- Some basic error treatments have been implemented.
	- The system considers that the input is in a valid format.
- It is considered that the value of an edge is always a positive integer greater than zero.


## ARCHITECTURE ##
The system has modules and sub-modules grouped together:

- *src*: Responsible for the application code.
	- *main*: Contains code related to the graph and interaction with the user.
	- *util*: Contains utilitarian classes.
- *tests*: Contains the code responsible for the tests of the application.

## DESIGN ##
Following the structure of the Architecture section, the system has the following classes:

- *src*
	- *main*
	- *Edge*: class that represents an edge of the graph.
	- *Graph*: class representing the graph. It has a list of vertices and each vertex has a list of adjacent vertices.
	- *util*
		- *InputUtil*: class responsible for reading from the standard input and returning the read data.
		- *ParserUtil*: class responsible for parsing a string and returning a list of edges.
		- *PrintUtil*: class responsible for printing formatted data to standard output.
- *tests*
	- *EdgeTest*: class responsible for doing tests related to the *Edge* class.
	- *GraphTest*: class responsible for doing tests related to the *Graph* class.
	- *ParserUtilTest*: class responsible for doing tests related to class *ParserUtil*.
	- *PrintUtilTest*: class responsible for doing tests related to the *PrintUtil* class.

## IMPLEMENTATION DETAILS ##
The main implementation details are explained below:

- The vertice lists used in the graph use a high performance Python datatype structure *defaultdict(list)*. This structure eases the implementation and allows direct access to the vertices and their edges.
- The implementations to find a direct distance between vertices and find all paths between vertices are implemented recursively.
- The implementation to get the shortest distance between two vertices use the Dijkstra algorithm. Note: this algorithm only works for positive edges.

## RUNNING THE CODE ##
To run the main code, from the *root directory*, run the command bellow:

    python -m src.main.main

To run the tests, from the *root directory*, run the command bellow:

    python -m unittest discover -s tests -p "*_test.py"

## TESTS ##
The unit tests developed were designed to ensure a correct solution, as well as aiding the development (eg, doing a refactoring and also ensuring that the code is still correct).

In addition to the tests performed in the graph obtained from the specification, a new graph was created (with special cases that were not occurring in the initial graph) to test the algorithm and guarantee the correctness of the solution.