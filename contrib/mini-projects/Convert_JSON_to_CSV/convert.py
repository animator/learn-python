import json

if __name__ == '__main__':
    try:
        with open('input.json', 'r') as f:
            data = json.load(f)

        # Extracting headers dynamically from the keys of the first object
        header = ','.join(data[0].keys())

        # Creating CSV content
        output = header
        for obj in data:
            output += f'\n{",".join(str(obj[key]) for key in obj)}'

        # Writing to output CSV file
        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')
