Course deliverable that emphasizes the importance of software engineering practices. Both .py files successfully run a simple calculator, that contains two argument functions for addition, subtraction, multiplication, and division.

The violated coding practices that can be found within poorDocumentation.py are:
1. Document your code
    - The comments are unclear and repetitive, they only restate what is already clear from the code
3. Clean code
    - The code is not spaced out, and the functions do not follow proper naming protocols. Redundant elif statement at the end of the code, the only statement needed is 
      if(flag.lower() == "n").
5. DRY code
    - Ask for user input four times throughout the if statement instead of just once before. Functions calculate and store the desired result as a variable and then converts 
      to string within print function, instead of performing the calculation within the print function. 
