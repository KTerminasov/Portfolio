from decimal import Decimal
import datetime

# Пример аргументов: goods, 'Пельмени Универсальные', Decimal('0.25'), '2024-11-01'
def add(items, title, amount, expiration_date=None):
    if expiration_date is not None:
        expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()       
        
    if title in items:
        items[title].append({'amount':Decimal(amount), 'expiration_date': expiration_date})
    else:
        items[title] = [{'amount':Decimal(amount), 'expiration_date': expiration_date}]

# Пример аргументов: goods, 'Яйца 4 2023-07-15;
def add_by_note(items, note):
    note = note.split()
    if '-' in note[-1]:
        add(items, ' '.join(note[:-2]), note[-2], note[-1])
    else: 
        add(items, ' '.join(note[:-1]), note[-1])
            


def find(items, needle):
    needle = needle.lower()
    res = []
    for i in items:
        if needle in i.lower():
            res.append(i)
    return res
            


def amount(items, needle):
    quantity = Decimal('0')
    for j in find(items, needle):  
        for i in items[j]:
            quantity += i['amount']
    return quantity
            


def expire(items, in_advance_days=0):
    today = datetime.date.today()
    expired_items = []

    # Определяем дату, до которой продукты считаются почти просроченными
    expiry_threshold = today + datetime.timedelta(days=in_advance_days)

    for name, batches in items.items():
        total_amount = Decimal('0')
        
        for batch in batches:
            expiration_date = batch['expiration_date']
            if expiration_date and expiration_date <= expiry_threshold:
                total_amount += batch['amount']
        
        if total_amount > 0:
            expired_items.append((name, total_amount))
    
    return expired_items
    
goods = {    'Хлеб': [
        {'amount': Decimal('1'), 'expiration_date': None},        {'amount': Decimal('1'), 'expiration_date': datetime.date(2023, 12, 9)}
    ],    'Яйца': [
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2024, 10, 31)},        {'amount': Decimal('3'), 'expiration_date': datetime.date(2024, 12, 11)}
    ],    'Вода': [{'amount': Decimal('100'), 'expiration_date': None}]
}

print(expire(goods))
