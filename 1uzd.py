#Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu.

def izlasit_izdrukat(fails):
    try:
        with open(fails, 'r', encoding='utf-8') as kk:
            saturs = kk.read()
            print("Failā atrodas:")
            print(saturs)
    except FileNotFoundError:
        print(f"Nevar atrast norādīto'{fails}' failu.")
    except Exception as e:
        print(f"Ir radusies kļūda: {e}")

b = 'teksts.txt'
izlasit_izdrukat(b)
