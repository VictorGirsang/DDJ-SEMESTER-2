belanja = [
    {"Buah":"semangka","harga":12000},
    {"Buah":"nanas","harga":10000},
    {"Buah":"pepaya","harga":12000}]

total_belanjaan = 0
for item in belanja:
    total_belanjaan += item["harga"]

print("Total Belanja : ",total_belanjaan)