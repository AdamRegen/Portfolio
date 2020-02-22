Receipt = [['Matt Paint','Decorating',6.99],['Floral Wallpaper','Decorating',7.99],['Magnolia Gloss Paint','Decorating',5.49],['Weed Killer','Gardening',2.99],['Picture Frame','Decorating',8.99],['Grass Seed','Gardening',1.99]]

total = 0
FullTotal = 0

for i in range(len(Receipt)):
    if Receipt[1] == 'Decorating':
        total += Receipt[2]
        FullTotal += Receipt[2]

if 'gardening' in Receipt[1]:
    if total == 20:
        Receipt[2] // 0.9
    print(Receipt[2])
    FullTotal += Receipt[2]

print(FullTotal)
    
