from guestbook01.models import findall, insert, deleteby_no_and_pw


def test_findall():
    results = findall()
    for result in results:
        print(f'{result["no"]}:{result["name"]}:{result["reg_date"]}:{result["message"]}')


def test_insert():
    name = '둘리'
    password = '1234'
    message = '호이~'

    result = insert(name, password, message)
    print(f'insert result: {result}')


def test_deleteby_no_and_pw():
    no = 3
    password = '1234'

    result = deleteby_no_and_pw(no, password)
    print(f'delete result: {result}')


def main():
    test_findall()
    # test_insert()
    # test_deleteby_no_and_pw()


__name__ == '__main__' and main()

