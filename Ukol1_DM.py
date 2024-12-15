#FizzBuzz game
print("START FIZZBUZZ GAME")
#Definice MAX čísla
max_cislo=30
#definice funkce fizzbuzz-přijímá n jako argument-vyvoláme a definujeme na konci->spustí se smyčka
def fizzbuzz(n):
    #iterace od 1 do n včetně (proto n+1)
    for f in range(1, n + 1):
        #využití zbytku po dělení (modulo %)
        #podmínka dělitelnosti 3 i 5 zároveň-výstup Fizz Buzz
        if f % 3 == 0 and f % 5 == 0:
            print("Fizz Buzz")
        # podmínka dělitelnosti 3 -výstup Fizz
        elif f % 3 == 0:
            print("Fizz")
        # podmínka dělitelnosti 5 -výstup Buzz
        elif f % 5 == 0:
            print("Buzz")
        #pokud není splněna žádná z následujících podmínek -> výstup aktuální f ve smyčce
        else:
            print(f)
    # po ukončení smyčky - výpis konce hry
    print("END FIZZBUZZ GAME")
#spuštění smyčky->
fizzbuzz(max_cislo)




