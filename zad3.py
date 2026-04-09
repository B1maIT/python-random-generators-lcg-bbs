#dane 
bit_len = 8
a = 5
c = 3
mod = 16
seed_lcg = 7
seq_len = 10
seed_bbs = 11

#generator liczby pierwszej o zadanej dlugosci bitowej
def gen_prime(bit_len):
    while True:
        p = random_prime(2^bit_len - 1, lbound=2^(bit_len - 1))
        if p.nbits() == bit_len:
            return p

#generator liniowy mieszany (LCG)
def lcg(a, c, m, seed, n):
    x = seed
    out = []
    for _ in range(n):
        x = (a * x + c) % m
        out.append(x)
    return out

#generator Blum Blum Shub (BBS) - generuje bity
def bbs(p, q, seed, n):
    assert p % 4 == 3 and q % 4 == 3, "p i q musza byc kongruentne 3 modulo 4"
    M = p * q
    x = (seed^2) % M
    out = []
    for _ in range(n):
        x = (x^2) % M
        out.append(x % 2)
    return out

#funkcja szukajaca okresu ciagu
def znajdz_okres(seq):
    for i in range(1, len(seq) // 2):
        if seq[:i] == seq[i:2*i]:
            return i
    return len(seq)

#generowanie liczby pierwszej
print("Generator liczby pierwszej")
liczba_pierwsza = gen_prime(bit_len)
print(f"Liczba pierwsza ({bit_len} bitow):", liczba_pierwsza)

#generowanie ciagu LCG
print("\nGenerator kongruencyjny (LCG)")
ciag_lcg = lcg(a, c, mod, seed_lcg, seq_len)
print("Ciag LCG:", ciag_lcg)

#obliczanie okresu LCG
okres_lcg = znajdz_okres(ciag_lcg)
print("Okres LCG:", okres_lcg)

#przygotowanie p i q do BBS
p_bbs = next_prime(2^8)
while p_bbs % 4 != 3:
    p_bbs = next_prime(p_bbs)

q_bbs = next_prime(p_bbs + 1)
while q_bbs % 4 != 3:
    q_bbs = next_prime(q_bbs)

#generowanie ciagu BBS
print("\nGenerator Blum Blum Shub (BBS)")
ciag_bbs = bbs(p_bbs, q_bbs, seed_bbs, seq_len)
print("Ciag BBS (bity):", ciag_bbs)

#obliczanie okresu BBS
okres_bbs = znajdz_okres(ciag_bbs)
print("Okres BBS:", okres_bbs)
