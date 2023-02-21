def Correct_Floating_Point(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
string = "15.75L"
print(Correct_Floating_Point(string))