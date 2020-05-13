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


def bi_coincidence_index(m):
    if m[-3:] != 'xxx':
        return 1000
    m_bigram = dict()
    m_trigram = dict()
    l = 0
    old_c = None
    for c in m:
        if c in monogram:
            if old_c and (old_c + c) in bigram:
                l += 1
                m_bigram[old_c + c] = m_bigram.get(old_c + c, 0) + 1
        old_c = c
    sum = 0
    ideal_sum = 0
    if l:
        for c in set(bigram.keys()) | set(m_bigram.keys()):
            sum += bigram.get(c, 0) * ((bigram.get(c, 0) / l) / monogram[c[0]])
            ideal_sum += bigram[c] * bigram[c]
        return -l + math.fabs(sum - ideal_sum)
    else:
        return 100000


with open('q2-cipher.txt') as file:
    cipher = file.readline().strip()

factors = []
for i in range(1, len(cipher) + 1):
    if len(cipher) % i == 0:
        factors.append(i)

# check cipher is permutaion
print('entebagh: ', coincidence_index(cipher) - 0.065)


# prints: entebagh:  -9.728752260397544e-05


def merge_blocks(blocks, i, j):
    new_blocks = []
    for kk in range(len(blocks)):
        if kk != i and kk != j:
            new_blocks.append(blocks[kk])
    block = []
    for kk in range(max(len(blocks[i]), len(blocks[j]))):
        a = ''
        if kk < len(blocks[i]):
            a += blocks[i][kk]

        if kk < len(blocks[j]):
            a += blocks[j][kk]
        block.append(a)
    new_blocks.append(block)
    return new_blocks


def blocks_bi_coincidence_index(blocks):
    text = ''.join(helper.make_text_blocks(blocks))
    return bi_coincidence_index(text)


def decrypt_with_block_size(cc, block_size):
    l = len(cc)
    block_size2 = (l + block_size - 1) // block_size
    blocks = [[] for _ in range(block_size)]
    for ii in range(l):
        char = cc[ii]
        blocks[ii // block_size2].append(char)
    return min(itertools.permutations(blocks), key=blocks_bi_coincidence_index)


def main():
    options = []
    for block_size in range(1, 8):
        options.append(decrypt_with_block_size(cipher, block_size))

    print(''.join(helper.make_text_blocks(min(options, key=blocks_bi_coincidence_index))))
    # prints: theobscuritywassodifficulttopenetratethatmrlorrypickinghiswayoverthewellwornturkeycarpetsupposedmissmanet
    # tetobeforthemomentinsomeadjacentroomuntilhavinggotpastthetwotallcandleshesawstandingtoreceivehimbythetablebetween
    # themandthefireayoungladyofnotmorethanseventeeninaridingcloakandstillholdingherstrawtravellinghatbyitsribboninherh
    # andashiseyesrestedonashortslightprettyfigureaquantityofgoldenhairapairofblueeyesthatmethisownwithaninquiringlooka
    # ndaforeheadwithasingularcapacityrememberinghowyoungandsmoothitwasofriftingandknittingitselfintoanexpressionthatwa
    # snotquiteoneofperplexityorwonderoralarmormerelyofabrightfixedattentionthoughitincludedallthefourexpressionsashise
    # yesrestedonthesethingsasuddenvividlikenesspassedbeforehimofachildwhomhehadheldinhisarmsonthepassageacrossthatvery
    # channelonecoldtimewhenthehaildriftedheavilyandthesearanhighthelikenesspassedawaylikeabreathalongthesurfaceofthega
    # untpierglassbehindherontheframeofwhichahospitalprocessionofnegrocupidsseveralheadlessandallcrippleswereofferingbl
    # ackbasketsofdeadseafruittoblackdivinitiesofthefemininegenderandhemadehisformalbowtomissmanettexxx


main()
