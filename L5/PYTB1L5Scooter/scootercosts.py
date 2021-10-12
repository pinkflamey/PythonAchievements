


def bereken_maand_kosten(km_p_maand):
    verzekering_per_maand = 23
    benzine_kosten_per_liter = 1.54
    liter_per_kilometer = 0.2

    try:
        km_p_maand = float(km_p_maand)

        maandkosten = (km_p_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand

        return maandkosten
    except ValueError:
        return "Voer een getal in."

x = input("km/maand: ")

print(bereken_maand_kosten(x))