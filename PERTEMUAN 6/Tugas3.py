data_penjualan = [
    {"produk":"baju","jumlah":20},
    {"produk":"sepatu","jumlah":15},
    {"produk":"sepatu","jumlah":25},
    {"produk":"Tas","jumlah":10},
    ]

total_penjualan= 0
for item in data_penjualan:
    total_penjualan += item["jumlah"]

print("Total_penjualan : ",total_penjualan)