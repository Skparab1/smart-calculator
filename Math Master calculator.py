#Math Master Calculator
import math
print('This is a command line interface')
print('You can run the following commands')
print('logs...........................log 2 8  for log₂8')
print('Synthetic divsion..............syn 1 -3 24 -31 /2 for (x³-x²+x-31)/(x-2)')
print('Quadratic formula..............qua 1 11 30 for x²+11x+30')
print('Polynomial factorizer..........pol 1 -3 24 -31 for x³-x²+x-31')
print('Number factorizer..............num 24 for factorizing 24')
print('Add list.......................add [list of numbers] ')
print('Average of list................ave [list of numbers] ')
print('Max value of list..............max [list of numbers] ')
print('Min value of list..............min [list of numbers] ')
print('Define a list..................def [list of numbers] ')
print('Most recent answer.............ans')
print('To implement a list............(def) ex. max(def)')
print('Mathematical calculation.......use regular math symbols ex. 34+52 56/4 7*7 2^5')
print('Clear screen...................clr')
print('Help center....................hlp')
command = input('Enter command > ')
command = command + (' ' * 5)
line = command[0] + command[1] + command[2] + command[3]
if line in command:
    command = command.replace(line,' ')
#log
if line == 'log ':
    fish = command
    num = 0
    reader = 'start'
    first = ''
    second = ''
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
    first, second = int(first), int(second)
    logged = math.log(second,first)
    print('log ',first,second,'  = ',logged)
#Synthetic dev
