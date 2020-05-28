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

## input
the input keyword with the input text that has to be shown
(input "give me some input:")

## Types and default values in the language
Integers are a default class in the language.
In a core folder there will probably be a class with functions for the integer. But I't will be implemented in the core structure of the language.
This approach is chosen because the the core values in the lanuage would otherwise look like:
(Type Int
    // the check if a value is an integer
    check (Raw: val) : Bool {
        // this function would make a regex check for the value type.
        // the value would be found be going into the right scope like most languages have these days.
        // if the match would return true 
        (return (match val, core.patterns.Int))
    }
)

## classes
the classes that define how the objects will be handled.


(class Scalar
    // initialize an object of this class
    init (Int: x) : void {
        public Int val := x;
    }
)

(class 2dVector
    // the class constructor this function does not return anything
    init (Int: x, Int: y) : void (
        public Int x := x;
        public Int y := y;
    )
)

## window creation
build-in function for making a window in the language.
(window 600, 400, "Window Title")

