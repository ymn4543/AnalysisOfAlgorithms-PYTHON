
import sys










def main():
    print("please enter first fighters name: ")
    nme = str(sys.stdin.readline())
    print("please enter fighters height ")
    height=str(sys.stdin.readline())
    print(nme," has a height of ",height)
    print("please allow fighters to fight")
    print("please enter next fighters name")
    nme2=str(sys.stdin.readline())
    print(nme," is fighting ",nme2, "...")


if __name__ == '__main__':
    main()