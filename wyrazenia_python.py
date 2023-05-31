#tabliczka mnożenia

def tabliczka(n_rows, n_cols):

    return [[i*j for j in range (1, n_cols+1)] for i in range (1, n_rows+1)]

print(tabliczka(3, 4))