st = input()

st = st.replace("<"," <<").replace(">",">> ").split()
for i in range(len(st)):
    if(st[i][0] != '<'):
        st[i] = st[i][::-1]
print(''.join(st))
        

