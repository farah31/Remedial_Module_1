# Soal Nomor 1
list_word = ['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']
finalword = []
keyword = input(f'{list_word}\nuser input : ')

def search_word(i):
    if keyword.lower() in i.lower():
        return i
    else:
        return False

final = filter(search_word, list_word)
result = []
for i in final:
    result.append(i)

print(result)

# Soal Nomor 2
tahun = int(input("User input: "))

if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print("Tahun Kabisat")
        else:
            print("Bukan Tahun Kabisat")
    else:
        print("Tahun Kabisat")
else:
    print("Bukan Tahun Kabisat")