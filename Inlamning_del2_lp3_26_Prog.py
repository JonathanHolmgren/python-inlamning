# Skriv en inledande kommentar som talar om vad programmet gör.


# Placera dina modulimpoter här:

import csv
# import matplotlib.pyplot as plt

import Inlamning_del1_lp3_26 as dl


# Konstanter med data/rubriker. Används i funktionerna som fråga användaren om val.
# lghData = None
# villaData = None
options_list = {'Lägenhet': None, 'Villa': None}
OPTIONS_YEAR = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
OPTIONS_REGION_FIXED_SPOT_PRICE = [
    'SE1-Fast pris 1 år',
    'SE1-Fast pris 3 år',
    'SE1-Rörligt pris',
    'SE1-Anvisat pris',
    'SE2-Fast pris 1 år',
    'SE2-Fast pris 3 år',
    'SE2-Rörligt pris',
    'SE2-Anvisat pris',
    'SE3-Fast pris 1 år',
    'SE3-Fast pris 3 år',
    'SE3-Rörligt pris',
    'SE3-Anvisat pris',
    'SE4-Fast pris 1 år',
    'SE4-Fast pris 3 år',
    'SE4-Rörligt pris',
    'SE4-Anvisat pris'
]
OPTIONS_PRICE_REGION = ['SE1', 'SE2', 'SE3', 'SE4']

# Placera ev. nya funktioner som används i flera deluppgifter här:
# Skriv din ev. kod här:

def clean_screen():
    """
    "Clean the screen without import os"
    """
    print("\n" * 100)

def wait():
    input("tryck [ENTER] för gå vidare")

def is_csv_loaded() -> bool:
    """
    Check if csv file is loaded to the constant, LGHDATA, VILLADATA

    return true if it is
    """
    if options_list['Lägenhet'] is None and options_list['Villa'] is None:
        return False
    else:
        return True

# NoneType


def choose_year() -> str:
    if OPTIONS_YEAR is None:
        print("Värde för OPTIONS_YEAR saknas.")
        wait()
        return None
    while True:
        print(f'{'=' * 80}')
        print(f'{'Välj ett årtal':80}')
        for i, value in enumerate(OPTIONS_YEAR, start=1):
            print(f'{i}: {value}')
        print(f'{'=' * 80}')
        selected_year = input('Välj år: ').strip()
        if selected_year.isdigit():
            selected_year = int(selected_year)
            if 1 <= selected_year <= len(OPTIONS_YEAR):
                return OPTIONS_YEAR[selected_year - 1]
        print('Valt år finns inte som alternativ')


def choose_data_list(include_resident=False) -> list | tuple[list, str]:
    """
    print dynamic menu with with options for customertype.

    return list or the list and the "filename"
    """
    while True:
        clean_screen()
        print(f'{"=" * 80}')
        print(f"{"Välj en lista":^80}")
        for i, value in enumerate(options_list, start=1):  # Start=1 används för att val alternativet (i) ska börja på 1.
            print(f"{i}: {value}")
        print(f'{"=" * 80}')
        selected_data_list = input("Välj lista: ").strip()
        match selected_data_list:
            case "1":
                if include_resident:
                    return options_list["Lägenhet"], "Lägenhet"
                return options_list["Lägenhet"]
            case "2":
                if include_resident:
                    return options_list["Villa"], "Lägenhet"
                return options_list["Villa"]
            case _:
                clean_screen()
                print("Vald lista finns inte som alternativ")


def choose_price_range() -> int:
    while True:
        clean_screen()
        print(f'{"=" * 80}')
        print(f"{"Välj en lista":^80}")
        for i, value in enumerate(OPTIONS_REGION_FIXED_SPOT_PRICE, start=1):  # Start=1 används för att val alternativet (i) ska börja på 1.
            print(f"{i}: {value}")
        print(f'{"=" * 80}')
        choice = input("Välj nummer: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(OPTIONS_REGION_FIXED_SPOT_PRICE):
                return choice + 1  # Då prisområden/priserna startar på lgh- villa[1][2] listorna, så +1 då choice startar på 1, se ovan.
        clean_screen()
        print("Valt nummer finns inte som alternativ")


def choose_price_region() -> str:
    while True:
        clean_screen()
        print(f'{"=" * 80}')
        print(f"{"Välj en lista":^80}")
        for i, value in enumerate(OPTIONS_PRICE_REGION, start=1):  # Start=1 används för att val alternativet (i) ska börja på 1.
            print(f"{i}: {value}")
        print(f'{"=" * 80}')
        choice = input("Välj nummer: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(OPTIONS_PRICE_REGION):
                return OPTIONS_PRICE_REGION[choice - 1]  # Då prisområden/priserna startar på lgh- villa[1][2] listorna, så +1 då choice startar på 1, se ovan.
        clean_screen()
        print("Valt nummer finns inte som alternativ")


def get_price_range_index(name_price_range: str) -> int:

    for i, value in enumerate(OPTIONS_REGION_FIXED_SPOT_PRICE):
        if name_price_range == value:
            return i


def print_table_min_max_avg_price(data_list: list, choice_of_resident: str, year: str):
    clean_screen()
    type_price_range = ["SE1", "SE2", "SE3", "SE4"]
    title = f"Analys av elpriserna för kategorin {choice_of_resident} år {year}"
    title_spot_price = "Rörligt pris (öre/kWh)"
    title_fixed_pris = "Anvisat pris (öre/kWh)"
    title_range = "Prisomr."
    title_month = "(mån)"
    title_min = "Min -"
    title_max = "Max -"
    title_avg = "medel -"

    # Lägg till
    # se1_spot = get_price_range_index('SE1-Rörligt pris')
    # se1_spec = get_price_range_index('SE1-Anvisat pris')

    se1_min_spec_price, se1_min_spec_month = dl.calc_min_price(data_list, get_price_range_index('SE1-Anvisat pris'), year)
    se1_max_spec_price, se1_max_spec_month = dl.calc_max_price(data_list, get_price_range_index('SE1-Anvisat pris'), year)
    se1_min_spot_price, se1_min_spot_month = dl.calc_min_price(data_list, get_price_range_index('SE1-Rörligt pris'), year)
    se1_max_spot_price, se1_max_spot_month = dl.calc_max_price(data_list, get_price_range_index('SE1-Rörligt pris'), year)

    se2_min_spec_price, se2_min_spec_month = dl.calc_min_price(data_list, get_price_range_index('SE2-Anvisat pris'), year)
    se2_max_spec_price, se2_max_spec_month = dl.calc_max_price(data_list, get_price_range_index('SE2-Anvisat pris'), year)
    se2_min_spot_price, se2_min_spot_month = dl.calc_min_price(data_list, get_price_range_index('SE2-Rörligt pris'), year)
    se2_max_spot_price, se2_max_spot_month = dl.calc_max_price(data_list, get_price_range_index('SE2-Rörligt pris'), year)

    se3_min_spec_price, se3_min_spec_month = dl.calc_min_price(data_list, get_price_range_index('SE3-Anvisat pris'), year)
    se3_max_spec_price, se3_max_spec_month = dl.calc_max_price(data_list, get_price_range_index('SE3-Anvisat pris'), year)
    se3_min_spot_price, se3_min_spot_month = dl.calc_min_price(data_list, get_price_range_index('SE3-Rörligt pris'), year)
    se3_max_spot_price, se3_max_spot_month = dl.calc_max_price(data_list, get_price_range_index('SE3-Rörligt pris'), year)

    se4_min_spec_price, se4_min_spec_month = dl.calc_min_price(data_list, get_price_range_index('SE4-Anvisat pris'), year)
    se4_max_spec_price, se4_max_spec_month = dl.calc_max_price(data_list, get_price_range_index('SE4-Anvisat pris'), year)
    se4_min_spot_price, se4_min_spot_month = dl.calc_min_price(data_list, get_price_range_index('SE4-Rörligt pris'), year)
    se4_max_spot_price, se4_max_spot_month = dl.calc_max_price(data_list, get_price_range_index('SE4-Rörligt pris'), year)

    print(f'{"=" * 80}')
    print(f"{title:^80}")
    print(f"{title_spot_price:^40}{title_fixed_pris:^40}")
    print(f"{title_range:<10}{title_min:<7}{title_month:<7}{title_max:<7}{title_month:<7}{title_avg:<7}{title_min:<7}{title_month:<7}{title_max:<7}{title_month:<7}{title_avg:<7}")
    print(f"{type_price_range[0]:<10}{se1_min_spot_price:<7.2f}{se1_min_spot_month:<7}{se1_max_spot_price:<7.2f}{se1_max_spot_month:<7}{dl.calc_avg_price(data_list, get_price_range_index('SE1-Rörligt pris'), year):<7.2f}{se1_min_spec_price:<7.2f}{se1_min_spec_month:<7}{se1_max_spec_price:<7.2f}{se1_max_spec_month:<7}{dl.calc_avg_price(data_list, get_price_range_index('SE1-Anvisat pris'), year):<7.2f}")
    print(f"{type_price_range[1]:<10}{se2_min_spot_price:<7.2f}{se2_min_spot_month:<7}{se2_max_spot_price:<7.2f}{se2_max_spot_month:<7}{dl.calc_avg_price(data_list, get_price_range_index('SE2-Rörligt pris'), year):<7.2f}{se2_min_spec_price:<7.2f}{se2_min_spec_month:<7}{se2_max_spec_price:<7.2f}{se2_max_spec_month:<7}{dl.calc_avg_price(data_list, get_price_range_index('SE2-Anvisat pris'), year):<7.2f}")
    print(f"{type_price_range[2]:<10}{se3_min_spot_price:<7.2f}{se3_min_spot_month:<7}{se3_max_spot_price:<7.2f}{se3_max_spot_month:<7}{dl.calc_avg_price(data_list, get_price_range_index('SE3-Rörligt pris'), year):<7.2f}{se3_min_spec_price:<7.2f}{se3_min_spec_month:<7}{se3_max_spec_price:<7.2f}{se3_max_spec_month:<7}{dl.calc_avg_price(data_list, get_price_range_index('SE3-Anvisat pris'), year):<7.2f}")
    print(f"{type_price_range[3]:<10}{se4_min_spot_price:<7.2f}{se4_min_spot_month:<7}{se4_max_spot_price:<7.2f}{se4_max_spot_month:<7}{dl.calc_avg_price(data_list, get_price_range_index('SE4-Rörligt pris'), year):<7.2f}{se4_min_spec_price:<7.2f}{se4_min_spec_month:<7}{se4_max_spec_price:<7.2f}{se4_max_spec_month:<7}{dl.calc_avg_price(data_list, get_price_range_index('SE4-Anvisat pris'), year):<7.2f}")
    print(f'{"=" * 80}')
    input("Tryck enter för att fortsätta...")


# Deluppgift 1: Funktioner för deluppgift 1 i ordning.
# Skriv din kod här:


def read_file(csv_filename: str) -> list:
    """
    param name of the csv file

    return a list of the csv file
    """
    rows = []

    try:
        with open(csv_filename, 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f, delimiter=';')
            for row in csv_reader:
                rows.append(row)
        return rows
    except FileNotFoundError:
        print(f'Fil: {csv_filename} hittades inte.')
        return None


# Denna funktion ligger inte med de andra funktioner pga av hierakisk bla bla.
def load_file(csv_filename: str, constant_variable: list):
    """
    Param name of the filename.

    load the data to constant.
    """
    raise NotImplementedError


# deluppgift 1b


# def control_function():
#     lghdata = read_file("lghpriser.csv")
#     villadata = read_file("villapriser.csv")

#     for x in range(3):
#         print(f"L: {lghdata[x + 1]}")
#         print(f"V: {villadata[x + 1]}")


# control_function()

# Deluppgift 2: Funktioner för deluppgift 2 i ordning. Ska använda funktioner från deluppgift VI på Del1 i modulen och ev. modifiera dem.
# Skriv din kod här:

def print_plot_line_chart(price_range: int, year:str):
    raise NotImplementedError


def get_all_price(selected_list: list, price_range: int) -> list: 
    data_list = []
    for row in selected_list:
        for column in row:
            print(column)
            wait()






# Deluppgift 3: Funktioner för deluppgift 3 i ordning.
# Skriv din kod här:


# Deluppgift 4: Funktioner för deluppgift 4 i ordning.
# Skriv din kod här:


# Deluppgift 5: Funktioner för deluppgift 5 i ordning.
# Skriv din kod här:
# Huvudprogram med Meny för deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:


while True:
    clean_screen()
    print('Program för att läsa in och analysera resultatet i uppgift 1 – 6')
    print('1. Läs in CSV-filer. (Måste köras innan övriga alternativ)')
    print('2. Analysera elpris valt år.')
    print('3. Årsvariation hos elpriset.')
    print('4. Beräknar förändringsfaktorerna per månad.')
    print('5. Lägsta, högsta och medelvärde.')
    print('6. Avsluta programmet.')

    input_choice = input("Välj ett menyalternativ (1–6):")

    if input_choice == "1" or is_csv_loaded():
        match input_choice:
            case '1':
                clean_screen()
                options_list['Lägenhet'] = read_file("lghpriser.csv")
                options_list['Villa'] = read_file("villapriser.csv")
                print("CSV-filerna har läst in")
                wait()
            case '2':
                selected_list, choice_of_resident = choose_data_list(include_resident=True)
                year = choose_year()

                print_table_min_max_avg_price(selected_list, choice_of_resident, year)
            case '3':
                choose_price_region()
                wait()
                selected_list = choose_data_list()
                price_range = choose_price_range()
                get_all_price(selected_list, price_range)

                # price_range = choose_price_range()
                # year = choose_year()
                # print_plot_line_chart(price_range, year)

            case '4':
                pass
            case '5':
                pass
            case '6':
                print('Programmet avslutas...')
                exit()
            case _:
                print('Försök igen, valet finns inte.')
                input('Tryck enter för att komma till menyn.')
    else:
        print("Läs in CSV-filer först.")
        wait()
