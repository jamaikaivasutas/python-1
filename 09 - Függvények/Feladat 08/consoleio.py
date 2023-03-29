def getPointX()->int:
    print("Adja meg a pont X értékét!")
    temp = str(input())
    truncatedString = temp.replace(" ", "").replace("-", "")
    isNumber = truncatedString.isnumeric