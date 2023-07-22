import random

menu = {
    1: {'food': 'Pizza', 'price': 3.50, 'quantity': 10},
    2: {'food': 'Hamburger', 'price': 2.50, 'quantity': 15},
    3: {'food': 'Hotdog', 'price': 2.30, 'quantity': 20},
    4: {'food': 'Salad', 'price': 1.50, 'quantity': 12},
    5: {'food': 'Frie', 'price': 1.80, 'quantity': 18},
}

selected_items = []
total_price = 0

def update_quantity(food_item, quantity):
    for item in menu.values():
        if item['food'] == food_item:
            item['quantity'] += quantity

while True:
    print('-Menu-')
    for key, item in menu.items():
        print(f'{key}) {item["food"]} - ${item["price"]}')
    print('Print (0) to quit the menu')
    print('Print (R) to random recommendation')
    print('Press (S) to select the selected items')
    print('Press (C) to clear the selected items')
    print('Press (P) to proceed to checkout')

    choice = input('Choose the item, ordering depends on the menu number or letter ranges: ')

    if choice.isdigit():
        choice = int(choice)

        if choice in menu:
            selected_item = menu[choice]
            
            if selected_item['quantity'] > 0:
                selected_items.append(selected_item['food'])
                total_price += selected_item['price']
                selected_item['quantity'] -= 1
                print(f'You have ordered a ({selected_item["food"]}) for (${selected_item["price"]:.2f})')
            
            else:
                print('Sorry, the item is out of stock.')

        elif choice == 0:
            quit_request = input('Are you sure that you want to quit the menu? (Yes(1))/(No(2)): ')

            if quit_request == '1':
                print('You quit the menu, thank you for using our menu system!')
                break

            elif quit_request == '2':
                print('Menu quit request canceled, you can still order the selected items.')

            else:
                print('Invalid input, please choose the number 1 or 2 otherwise the quit request will not be completed.')

        else:
            print('Invalid input, please choose the digital number that given in our menu system.')

    elif choice.lower() == 'r':
        random_item = random.choice(list(menu.values()))
        
        if random_item['quantity'] > 0:
            selected_items.append(random_item['food'])
            total_price += random_item['price']
            random_item['quantity'] -= 1
            print(f'We trying to recommend for you a ({random_item["food"]}) for (${random_item["price"]:.2f})')
        
        else:
            print('Sorry, the recommended item is out of stock.')

    elif choice.lower() == 's':
        
        if len(selected_items) > 0:
            print('\nYou have ordered the following items:')
            item_counts = {item: selected_items.count(item) for item in selected_items}
            for item, quantity in item_counts.items():
                print(f'({item}) - x{quantity}')
        
        else:
            print('To select the selected items, you must order at least one item.')

    elif choice.lower() == 'c':
        clearing_request = input('Are you sure that you want to clear the selected items? (Yes(1))/No(2): ')

        if clearing_request == '1':
            
            if len(selected_items) > 0:
                for item in selected_items:
                    update_quantity(item, 1)
                selected_items = []
                total_price = 0
                print('Menu cleared!')
            
            else:
                print('To clear the selected items, you must order at least one item.')

        elif clearing_request == '2':
            print('The clearing request canceled!')

        else:
            print('Invalid input, please choose the digital number that given in our menu system.')

    elif choice.lower() == 'p':
        checkout_request = input('Are you sure that you want to proceed to checkout? (Yes(1))/(No(2)): ')

        if checkout_request == '1':
            
            if len(selected_items) > 0:
                print('\nProceeding to checkout..')
                print('You have ordered the following items:')
                item_counts = {item: selected_items.count(item) for item in selected_items}
                for item, quantity in item_counts.items():
                    print(f'({item}) - x{quantity}')
                print(f'You total payable is (${total_price})')
                print('Thank you for using our menu system, visit us later and Enjoy each of your visit :)')
           
            else:
                print('To proceed to checkout, you must order at least one item.')

        elif checkout_request == '2':
            print('The checkout request canceled, you can still order the items!')

        else:
            print('Invalid input, please choose a number 1 or 2 otherwise the checkout request will not be completed.')

    else:
        print('Invalid input, please select the number or letter directly, otherwise choosing request will not be completing.')
