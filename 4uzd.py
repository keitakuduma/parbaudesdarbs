#Izveidot Python programmu, kur lietotājs ievada faila nosaukumu un faila paplašinājumu,
# un atkarībā no faila paplašinājuma tiek nolasīts faila saturs.

def lasit_failu(fails):
    try:
        with open (fails, 'r') as fails:
            teksts=fails.read()
            print("Ievadītā faila saturs:")
            print(teksts)
    except FileNotFoundError:
        print("Kļūda: fails nav atrasts!")
    except Exception as e:
        print("Kļūda:", e)

def main():
    failanosaukums=input("Ievadiet faila nosaukumu:")
    faila_paplasinajums=input("Ievadiet faila paplasinajumu:")
    faila_paplasinajums=failanosaukums + '.' + faila_paplasinajums
    lasit_failu(faila_paplasinajums)

if __name__ == "__main__":
   main()