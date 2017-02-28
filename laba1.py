k, l, n, m = map(int, raw_input().split())
print('danger' if (k == n or l == m or abs(k-n) == abs(l-m)) else 'no danger')
