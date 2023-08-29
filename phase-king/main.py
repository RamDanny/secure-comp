import copy

def main():
    print('Phase-King Protocol\nn > 4t')
    n, t = map(int, input('Num of parties, Corruptions : ').split())
    if n <= 4 * t:
        print('Enter n > 4t')
        return
    parties = [i+1 for i in range(n)]
    corrupt = list(map(int, input('Enter corrupt parties: ').split()))
    if len(corrupt) != t:
        print('Enter only t corruptions')
        return
    inputs = list(map(int, input('Enter party inputs: ').split()))
    prefs, outputs, rcv, vk = copy.deepcopy(inputs), [], [], []
    for i in range(n):
        rcv.append(None)
        vk.append(None)
    # run phases
    for k in range(1, t+2):
        # decide king for phase
        king = k
        # round 1
        for i in range(n):
            rcv[i] = [(prefs[j] if j+1 not in corrupt else int(input(f'p{j+1} -> p{i+1} send pref value as? '))) for j in range(n)]
            vk[i] = max(rcv[i], key=rcv[i].count)
            #print(f'{rcv[i]} {vk[i]}')
        # round 2
        vk_king = vk[king-1]
        for i in range(n):
            if rcv[i].count(vk[i]) > t + n//2:
                prefs[i] = vk[i]
            else:
                prefs[i] = vk_king if king not in corrupt else int(input(f'p{king} -> p{i+1} send king value as? '))
            #print(prefs[i])
    # output decision
    print(prefs)
    outputs = copy.deepcopy(prefs)

if __name__ == '__main__':
    main()
