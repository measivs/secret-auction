from replit import clear
from art import logo
print(logo)
print('welcome to the secret auction program!')

dict1 = {}

process_continue = True
while process_continue:
    name = input('what\'s your name?: ')
    bid = input('what\'s your bid?: $')
    dict1[name] = bid
    q = input('are there any other bidders? (yes/no) ')
    list1 = []
    for key in dict1:
        list1.append(dict1[key])
        max_bid = max(list1)
    if dict1[key]==max(list1):
        winner = key
    if q == 'no':
        process_continue = False
        print(f'the winner is {winner} with a bid of ${max_bid}.')
    else:
        clear()
    
