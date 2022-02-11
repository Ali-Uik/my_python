import sqlite3

database = sqlite3.connect('fastfood.db')
cursor = database.cursor()


def create_users_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(50) NOT NULL,
        telegram_id INTEGER NOT NULL UNIQUE
                                    );
                    ''')


def create_categories_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name VARCHAR(20) NOT NULL UNIQUE
                                        );
                    ''')


def create_products_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        product_name VARCHAR(20) NOT NULL UNIQUE,
        price DECIMAL(12, 2) NOT NULL,
        ingredients VARCHAR(50),
        images TEXT,
        FOREIGN KEY(category_id) REFERENCES categories(category_id)
                                        );
                ''')


def create_cart_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carts(
        cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(user_id) UNIQUE,
        total_products INTEGER DEFAULT 0,
        total_price DECIMAL(12,2) DEFAULT 0
                                    );
                    ''')


def create_cart_products_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cart_products(
        cart_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cart_id INTEGER REFERENCES carts(cart_id),
        product_name VARCHAR(20) NOT NULL,
        quantity INTEGER NOT NULL,
        final_price DECIMAL(12, 2) NOT NULL,
        UNIQUE(cart_id, product_name)
                                            );
                    ''')


def create_orders_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(user_id) UNIQUE,
        time_create DATETIME,
        total_products INTEGER DEFAULT 0,
        total_price DECIMAL(12,2) DEFAULT 0
                                    );
                    ''')


def create_order_products_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_products(
        order_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER REFERENCES orders(order_id),
        product_name VARCHAR(20) NOT NULL,
        quantity INTEGER NOT NULL,
        final_price DECIMAL(12, 2) NOT NULL,
        UNIQUE(order_id, product_name)
                                            );
                    ''')


# create_users_table()
# create_cart_table()
# create_cart_products_table()
# create_categories_table()
create_products_table()
# create_orders_table()
# create_order_products_table()

def insert_categories():
    cursor.execute('''
    INSERT INTO categories(category_name) VALUES 
    ('Лаваш'),('Донар'),('Бургер'),('Хот-Дог'),('Десерты'),('Напитки'),('Соусы')''')


# insert_categories()

def insert_products():
    cursor.execute('''INSERT INTO products(category_id,product_name,price,ingredients,images) VALUES
    (1,'mini lavash', 20000, 'Мясо, тесто, помидоры', 'media/lavash_1.jpg'),
    (1,'Лаваш говяжий', 25000, 'Мясо, тесто, помидоры', 'media/lavash_2.jpg'),
    (1,'Лаваш куриный', 25000, 'Курица, тесто, помидоры', 'media/lavash_3.jpg')''')


def drop_table_products():
    cursor.execute('''DROP TABLE IF EXISTS products;''')


# drop_table_products()
insert_products()

database.commit()
database.close()
