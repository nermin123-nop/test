new_words = {
    "LOL" : "komik bir şeye verilen cevap",
    "CRINGE ": "garip ya da utandırıcı bir şey",
    "ROFL" : "bir şakaya karşılık cevap",
    "SHEESH" : "onaylamamak",
    "CREEPY" : "korkunç",
    "AGGRO" : "agresifleşmek/sinirlenmek"
}
soru = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!):")
if word in new_words.keys():
    print(new_words[word])
else:
   print("Böyle bir kelime yok!")
