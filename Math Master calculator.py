#Math Master Calculator
import math, shelve

def shelvewrite(textfilename,towrite): #write to text file
    textfilenametxt = textfilename + '.txt'
    writer = shelve.open(str(textfilenametxt))
    writer[str(textfilename)] = towrite
    writer.close()

def shelveread(textfilename): # read from text file
    textfilenametxt = textfilename + '.txt'
    reader = shelve.open(str(textfilenametxt))
    text = reader[str(textfilename)]
    reader.close()
    return text

def clearscreen(): 
    print('\n' * 50)

def num_extractor(toread,numtoscan):
    if True:
        fish = toread
        num = 0
        reader = 'start'
        first, second, third, fourth = '','','',''
        try:
            while True:
                reader = fish[num]
                while reader != ' ':
                    first = first + reader
                    num += 1
                    reader = fish[num]
                num += 1
                if first != '':
                    break
        except:
            print('')
        try:
            while True:
                reader = fish[num]
                while reader != ' ':
                    second = second + reader
                    num += 1
                    reader = fish[num]
                num += 1
                if second != '':
                    break
        except:
            print('')
        if numtoscan == 3:
            try:
                while True:
                    reader = fish[num]
                    while reader != ' ':
                        third = third + reader
                        num += 1
                        reader = fish[num]
                    num += 1
                    if third != '':
                        break
            except:
                third = third.replace(' ','')
                third = int(third)
        if numtoscan == 4:
            try:
                while True:
                    reader = fish[num]
                    while reader != ' ':
                        fourth = fourth + reader
                        num += 1
                        reader = fish[num]
                    num += 1
                    if fourth != '':
                        break
            except:
                fourth = fourth.replace(' ','')
                fourth = int(fourth)
    first, second = first.replace(' ',''), second.replace(' ','')
    first, second = int(first), int(second)
    if numtoscan <= 2:
        return  first, second
    elif numtoscan <= 3:
        return  first, second, third
    else:
        return  first, second, third, fourth

def logs():
    global command, memory
    first, second = num_extractor(command,2)
    logged = math.log(second,first)        
    print('log ',first,second,'  = ',logged)
    memory = memory + '\n' + 'log' + str(first) + str(second) + ' =' + str(logged)
    shelvewrite('mastermathmemory',memory)

def quadratic_formula():
    global command
    val1, val2, val3 = 0, 0, 0
    a, b, c = num_extractor(command,3)
    a, b, c = str(a), str(b), str(c)
    w = (str(a) + str(b) + str(c))
    w = w.lower()
    if True:
        a, b, c = (float(a) if '.' in a else int(a)), (float(b) if '.' in b else int(b)), (float(c) if '.' in c else int(c))
        a, val1, val2, val3 = (99999 if a == 0 else a), (-1 * b), (-1 * b), ((b*b)-4*a*c)
        bsign, csign, astring, bstring, cstring, msquared, m = ('+ ' if b >= 0 else ' '), ('+ ' if c >= 0 else ' '), str(a), str(b), str(c), 'x² ', 'x '
        astring, bstring, astring, msquared, bstring, bsign, m, cstring, csign = ('' if astring == '1' else astring), ('' if bstring == '1' else bstring), ('' if astring == '0' else astring), ('' if astring == '0' else msquared), ('' if bstring == '0' else bstring), ('' if bstring == '0' else bsign), ('' if bstring == '0' else m), ('' if cstring == '0' else cstring), ('' if cstring == '0' else csign)
        equation = astring + msquared + bsign + bstring + m + csign + cstring
        print('You entered: a =',a,'  b =',b,'  c =',c)
        print('\nThe equation detected is' , equation)
        print('\nThe solution(s) are')
        if val3 < 0:
            val3 = val3 * -1
            print ('         ____\n' , val1,' ±i √', val3 , '\n-------------------\n' ,'     ',       2*a )
            sqrtval, val1, = math.sqrt(val3), val1/(2*a)
            sqrtval = sqrtval/(2*a)
            print('\nFurthur simplified to:\n')
            roundval1 = round(val1,5)
            roundsqrtval = round(sqrtval,5)
            if val1 == 0:
                print('+',roundsqrtval,'i   ,     -',roundsqrtval,'i')
                memory = memory + '\n' + 'You entered: a =' + str(a)+'  b =' +str(b)+'  c =' + str(c) + '\nThe equation detected is' + str(equation) + '\nThe solution(s) are\n' + '+'+str(roundsqrtval)+'i   ,     -'+str(roundsqrtval)+'i'
                shelvewrite('mastermathmemory',memory)
            else:
                print(roundval1 , '+',roundsqrtval, 'i  ,  ', roundval1 , '-',roundsqrtval, 'i ')
                memory = memory + '\n' + 'You entered: a =' + str(a)+'  b =' +str(b)+'  c =' + str(c) + '\nThe equation detected is' + str(equation) + '\nThe solution(s) are\n' + str(roundval1) + '+'+str(roundsqrtval)+ 'i  ,  '+ str(roundval1) + '-'+str(roundsqrtval)+ 'i '
                shelvewrite('mastermathmemory',memory)
        else:
            val1 = val1 + math.sqrt(val3)
            val2 = val2 - math.sqrt(val3)
            val1 = (val1 / (2*a))
            val2 = (val2 / (2*a))
            toprint = val1 if val1 == val2 else val1, val2
            print(toprint)
            memory = memory + '\n' + 'You entered: a =' + str(a)+'  b =' +str(b)+'  c =' + str(c) + '\nThe equation detected is' + str(equation) + '\nThe solution(s) are' + str(toprint)
            shelvewrite('mastermathmemory',memory)

def factorfinder(number):
    number = int(number)
    factortry = 1
    factors = list(str(1))
    while factortry <= number:
        if number % factortry == 0:
            if factortry > 1:
                factors.append(str(factortry))
            else:
                factors = list(str(factortry))
        factortry += 1
    return (factors)

# initialize memory:
try:
    memory = shelveread('mastermathmemory')
except:
    shelvewrite('mastermathmemory','')

while True:
    try:
        print('\n')
        print('This is a command line interface')
        print('You can run the following commands')
        print('logs...........................log 2 8  for log₂8')
        #print('Synthetic divsion..............syn 1 -3 24 -31 /2 for (x³-x²+x-31)/(x-2)')
        print('Quadratic formula..............qua 1 11 30 for x²+11x+30')
        #print('Polynomial factorizer..........pol 1 -3 24 -31 for x³-x²+x-31')
        print('Number factorizer..............fac 24 for factorizing 24')
        print('Trig ratios....................sec 23 for secant 23 degrees')
        print('Convert deg to rad.............rad 23 to convert 23 degrees to radians')
        #print('Add list.......................add list of numbers ')
        #print('Average of list................ave list of numbers ')
        #print('Max value of list..............max list of numbers ')
        #print('Min value of list..............min list of numbers ')
        #print('Define a list..................def list of numbers ')
        #print('Most recent answer.............ans')
        #print('To implement a list............(def) ex. max(def)')
        print('Mathematical calculation.......use regular math symbols ex. 34+52 56/4 7*7 2^5')
        print('Square root....................sqt 9 for square root 9')
        print('factorial......................fct')
        print('Show memory....................mem')
        print('Clear screen...................clr')
        print('Help center....................hlp')
        command = input('Enter command > ')

        try:
            if '+' not in command and '-' not in command and '/' not in command and'*' not in command and '^' not in command:
                line = command[0] + command[1] + command[2] + command[3]
                command = command[4:]
            else:
                line = 'math operation'
        except:
            line = 'clr ' if 'clr' in command else 'hlp '

        if line == 'log ':
            logs()

        if line == 'qua ':
            quadratic_formula()

        if line == 'fac ':
            facs = factorfinder(command)
            print('The factors of the number are: ', facs)
            memory = memory + '\n' + 'Factors of '+ str(command) + ' are ' + str(facs)
            shelvewrite('mastermathmemory',memory)

        if line == 'fct ':
            command = command.replace(' ','')
            command = int(command)
            print(math.factorial(command))
            command = str(command)
            memory = memory + '\n' + str(command) + ' factorial is ' + str(math.factorial(command))
            shelvewrite('mastermathmemory',memory)
            
        if '+' in command:
            store = command.replace('+',' ')
            add1, add2 = num_extractor(store,2)
            toprint = command+' = '+ (add1+add2)
            memory = memory + '\n' + toprint
            shelvewrite('mastermathmemory',memory)

        if '-' in command:
            store = command.replace('-',' ')
            add1, add2 = num_extractor(store,2)
            print(command,' = ', add1-add2)

        if '/' in command:
            store = command.replace('/',' ')
            add1, add2 = num_extractor(store,2)
            print(command,' = ', add1/add2)

        if '*' in command:
            store = command.replace('*',' ')
            add1, add2 = num_extractor(store,2)
            print(command,' = ', add1*add2)

        if '^' in command:
            store = command.replace('^',' ')
            add1, add2 = num_extractor(store,2)
            print(command,' = ', add1**add2)

        if line == 'sqt ':
            command = int(command)
            print(math.sqrt(command))

        if line == 'sin ':
            command = int(command)
            print(math.sin(math.radians(command)))

        if line == 'cos ':
            command = int(command)
            print(math.cos(math.radians(command)))

        if line == 'tan ':
            command = int(command)
            print(math.tan(math.radians(command)))

        if line == 'csc ':
            command = int(command)
            print(1/(math.sin(math.radians(command))))

        if line == 'sec ':
            command = int(command)
            print(1/(math.cos(math.radians(command))))
            
        if line == 'cot ':
            command = int(command)
            print(1/(math.tan(math.radians(command))))

        if line == 'rad ':
            command = int(command)
            print(math.radians(command))

        if line == 'clr ':
            print('\n'*50)

        if line == 'hlp ':
            print('\n'*50)
            print('Welcome to the help center')
            print('How to use this calculator:')
            print('  * This calculator has several built in functions')
            print('       - logarithms')
            print('       - quadratic formula')
            print('       - integer factorization')
            print('       - addition')
            print('       - subtraction')
            print('       - multiplication')
            print('       - division')
            print('       - exponents')
            print('       - square roots')
            print('       - factorials')
            print('  * follow the directions on the home page to activate a function')
    
    except Exception as e:
        print(e)
        print('sorry, an error occured')
