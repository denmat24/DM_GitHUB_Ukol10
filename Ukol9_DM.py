import time
import random


# Výběrové třídění
def selection_sort(arr):
    n = len(arr) #délka seznamu
    for i in range(n):
        min_idx = i #index minimálního prvku
        for j in range(i+1, n):  #hledá ve zbytku seznamu menší prvek než nejmenší aktuální v setřízeném
            if arr[j] < arr[min_idx]: #pokud nalezen - aktuslizace indexu
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] #výměna aktuálního s minimálním nalezeným

# Bublinové třídění
def bubble_sort(arr):
    n = len(arr)
    for i in range(n): #pro každý průchod posun max prvku na konec seznamu
        for j in range(0, n-i-1): #porovnání v neseřazené části
            if arr[j] > arr[j+1]: #větší než následující -> výměna
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Slévací třídění
def merge_sort(arr):
    if len(arr) > 1: #pokud je délka seznami >1 dělí seznam na L a R část
        mid = len(arr) // 2 # střední index
        #poloviny
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]: #přidání menšího prvku z levé nebo pravé ploviny
                arr[k] = L[i] #aktualizace seznamu
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # přidání zbýv. prvků
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Funkce na měření času
def measure_execution_time(sort_func, data):
    start_time = time.time()
    sort_func(data.copy()) # algoritmi - na kopii seznamu
    return time.time() - start_time

# Výpočet průměru
def calculate_mean(data):
    return sum(data) / len(data)

# Výpočet směrodatné odchylky
def calculate_std_dev(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5

# Funkce pro testování algoritmů třídění
def evaluate_sorting_algorithms(num_tests=100, categories=None):
    if categories is None:
        categories = [100, 1000, 10000, 100000]  # Kategorie velikostí seznamů

    results = {cat: {"SelectionSort": [], "BubbleSort": [], "MergeSort": [], "BuiltInSort": []} for cat in categories}

    for n in categories:
        print(f"\n--- Testování pro n = {n} ---")
        for _ in range(num_tests):
            test_data = [random.randint(0, 1000) for _ in range(n)]

            # Výběrové třídění
            if n <= 1000:  # Omezit SelectionSort pro menší velikosti seznamů
                results[n]["SelectionSort"].append(measure_execution_time(selection_sort, test_data))

            # Bublinové třídění
            if n <= 1000:  # Omezit BubbleSort pro menší velikosti seznamů
                results[n]["BubbleSort"].append(measure_execution_time(bubble_sort, test_data))

            # Slévací třídění
            results[n]["MergeSort"].append(measure_execution_time(merge_sort, test_data))

            # Vestavěné třídění
            results[n]["BuiltInSort"].append(measure_execution_time(sorted, test_data))

        # Výpočet průměrného času a směrodatné odchylky
        for key in results[n]:
            if results[n][key]:  # Přeskočit algoritmy bez výsledků
                avg_time = calculate_mean(results[n][key])
                std_dev = calculate_std_dev(results[n][key])
                print(f"{key} - Průměrný čas: {avg_time:.6f}s, Směrodatná odchylka: {std_dev:.6f}s")

# Spustit testování bez numpy
evaluate_sorting_algorithms(num_tests=100, categories=[100, 1000, 10000, 100000])
