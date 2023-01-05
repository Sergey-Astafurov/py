import sqlite3


def connect():
    global conn, cursor
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()


def disconnect():
    conn.commit()
    conn.close()


def all(update, context):
    cursor.execute("select * from people")
    results = cursor.fetchall()
    update.message.reply_text('\n'.join([str(element) for element in results]))

def find(update, context):
    name = update.message.text
    cursor.execute(f"select * from people where lastname like '%{name}%'")
    results = cursor.fetchall()
    update.message.reply_text('\n'.join([str(element) for element in results]))

def add(update, context):
    lastname,firstname,number,position = update.message.text.split()
    cursor.execute(
    f"insert into people (lastname,firstname,number,position) "
    f"values ('{lastname}', '{firstname}', '{number}', '{position}')")
    conn.commit()
    update.message.reply_text("Контакт добавлен")


def update_info(update, context):
    lastname, number = update.message.text.split()
    cursor.execute(
        f"update people set number={number} where lastname='{lastname}'"
    )
    conn.commit()
    update.message.reply_text("Изменения внесены")


def delete(update,context):
    id = update.message.text
    cursor.execute(f"delete from people where id={id}")
    update.message.reply_text("Контакт удален")
    conn.commit()
    update.message.reply_text("Отключение базы данных")

