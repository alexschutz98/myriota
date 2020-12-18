
def norm2(a,b,c,d):
    return a*a + b*b + c*c + d*d

lower_bound = -3
upper_bound = 3

hypersphere = []
for a in range(lower_bound, upper_bound + 1):
    for b in range(lower_bound, upper_bound + 1):
        for c in range(lower_bound, upper_bound + 1):
            for d in range(lower_bound, upper_bound + 1):
                if norm2(a, b, c, d) < 10:
                    hypersphere.append((a, b))

print(len(hypersphere))