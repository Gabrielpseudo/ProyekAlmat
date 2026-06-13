import Gabriel087

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

Perkalian = Gabriel087.perkalianmatriks(A, B)
print("Hasil Perkalian Matriks A dan B:")
for row in Perkalian:
    print(row)

Penjumlahan = Gabriel087.penjumlahanmatriks(A, B)
print("Hasil Penjumlahan Matriks A dan B:")
for row in Penjumlahan:
    print(row)

Transpose = Gabriel087.transposematriks(A)
print("Hasil Transpose Matriks A:")
for row in Transpose:
    print(row)
