# Practice on strings.

import re

if __name__ == '__main__':
    # Task 1
    print('\nTask 1')

    s = 'Сидел барсук в своей норе и ел картошечку пюре'

    print(len(s))

    s += '.'
    print(s)

    print(s.count('ре'))

    print(s[-2])

    print(s[1::2])

    print(s.count(' ') + 1)

    # Task 2
    print('\nTask 2')

    s2 = '''пишите код так, как будто
    сопровождать его будет склонный к насилию
    психопат, который знает, где вы живете.'''

    if s2.islower(): s2 = s2.capitalize()
    print(s2)

    print(s2.find('сопровождать'))

    s2 = s2.replace('сопровождать', 'поддерживать')
    print(s2)

    part = s2.split(',')
    print(part)
    print(','.join(part))

    # Task 3
    print('\nTask 3')
    s3 = r'C:\Users\Matvei\Documents\Work\Name.exe'
    match = re.search(r'\.(.+$)', s3)[0]
    if match:
        print('found', match)
    else:
        print('did not find')

    # Task 4
    print('\nTask 4')

    num = 5658
    sum_num = 0
    str_num = str(num)
    for i in str_num:
        sum_num += int(i)
    print(sum_num)

    # Task 5
    print('\nTask 5')

    s4 = '11001011001100101001'

    print(s4 + '\n')
    print(s4.replace('1', '0', 2))
    print(s4.replace('1', '0', 5))
    print(s4.replace('1', '0'))
    print(s4.replace('0', '1', 2))
    print(s4.replace('0', '1', 5))
    print(s4.replace('0', '1'))

    # Task 'String Polynomial'
    print('Task String Polynomial')

    test = ['Аргентина манит негра',
             'аргентина манит негра',
             'Манит Аргентина негра']
    s_test = ''

    for s in test:
        s_test = s.lower().replace(' ', '')
        if s_test == s_test[::-1]:
            print(f'string {s} is polynomial')
        else:
            print(f'string {s} did not polynomial')

    # Task 'Switch words'
    print('\nTask switch words')

    s5 = 'momo mama papa'
    print(s5)
    s5 = ' '.join(s5.split(' ')[::-1])
    print(s5)

 # Task 1
    print('\nTask 1')

    s = 'Сидел барсук в своей норе и ел картошечку пюре'

    print(len(s))

    s += '.'
    print(s)

    print(s.count('ре'))

    print(s[-2])

    print(s[1::2])

    print(s.count(' ') + 1)

    # Task 2
    print('\nTask 2')

    s2 = '''пишите код так, как будто
    сопровождать его будет склонный к насилию
    психопат, который знает, где вы живете.'''

    if s2.islower(): s2 = s2.capitalize()
    print(s2)

    print(s2.find('сопровождать'))

    s2 = s2.replace('сопровождать', 'поддерживать')
    print(s2)

    part = s2.split(',')
    print(part)
    print(','.join(part))

    # Task 3
    print('\nTask 3')
    s3 = r'C:\Users\Matvei\Documents\Work\Name.exe'
    match = re.search(r'\.(.+$)', s3)[0]
    if match:
        print('found', match)
    else:
        print('did not find')

    # Task 4
    print('\nTask 4')

    num = 5658
    sum_num = 0
    str_num = str(num)
    for i in str_num:
        sum_num += int(i)
    print(sum_num)

    # Task 5
    print('\nTask 5')

    s4 = '11001011001100101001'

    print(s4 + '\n')
    print(s4.replace('1', '0', 2))
    print(s4.replace('1', '0', 5))
    print(s4.replace('1', '0'))
    print(s4.replace('0', '1', 2))
    print(s4.replace('0', '1', 5))
    print(s4.replace('0', '1'))

    # Task 'String Polynomial'
    print('Task String Polynomial')

    test = ['Аргентина манит негра',
             'аргентина манит негра',
             'Манит Аргентина негра']
    s_test = ''

    for s in test:
        s_test = s.lower().replace(' ', '')
        if s_test == s_test[::-1]:
            print(f'string {s} is polynomial')
        else:
            print(f'string {s} did not polynomial')

    # Task 'Switch words'
    print('\nTask switch words')

    s5 = 'momo mama papa'
    print(s5)
    s5 = ' '.join(s5.split(' ')[::-1])
    print(s5)