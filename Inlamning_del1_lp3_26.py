# Uppdaterad 2026-02-10

# Skriv en inledande kommentar som talar om vad programmet gör.
# Detta program tar fram och jämför priser för olika prisområden
# baserat valt år och boendetyp, med hjälp av två olika listor.


# Deluppgift 1: Funktioner för deluppgift I i ordning.
# Funktion som skriver ut listan som skickas med in på olika sett utifrån ett menyval.
# Inparameter: Listan som skall skrivas ut.
# Returvärde: Funktionen har inget returvärde.
def print_lista(namn):
    print("Skriver ut en lista")
    print("1: Hela listan")
    print("2: Listan radvis")
    print("3: Listan elementvis som matris")
    val = input("Hur vill du skriva ut listan? ")

    if val == "1":
        print("\nHela listan\n")
        print(
            namn
        )  # Skriver ut hela listan i en utskrift utan radbrytning för varje rad

    elif val == "2":
        print("\nListan radvis\n")
        for row in namn:  # Skriver ut hela listan radvis med radbrytning för varje rad
            print(row)

    elif val == "3":
        print("\nListan som matris\n")
        for (
            row
        ) in namn:  # Skriver ut hela listan elementvis med radbrytning för varje rad
            for item in row:
                print(f"{item:<20}", end=" ")
            print("")
    else:
        print("Ogiltigt val. Du kommer tillbaka till huvudmenyn.")


# Deluppgift II: Funktioner för deluppgift II i ordning.
# Funktion som tar fram total pris genom att loppa en lista.
# Inparameter: lista med data, kolumnindexet för prisområde, valt år,
# Returvärde: Funktionen returnerar en float.
def calc_total_price(data_list: list, column: int, year: str) -> float:
    total_price = 0
    for row in data_list:
        if row[0] == year:
            total_price += float(row[column])
    return total_price


# Deluppgift III: Funktioner för deluppgift III i ordning.
# Funktion som tar fram medelpriset genom att loppa en lista.
# Inparameter: lista med data, kolumnindexet för prisområde, valt år,
# Returvärde: Funktionen returnerar en float.
def calc_avg_price(data_list: list, column: int, year: str) -> float:
    total_price = calc_total_price(data_list, column, year)
    avg_price = total_price / 12

    return avg_price


# Deluppgift IV: Funktioner från deluppgift IV i ordning.
# Funktion som tar fram högsta pris genom att loppa en lista.
# Inparameter: lista med data, kolumnindexet för prisområde, valt år,
# Returvärde: Funktionen returnerar en float.
def calc_max_price(data_list: list, column: int, year: str) -> tuple[float, str]:
    max_price = None
    max_month = None
    for row in data_list:
        if row[0] == year:
            temp = float(row[column])  # Priset för aktuell rad
            if max_price is None or temp > max_price:  # Uppdaterar pris, om första rad eller nytt högsta pris.
                max_price = temp
                max_month = row[1]

    return max_price, max_month[:3]


# Deluppgift V: Funktioner från deluppgift V i ordning.
# Funktion som tar fram lägsta pris genom att loppa en lista.
# Inparameter: lista med data, index för kolumnen för prisområde, valt år,
# Returvärde: Funktionen returnerar en float.
def calc_min_price(data_list: list, column: int, year: str) -> tuple[float, str]:
    min_price = None
    min_month = None
    for row in data_list:
        if row[0] == year:
            temp = float(row[column])  # Priset för aktuell rad
            if min_price is None or temp < min_price:  # Uppdaterar pris, om första rad eller nytt minsta pris.
                min_price = temp
                min_month = row[1]
    return min_price, min_month[:3]


# Deluppgift VI: Funktioner från deluppgift IV i ordning.
# Skriver ut resultatet av min-, max- och medelpris från vald lista.
# Inparameter: lista med data, valt år,
# Returvärde: Funktionen returnerar inget värde.
# def print_table_min_max_avg_price(data_list: list, year: str):
#     type_price_range = ["SE1", "SE2", "SE3", "SE4"]
#     title = f"Analys av elpriserna för kategorin år {year}"
#     title_spot_price = "rörligt pris (öre/kWh)"
#     title_fixed_pris = "fast pris 3 år (öre/kWh)"
#     title_range = "Prisomr."
#     title_month = "(mån)"
#     title_min = "Min -"
#     title_max = "Max -"
#     title_avg = "medel -"

   
#     se1_min_fixed_price, se1_min_fixed_month = calc_min_price(data_list, 2, year)
#     se1_max_fixed_price, se1_max_fixed_month = calc_max_price(data_list, 2, year)
#     se1_min_spot_price, se1_min_spot_month = calc_min_price(data_list, 3, year)
#     se1_max_spot_price, se1_max_spot_month = calc_max_price(data_list, 3, year)

#     se2_min_fixed_price, se2_min_fixed_month = calc_min_price(data_list, 4, year)
#     se2_max_fixed_price, se2_max_fixed_month = calc_max_price(data_list, 4, year)
#     se2_min_spot_price, se2_min_spot_month = calc_min_price(data_list, 5, year)
#     se2_max_spot_price, se2_max_spot_month = calc_max_price(data_list, 5, year)

#     se3_min_fixed_price, se3_min_fixed_month = calc_min_price(data_list, 6, year)
#     se3_max_fixed_price, se3_max_fixed_month = calc_max_price(data_list, 6, year)
#     se3_min_spot_price, se3_min_spot_month = calc_min_price(data_list, 7, year)
#     se3_max_spot_price, se3_max_spot_month = calc_max_price(data_list, 7, year)

#     se4_min_fixed_price, se4_min_fixed_month = calc_min_price(data_list, 8, year)
#     se4_max_fixed_price, se4_max_fixed_month = calc_max_price(data_list, 8, year)
#     se4_min_spot_price, se4_min_spot_month = calc_min_price(data_list, 9, year)
#     se4_max_spot_price, se4_max_spot_month = calc_max_price(data_list, 9, year)

#     print(f'{"=" * 80}')
#     print(f"{title:^80}")
#     print(f"{title_spot_price:^40}{title_fixed_pris:^40}")
#     print(f"{title_range:<10}{title_min:<7}{title_month:<7}{title_max:<7}{title_month:<7}{title_avg:<7}{title_min:<7}{title_month:<7}{title_max:<7}{title_month:<7}{title_avg:<7}")
#     print(f"{type_price_range[0]:<10}{se1_min_spot_price:<7.2f}{se1_min_spot_month:<7}{se1_max_spot_price:<7.2f}{se1_max_spot_month:<7}{calc_avg_price(data_list, 3, year):<7.2f}{se1_min_fixed_price:<7.2f}{se1_min_fixed_month:<7}{se1_max_fixed_price:<7.2f}{se1_max_fixed_month:<7}{calc_avg_price(data_list, 2, year):<7.2f}")
#     print(f"{type_price_range[1]:<10}{se2_min_spot_price:<7.2f}{se2_min_spot_month:<7}{se2_max_spot_price:<7.2f}{se2_max_spot_month:<7}{calc_avg_price(data_list, 5, year):<7.2f}{se2_min_fixed_price:<7.2f}{se2_min_fixed_month:<7}{se2_max_fixed_price:<7.2f}{se2_max_fixed_month:<7}{calc_avg_price(data_list, 4, year):<7.2f}")
#     print(f"{type_price_range[2]:<10}{se3_min_spot_price:<7.2f}{se3_min_spot_month:<7}{se3_max_spot_price:<7.2f}{se3_max_spot_month:<7}{calc_avg_price(data_list, 7, year):<7.2f}{se3_min_fixed_price:<7.2f}{se3_min_fixed_month:<7}{se3_max_fixed_price:<7.2f}{se3_max_fixed_month:<7}{calc_avg_price(data_list, 6, year):<7.2f}")
#     print(f"{type_price_range[3]:<10}{se4_min_spot_price:<7.2f}{se4_min_spot_month:<7}{se4_max_spot_price:<7.2f}{se4_max_spot_month:<7}{calc_avg_price(data_list, 9, year):<7.2f}{se4_min_fixed_price:<7.2f}{se4_min_fixed_month:<7}{se4_max_fixed_price:<7.2f}{se4_max_fixed_month:<7}{calc_avg_price(data_list, 8, year):<7.2f}")
#     print(f'{"=" * 80}')
#     input("Tryck enter för att fortsätta...")


# Övriga funktioner för att minska redundans av kod.


# Frågar användaren vilket prisområde användaren vill välja (SE1 rörligt/fast).
# Inparameter: Funktionen returnerar inget värde.
# Returvärde: Funktionen returnerar kolumnindexet för prisområdet i lista.

# Skriver ut resultatet av vald beräkning.
# Inparameter: Namn av beräkning, kolumnindex av prisområden, året och resultatet av beräkningen.
# Returvärde: Funktionen returnerar retunerar inget värde..

# def print_result(type_of_calc: str, Column_index_price_range: int, year: str,
#                  result, month: str = None):
    
#     print(f'{"=" * 80}')
#     print(f"{"Resultatet":^80}")
#     print(f"Du har valt beräkna {type_of_calc} av följande kriterier:")
#     print(f"Du har valt prisområde: {OPTIONS_REGION_FIXED_SPOT_PRICE[
#         Column_index_price_range-2]}")  # Då listan valternativ listan startar på index 0, så tar jag -2 så det ska matchas.
#     print(f"Du har valt år: {year}")
#     if month:
#         print(f"Kalkylerat värde: {result:.2f} KR och gäller: {month}")
#     else:
#         print(f"Kalkylerat värde: {result:.2f} KR")
#     print(f'{"=" * 80}')

#     input("Tryck enter för att gå vidare...")


# Huvudprogram med menyval för de olika beräkningar i programmet.
# def main_menu():
#     while True:
#         clean_screen()
#         print("Program för att läsa in och analysera resultatet i uppgift 1 – 7")
#         print("1. Skriv ut listan.")
#         print("2. Beräkna summa.")
#         print("3. Beräkna medelvärde")
#         print("4. Hitta största värdet")
#         print("5. Hitta minsta värdet")
#         print("6. Analysera rörligt elpris valt år")
#         print("7. Avsluta programmet.")
#         input_choice = input("Välj ett menyalternativ (1–7) \n")
#         match input_choice:  # match används istället för if, för att endast matcha de godkända valen (choice).
#             case "1":
#                 print_lista(choose_data_list())
#             case "2":
#                 selected_list = choose_data_list()
#                 price_range = choose_price_range()
#                 year = choose_year()
#                 total = calc_total_price(selected_list, price_range, year)
#                 print_result("summan", price_range, year, total)
#             case "3":
#                 selected_list = choose_data_list()
#                 price_range = choose_price_range()
#                 year = choose_year()
#                 avg_price = calc_avg_price(selected_list, price_range, year)
#                 print_result("medelvärdet", price_range, year, avg_price)
#             case "4":
#                 selected_list = choose_data_list()
#                 price_range = choose_price_range()
#                 year = choose_year()
#                 max_price, max_month = calc_max_price(selected_list, price_range, year)
#                 print_result("max värdet", price_range, year, max_price, max_month)
#             case "5":
#                 selected_list = choose_data_list()
#                 price_range = choose_price_range()
#                 year = choose_year()
#                 min_price, min_month = calc_min_price(selected_list, price_range, year)
#                 print_result("minsta värdet", price_range, year, min_price, min_month)
#             case "6":
#                 print_table_min_max_avg_price(choose_data_list(), choose_year())
#             case "7":
#                 print("Programmet avslutas....")
#                 break
#             case _:  # Förvalt värde, om inget val matchas med något case.
#                 print("Försök igen, valet finns inte.")
#                 input("Tryck enter för att komma till menyn.")


# Kör huvud programmet