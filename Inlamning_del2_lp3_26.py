# Skriv en inledande kommentar som talar om vad programmet gör.
# Detta program analyserar och jämför priser för olika prisområden, prisavtal och år
# beroende på boendetyp. Analysen och jämförelse visas som tabell, diagram eller båda.

# Placera dina modulimpoter här:
import csv
import matplotlib.pyplot as plt

# Konstanter med data/rubriker. Används i funktionerna som fråga användaren om val.
options_list = {'Lägenhet': None, 'Villa': None}
YEARS = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
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
PRICE_REGIONS = ['SE1', 'SE2', 'SE3', 'SE4']
MONTHS = ['jan', 'feb', 'mar', 'apr', 'maj', 'juni','juli', 'aug','sep','okt','nov','dec']

OPTIONS_PRICE_AGREEMENT_THREE = ['Rörligt pris', 'Fast pris 1 år', 'Fast pris 3 år']
OPTIONS_PRICE_AGREEMENT_FOUR = ['Rörligt pris', 'Fast pris 1 år', 'Fast pris 3 år', 'Anvisat pris']


# Placera dina funktioner för deluppgift II - V på Del1 här:

def calculate_total_price(data_list: list, column: int, year: str | None = None) -> float:
    """
    Funktion som tar fram total pris genom att loppa en lista.
    Inparameter: lista med data, kolumnindexet för prisområde, valt år,
    Returvärde: Funktionen returnerar en float.
    """
    total_price = 0
    for row in data_list:
        if year is None or row[0] == year:
            total_price += float(row[column])
    return total_price


def calculate_avg_price(data_list: list, column: int, year: str | None = None) -> float:
    """
    Funktion som tar fram medelpriset genom att loppa en lista.
    Inparameter: lista med data, kolumnindexet för prisområde, valt år,
    Returvärde: Funktionen returnerar en float.
    """
    total_price = calculate_total_price(data_list, column, year)
    if year is None:
        avg_price = total_price / len(data_list)
    else:
        avg_price = total_price / 12

    return avg_price


def calculate_max_price(data_list: list, column: int, year: str | None = None) -> tuple[float, str]:
    """
    Kalkylerar max priset av en lista.
    param lista med värden, column som motsvarar index för elementet för priset.
    retunerar en tuple [år, månad, pris]
    """
    max_price = None
    max_month = None
    max_year = None

    for row in data_list:
        if year is None or row[0] == year:
            temp = float(row[column])  # Priset för aktuell rad

            if max_price is None or temp > max_price:  # Uppdaterar pris, om första rad eller nytt högsta pris.
                max_price = temp
                max_month = row[1]
                max_year = row[0]

    return max_year, max_month[:3], max_price


def calculate_min_price(data_list: list, column: int, year: str | None = None) -> tuple[float, str]:
    """
    Kalkylerar minimum priset av en lista.
    param lista med värden, column som motsvarar index för elementet för priset.
    retunerar en tuple [år, månad, pris]
    """
    minimum_price = None
    minimum_month = None
    min_year = None
    for row in data_list:
        if year is None or row[0] == year:         
            temp = float(row[column])  # Priset för aktuell rad
            if minimum_price is None or temp < minimum_price:  # Uppdaterar pris, om första rad eller nytt minsta pris.
                minimum_price = temp
                minimum_month = row[1]
                min_year = row[0]
    return min_year, minimum_month[:3], minimum_price


# Placera nya funktioner som används i flera deluppgifter här:


def clean_screen():
    """
    "Clean the screen without import os"
    """
    print("\n" * 100)


def wait_interaction():
    """
    Whait for user interaction to move on
    """
    input("tryck [ENTER] för gå vidare")


def is_csv_loaded() -> bool:
    """
    Check if csv file is loaded to the constant, LGHDATA, VILLADATA

    return true if it is
    """
    if options_list['Lägenhet'] is None or options_list['Villa'] is None:
        return False
    else:
        return True


def choose_year(years: list[str]) -> str:
    """
    Return the year selected by the user from the list.
    """
    clean_screen()
    if years is None:
        print("Värde för OPTIONS_YEAR saknas.")
        wait_interaction()
        return None
    while True:
        print(f'{'=' * 80}')
        print(f'{'Välj ett årtal':80}')
        for i, value in enumerate(years, start=1):
            print(f'{i}: {value}')
        print(f'{'=' * 80}')
        selected_year = input('Välj år: ').strip()
        if selected_year.isdigit():
            selected_year = int(selected_year)
            if 1 <= selected_year <= len(years):
                return years[selected_year - 1]
        print('Valt år finns inte som alternativ')


def choose_data_list(customer_data: dict[str: list | None], include_resident=False) -> list | tuple[list, str]:
    """
    print menu with with options for customertype.

    Parameters:
        customer_data (dict): with keys for customer_type and value with the data.
        Boolean True or False to include name.
    return list or tuple with the list and the "filename"
    """
    while True:
        clean_screen()
        print(f'{"=" * 80}')
        print(f"{"Välj en lista":^80}")
        for i, value in enumerate(customer_data, start=1):  # Start=1, Is used becuase the menu options(i) should start at 1.
            print(f"{i}: {value}")
        print(f'{"=" * 80}')
        selected_data_list = input("Välj lista: ").strip()
        match selected_data_list:
            case "1":
                if include_resident:
                    return customer_data["Lägenhet"], "Lägenhet"
                return customer_data["Lägenhet"]
            case "2":
                if include_resident:
                    return customer_data["Villa"], "Lägenhet"
                return customer_data["Villa"]
            case _:
                clean_screen()
                print("Vald lista finns inte som alternativ")


def get_price_agreement_column_index(price_agreements: list[str], price_agreement: str) -> int:
    """
    Check for the index that match name

    Parameters:
    name of the price range and a list that contains options for price agreement.

    return index for the price agreement.
    """
    for i, value in enumerate(price_agreements):
        if price_agreement == value:
            return i + 2  # since the CSV file structure starts with column year, month we add 2 to align with the correct column for price range.


def choose_price_region(price_regions: list[str]) -> str:
    """
    print menu with with options for price region.

    Parameters:
    List of price regions.
    return name of the price region
    """
    while True:
        clean_screen()
        print(f'{"=" * 80}')
        print(f"{"Välj en lista":^80}")
        for i, value in enumerate(price_regions, start=1):  # Start=1, Is used becuase the menu options(i) should start at 1.
            print(f"{i}: {value}")
        print(f'{"=" * 80}')
        user_input = input("Välj region: ").strip()
        if user_input.isdigit():
            region_index = (int(user_input)-1)
            if 0 <= region_index < len(price_regions):
                return price_regions[region_index]  # Since prices for respective pricerange start at the lgh[1][2] in the list, so -1 we add align index for the list.
        clean_screen()
        print("Valt alternativ finns inte, försökt igen")
        wait_interaction()


def choose_price_agreement_for_regions(regions: list[str], options_regions_fixed_spot_price: list[str], options_price_agreement: list[str]) -> list[tuple[int, str]]:
    """
    print menu with with options for price agreement.

    Parameters:
    List of price regions, price regions price agreement and priceagreement

    return column index and the name of name of the price agreement
    """
    while True:
        clean_screen()
        print(f'{"=" * 80}')
        print(f"{"Välj en prisavatal":^80}")
        for i, value in enumerate(options_price_agreement, start=1):  # Start=1 används för att val alternativet (i) ska börja på 1.
            print(f"{i}: {value}")
        print(f'{"=" * 80}')
        choice = input("Välj nummer: ").strip()
        if choice.isdigit():
            choice = (int(choice) - 1)
            if 0 <= choice < len(options_price_agreement):

                return [(get_price_agreement_column_index(options_regions_fixed_spot_price, f'{str(reggion)}-{options_price_agreement[choice]}'), options_price_agreement[choice]) for reggion in regions]
        print('Valt prisavtal finns inte som alternativ')
        wait_interaction()


def get_monthly_prices(selected_list: list, price_agreement_index: int, year: str, include_month=False) -> list | tuple[list, str]:
    """
    Extract the monthly prices from a resident type, price agreement and year.
    Then save the monthly price to a list.

    return a list contain only monnthly prices,
    if include_month is True return tuple with prices and months.
    """
    months = [f'{month}-{year}' for month in ['jan', 'feb', 'mar', 'apr', 'maj', 'juni', 'juli', 'aug', 'sep', 'okt', 'nov', 'dec']]
    data_list = [float(row[price_agreement_index]) for row in selected_list[1:] if row[0] == year]
    if include_month is True:
        return zip(months, data_list)
    return data_list


def add_dec_for_prev_year(all_prices, selected_list: list, index: int, year: str) -> tuple:
    """
    Add the price for december previous year
    """
    price_prev_dec = 0
    prev_year = str(int(year) - 1)
    months, prices = zip(*all_prices)
    prices = list(prices)
    months = list(months)
    dec = f'dec-{prev_year}'

    for row in selected_list[1:]:
        if row[0] == prev_year and row[1] == "december":
            price_prev_dec = float(row[index])

    prices.insert(0, price_prev_dec)
    months.insert(0, dec)
    return zip(months, prices)


# Deluppgift 1: Funktioner för deluppgift 1 i ordning.
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


# deluppgift 1b

def control_function():
    lghdata = read_file("lghpriser.csv")
    villadata = read_file("villapriser.csv")

    for x in range(3):
        print(f"L: {lghdata[x + 1]}")
        print(f"V: {villadata[x + 1]}")


# Deluppgift 2: Placera funktioner från deluppgift VI på Del1 här och modifiera den.

def print_table_min_max_avg_price(data_list: list, choice_of_resident: str, year: str, options_region_fixed_spot_price: list[str]):
    """
    Print a table in terminal with min,max and avg prices for price regions for a selected resident type and year,
    """
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

    _, se1_min_spec_month, se1_min_spec_price = calculate_min_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE1-Anvisat pris'), year)
    _, se1_max_spec_month, se1_max_spec_price = calculate_max_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE1-Anvisat pris'), year)
    _, se1_min_spot_month, se1_min_spot_price = calculate_min_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE1-Rörligt pris'), year)
    _, se1_max_spot_month, se1_max_spot_price = calculate_max_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE1-Rörligt pris'), year)

    _, se2_min_spec_month, se2_min_spec_price = calculate_min_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE2-Anvisat pris'), year)
    _, se2_max_spec_month, se2_max_spec_price = calculate_max_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE2-Anvisat pris'), year)
    _, se2_min_spot_month, se2_min_spot_price = calculate_min_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE2-Rörligt pris'), year)
    _, se2_max_spot_month, se2_max_spot_price = calculate_max_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE2-Rörligt pris'), year)

    _, se3_min_spec_month, se3_min_spec_price = calculate_min_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE3-Anvisat pris'), year)
    _, se3_max_spec_month, se3_max_spec_price = calculate_max_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE3-Anvisat pris'), year)
    _, se3_min_spot_month, se3_min_spot_price = calculate_min_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE3-Rörligt pris'), year)
    _, se3_max_spot_month, se3_max_spot_price = calculate_max_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE3-Rörligt pris'), year)

    _, se4_min_spec_month, se4_min_spec_price = calculate_min_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE4-Anvisat pris'), year)
    _, se4_max_spec_month, se4_max_spec_price = calculate_max_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE4-Anvisat pris'), year)
    _, se4_min_spot_month, se4_min_spot_price = calculate_min_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE4-Rörligt pris'), year)
    _, se4_max_spot_month, se4_max_spot_price = calculate_max_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE4-Rörligt pris'), year)

    print(f'{"=" * 80}')
    print(f"{title:^80}")
    print(f"{title_spot_price:^40}{title_fixed_pris:^40}")
    print(f"{title_range:<10}{title_min:<7}{title_month:<7}{title_max:<7}{title_month:<7}{title_avg:<7}{title_min:<7}{title_month:<7}{title_max:<7}{title_month:<7}{title_avg:<7}")
    print(f"{type_price_range[0]:<10}{se1_min_spot_price:<7.2f}{se1_min_spot_month:<7}{se1_max_spot_price:<7.2f}{se1_max_spot_month:<7}{calculate_avg_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE1-Rörligt pris'), year):<7.2f}{se1_min_spec_price:<7.2f}{se1_min_spec_month:<7}{se1_max_spec_price:<7.2f}{se1_max_spec_month:<7}{calculate_avg_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE1-Anvisat pris'), year):<7.2f}")
    print(f"{type_price_range[1]:<10}{se2_min_spot_price:<7.2f}{se2_min_spot_month:<7}{se2_max_spot_price:<7.2f}{se2_max_spot_month:<7}{calculate_avg_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE2-Rörligt pris'), year):<7.2f}{se2_min_spec_price:<7.2f}{se2_min_spec_month:<7}{se2_max_spec_price:<7.2f}{se2_max_spec_month:<7}{calculate_avg_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE2-Anvisat pris'), year):<7.2f}")
    print(f"{type_price_range[2]:<10}{se3_min_spot_price:<7.2f}{se3_min_spot_month:<7}{se3_max_spot_price:<7.2f}{se3_max_spot_month:<7}{calculate_avg_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE3-Rörligt pris'), year):<7.2f}{se3_min_spec_price:<7.2f}{se3_min_spec_month:<7}{se3_max_spec_price:<7.2f}{se3_max_spec_month:<7}{calculate_avg_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE3-Anvisat pris'), year):<7.2f}")
    print(f"{type_price_range[3]:<10}{se4_min_spot_price:<7.2f}{se4_min_spot_month:<7}{se4_max_spot_price:<7.2f}{se4_max_spot_month:<7}{calculate_avg_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE4-Rörligt pris'), year):<7.2f}{se4_min_spec_price:<7.2f}{se4_min_spec_month:<7}{se4_max_spec_price:<7.2f}{se4_max_spec_month:<7}{calculate_avg_price(data_list, get_price_agreement_column_index(options_region_fixed_spot_price, 'SE4-Anvisat pris'), year):<7.2f}")
    print(f'{"=" * 80}')
    input("Tryck enter för att fortsätta...")

# Deluppgift 3: Funktioner för deluppgift 3 i ordning.


def print_plot_line_chart(data_list: list, region: str, year: str, month: list):
    """
    Print a plot line chart, showing the monthly price changes from jan-dec for price agreement, region and year.
    """
    plt.figure(figsize=(10, 10))
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

def calculate_change_factor_monthly(data_list) -> float:
    """
    Take a list with prices inclusice the price for december previous year.
    Then calculate the monthly change in procent.

    return change in procent.
    """
    _, data_list = zip(*data_list)
    data = []
    for prev, curr in zip(data_list, data_list[1:]):
        if prev != 0:
            data.append(round(((curr-prev)/prev)*100))
        else:
            data.append(0)
    return data


def print_bar_chart(data_list: list, choice_of_resident: str, region: str, name: str, year: str, months: list):
    """
    Print a bar chart, with the monthly change for resident typ, region and year
    """

    plt.figure(figsize=(10, 10))
    plt.xticks(rotation=90)
    plt.bar(months, data_list, label=name)
    plt.xlabel('månad')
    plt.ylabel('Förändring [%]', )
    plt.title(f'Månatlig förändring av elpriset för {choice_of_resident} i prisområde {region} år {year}')
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.5)
    plt.show()

# Deluppgift 5: Funktioner för deluppgift 5 i ordning.
def get_prices_for_timeperiod(datalist: list, column_index: int, func) -> list:
    """
    Generic function that takes list with data, column_index for the price agreement and a function,
    to calculate min,max and avg.

    return a list
    """

    data_list = []
    for value in (YEARS):
        data = func(datalist, column_index, value)
        if isinstance(data, tuple):  # Check if function return a tuple containing month and price. Like Min and Max function.
            year, month, price = data
        else:   # Catches the average function that return one value.
            year = None
            month = None
            price = data

        data_list.append((year, month, price))

    return data_list


def get_prices_for_period(data_list: list, column: int, function) -> tuple:
    """
    Take a list contains all prices "max|min|avg" for respective month.
    and loop the list and return a tuple "max|min|avg" for respective price region.
    """
    return [function(data_list[x], column) for x in range(len(data_list))]


def print_table_min_max_avg_price_timeperiod(list_index: list[tuple[int, str]], minimum_prices_apartment: list[tuple[int, str]], max_prices_apartment: list[tuple[int, str]], average_prices_apartment: list[float], minimum_prices_house: list[tuple[int, str]], max_prices_house: list[tuple[int, str]], average_prices_house: list[float]):
    """
    Print a table in terminal with min,max and avg prices for a time period
    """

    clean_screen()
    type_price_range = ["SE1", "SE2", "SE3", "SE4"]
    title1 = "Lägsta-, högsta-, och medelvärde av elpriserna"
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
    print(f"\n\n{title1:^80}")
    print(f"{title2:^80}\n\n")
    print(f"{title_spot_price:^40}{title_fixed_pris:^40}")
    print(f"{title_range:<10}{title_min:<10}{title_year:<10}{title_month:<10}{title_max:<10}{title_year:<10}{title_month:<10}{title_avg:<10}")
    print(f'{"-" * 80}')
    print('Kategori lägenhetskud:')
    print(f"{type_price_range[0]:<10}{minimum_prices_apartment[0][2]:<10.2f}{minimum_prices_apartment[0][0]:<10}{minimum_prices_apartment[0][1]:<10}{max_prices_apartment[0][2]:<10}{max_prices_apartment[0][0]:<10}{max_prices_apartment[0][1]:<10}{average_prices_apartment[0]:<10.2f}")
    print(f"{type_price_range[1]:<10}{minimum_prices_apartment[1][2]:<10.2f}{minimum_prices_apartment[1][0]:<10}{minimum_prices_apartment[1][1]:<10}{max_prices_apartment[1][2]:<10}{max_prices_apartment[1][0]:<10}{max_prices_apartment[1][1]:<10}{average_prices_apartment[1]:<10.2f}")
    print(f"{type_price_range[2]:<10}{minimum_prices_apartment[2][2]:<10.2f}{minimum_prices_apartment[2][0]:<10}{minimum_prices_apartment[2][1]:<10}{max_prices_apartment[2][2]:<10}{max_prices_apartment[2][0]:<10}{max_prices_apartment[2][1]:<10}{average_prices_apartment[2]:<10.2f}")
    print(f"{type_price_range[3]:<10}{minimum_prices_apartment[3][2]:<10.2f}{minimum_prices_apartment[3][0]:<10}{minimum_prices_apartment[3][1]:<10}{max_prices_apartment[3][2]:<10}{max_prices_apartment[3][0]:<10}{max_prices_apartment[3][1]:<10}{average_prices_apartment[3]:<10.2f}")
    print('Kategori villa:')
    print(f"{type_price_range[0]:<10}{minimum_prices_house[0][2]:<10.2f}{minimum_prices_house[0][0]:<10}{minimum_prices_house[0][1]:<10}{max_prices_house[0][2]:<10}{max_prices_house[0][0]:<10}{max_prices_house[0][1]:<10}{average_prices_house[0]:<10.2f}")
    print(f"{type_price_range[1]:<10}{minimum_prices_house[1][2]:<10.2f}{minimum_prices_house[1][0]:<10}{minimum_prices_house[1][1]:<10}{max_prices_house[1][2]:<10}{max_prices_house[1][0]:<10}{max_prices_house[1][1]:<10}{average_prices_house[1]:<10.2f}")
    print(f"{type_price_range[2]:<10}{minimum_prices_house[2][2]:<10.2f}{minimum_prices_house[2][0]:<10}{minimum_prices_house[2][1]:<10}{max_prices_house[2][2]:<10}{max_prices_house[2][0]:<10}{max_prices_house[2][1]:<10}{average_prices_house[2]:<10.2f}")
    print(f"{type_price_range[3]:<10}{minimum_prices_house[3][2]:<10.2f}{minimum_prices_house[3][0]:<10}{minimum_prices_house[3][1]:<10}{max_prices_house[3][2]:<10}{max_prices_house[3][0]:<10}{max_prices_house[3][1]:<10}{average_prices_house[3]:<10.2f}")
    print(f'{"=" * 80}')
    input("Tryck enter för att fortsätta...")


def print_scatter_diagram(price_regions,list_index, list_minimum_apt, list_maximum_apt, list_average_apt, list_minimum_house, list_maximum_house, list_average_house):
    """
    Print a scatter diagram min,max and avg prices for a time period
    """
    fig, axes = plt.subplots(1, 2, figsize=(10, 10))
    fig.suptitle('Analys elpriser', fontsize=16, fontweight='bold')

    axes[0].scatter(price_regions, list_minimum_apt, label="lägsta pris")
    axes[0].scatter(price_regions, list_maximum_apt, label="högsta pris")
    axes[0].scatter(price_regions, list_average_apt, label="medelvärde")
    axes[0].set_ylabel('pris (öre/kWh)')
    axes[0].set_xlabel('prisområde')
    axes[0].set_title(f'Elpriser Lägsta-, högsta-, och medelvärde av elpriserna \n Kategori lägenhet - {list_index[0][1]}')
    axes[0].legend(loc='upper right')
    axes[0].grid(True, alpha=0.5)

    axes[1].scatter(price_regions, list_minimum_house, label="lägsta pris")
    axes[1].scatter(price_regions, list_maximum_house, label="högsta pris")
    axes[1].scatter(price_regions, list_average_house, label="medelvärde")
    axes[1].set_ylabel('pris (öre/kWh)')
    axes[1].set_xlabel('prisområde')
    axes[1].set_title(f'Elpriser Lägsta-, högsta-, och medelvärde av elpriserna \n Kategori Villakund - {list_index[0][1]}')
    axes[1].legend(loc='upper right')
    axes[1].grid(True, alpha=0.5)

    plt.subplots_adjust(wspace=1)
    plt.show()


# Huvudprogram med Meny för deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.

def main_program():
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

                    if is_csv_loaded():
                        print("CSV-filerna har läst in")
                        control_function()
                        wait_interaction()
                    else:
                        print('Försök igen')
                        wait_interaction()

                case '2':
                    selected_list, resident_type = choose_data_list(options_list, include_resident=True)
                    year = choose_year(YEARS)
                    print_table_min_max_avg_price(selected_list, resident_type, year, OPTIONS_REGION_FIXED_SPOT_PRICE)
                case '3':
                    region = choose_price_region(PRICE_REGIONS)
                    lgh_data = options_list['Lägenhet']
                    villa_data = options_list['Villa']
                    index_spot = get_price_agreement_column_index(OPTIONS_REGION_FIXED_SPOT_PRICE, f'{region}-Rörligt pris')
                    index_fixed = get_price_agreement_column_index(OPTIONS_REGION_FIXED_SPOT_PRICE, f'{region}-Fast pris 1 år')
                    year = choose_year(YEARS)

                    prices_spot_lgh = get_monthly_prices(lgh_data, index_spot, year)
                    prices_fixed_lgh = get_monthly_prices(lgh_data, index_fixed, year)
                    prices_spot_villa = get_monthly_prices(villa_data, index_spot, year)
                    prices_fixed_villa = get_monthly_prices(villa_data, index_fixed, year)
                    data_list = [prices_spot_lgh, prices_fixed_lgh, prices_spot_villa, prices_fixed_villa]

                    print_plot_line_chart(data_list, region, year, MONTHS)

                case '4':

                    selected_list, resident_type = choose_data_list(options_list, include_resident=True)
                    region = choose_price_region(PRICE_REGIONS)
                    index_agreement = choose_price_agreement_for_regions([region], OPTIONS_REGION_FIXED_SPOT_PRICE, OPTIONS_PRICE_AGREEMENT_THREE)
                    year = choose_year(YEARS)
                    monthly_prices = get_monthly_prices(selected_list, index_agreement[0][0], year, include_month=True)
                    prices_plus_dec = add_dec_for_prev_year(monthly_prices, selected_list, index_agreement[0][0], year)
                    difference = calculate_change_factor_monthly(prices_plus_dec)
                    print_bar_chart(difference, resident_type, region, index_agreement[0][1], year, MONTHS)

                case '5':

                    index_agreement = choose_price_agreement_for_regions(PRICE_REGIONS, OPTIONS_REGION_FIXED_SPOT_PRICE, OPTIONS_PRICE_AGREEMENT_FOUR)

                    # Appartment
                    apparment_data_min = [get_prices_for_timeperiod(options_list['Lägenhet'], index_agreement[x][0], calculate_min_price) for x in range(4)]
                    apparment_data_max = [get_prices_for_timeperiod(options_list['Lägenhet'], index_agreement[x][0], calculate_min_price) for x in range(4)]
                    apparment_data_avg = [get_prices_for_timeperiod(options_list['Lägenhet'], index_agreement[x][0], calculate_avg_price) for x in range(4)]

                    minimum_prices_apartment = get_prices_for_period(apparment_data_min, 2, calculate_min_price)
                    max_prices_apartment = get_prices_for_period(apparment_data_max, 2, calculate_max_price)
                    average_prices_apartment = get_prices_for_period(apparment_data_avg, 2, calculate_avg_price)

                    # House
                    house_data_min = [get_prices_for_timeperiod(options_list['Villa'], index_agreement[x][0], calculate_min_price) for x in range(4)]
                    house_data_max = [get_prices_for_timeperiod(options_list['Villa'], index_agreement[x][0], calculate_min_price) for x in range(4)]
                    house_data_avg = [get_prices_for_timeperiod(options_list['Villa'], index_agreement[x][0], calculate_avg_price) for x in range(4)]

                    minimum_prices_house = get_prices_for_period(house_data_min, 2, calculate_min_price)
                    max_prices_house = get_prices_for_period(house_data_max, 2, calculate_max_price)
                    average_prices_house = get_prices_for_period(house_data_avg, 2, calculate_avg_price)

                    print_table_min_max_avg_price_timeperiod(index_agreement, minimum_prices_apartment, max_prices_apartment, average_prices_apartment, minimum_prices_house, max_prices_house, average_prices_house)

                    minimum_apt = [minimum_prices_apartment[0][2], minimum_prices_apartment[1][2], minimum_prices_apartment[2][2], minimum_prices_apartment[3][2]]
                    maximum_apt = [max_prices_apartment[0][2], max_prices_apartment[1][2], max_prices_apartment[2][2], max_prices_apartment[3][2]]
                    average_apt = [average_prices_apartment[0], average_prices_apartment[1], average_prices_apartment[2], average_prices_apartment[3]]

                    minimum_house = [minimum_prices_house[0][2], minimum_prices_house[1][2], minimum_prices_house[2][2], minimum_prices_house[3][2]]
                    maximum_house = [max_prices_house[0][2], max_prices_house[1][2], max_prices_house[2][2], max_prices_house[3][2]]
                    average_house = [average_prices_house[0], average_prices_house[1], average_prices_house[2], average_prices_house[3]]

                    print_scatter_diagram(PRICE_REGIONS, index_agreement, minimum_apt, maximum_apt, average_apt, minimum_house, maximum_house, average_house)

                case '6':
                    print('Programmet avslutas...')
                    exit()
                case _:
                    print('Försök igen, valet finns inte.')
                    wait_interaction()
        else:
            clean_screen()
            print("Läs in CSV-filer först.")
            wait_interaction()


# Run program

main_program()
