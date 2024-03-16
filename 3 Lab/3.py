def number_to_words(number):
    ones = ['','один','два','три','четыре','пять','шесть','семь','восемь','девять']
    teens = ['','одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать']
    tens = ['','десять','двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']
    hundreds = ['','сто','двести','триста','четыреста','пятьсот','шестьсот','семьсот','восемьсот','девятьсот']
    if number == 0:
        return 'ноль'
    if number < 10:
        return ones[number]
    if number < 20:
        return teens[number-10]
    if number < 100:
        return tens[number//10] + ' ' + ones[number%10]
    if number < 1000:
        return hundreds[number//100] + ' ' + number_to_words(number%100)

    return "число вне диапазона"
number = int(input("Введите число от 1 до 1000: "))
if 1 <= number <= 1000:
    print(number_to_words(number))
else:
    print("Число вне диапазона")