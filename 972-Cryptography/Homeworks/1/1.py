import helper



ciphers = []
with open('q1-ciphers.txt') as file:
    for line in file.readlines():
        ciphers.append(bin(int(line.strip(), 16))[2:])

max_len = len(ciphers[len(ciphers) - 1])

for i in range(len(ciphers)):
    while len(ciphers[i]) < max_len:
        ciphers[i] += '0'
    ciphers[i] = ciphers[i][:max_len]

for i in range(len(ciphers)):
    ciphers[i] = helper.to_bytes(int(ciphers[i], 2))

cspaces = []
for i in range(len(ciphers)):
    cspaces.append([0] * len(ciphers[i]))
    for j in range(len(ciphers)):
        for k in range(len(ciphers[i])):
            x = (ciphers[i][k] ^ ciphers[j][k])
            if ord('a') <= x <= ord('z') or ord('A') <= x <= ord('Z'):
                cspaces[i][k] += 1

spaces = []
for i in range(len(ciphers)):
    spaces.append([])
    for k in range(len(ciphers[i])):
        cnt_space = 0
        max_cnt_space = max(cspaces[j][k] for j in range(len(ciphers)))
        for j in range(len(ciphers)):
            if cspaces[j][k] and cspaces[j][k] == max_cnt_space:
                cnt_space += 1
        spaces[i].append(max_cnt_space == cspaces[i][k] >= len(ciphers) / 2)

raw_key = []
for k in range(len(ciphers[0])):
    hads = []
    for i in range(len(ciphers)):
        if spaces[i][k]:
            hads.append(ord(' ') ^ ciphers[i][k])
    raw_key.append(hads)

key = []
for i in range(len(raw_key)):
    hads = raw_key[i]


    def cc(x):
        cnt = 0
        for j in range(len(ciphers)):
            y = ciphers[j][i] ^ x
            if ord('a') <= y <= ord('z') or ord('A') <= y <= ord('Z') or y in [' ', '.', '!', '?']:
                cnt += 1
        return cnt


    if len(hads):
        n = max(hads, key=cc)
        key += [n]
    else:
        key += [0]

# Fix key issues by hand
key[0] = ord('T') ^ ciphers[3][0]
key[4] = ord('a') ^ ciphers[0][4]
key[7] = ord('o') ^ ciphers[1][7]
key[12] = ord('p') ^ ciphers[1][12]
key[14] = ord('o') ^ ciphers[1][14]
key[25] = ord('y') ^ ciphers[1][25]
key[29] = ord('a') ^ ciphers[1][29]
key[35] = ord('a') ^ ciphers[0][35]
key[36] = ord('n') ^ ciphers[0][36]
key[45] = ord('u') ^ ciphers[0][45]
key[47] = ord('e') ^ ciphers[0][47]
key[52] = ord('m') ^ ciphers[8][52]
key[59] = ord('a') ^ ciphers[0][59]
key[67] = ord('t') ^ ciphers[0][67]
key[75] = ord('r') ^ ciphers[1][75]
key[77] = ord('p') ^ ciphers[1][77]

texts = []
for i in range(len(ciphers)):
    text = ''
    for j in range(len(ciphers[i])):
        n = ciphers[i][j] ^ key[j]
        if key[j] and n < 128:
            text += n.to_bytes(1, 'big').decode('ascii')
        else:
            text += '*'
    texts.append(text)

print(texts[10])
# prints: The secret message is: When using a stream cipher, never use the key more than once
