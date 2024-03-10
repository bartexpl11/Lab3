try:
    a = int(input())
    b = int(input())
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Error")
except ValueError:
    print("Wrong value")
except Exception:
    print("Error na wszytskie bledy")
else:
    print(result)