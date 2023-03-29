def sameChar(str1:str, str2:str)->str:
    intersection: str = ""
    for char in str1:
        if(str2.find(char)>0 and intersection.find(char)==0):
            intersection=intersection+char
    return intersection