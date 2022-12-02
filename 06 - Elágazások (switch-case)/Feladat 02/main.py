month: str=None

print("Milyen hónap van?")
month=str(input().strip().lower())

match month:
    case "január":
        print("Az év 1. hónapja.")
    case "február":
        print("Az év 2. hónapja.")
    case "március":
        print("Az év 3. hónapja.")
    case "április":
        print("Az év 4. hónapja.")
    case "május":
        print("Az év 5. hónapja.")
    case "június":
        print("Az év 6. hónapja.")
    case "július":
        print("Az év 7. hónapja.")
    case "augusztus":
        print("Az év 8. hónapja.")
    case "szeptember":
        print("Az év 9. hónapja.")
    case "október":
        print("Az év 10. hónapja.")
    case "november":
        print("Az év 11. hónapja.")
    case "december":
        print("Az év 12. hónapja.")
    case _:
        print("Ilyen hónap nem létezik.")