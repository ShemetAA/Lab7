import sqlite3

def create_database():
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gifts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            gift_name TEXT NOT NULL,
            price REAL NOT NULL,
            status TEXT NOT NULL
        )
    ''')

    gifts_data = [
        ('Михаил Иванович ГЛИНКА', 'Гитарные струны', 2000, 'куплен'),
        ('Александр Порфирьевич БОРОДИН', 'Дрампэд', 8000, 'некуплен'),
        ('Модест Петрович МУСОРГСКИЙ', 'Подарочная карта', 5000, 'куплен'),
        ('Пётр Ильич ЧАЙКОВСКИЙ', 'Педалборд', 10000, 'некуплен'),
        ('Николай Андреевич РИМСКИЙ-КОРСАКОВ', 'Педаль EarthQuaker Devices Plumes', 4500, 'куплен'),
        ('Александр Николаевич СКРЯБИН', 'Аудиокарта Audient', 4000, 'некуплен'),
        ('Сергей Васильевич РАХМАНИНОВ', 'Часы', 9000, 'куплен'),
        ('Игорь Фёдорович СТРАВИНСКИЙ', 'Телефон', 25000, 'некуплен'),
        ('Сергей Сергеевич ПРОКОФЬЕВ', 'Наушники', 7500, 'куплен'),
        ('Дмитрий Дмитриевич ШОСТАКОВИЧ', 'Микрофон', 8000, 'некуплен'),
    ]

    cursor.executemany('INSERT INTO gifts (full_name, gift_name, price, status) VALUES (?, ?, ?, ?)', gifts_data)

    conn.commit()
    conn.close()

create_database()