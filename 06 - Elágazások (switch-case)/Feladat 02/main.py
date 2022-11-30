month: str=None

print("Milyen hónap van?")
month=str(input())

match month:
    case "Január":
        print("Az év 1. hónapja.")
    case "Február":
        print("Az év 2. hónapja.")
    case "Március":
        print("Az év 3. hónapja.")
    case "Április":
        print("Az év 4. hónapja.")
    case "Május":
        print("Az év 5. hónapja.")
    case "Június":
        print("Az év 6. hónapja.")
    case "Július":
        print("Az év 7. hónapja.")
    case "Augusztus":
        print("Az év 8. hónapja.")
    case "Szeptember":
        print("Az év 9. hónapja.")
    case "Október":
        print("Az év 10. hónapja.")
    case "November":
        print("Az év 11. hónapja.")
    case "December":
        print("Az év 12. hónapja.")
    case _:
        print("Ilyen hónap nem létezik.")