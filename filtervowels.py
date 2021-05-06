def filterwolves(letter):
    if letter.lower() in vowels:
        return True
    else:
        return False
vowels = ["a", "e", "i", "o", "u"]    
print("b" in vowels)
sentence = "the clarusway is the best"
filtered_vowels = filter(filterwolves, sentence)
print(* filtered_vowels)
print(* filtered_vowels)
