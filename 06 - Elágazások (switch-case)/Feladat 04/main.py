number1: int=None
number2: int=None
operator: str=None
number: int=None

print("Kérek két számot!")
number1=int(input())
number2=int(input())

print("Kérek egy matematikai műveletet (+,-,*,/)!")
operator=str(input())

match operator:
    case "+":
        number = number1 + number2
        print(f"A két szám összege: {number}")
    case "-":
        number = number1 - number2
        print(f"A két szám különbsége: {number}")
    case "*":
        number = number1 * number2
        print(f"A két szám szorzata: {number}")
    case "/":
        number = number1 / number2
        print(f"A két szám hányadosa: {number}")