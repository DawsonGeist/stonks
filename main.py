import json 

with open('tickers-11-11-2024.json', 'r') as f:
    file_data = f.read()
    json_data = json.loads(file_data)
    with open('stock-symbols-11-11-2024.csv', 'w') as o:
        for chunk in json_data:
            o.write(f"{chunk['normalizedTicker']},{chunk['instrumentName']}\n")