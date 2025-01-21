# iterates over a ite obj based on the condition


l1 = [i for i in range(1,101)]

idx = 0

while idx < len(l1):
    if l1[idx] % 2 == 0:
        print(f'index: {idx} --> list value : {l1[idx]}')
    idx += 1







