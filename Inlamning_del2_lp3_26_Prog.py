# Skriv en inledande kommentar som talar om vad programmet gör.


# Placera dina modulimpoter här:

import csv
import matplotlib.pyplot as plt

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
MONTHS = ['jan', 'feb', 'mar', 'apr', 'maj', 'juni','juli', 'aug','sep','okt','nov','dec']



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
            return i + 2 # då csv innehåller år,månad, så lägger jag till 2 för att det ska bli korrekt index.

def get_price_agreement_index(region) -> list:
    options_price_agreement = ['Rörligt pris', 'Fast pris 1 år', 'Fast pris 3 år']

    while True:
        clean_screen()
        print(f'{"=" * 80}')
        print(f"{"Välj en prisavatal":^80}")
        for i, value in enumerate(options_price_agreement, start=1):  # Start=1 används för att val alternativet (i) ska börja på 1.
            print(f"{i}: {value}")
        print(f'{"=" * 80}')
        choice = input("Välj nummer: ").strip()
        if choice == '1':
            return get_price_range_index(f'{region}-Rörligt pris'), options_price_agreement[0]
        elif choice == '2':
            return get_price_range_index(f'{region}-Fast pris 1 år'), options_price_agreement[1]
        elif choice == '3':
            return get_price_range_index(f'{region}-Fast pris 3 år'), options_price_agreement[2]
        
def get_price_agreement_index_four(regions) -> list:
    options_price_agreement = ['Rörligt pris', 'Fast pris 1 år', 'Fast pris 3 år', 'Anvisat pris']
    data_list =[] 
    while True:
        clean_screen()
        print(f'{"=" * 80}')
        print(f"{"Välj en prisavatal":^80}")
        for i, value in enumerate(options_price_agreement, start=1):  # Start=1 används för att val alternativet (i) ska börja på 1.
            print(f"{i}: {value}")
        print(f'{"=" * 80}')
        choice = input("Välj nummer: ").strip()
        if choice == '1':
            for region in regions:
               data_list.append((get_price_range_index(f'{region}-Rörligt pris'), options_price_agreement[0]))
        elif choice == '2':
            for region in regions:
                 data_list.append((get_price_range_index(f'{region}-Fast pris 1 år'), options_price_agreement[1]))
        elif choice == '3':
            for region in regions:
                data_list.append((get_price_range_index(f'{region}-Fast pris 3 år'), options_price_agreement[2]))
        elif choice == '4':
            for region in regions:
                data_list.append((get_price_range_index(f'{region}-Anvisat pris'), options_price_agreement[3]))
        return data_list

def get_all_price(selected_list: list, index: int, year: str, include_month=False) -> list | tuple[list, str]: 
    data_list = []
    # month = ['jan', 'feb', 'mar', 'apr', 'maj', 'juni', 'juli', 'aug','sep','okt','nov','dec']
    month = [f'jan-{year}', f'feb-{year}', f'mar-{year}', f'apr-{year}', f'maj-{year}', f'juni-{year}', f'juli-{year}', f'aug-{year}',f'sep-{year}',f'okt-{year}',f'nov-{year}',f'dec-{year}']

    for row in selected_list[1:]:
        if row[0] == year:
                data_list.append(float(row[index]))
    if include_month == True:
        return zip(month,data_list)
    
    return data_list

def add_dec_for_prev_year(all_prices, selected_list: list, index: int, year: str):
    price_prev_dec = 0
    prev_year = str(int(year) - 1)
    month_list, data_list = zip(*all_prices)
    data_list = list(data_list)
    month_list = list(month_list)
    dec = f'dec-{prev_year}'

    for row in selected_list[1:]:
        if row[0] == prev_year and row[1] == "december":
                price_prev_dec = float(row[index])
    
    data_list.insert(0,price_prev_dec)
    month_list.insert(0,dec)
    return zip(month_list,data_list)





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


# Deluppgift 2: Funktioner för deluppgift 2 i ordning. Ska använda funktioner från deluppgift VI på Del1 i modulen och ev. modifiera dem.
# Skriv din kod här:

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

    _, se1_min_spec_month, se1_min_spec_price = dl.calc_min_price(data_list, get_price_range_index('SE1-Anvisat pris'), year)
    _, se1_max_spec_month, se1_max_spec_price = dl.calc_max_price(data_list, get_price_range_index('SE1-Anvisat pris'), year)
    _, se1_min_spot_month, se1_min_spot_price = dl.calc_min_price(data_list, get_price_range_index('SE1-Rörligt pris'), year)
    _, se1_max_spot_month,se1_max_spot_price = dl.calc_max_price(data_list, get_price_range_index('SE1-Rörligt pris'), year)

    _, se2_min_spec_month, se2_min_spec_price = dl.calc_min_price(data_list, get_price_range_index('SE2-Anvisat pris'), year)
    _, se2_max_spec_month, se2_max_spec_price = dl.calc_max_price(data_list, get_price_range_index('SE2-Anvisat pris'), year)
    _, se2_min_spot_price, se2_min_spot_month = dl.calc_min_price(data_list, get_price_range_index('SE2-Rörligt pris'), year)
    _, se2_max_spot_price, se2_max_spot_month = dl.calc_max_price(data_list, get_price_range_index('SE2-Rörligt pris'), year)

    _, se3_min_spec_month, se3_min_spec_price = dl.calc_min_price(data_list, get_price_range_index('SE3-Anvisat pris'), year)
    _, se3_max_spec_month, se3_max_spec_price = dl.calc_max_price(data_list, get_price_range_index('SE3-Anvisat pris'), year)
    _, se3_min_spot_month, se3_min_spot_price = dl.calc_min_price(data_list, get_price_range_index('SE3-Rörligt pris'), year)
    _, se3_max_spot_month, se3_max_spot_price = dl.calc_max_price(data_list, get_price_range_index('SE3-Rörligt pris'), year)

    _, se4_min_spec_month, se4_min_spec_price = dl.calc_min_price(data_list, get_price_range_index('SE4-Anvisat pris'), year)
    _, se4_max_spec_month, se4_max_spec_price = dl.calc_max_price(data_list, get_price_range_index('SE4-Anvisat pris'), year)
    _, se4_min_spot_month, se4_min_spot_price = dl.calc_min_price(data_list, get_price_range_index('SE4-Rörligt pris'), year)
    _, se4_max_spot_month, se4_max_spot_price = dl.calc_max_price(data_list, get_price_range_index('SE4-Rörligt pris'), year)

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




# Deluppgift 3: Funktioner för deluppgift 3 i ordning.
# Skriv din kod här:

def print_plot_line_chart(data_list: list, region: str, year: str, month: list):

    plt.figure(figsize=(10,10))
    plt.xticks(rotation=90)
    plt.plot(month, data_list[0], label='Rörligt - lgh')
    plt.plot(month, data_list[2], label='Rörligt - villa')
    plt.plot(month, data_list[1], label='Fast 1 år - lgh')
    plt.plot(month, data_list[3], label='Fast 1 år - villa')
    plt.xlabel('månad')
    plt.ylabel('pris (öre/kWh)')
    plt.title(f'Elpriser prisområde {region} år {year}')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

# Deluppgift 4: Funktioner för deluppgift 4 i ordning.
# Skriv din kod här:

def calc_change_factor_monthly(data_list) -> float:
    _, data_list = zip(*data_list)
    data = []
    for prev, curr in zip(data_list, data_list[1:]):
        if prev != 0:
            change = round(((curr-prev)/prev)*100)
            data.append(change)
        else:
            data.append(0)

    return data
    

def print_bar_chart(data_list: list, choice_of_resident: str, region: str, name: str, months: list):
    plt.figure(figsize=(10,10))
    plt.xticks(rotation=90)
    plt.bar(months, data_list, label=name)
    plt.xlabel('månad')
    plt.ylabel('Förändring [%]', )
    plt.title(f'Månatlig förändring av elpriset för {choice_of_resident} i prisområde {region} år {year}')
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.5)
    plt.show()




# Deluppgift 5: Funktioner för deluppgift 5 i ordning.
# Skriv din kod här:

def get_all_prices_for_timeperiod(datalist: list, price, func):
    
    data_list = []
    for value in (OPTIONS_YEAR):
        data = func(datalist,price,value)
        if isinstance(data, tuple):
            x, y, z = data
        else:
            x = None
            y = None
            z = data

        data_list.append((x,y,z))

    return data_list
     
    



def print_table_min_max_avg_price_timeperiod(data_list: list, price_agreement: list):
    type_price_range = ["SE1", "SE2", "SE3", "SE4"]
    title = f"Analys av elpriserna för kategorin år {year}"
    title_spot_price = "rörligt pris (öre/kWh)"
    title_fixed_pris = "fast pris 3 år (öre/kWh)"
    title_range = "Prisomr."
    title_month = "(mån)"
    title_min = "Min -"
    title_max = "Max -"
    title_avg = "medel -"

   
    se1_min_fixed_price, se1_min_fixed_month = calc_min_price(data_list, 2, year)
    se1_max_fixed_price, se1_max_fixed_month = calc_max_price(data_list, 2, year)
    se1_min_spot_price, se1_min_spot_month = calc_min_price(data_list, 3, year)
    se1_max_spot_price, se1_max_spot_month = calc_max_price(data_list, 3, year)

    se2_min_fixed_price, se2_min_fixed_month = calc_min_price(data_list, 4, year)
    se2_max_fixed_price, se2_max_fixed_month = calc_max_price(data_list, 4, year)
    se2_min_spot_price, se2_min_spot_month = calc_min_price(data_list, 5, year)
    se2_max_spot_price, se2_max_spot_month = calc_max_price(data_list, 5, year)

    se3_min_fixed_price, se3_min_fixed_month = calc_min_price(data_list, 6, year)
    se3_max_fixed_price, se3_max_fixed_month = calc_max_price(data_list, 6, year)
    se3_min_spot_price, se3_min_spot_month = calc_min_price(data_list, 7, year)
    se3_max_spot_price, se3_max_spot_month = calc_max_price(data_list, 7, year)

    se4_min_fixed_price, se4_min_fixed_month = calc_min_price(data_list, 8, year)
    se4_max_fixed_price, se4_max_fixed_month = calc_max_price(data_list, 8, year)
    se4_min_spot_price, se4_min_spot_month = calc_min_price(data_list, 9, year)
    se4_max_spot_price, se4_max_spot_month = calc_max_price(data_list, 9, year)

    print(f'{"=" * 80}')
    print(f"{title:^80}")
    print(f"{title_spot_price:^40}{title_fixed_pris:^40}")
    print(f"{title_range:<10}{title_min:<7}{title_month:<7}{title_max:<7}{title_month:<7}{title_avg:<7}{title_min:<7}{title_month:<7}{title_max:<7}{title_month:<7}{title_avg:<7}")
    print(f"{type_price_range[0]:<10}{se1_min_spot_price:<7.2f}{se1_min_spot_month:<7}{se1_max_spot_price:<7.2f}{se1_max_spot_month:<7}{calc_avg_price(data_list, 3, year):<7.2f}{se1_min_fixed_price:<7.2f}{se1_min_fixed_month:<7}{se1_max_fixed_price:<7.2f}{se1_max_fixed_month:<7}{calc_avg_price(data_list, 2, year):<7.2f}")
    print(f"{type_price_range[1]:<10}{se2_min_spot_price:<7.2f}{se2_min_spot_month:<7}{se2_max_spot_price:<7.2f}{se2_max_spot_month:<7}{calc_avg_price(data_list, 5, year):<7.2f}{se2_min_fixed_price:<7.2f}{se2_min_fixed_month:<7}{se2_max_fixed_price:<7.2f}{se2_max_fixed_month:<7}{calc_avg_price(data_list, 4, year):<7.2f}")
    print(f"{type_price_range[2]:<10}{se3_min_spot_price:<7.2f}{se3_min_spot_month:<7}{se3_max_spot_price:<7.2f}{se3_max_spot_month:<7}{calc_avg_price(data_list, 7, year):<7.2f}{se3_min_fixed_price:<7.2f}{se3_min_fixed_month:<7}{se3_max_fixed_price:<7.2f}{se3_max_fixed_month:<7}{calc_avg_price(data_list, 6, year):<7.2f}")
    print(f"{type_price_range[3]:<10}{se4_min_spot_price:<7.2f}{se4_min_spot_month:<7}{se4_max_spot_price:<7.2f}{se4_max_spot_month:<7}{calc_avg_price(data_list, 9, year):<7.2f}{se4_min_fixed_price:<7.2f}{se4_min_fixed_month:<7}{se4_max_fixed_price:<7.2f}{se4_max_fixed_month:<7}{calc_avg_price(data_list, 8, year):<7.2f}")
    print(f'{"=" * 80}')
    input("Tryck enter för att fortsätta...")

    

def print_bar_chart():
    raise NotImplementedError

def print_bar_chart():
    raise NotImplementedError






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

    if input_choice == "1" or input_choice == "6" or is_csv_loaded():
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
                region = choose_price_region()
                
                wait()
            
                lgh_data = options_list['Lägenhet']
                villa_data = options_list['Villa']
                index_spot = get_price_range_index(f'{region}-Rörligt pris')
                index_fixed = get_price_range_index(f'{region}-Fast pris 1 år')
                year = choose_year()

                all_prices_spot_lgh = get_all_price(lgh_data, index_spot,year)
                all_prices_fixed_lgh = get_all_price(lgh_data, index_fixed, year)
                all_prices_spot_villa = get_all_price(villa_data, index_spot, year)
                all_prices_fixed_villa = get_all_price(villa_data, index_fixed, year)
                data_list = [all_prices_spot_lgh, all_prices_fixed_lgh, all_prices_spot_villa, all_prices_fixed_villa]

                print_plot_line_chart(data_list, region, year, MONTHS)
                
            case '4':

                selected_list, choice_of_resident = choose_data_list(include_resident=True)
                region = choose_price_region()
                index, name = get_price_agreement_index(region)
                year = choose_year()
                all_prices2 = get_all_price(selected_list,index,year, include_month=True)
                x = add_dec_for_prev_year(all_prices2,selected_list,index,year)
                y = calc_change_factor_monthly(x)
                print_bar_chart(y, choice_of_resident, region, name, MONTHS)
                wait()
                
            case '5':
                
                
                list_index = get_price_agreement_index_four(OPTIONS_PRICE_REGION)
                
                # lgh

                # Lägenhetskund 
              
                apparment_data_min = []
                for x in range(4):
                    data = get_all_prices_for_timeperiod(options_list['Lägenhet'], list_index[x][0], dl.calc_min_price)
                    apparment_data_min.append(data)

                apparment_data_max = []
                for x in range(4):
                    data = get_all_prices_for_timeperiod(options_list['Lägenhet'], list_index[x][0], dl.calc_min_price)
                    apparment_data_max.append(data)
                  

                apparment_data_avg = []
                for x in range(4):
                    data = get_all_prices_for_timeperiod(options_list['Lägenhet'], list_index[x][0], dl.calc_avg_price)
                    apparment_data_avg.append(data)

                # Villa
                house_data_min = []
                for x in range(4):
                    data = get_all_prices_for_timeperiod(options_list['Villa'], list_index[x][0], dl.calc_min_price)
                    house_data_min.append(data)

                house_data_max = []
                for x in range(4):
                    data = get_all_prices_for_timeperiod(options_list['Villa'], list_index[x][0], dl.calc_min_price)
                    house_data_max.append(data)

                house_data_avg = []
                for x in range(4):
                    data = get_all_prices_for_timeperiod(options_list['Villa'], list_index[x][0], dl.calc_avg_price)
                    apparment_data_avg.append(data)
        
              
                wait()
                xx1 = dl.calc_min_price(apparment_data_min[0],2)
                xx2 = dl.calc_min_price(apparment_data_min[1],2)
                xx3 = dl.calc_min_price(apparment_data_min[2],2)
                xx4 = dl.calc_min_price(apparment_data_min[3],2)

                yy1 = dl.calc_max_price(apparment_data_max[0],2)
                yy2 = dl.calc_max_price(apparment_data_max[1],2)
                yy3 = dl.calc_max_price(apparment_data_max[2],2)
                yy4 = dl.calc_max_price(apparment_data_max[3],2)

                zz1 = dl.calc_avg_price(apparment_data_avg[0],2)
                zz2 = dl.calc_avg_price(apparment_data_avg[1],2)
                zz3 = dl.calc_avg_price(apparment_data_avg[2],2)
                zz4 = dl.calc_avg_price(apparment_data_avg[3],2)

                x1 = dl.calc_min_price(house_data_min[0],2)
                x2 = dl.calc_min_price(house_data_min[1],2)
                x3 = dl.calc_min_price(house_data_min[2],2)
                x4 = dl.calc_min_price(house_data_min[3],2)

                y1 = dl.calc_max_price(house_data_max[0],2)
                y2 = dl.calc_max_price(house_data_max[1],2)
                y3 = dl.calc_max_price(house_data_max[2],2)
                y4 = dl.calc_max_price(house_data_max[3],2)

                z1 = dl.calc_avg_price(house_data_avg,2)
                z2 = dl.calc_avg_price(house_data_avg,2)
                z3 = dl.calc_avg_price(house_data_avg,2)
                z4 = dl.calc_avg_price(house_data_avg,2)

 
                type_price_range = ["SE1", "SE2", "SE3", "SE4"]
                title1 = f"Lägsta-, högsta-, och medelvärde av elpriserna"
                title2 = f"under tidperioden 2018-2025 för {list_index[0][1]}"

                title_spot_price = 'rörligt pris (öre/kWh)'
                title_fixed_pris = 'fast pris 3 år (öre/kWh)'
                title_range = 'Prisomr.'
                title_year = 'år'
                title_month = 'mån'
                title_min = 'Lägsta'
                title_max = 'högsta'
                title_avg = 'medel'
                print(f'{"=" * 80}')
                print(f"{title1:^80}")
                print(f"{title2:^80}")
                print(f"{title_spot_price:^40}{title_fixed_pris:^40}")
                print(f"{title_range:<10}{title_min:<7}{title_year:<7}{title_month:<7}{title_max:<7}{title_year:<7}{title_month:<7}{title_avg:<7}")
                print(f'{"-" * 80}')
                print('Kategori lägenhetskud:')
                print(f"{type_price_range[0]:<10}{xx1[2]:<7.2f}{xx1[0]:<7}{xx1[1]:<7}{yy1[2]:<7}{yy1[0]:<7}{yy1[1]:<7}{zz4:<7}")
                print(f"{type_price_range[1]:<10}{xx2[2]:<7.2f}{xx2[0]:<7}{xx2[1]:<7}{yy2[2]:<7}{yy2[0]:<7}{yy2[1]:<7}{zz4:<7}")
                print(f"{type_price_range[2]:<10}{xx3[2]:<7.2f}{xx3[0]:<7}{xx3[1]:<7}{yy3[2]:<7}{yy3[0]:<7}{yy3[1]:<7}{zz4:<7}")
                print(f"{type_price_range[3]:<10}{xx4[2]:<7.2f}{xx4[0]:<7}{xx4[1]:<7}{yy4[2]:<7}{yy4[0]:<7}{yy4[1]:<7}{zz4:<7}")
                print('Kategori villa:')
                print(f"{type_price_range[0]:<10}{x1[2]:<7.2f}{x1[0]:<7}{x1[1]:<7}{y1[2]:<7}{y1[0]:<7}{y1[1]:<7}{z1:<7}")
                print(f"{type_price_range[1]:<10}{x2[2]:<7.2f}{x2[0]:<7}{x2[1]:<7}{y2[2]:<7}{y2[0]:<7}{y2[1]:<7}{z2:<7}")
                print(f"{type_price_range[2]:<10}{x3[2]:<7.2f}{x3[0]:<7}{x3[1]:<7}{y3[2]:<7}{y3[0]:<7}{y3[1]:<7}{z3:<7}")
                print(f"{type_price_range[3]:<10}{x4[2]:<7.2f}{x4[0]:<7}{x4[1]:<7}{y4[2]:<7}{y4[0]:<7}{y4[1]:<7}{z4:<7}")
                print(f'{"=" * 80}')
                input("Tryck enter för att fortsätta...")


            case '6':
                print('Programmet avslutas...')
                exit()
            case _:
                print('Försök igen, valet finns inte.')
                input('Tryck enter för att komma till menyn.')
    else:
        clean_screen()
        print("Läs in CSV-filer först.")
        wait()