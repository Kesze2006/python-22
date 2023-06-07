#készíts egy modult, tartalmazzon egy osztályt téglalap néven ami 2 adatot (hosszúság,szélesség) és 2 fügvényt(terület és kerület) 5 téglalap, írja ki a legnagyobb területű és kerületű téglalap oldalait
import modul

for i in range(5):
    tegla=modul.teg(int(input("Kérem a téglalap hosszát: ")),int(input("Kérem a téglalap szélességét: ")))
    kerulet=tegla.kerulet()
    terulet=tegla.terulet()
    print()
    print("A téglalap területe: {}".format(terulet))
    print("A téglalap kerülete: {}".format(kerulet))
    print("-"*80)
