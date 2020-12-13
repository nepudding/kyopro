MOD = 998244353         # 問題に合わせて適宜書き換え
list_size = 10000010    # 問題に合わせて適宜書き換え

f_list = [1] * list_size
f_r_list = [1] * list_size

for i in range(1,list_size):
	f_list[i] = f_list[i-1]*i % MOD

f_r_list[-1] = pow(f_list[-1], MOD - 2, MOD)

for i in range(-2, -list_size-1, -1):
	f_r_list[i] = ((f_r_list[i+1] * (list_size + 1 + i)) % MOD)

def comb(n,r):
    if n < r:
        return 0
    if n==0 or r == 0 or n == r:
        return 1
    return (((f_list[n] * f_r_list[n - r]) % MOD) * f_r_list[r]) % MOD

def P(n,r):
    if n < r:
        return 0
    if r == 0 or n == 0:
        return 1
    return (f_list[n] * f_r_list[n - r]) % MOD

N = int(input())
print(comb(N,N))