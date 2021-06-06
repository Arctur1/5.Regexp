import re
import csv
import pandas
words_pattern = '[а-яА-Я]+'
phone_number = '(\+7|8)[\s(]*(\d{3})[)\s-]*(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})[\s(]*([а-яА-Я]+.)*[\s]*(\d{4})*[\)]*'
phone_replace = '\\1(\\2)\\3-\\4-\\5 \\6\\7'

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    for contact in contacts_list[1:]:
        contact[:3] = [','.join(contact[:3])]
    i = 1
    while i < len(contacts_list):
        name = ['', '', '']
        pattern = re.findall(words_pattern, contacts_list[i][0], flags=re.IGNORECASE)
        name[:len(pattern)] = pattern
        del contacts_list[i][0]
        contacts_list[i] = name + contacts_list[i]
        contacts_list[i][-2] = re.sub(phone_number, phone_replace, contacts_list[i][-2])
        contacts_list[i] = contacts_list[i][:7]
        i += 1
        df = pandas.DataFrame(contacts_list[1:], columns=contacts_list[0])
        df.groupby('lastname').first().reset_index().to_csv(r'phonebook.csv', header=1, index=None, sep=',',
                                                            mode='w', encoding='cp1251')






