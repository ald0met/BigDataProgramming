num = list(range(11))

while True:
    try:
        index = int(input("리스트의 인덱스를 입력하세요 (0-10): "))
        print(num[index])
    
    except IndexError:
        print("-1")
    
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
        break

    except ValueError:
        print("\n프로그램을 종료합니다.")
        break
