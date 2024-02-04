try:
    age=int(input("Age: "))
    income=20000
    risk=income/age
    print(risk)
except ZeroDivisionError:
    print("age can't be 0")
except ValueError:
    print("Invalid value")
