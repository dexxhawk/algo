seq = list(map(int, input().split()))
st = set()

for elem in seq:
    if elem not in st:
        print("NO")
        st.add(elem)
    else:
        print("YES")