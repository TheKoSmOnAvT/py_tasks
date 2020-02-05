import re

mas = ["А123АА11", "А222АА123", "А12АА123", "А123СС1234", "АА123А12"
    , "у555ППП3", "А123бА125", "А11115А5", "1АА111111", "АААААААА", "1ААИ55598", "Т258А569", "К555кК55", "К555кК552", "К555кК", "К555к"]

for number in mas:
    if( len(number) >= 8 and len(number) <= 9 ):
        nums = number[1:4] + number[6:] #only numbers
        nums = len(re.findall(r'\d', nums)) #only letters
        letters = len(re.findall(r'[АВЕКМНОРСТУХавекмнорстух]', number))
        if( (nums == 5 or nums == 6 ) and letters == 3 ):
            print(number)




