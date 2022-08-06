a = 10
b = 0

try:
    print(a/b)

except Exception as e: #except ZeroDivisionError as e
    print("Cannot divide by zero")
    print("Exception:", e)

finally:
    print("Over")
