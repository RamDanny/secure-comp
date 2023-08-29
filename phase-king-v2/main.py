import copy

def main():
    print('Phase-King Protocol (improved)\nn > 3t')
    n, t = map(int, input('Num of parties, Corruptions : ').split())
    if n <= 3 * t:
        print('Enter n > 3t')
        return
    parties = [i+1 for i in range(n)]
    corrupt = list(map(int, input('Enter corrupt parties: ').split()))
    if len(corrupt) != t:
        print('Enter only t corruptions')
        return
    inputs = list(map(int, input('Enter party inputs: ').split()))
    prefs, outputs, rcv, vk, propose = copy.deepcopy(inputs), [], [], [], []
    for i in range(n):
        rcv.append(None)
        vk.append(None)
        propose.append([])
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
        for i in range(n):
            if rcv[i].count(vk[i]) >= n - t:
                # send propose msg
                for j in range(n):
                    propose[j].append(vk[i] if i+1 not in corrupt else int(input(f'p{i+1} -> p{j+1} send proposed value as? ')))
        # round 3
        vk_king = prefs[king-1]
        for i in range(n):
            proposed = max(propose[i], key=propose[i].count)
            if propose[i].count(proposed) >= n - t:
                prefs[i] = proposed
            else:
                prefs[i] = vk_king if king not in corrupt else int(input(f'p{king} -> p{i+1} send king value as? '))
            #print(propose[i], prefs[i])
            propose[i] = []
    # output decision
    print(prefs)
    outputs = copy.deepcopy(prefs)

if __name__ == '__main__':
    main()
