documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
#--------------------------------#
def document_owner(docnum, lst):
    owner = ''
    for val in lst:
        if val['number'] == docnum:
            owner = val["name"]
        else:
            pass
    if len(owner) > 0:
        res = f'Владелец документа: {owner}'
    else:
        res = ('Документ не найден в базе')
    return res

#--------------------------------#
def document_storage(docnum, data):
    for key, val in data.items():
        for doc in val:
            if doc == docnum:
                return f'Документ хранится на полке: {key}'
    return 'Документ не найден в базе'

#--------------------------------#
def document_info(documents, directories):
    docNT = {}
    for val in documents:
        docNT[val['number']] = val['type']
    
    for key, val in docNT.items():
        print (f'№ {key}, тип: {val}, {document_owner(key, documents)}, полка хранения: {document_storage(key, directories)[28:]}')

#--------------------------------#
def add_shelf(directories):
    print('Добавление полок в архив')
    print('Введите номер полки')
    newshelf = input()
    if newshelf in directories:
        return f'Такая полка уже существует. Текущий перечень полок: {", ".join(list(directories.keys()))}.'
    else:
        directories[newshelf] = []
        return f'Полка добавлена. Текущий перечень полок: {", ".join(list(directories.keys()))}.'
    
#--------------------------------#
def delete_shelf(directories):
    print('Удаление полок из архива')
    print('Введите номер полки:')
    delshelf = input()
    emptyshelfs = []
    for key, val in directories.items():
        if val == []:
            emptyshelfs.append(key)
    
    if delshelf in directories.keys():
        if delshelf not in emptyshelfs:
            return f'На полке есть документ(ы), удалите их перед удалением полки. Текущий перечень полок: {", ".join(list(directories.keys()))}.'
        else:
            del directories[delshelf]
            return f'Полка удалена. Текущий перечень полок: {", ".join(list(directories.keys()))}.'
    else:
        return f'Такой полки не существует. Текущий перечень полок: {", ".join(list(directories.keys()))}.'
     
#--------------------------------#
def add_document(documents, directories):
    print('Добавление документов в архив')
    docnum = input('Введите номер документа: ')
    doctype = input('Введите тип документа: ')
    docowner = input('Введите владельца документа: ')
    shelf = input('Введите полку для хранения: ')
    documents.append({'type': doctype, 'number': docnum, 'name': docowner})
    if shelf in directories:
        directories[shelf].append(docnum)
        print('Документ добавлен. Текущий список документов:')        
    else:
        print('Такой полки не существует. Добавьте полку командой as. ')
        print('Текущий список документов:')
    print(document_info(documents, directories))
    
#--------------------------------#
def delete_document(documents, directories):
    print('Удаление документов из архива')
    docnum = input('Введите номер документа: ')
    for doc in documents:
        if doc['number'] == docnum:
            documents.remove(doc)
            print('Документ удален')
            print('Текущий список документов:')
            return (document_info(documents, directories))
    print('Документ не найден в базе')
    print('Текущий список документов:')
    return (document_info(documents, directories))

#--------------------------------#
def change_shelf(data):
    print('Переместить документ на другую полку')
    docnum = input('Введите номер документа: ')
    shelf = input('На какую полку его нужно переместить? ')
    if not shelf in data:
        return f'Такой полки не существует. Текущий перечень полок: {", ".join(list(directories.keys()))}.'
    
    for key, val in data.items():
        for doc in val:
            if doc == docnum:
                data[shelf].append(doc)
                data[key].remove(doc)
                print('Документ перемещен.')
                print('Текущий список документов:')
                return (document_info(documents, directories))
    print ('Документ не найден в базе.')
    print('Текущий список документов:')
    return (document_info(documents, directories))

#--------------------------------#
def main():
    while True:
        print('')
        print('Доступные команды: p | s | l | ads | ds | ad | d | m | q')
        user_comand = input('Введите команду: ')
        if user_comand == 'p':
            docnum = input('Введите номер документа:')
            print(document_owner(docnum, documents))
        elif user_comand == 's':
            docnum = input('Введите номер документа:')
            print(document_storage(docnum, directories))
        elif user_comand == 'l':
            print(document_info(documents, directories))
        elif user_comand == 'ads':
            print(add_shelf(directories))
        elif user_comand == 'ds':
            print(delete_shelf(directories))
        elif user_comand == 'ad':
            print(add_document(documents, directories))
        elif user_comand == 'd':
            print(delete_document(documents, directories))
        elif user_comand == 'm':
            print(change_shelf(directories))
        elif user_comand == 'q':
            print('Выход')
            break
main()