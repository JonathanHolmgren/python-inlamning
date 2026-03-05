# Skriv en inledande kommentar som talar om vad programmet gör. 


# Placera dina modulimpoter här:

import csv
# import matplotlib.pyplot as plt
# import Inlamning_del1_lp3_26 as dl



# Placera ev. nya funktioner som används i flera deluppgifter här:
# Skriv din ev. kod här:



# Deluppgift 1: Funktioner för deluppgift 1 i ordning.
# Skriv din kod här:

def read_file(csv_filename : str) -> list:
    """
    param name of the csv file

    return a list of the csv file
    """
    rows = []
    with open(csv_filename,'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=';')
        for row in csv_reader:
            rows.append(row)

    return rows

# deluppgift 1b
def control_function():
    lghdata = read_file("lghpriser.csv")
    villadata = read_file("villapriser.csv")

    for x in range(3):
        print(f"L: {lghdata[x + 1]}")
        print(f"V: {villadata[x + 1]}")




control_function()

# Deluppgift 2: Funktioner för deluppgift 2 i ordning. Ska använda funktioner från deluppgift VI på Del1 i modulen och ev. modifiera dem.
# Skriv din kod här:





# Deluppgift 3: Funktioner för deluppgift 3 i ordning.
# Skriv din kod här:


# Deluppgift 4: Funktioner för deluppgift 4 i ordning.
# Skriv din kod här:


# Deluppgift 5: Funktioner för deluppgift 5 i ordning.
# Skriv din kod här:


# Huvudprogram med Meny för deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:

while True:
  print('Program för att läsa in och analysera resultatet i uppgift 1 – 5')
  print('1. Läs in CSV-filer. (Måste köras innan övriga alternativ)')
  print('2. Analysera elpris valt år.')
  print('3. Årsvariation hos elpriset.')
  print('4. Beräknar förändringsfaktorerna per månad.')
  print('5. Lägsta, högsta och medelvärde.')
  print('6. Avsluta programmet.')

  input_answer = input("Välj ett menyalternativ (1–6):")

  match input_answer:
      case '1':
          pass
      case '2':
          pass
      case '3':
          pass
      case '4':
          pass
      case '5':
          pass
      case '6':
        print('Programmet avslutas...')
        exit()
      case _:
          print('Försök igen')


