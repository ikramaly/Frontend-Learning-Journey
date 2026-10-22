try: 
    n=2
    res=100/n
except ZeroDivisionError:
    print("Can't devide by zero")
except ValueError:
else:
    print("result",res)
finally:
    print("Now completed")