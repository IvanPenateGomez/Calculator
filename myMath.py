class math:
    def __init__(self):
        self._NULL = -1 
        self._PI = 3.14159265358979323846264338327950288419716939937510
        self._E = 2.71828182845904523536028747135266249775724709369995
    
    def _binary_search_logarithm(self, number, base, epsilon=0.0000000001):
        # Initialize the boundaries
        low = 0
        high = number

        # Perform binary search
        while high - low > epsilon:
            mid = (low + high) / 2
            if base ** mid < number:
                low = mid
            else:
                high = mid

        return low

    def _log_a_b(self, base, number):return self._rounder(self._binary_search_logarithm(base,number))
    def _log(self, number, round=None):return self._rounder(self._binary_search_logarithm(number,10), round)
    def _ln(self, number):return self._rounder(self._binary_search_logarithm(number, self._E))

    def _euclidean(a,b):
        if a > b: a,b = b,a
        while b != 0:
            r = a % b
            a = b
            b = r
            
        return a
    
    def _factorial(self, num):
        if num == 1 or num == 0: return 1
        return num * self._factorial(num-1)  
    
    def _sin(self, num , form = "deg" , round = 3):
        if form.lower() == "deg" : num = ( num * self._PI) / 180
            
        total = 0
        positive = True
        
        for x in range(1 , 10 , 2):
            
            if positive:
                
                total += (num ** x) / self._factorial(x)
                positive = False
                
            else:
                
                total -= (num ** x) / self._factorial(x)
                positive = True
        
        return self._rounder(total, round)
    def _cos(self, num, form = "deg" , round = 3):
        if form == "deg" : num = ( num * self._PI ) / 180
            
        total = 0
        positive = True
        
        for x in range(0 , 100 , 2):
            
            if positive:
                
                total += (num ** x) / self._factorial(x)
                positive = False
                
            else:
                
                total -= (num ** x) / self._factorial(x)
                positive = True

        return self._rounder(total, round)

    def _tan(self,num, type = "deg"):return self._rounder(self._sin(num, type , 15) / self._cos(num, type, 15) , 3)
    def _sec(self, num, type = "deg"):return self._rounder(1 / self._cos(num, type,15))
    def _cosec(self, num, type = "deg"):return self._rounder(1 / self._sin(num, type,15))
    def _cot(self, num, type = "deg"):return self._rounder(self._cos(num, type,15) / self._sin(num, type,15))
    
    def _rounder(self, solution , rounding = None):
        solution = str(solution)
        newSolution = ""
        
        if rounding:
            counter = -1
            for c in solution:
                counter += 1
                
                if c == '.' : newSolution += '.'
                else:
                    newSolution += c
                
                if counter > rounding: break
            
            if newSolution[-1] < "5":
                newSolution = newSolution[:-1]
            else:
                placed = False
                while not placed:
                    if newSolution[-2] != '9':
                        placed = True
                        newSolution = newSolution[:-2] + str(int(newSolution[-2]) + 1) 
                    else:
                        newSolution = newSolution[:-1]
                
            
            for y in range(len(newSolution) -1, self._NULL + 1, self._NULL):
                if newSolution[-1] == "0" and "." in newSolution:newSolution = newSolution[:-1]
                elif newSolution[-1] == ".":
                    newSolution = newSolution[:-1]
                    break
                
            return float(newSolution)                    
            
        else: return float(solution)