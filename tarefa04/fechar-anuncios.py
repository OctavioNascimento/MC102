x0, y0, x1, y1 = input().split()

x0 = int(x0)
y0 = int(y0)
x1 = int(x1)
y1 = int(y1)

linhas = input()

linhas = int(linhas)

fechados = 0

while 0 < linhas:
    linhas -= 1
    xa, ya, xb, yb = input().split()
    
    xa = int(xa)
    ya = int(ya)
    xb = int(xb)
    yb = int(yb)

    if not (x0 >= xb or x1 <= xa or y0 >= yb or y1 <= ya):
        fechados += 1

print(f"Devem ser fechados {fechados} anúncios")