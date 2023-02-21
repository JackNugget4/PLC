def IntegerLiteralValidity(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
print(IntegerLiteralValidity(0x2a))