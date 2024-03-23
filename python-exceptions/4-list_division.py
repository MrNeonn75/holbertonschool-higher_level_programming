#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    lis = list()
    while i < list_length:
        try:
            lis.append(my_list_1[i] / my_list_2[i])
            i = i + 1
        except TypeError:
            print("wrong type")
            lis.append(0)
            i = i + 1
            continue
        except IndexError:
            print("out of range")
            lis.append(0)
            i = i + 1
            continue
        except ZeroDivisionError:
            print("division by 0")
            lis.append(0)
            i = i + 1
            continue
        finally:
            pass
    return lis
