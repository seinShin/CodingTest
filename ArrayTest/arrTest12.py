st = [i for i in range(1,31)]

for _ in range(28):
    x = int(input())
    st.remove(x)

print(min(x))
print(max(x))