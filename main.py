import csv

outputFilename = "vesszobol-pont-kesz.csv"
fo = open(outputFilename, "w")
fo.close()

with open('vesszobol-pont.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            row[6] = row[6].replace(',', '.')
            print(row[6])
            line_count += 1

        with open(outputFilename, mode='a') as output_file:
            csv_writer = csv.writer(output_file, delimiter=';')

            csv_writer.writerow(row)

    print(f'Processed {line_count} lines.')
