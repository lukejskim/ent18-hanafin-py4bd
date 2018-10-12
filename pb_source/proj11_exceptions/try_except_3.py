# 예외상황 테스트를 위한 함수
def exception_test3():
    print("[1] Can you add 2 and '2' in python? ")

    try:
        print("[2] Try it~! ", 2 + '2')  # 예외 발생
    except Exception as err:
        print('TypeError 발생 : {}'.format(err))

    print("[3] It's not possible to add integer and string together. ")


exception_test3()