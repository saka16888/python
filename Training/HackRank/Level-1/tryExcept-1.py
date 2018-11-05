try:
    raise NameError('Hi There')
    #raise Error1("error 1")
except NameError as err:
    print(err)
except Error1 as err:
    print(err)
else :
    raise Error1("error 1")
finally:
    print("executing finally clause")


try:
    f = open('Notes/myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
else:
    print("result is", result)
finally:
    print("executing finally clause")

print('-' * 60)
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2,0)
divide(2,1)