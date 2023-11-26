from myCalculator import equation 
import time

def main():
    while True:
        print("\n\n\nCalculator, commands:\n\n    HELP : for syntax of equations\n    ALL : will return all the operators the calculator has\n    STOP: exit program\n    directly write an equation.")
        option = input("\n      = ")
        print()
        
        match option.upper():
            
            case "HELP":
                print("\n\nEquations should be written in any way you want: 2+3 - 7, 4 ^ 6")
                time.sleep(0.5)
                print("Requires all operators have their exact amount of tokens, e.g. 3 + 5, not 6 +")
                time.sleep(0.5)
                print("\nEquations can be as long as you want and with any numbers python can support e.g.")
                
                time.sleep(0.5)
                equ = equation("4 ^ (sin 5 - 6 / 10) + 10 ^ 0.5 - 4 * ln 9")
                print("\n    " , equ.getEqu() , " = " , equ.calculate())
                
                time.sleep(1)
                
            
            case "ALL":
                print("The calculator has many functions, more than eval:")
                time.sleep(0.5)
                print("     + , - , * , / , ^ : syntax -> a operator b -> (a) operator (b)")
                time.sleep(0.5)
                print("     sin , cos , tan , cot , cosec , sec , ln , log (base 10) : syntax -> operator a || operator (a + b ..)")
                time.sleep(1)
                print("\nIf you do not want to write a  equation, equation.create_equation() can be used with parameters:")
                time.sleep(0.5)
                print("     size = the amount of numbers the equation will have.")
                time.sleep(0.5)
                print("     limit = the range of the numbers, e.g. limit = 100 -> numbers can be from 0,100")
                time.sleep(0.5)
                print("     symbols = the operators you want to use in the equation, for practicing purposes")
                time.sleep(1)
                
                print("\n       All the parameters have default values used for testing the calculator with eval, some symbols in ")
                print("     this calculator are not supported by eval such as ^ and the trig and log functions.")
        
            case "STOP":
                return
            
            case _:
                equ = equation(option)
                print("\nResult is: " , equ.calculate())
                time.sleep(0.3)
                

if "__main__" == __name__:
    main()
    print("Calculator by Iván Peñate Gómez")