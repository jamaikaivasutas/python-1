number1: int=None
number2: int=None
operator: str=None
number: int=None

print("Kérek két számot!")
number1=int(input().strip())
number2=int(input().strip())

print("Kérek egy matematikai műveletet (+,-,*,/)!")
operator=str(input().strip())

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