import operator
import re
from math import floor

OPS = {'+': operator.add,
       '*': operator.mul,}

COMMON_NR = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29

class Monkey:
    def __init__(self, items: list = None, operation = None, test_str = None, if_true = None, if_false = None) -> None:
        self.items = items
        self.operation = operation
        self.test_str = test_str
        self.if_true = if_true
        self.if_false = if_false
        self.nr_inspected_items = 0

    def __repr__(self):
        return str(self.items)

    def __str__(self):
        return str(self.items)
    
    def __calc_new_worry(self, item, worry_divider:int, divide: bool = True):
        operations = self.operation.split(' ')
        if operations[-1] == 'old':
            operations[-1] = item
        if divide:
            return floor(OPS[operations[-2]](int(item),int(operations[-1]))/worry_divider)
        else:
            return floor(OPS[operations[-2]](int(item),int(operations[-1]))%worry_divider)

    def __test(self, item):
        if item % int(self.test_str) == 0:
            return True
        return False

    def inspect_item(self, item, worry_divider, divide):
        self.nr_inspected_items += 1
        new_worry = self.__calc_new_worry(item, worry_divider, divide)
        divisable = self.__test(new_worry)
        if divisable:
            return (new_worry, self.if_true)
        return (new_worry, self.if_false)
    
    def inspect_all_items(self, worry_divider, divide):
        lst = []
        for item in self.items:
            lst.append(self.inspect_item(item, worry_divider, divide))
        self.items = []
        return lst

def parser(path:str) -> list:
    with open(path) as file:
        monkey_list = []
        monkey = Monkey()
  
        for line in file:
            line = line.rstrip('\n')
            if 'Monkey' in line:
                monkey = Monkey()
            elif 'Starting items' in line:
                monkey.items = re.findall('\d+', line)
            elif 'Operation' in line:
                monkey.operation = line
            elif 'Test' in line:
                monkey.test_str = re.search('\d+',line).group(0)
            elif 'If true' in line:
                monkey.if_true = re.search('\d+',line).group(0)
            elif 'If false' in line:
                monkey.if_false = re.search('\d+',line).group(0)
            else:
                monkey_list.append(monkey)
        monkey_list.append(monkey)
     
    return monkey_list


def move_items(monkey_instructions:list, monkey_list:list):
    for instruction in monkey_instructions:
        monkey_list[int(instruction[1])].items.append(instruction[0])
    return monkey_list

def round(monkey_list:list, worry_divider, divide):
    monkey_instructions = []
    for monkey in monkey_list:
        monkey_instructions = monkey.inspect_all_items(worry_divider, divide)
        monkey_list = move_items(monkey_instructions, monkey_list)
    return monkey_list

def calc_monkey_business(monkey_list:list):
    inspected_list = []
    for monkey in monkey_list:
        inspected_list.append(monkey.nr_inspected_items)
    print(inspected_list)
    inspected_list.sort()

    return (inspected_list[-1]* inspected_list[-2])

def test(path:str):
    monkey_list= parser(path=path)
    for i in range (0,20):
        monkey_list = round(monkey_list,1,False)
    i = calc_monkey_business(monkey_list)


test(r'2022\11\test.txt')

monkey_list = parser(path=r'2022\11\input')
for i in range(0,10000):
    monkey_list = round(monkey_list,COMMON_NR, divide= False)
print(calc_monkey_business(monkey_list))
