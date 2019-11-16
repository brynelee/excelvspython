da = ['e3cd', 'e547', 'e63d', '0ffd', 'e39b', 'e539', 'e5be', '0dd2', 'e3d6', 'e52e', 'e5f8', '0000', 'e404', 'e52b', 'e63d', '0312', 'e38b']
k = 0
num1 = 0
fetal1 = []
fetal2 = []
mother1 = []
ECG = []
for k in range(len(da)-int(len(da) % 4)):
    if num1 == 1:
       fetal2.append(da[k])
    elif num1 == 2:
       mother1.append(da[k])
    elif num1 == 3:
       ECG.append(da[k])
    else:
        num1 = 0
        fetal1.append(da[k])
    num1 += 1
print("fetal1:", fetal1)
print("fetal2:", fetal2)
print("mother1", mother1)
print("ECG:", ECG)

