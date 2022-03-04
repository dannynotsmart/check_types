check_types
===========

simple decorator that ensures the arguments you pass into a function is the correct type, specified by typehints

y did i make dis
----------------
i enjoy how in java, arguments in methods have a specified type that you must pass in. 

for example


.. code:: java

    public static void killBalls(String name) {
    	System.out.println("i have executed the balls of" + name)
    }
    //im pretty sure this right

however, in python you really cant enforce types of argument. you'd have to manually check, which can get messy and/or annoying

this is just a simple decorator that handles all that checking for you

U STUPID
--------
i sory

ok but how 2 use
----------------
1. copy the contents of the `file <https://github.com/dannynotsmart/check_types/blob/main/check_types.py>`_ (this has the actual decorator)
2. make sure to put this in an ACCESSIBLE place. you can put in a new file and import the decorator from the file, or just put it in the same file
3. use decorator


.. code:: python
    @check_types
    def shoot_balls(who : str, *, why : str, how : str = "gun"):
        print(f"i have shot {who} because {why}. i shot ball by {how}")
        
    shoot_balls("cat", why = "i don't like")
    
`so ya <https://github.com/dannynotsmart/check_types/blob/main/example.py>`_
4. ya

ok but wat hapens
-----------------
- when you incorrectly pass in an argument that does not match the typehint, big scary error hapens (it is TypeError)
- if your argument has no typehint then it ignore

WAIT!!!!!!!
-----------
this does not support typing typehints from the typing library bedause the typing lib dumb

hav fun
-------
birls
