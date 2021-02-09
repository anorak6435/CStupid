# CStupid
A language for making visuals on the HTML canvas and python (pygame / turtle) module

starting with general features for programming languages

## features for the language
1. comments
2. variables
3. functions
4. classes
5. conditions
6. loops
7. output
8. input

## comments
// one line comment

//--> this is a multiline comment
all this text will be in here
<--//

## variables
var Age : Int = 20;
var Name : String = "Anorak6435";

## functions
// function definition
func getAge() : Int {
    return Age;
}

// function call
getAge();

## classes
class Scalar {
    // create an attribute with it's accessability
    public val : Int;

    //initialize an object of this class (constructor)
    public func init (x : Int) : void {
        this.val = x;
    }
}

class Vector2d {
    public x : Int;
    public y : Int;
    
    // constructor for 2d vector
    public func init(_x : Int, _y : Int) : void {
        this.x = _x;
        this.y = _y;
    }
}

## conditions
if (true == true) then {
    echo("it's totally true");
} else {
    echo("it will never be false");
}

if (5 < 3) then {
    echo("True feels sad");
} else {
    echo("False may talk now");
}

## loops

// a loop for the language
times 7 {
    //this code get's executed 7 times
    echo("print this 7 times!");
}

var index : Int = 1; //
var people : Int = 10; // the number of people
while (index < people) {
    echo("Hello person: %index%");
    index = index + 1;
}

## output
echo("hello world!");
echo("something to print!");
var name : String = "Anorakfour";
echo(name);

## input
// the input function seems for now that it will be part of an console edition of the
// language
// a simple program that askes the user for input their age in this case.
echo("how old are you?");
var age : String = input();