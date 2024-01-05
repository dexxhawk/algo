n = int(input())
st = set(range(1, n + 1))	
while True:
    s = input().strip()
    if s == "HELP": break

    inp_st = set(map(int, s.split()))
    ans = input().strip()
    if ans == "YES":
        st.intersection_update(inp_st)
    else:
        st.difference_update(inp_st)
print(*sorted(st))
