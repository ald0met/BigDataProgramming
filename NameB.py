
import NameA

print("top-level in B.py")
NameA.func()

if __name__=="__main__":
    print("B.py가 직접 실행")
else:
    print("B.py가 임포트되어 사용됨")
