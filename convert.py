import csv, os
with open('USCensus1990.data.csv', "rt", encoding='utf8') as inp, open('new.csv', 'wt', encoding='utf8') as out:
    writer = csv.writer(out)
    counter = 0
    for row in csv.reader(inp):
        if counter % 2 == 0:
            writer.writerow(row)
        counter = counter + 1
        print(counter) 
os.remove('USCensus1990.data.csv')
os.rename('new.csv', 'USCensus1990.data.csv')
