import math
import itertools

import helper

monogram = dict()
with open('monogram.txt') as file:
    for line in file.readlines():
        k, v = line.split()
        monogram[k] = float(v) / 100

bigram = dict()
with open('bigram.txt') as file:
    for line in file.readlines():
        k, v = line.split()
        bigram[k] = float(v) / 100

trigram = dict()
with open('trigram.txt') as file:
    for line in file.readlines():
        k, v = line.split()
        trigram[k.lower()] = float(v) / 100


def mono_variance(m):
    m_monogram = dict()
    l = 0
    for c in m:
        if c in monogram:
            l += 1
            m_monogram[c] = m_monogram.get(c, 0) + 1
    sum = 0
    ideal_sum = 0
    for c in monogram.keys():
        ideal_sum += monogram[c] ** 2
        sum += (m_monogram.get(c, 0) / l) ** 2
    return math.fabs(sum - ideal_sum)


def coincidence_index(m):
    m_monogram = dict()
    l = 0
    for c in m:
        if c in monogram:
            l += 1
            m_monogram[c] = m_monogram.get(c, 0) + 1
    sum = 0
    for c in monogram.keys():
        sum += monogram[c] * (m_monogram.get(c, 0) / l)
    return sum


def diff_coincidence_index(m):
    return math.fabs(coincidence_index(m) - 0.065)


with open('q3-cipher.txt') as file:
    cipher = file.readline().strip().lower()


def get_block(m, block_size, i):
    s = ''
    for j in range(len(m)):
        if j % block_size == i:
            s += m[j]
    return s


def sezar_attack(m):
    options = []
    for k in range(26):
        s = ''
        for c in m:
            s += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
        options.append(s)
    return min(options, key=diff_coincidence_index)


block_size = 5
print(''.join(helper.make_text_blocks([sezar_attack(get_block(cipher, block_size, i)) for i in range(block_size)])))
# prints: ihaveadreamthatonedaythisnationwillriseupandliveoutthetruemeaningofitscreedweholdthesetruthstobeselfevident
# thatallmenarecreatedequalihaveadreamthatonedayontheredhillsofgeorgiathesonsofformerslavesandthesonsofformerslaveown
# erswillbeabletositdowntogetheratthetableofbrotherhood
