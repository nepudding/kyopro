MOD = 998244353         # 問題に合わせて適宜書き換え
list_size = 10000010    # 問題に合わせて適宜書き換え

f_list = [1] * list_size
f_r_list = [1] * list_size

for i in range(list_size - 1):
	f_list[i + 1] = ((f_list[i] * (i+2)) % MOD)

f_r_list[-1] = pow(f_list[-1], MOD - 2, MOD)

for i in range(-2, -list_size-1, -1):
	f_r_list[i] = ((f_r_list[i+1] * (list_size + 2 + i)) % MOD)

def comb(n,r):
    if n < r:
        return 0
    if n == 0 or r == 0 or n == r:
        return 1
    return (((f_list[n - 1] * f_r_list[n - r - 1]) % MOD) * f_r_list[r - 1]) % MOD

N = int(input())
print(comb(N,N))