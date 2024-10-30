from decimal import Decimal
from datetime import date, datetime

# Пример аргументов: goods, 'Пельмени Универсальные', Decimal('0.25'), '2024-11-01'
def add(items, title, amount, expiration_date=None):
    expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
    if title in items:
        items[title].append({'amount':Decimal(amount), 'expiration_date': expiration_date})
    else:
        items[title] = {'amount':Decimal(amount), 'expiration_date': expiration_date}

# Пример аргументов: goods, 'Яйца 4 2023-07-15;
def add_by_note(items, note):
    note = note.split()
    if len(note) == 2:
        add(items, note[0], note[1])
    else:
        add(items, note[0], note[1], note[2])
