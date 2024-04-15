#Izveidot python programmu, kas nolasītu un izdrukātu trešās teksta faila rindas saturu.

def lasit_treso_rindu(fails):
    try:
        with open (fails, 'r', encoding='utf-8') as f:
            rindas=f.readlines()
            if len (rindas)>3:
                tresa_rinda=rindas[2].strip()
                print("Teksts, kas atrodas trešajā rindā:")
                print(tresa_rinda)
            else:
                print (f"Nevarēja izdrukāt {fails}, failā nav pietiekams rindu skaits")
    except FileNotFoundError:
        print (f'Nevarēja atrast {fails} failu')
    except Exception as e:
        print (f"Failā ir kļūda{e}")
t="teksts.txt"
lasit_treso_rindu
