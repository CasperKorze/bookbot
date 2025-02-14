def count_characters(text):

    biblioteczka_na_literki = {} #Moja bilbioteka / bank na literki

    for character in text: #Iteracja przez znaki w tekście
        maly_znak = character.lower()  # zamień znak na małą literę
        if maly_znak.isalpha():  # sprawdzamy czy to litera
        
            if maly_znak in biblioteczka_na_literki: #System dodawania literek do dictionary 
                biblioteczka_na_literki[maly_znak] += 1
            else :
                biblioteczka_na_literki[maly_znak] = 1 #Jeśli nie ma, ustawia na 0

    lista_na_literki = [
        {"char": key, "num": value} for key,
        value in biblioteczka_na_literki.items()
        ] # .items() zwraca pary klucz-wartość. 
    #Dla każdego klucza (litery) i wartości (liczby wystąpień) w naszym słowniku tworzymy nowy słownik.
    #Tworzymy listę słowników, gdzie każdy element zawiera literę (char) i jej liczbę wystąpień (num), pobierając dane ze słownika biblioteczka_na_literki. 

    lista_na_literki.sort(reverse=True, key=sorter)

    return (lista_na_literki)

def sorter(biblioteka):
    return biblioteka["num"]

def count_words(text):
    words = text.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    character_count = count_characters(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for item in character_count:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
main()
