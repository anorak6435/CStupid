# The Idea of this language is to have a little language that helps with visuals in python. 
(turtle module / pygame) these are the future Ideas for the language

Yes this would not be nessesary. '''But it's fun for me.'''

() are used for commands
{} are used for body's of commands (multiple commands)
and where I feel like it makes the most sense to use it.

In this language I want my names to be able to start with characters from the alphabeth and numbers.
Let's see how long this will last.
# a list of features (will be expanded upon further development)
## these items are ordered. (this order can change in the future)
1. printing text
2. comments
3. if statement
4. classes
5. objects / variables
6. input from the human
7. window creation
8. turtle controls
9. functions


# testcases that make for the syntax of the language
## printing text
print to the screen: (String to the screen)

(echo ~String~)

(echo "Hello world!")
(echo "The language of gods")
(echo "Scripting?")

## comments
// This will become a python comment
// These comments work just like javascript comments
// I do not only know one line comments

//-->
This will be a multi line comment.
So this text is still part of this comment.
<--// // and that is how a double comment is closed.
// check that when a multiline comment is closed
// the compiler goes directly to the next part of the code.
// don't be mislead by those double lines at the end.

//--> It is not a problem to start your multiline comment directly 
after the opening because you are already inside the comment.
<--//

## controlflow
## if
(if (== true, true)
    then {(echo "it's so true")}
    else {(echo "It's over")}
)

(if (> 5, 3)
    then {(echo "five is greather than tree")}
)

(if ~condition~ then ~stmt_body~ else ~stmt_body~)

~condition~ : (~comparison~ ~val1~ ~val2~)
~stmt_body~ : {~stmt~+}

## classes
the classes that define how the objects will be handled.


(class Scalar
    // initialize an object of this class
    func init (Int: x) : void {
        public Int val := x;
    }
)

(class 2dVector
    // the class constructor this function does not return anything
    func init (Int: x, Int: y) : void {
        public Int x := x;
        public Int y := y;
    }
)

## variables
//declare the age variable as an Integer
(var Int Age := 20)
(var String Name := "Anorak6435")

//print the variables I created
(echo (var Age))
(echo (var Name))

## input
the input keyword with the input text that has to be shown
(input "give me some input:")

## window creation
build-in function for making a window in the language.
// (window ~width~, ~height~, ~title~)
(window 600, 400, "Window Title")

## turtle controls
Here we write the commands for the turtle

line:
A line could be between 2 vectors
(line ~vector~, ~vector~)
(line (var 2dVector 10, 10), (var 2dVector 30, 30))
or between two collection of integers
(line [15, 10], [12, 7])
(line ~list~, ~list~)

triangle:
(triangle ~vector~, ~vector~, ~vector~)
//create the variables that are the vector variables
(triangle (var 2dVector 10, 10), (var 2dVector 30, 30), (var 2dVector 0, 30))
(triangle ~variable~, ~variable~, ~variable~)
(triangle (var p1), (var p2), (var P3))

## functions
(func ~name~ ~stmt_body~)

in the stmt_body there can be all kinds of statements. (But not class statements)