def convert_inch_to_centimeters (inch):
    centimeters = inch*2.54
    return centimeters
    
def convert_centimeters_to_inch (centimeters):
    inch = centimeters / 2.54
    return inch
    
def convert_miles_to_km (miles):
    return miles * 1.60934
 
def convert_km_to_miles (km):
    return km * 0.621371
      
def convert_pounds_to_kg(pounds):
    return pounds * 0.4535924
    
def convert_kg_to_pounds(kg):
     return kg * 2.204623
     
def convert_ounces_to_grams(ounces):
    return ounces * 28.34952
    
def convert_grams_to_ounces(grams):
    return grams / 28.34952
    
def convert_gallons_to_liters(gallons):
     return gallons * 3.79
     
def convert_liters_to_gallons(liters):
    return liters * 0.26
      
def convert_pints_to_liters(pints):
    return pints * 0.5683
    
def convert_liters_to_pints(liters):
    return liters / 0.5683

print('1: Дюймы в сантиметры\n2: Сантимерты в дюймы\n3: Мили в километры\n4: Километры в мили\n5: Фунты в килограммы\n6: Килограммы в фунты\n7: Унции в граммы\n8: Граммы в унции\n9: Галлон в литры\n10: Литры в галлоны\n11: Пинты в литры\n12: Литры в пинты')
    
while True:
    
    number = int(input('Введите цифру от 1 до 12: '))
    if number == 0:
        break
    if number<1 or number > 12:
        print('Ошибка!')
        continue
    val = float(input('Введите значение: '))
    if number == 1:
        print(convert_inch_to_centimeters(val),'см')
    elif number == 2:
        print(convert_centimeters_to_inch(val),'дюймов')
    elif number == 3:
        print(convert_miles_to_km(val),'км')
    elif number == 4:
        print(convert_km_to_miles(val),'мили')
    elif number == 5:
        print(convert_pounds_to_kg(val),'кг')
    elif number == 6:
        print(convert_kg_to_pounds(val),'фунтов')
    elif number == 7:
        print(convert_ounces_to_grams(val),'грамм')
    elif number == 8:
        print(convert_grams_to_ounces(val),'унций')
    elif number == 9:
        print(convert_gallons_to_liters(val),'литров')
    elif number == 10:
        print(convert_liters_to_gallons(val),'галлона')
    elif number == 11:
        print(convert_pints_to_liters(val),'литров')
    elif number == 12:
        print(convert_liters_to_pints(val),'пинт')