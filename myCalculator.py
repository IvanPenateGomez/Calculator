from myMath import math
import random

class equation(math):
    class _NODE:
        def __init__(self,p):
            self.data = ""
            self.left_p = p
            self.right_p = -1

    def __init__ (self , e = None):
        super().__init__()
        self.__free_p = 0
        self.__strEqu = e
        self.__root_p = 0
        self.__parenthesis = {}
        self.__counter = 0
        self.__counter_2 = 1      
        
        if e != None:
            self.__equ = self.__adaptInput(e)
            self.tree = [equation._NODE(x + 1) for x in range(len(self.__equ))]
            self.__initialize()
        else:
            self.create_equation()
    
    def getEqu(self):return self.__strEqu
        
    def __adaptInput(self,equ):
        newEqu = ""
        for x in range(len(equ) - 1):
            char1 = equ[x]
            char2 = equ[x+1]
            char1Type = self.__getType(char1)
            char2Type = self.__getType(char2)
            
            newEqu += char1 
            if (char1Type != char2Type and char1Type != "Space" and char2Type != "Space") or char1Type == char2Type == "brackets":
                newEqu += " "
            
        newEqu += char2
        
        return newEqu
        
    def __getType(self, c):
        if c in "123456890": return "nums"
        elif c in "+-/*^sincosectancotgcdlogln": return "operator"
        elif c in "()": return "brackets"
        else: return "Space"
                    
    def create_equation(self, size = 10 , limit = 1000 , symbols = "+-*/"):
        if any(symbol not in "+-*/^" for symbol in symbols):
            print("Invalid symbols")
            return
                    
        equ = ""
        for x in range(size):
            equ += str(random.randint(1, limit)) + " "
            equ += random.choice(symbols) + " "
        equ += str(random.randint(1,limit))
        self.strEqu = equ
        self.__init__(equ)

    def __initialize(self):
        try:
            self.__equ = self.__get_letters(self.__equ)
            self.__equation_to_tree(self.__equ, self.__free_p)
            self.__convert_ends_null(0)
        except:
            print("Invalid input, try again.")
    
    def __get_parenthesis(self, sub_equNotSplit):
        counter_paren = 0
        found = False
        new_sub_equ  = ""
        sub_equ = sub_equNotSplit
        
        try:
            for x in range(len(sub_equ)):
                val = sub_equ[x].lower()
                match val:
                    case '(':
                        found = True
                        
                        if sub_equ[x] == "(":
                            counter_paren += 1
                            if counter_paren == 1:start = x              
                        
                    case ")": counter_paren -= 1
                    
                    
                
                if counter_paren == 0:
                    if found:
                        found = False
                        new_sub_equ += self.__get_letters(sub_equNotSplit[start + 1: x])
                        
                    else:
                        new_sub_equ += sub_equ[x]
                
            return new_sub_equ
        
        except:
            print(10000)
            return sub_equNotSplit

    def __get_letters(self, sub_equ):     
        if "(" not in sub_equ:
            self.__parenthesis[(letters := (chr(self.__counter + 65) * self.__counter_2))] = sub_equ
            self.__counter += 1

            if self.__counter == 26:
                self.__counter_2 += 1
                self.__counter = 0
            
            return letters

        else:
            sub_equ = self.__get_parenthesis(sub_equ)
            trial = self.__get_letters(sub_equ)
            
            if trial == sub_equ: return sub_equ
            return trial

    def __separate(self, operator, equation):
        for x in range(len(equation)-1,self._NULL,self._NULL):
            if equation[x] == operator:
                return equation[:x] , equation[x+1:]

    def __equation_to_tree (self, sub_equ , free_p):
        sub_equ = sub_equ.strip(" ")
        specialFunc = False
        
        if sub_equ in self.__parenthesis: sub_equ = self.__parenthesis[sub_equ]
        if len(sub_equ.split()) == 1:
            if sub_equ == "e": sub_equ = str(self._E)
            elif sub_equ == "pi": sub_equ = str(self._PI)
            
            self.tree[free_p].data = sub_equ.strip(" ")
            
            return free_p
        
        else:
            if "+" in sub_equ: left , right = self.__separate("+" , sub_equ);operator = "+"
            elif "-" in  sub_equ: left , right = self.__separate("-" , sub_equ);operator = "-"
            elif "*" in  sub_equ: left , right = self.__separate("*" , sub_equ);operator = "*"
            elif "/" in  sub_equ: left , right = self.__separate("/" , sub_equ);operator = "/"   
            elif "^" in  sub_equ: left , right = self.__separate("^" , sub_equ);operator = "^"
            else:
                if sub_equ != '':
                    specialFunc = True
                    operator , left = sub_equ.split()

            self.tree[free_p].data = operator
            previous_p = free_p
            free_p = self.tree[free_p].left_p
            self.tree[previous_p].left_p = free_p
            free_p = self.__equation_to_tree(left, free_p)
            if not specialFunc:
                
                free_p = self.tree[free_p].left_p
                self.tree[previous_p].right_p = free_p
                free_p = self.__equation_to_tree(right, free_p)
            return free_p
    
    def __convert_ends_null(self, this_node):
        if this_node != self._NULL:
            if self.tree[this_node].data[0] not in "+-/*^sincosectancotgcdlnlog":
                self.tree[this_node].left_p = self._NULL
                self.tree[this_node].right_p = self._NULL
            else:
                self.__convert_ends_null(self.tree[this_node].left_p)
                self.__convert_ends_null(self.tree[this_node].right_p)

    def calculate(self, rounding = None):
        try:
            solution, error =  self.__calculator(self.__root_p, error = False)
            return "Math Error, can not divide by 0" if error else self._rounder(solution , rounding) 
        except:
            return "Invalid input, try again."
    def __calculator(self, root_p, error):
        this_node = root_p
        if this_node != self._NULL and not error:
            currentNode = self.tree[this_node]
            if currentNode.data in "+-/*^":
                num_1 , error1= self.__calculator(currentNode.left_p,error)
                num_2 , error2= self.__calculator(currentNode.right_p,error)
                
                match currentNode.data:
                    case "+":value = num_1 + num_2
                    case "-":value = num_1 - num_2
                    case "/":
                        if num_2 == 0: error1 = True
                        else:value = num_1 / num_2
                    case "*": value = num_1 * num_2
                    case "^": value = num_1 ** num_2
                
                error = error or error1 or error2

            elif currentNode.data in "sinloglntancoseccotgcd":
                num , error = self.__calculator(currentNode.left_p , error)
                match currentNode.data:
                    case "sin":value = self._sin(num)
                    case "cos":value = self._cos(num)
                    case "tan":value = self._tan(num)
                    case "cot":value = self._cot(num)
                    case "sec":value = self._sec(num)
                    case "cosec":value = self._cosec(num) 
                    case "log":value = self._log(num)
                    case "ln":value = self._ln(num)                   

            else: return (0, True) if error else (float(currentNode.data) , False)

            return (0,True) if error else (float(value) , False)


    def RPN_printer(self):self.__RPN(self.__root_p);print()
    def __RPN(self, root_p):
        this_node = root_p
        if this_node != self._NULL:
            self.__RPN(self.tree[this_node].left_p)
            self.__RPN(self.tree[this_node].right_p)
            print(self.tree[this_node].data, end = "")
    
    def print(self):self.__in_order(self.__root_p);print()
    def __in_order(self, root_p):
        this_node = root_p
        if this_node != self._NULL:
            self.__in_order(self.tree[this_node].left_p)
            print(self.tree[this_node].data, end = " ")  
            self.__in_order(self.tree[this_node].right_p)
    