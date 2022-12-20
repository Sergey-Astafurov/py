import csv


phonebook = [["Самойлов", "Иван", 89111111111], ["Викторов","Виктор", 89222222222], ["Миронов", "Мирон", 89333333333]]


def exp_csv():
    with open("lesson7_HomWork/phonebook.csv", mode="w", encoding="utf-8")as phbook:
        file_writer = csv.writer(phbook, delimiter=";", lineterminator="\r")
        for row in phonebook:
            file_writer.writerow(row)


def exp_txt():
    with open("lesson7_HomWork/phonebook.txt", mode="w", encoding="utf-8")as phbook:
        for i in phonebook:
            for j in i:
                phbook.write(str(j) + '\n')
            phbook.write('\n')


def imp_csv():
    export_csv = []
    with open("phonebook.csv", encoding="utf-8") as read_file:
        reader_object = csv.reader(read_file, delimiter=';')
        for row in reader_object:
            export_csv.append(row)
            print(row)


def imp_txt():
    with open('phonebook.txt', 'r', encoding="utf-8") as read:
        for line in read:
            print(line)
