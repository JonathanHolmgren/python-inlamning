# Uppdaterad 2026-02-10

# Skriv en inledande kommentar som talar om vad programmet gör.
# Detta program tar fram och jämför priser för olika prisområden
# baserat valt år och boendetyp, med hjälp av två olika listor.

# Deluppgift II: Funktioner för deluppgift II i ordning.
# Funktion som tar fram total pris genom att loppa en lista.
# Inparameter: lista med data, kolumnindexet för prisområde, valt år,
# Returvärde: Funktionen returnerar en float.
def calculate_total_price(data_list: list, column: int, year: str | None = None) -> float:
    total_price = 0
    for row in data_list:
        if year is None or row[0] == year:
            total_price += float(row[column])
    return total_price


 
def calculate_avg_price(data_list: list, column: int, year: str | None = None) -> float:
    """
    Kalkylerar avg priset av en lista.
    param lista med värden, column som motsvarar index för elementet för priset.
    retunerar priset i form av float
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


# Deluppgift IV: Funktioner från deluppgift IV i ordning.

def calculate_max_price(data_list: list, column: int, year: str | None = None) -> tuple[float, str]:
    """
    Kalkylerar max priset av en lista.
    param lista med värden, column som motsvarar index för elementet för priset.
    retunerar en tuple [år, månad, pris]
    # Funktion som tar fram högsta pris genom att loppa en lista.
    # Inparameter: lista med data, kolumnindexet för prisområde, valt år,
    # Returvärde: Funktionen returnerar en float.
    
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


# Deluppgift V: Funktioner från deluppgift V i ordning.
# Funktion som tar fram lägsta pris genom att loppa en lista.
# Inparameter: lista med data, index för kolumnen för prisområde, valt år,
# Returvärde: Funktionen returnerar en float.
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
