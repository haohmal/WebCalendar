with open('name.txt', 'r', encoding='utf-8') as f1:
    with open('surname.txt', 'r', encoding='utf-8') as f2:
        with open('full_name.txt', 'w', encoding='utf-8') as f3:
            name = f1.read()
            surname = f2.read()
            full_name = name + ' ' + surname
            f3.write(full_name)