import poker_environment as pe

def tuple_to_card_number(t):
    if t[1]=="diamonds":
        return t[0]*4+0
    elif t[1]=="clubs":
        return t[0]*4+1
    elif t[1]=="hearts":
        return t[0]*4+2
    elif t[1]=="spades":
        return t[0]*4+3

def tuples_to_string(a):
    s=""
    for i in a:
        s += str(tuple_to_card_number(i))

    return s

hands=[]
#1.royal flush
hands.append([ (12,"spades"),
               (11,"spades"),
               (10,"spades"),
               (9,"spades"),
               (8,"spades")])

'''
#2.royal flush with hearts
hands.append([ (12,"hearts"),
               (11,"hearts"),
               (10,"hearts"),
               (9,"hearts"),
               (8,"hearts")])
'''
#3.straight flush
hands.append([ (10,"spades"),
                (9,"spades"),
                (8,"spades"),
                (7,"spades"),
                (6,"spades")])

#4.four of a kind with aces with queen kicker
hands.append([ (12,"spades"),
                (12,"hearts"),
                (12,"clubs"),
                (12,"diamonds"),
                (10,"spades")])

#5.four of a kind with aces with jack kicker
hands.append([ (12,"spades"),
                (12,"hearts"),
                (12,"clubs"),
                (12,"diamonds"),
                (9,"spades")])

#6.four of a kind with kings with jack kicker
hands.append([ (11,"spades"),
                (11,"hearts"),
                (11,"clubs"),
                (11,"diamonds"),
                (9,"spades")])

#7.Full house AAAJJ
hands.append([ (12,"spades"),
                (12,"hearts"),
                (12,"clubs"),
                (9,"diamonds"),
                (9,"spades")])

#8.Full house KKKQQ
hands.append([ (11,"spades"),
                (11,"hearts"),
                (11,"clubs"),
                (10,"diamonds"),
                (10,"spades")])

#9.Full house KKKJJ
hands.append([ (11,"spades"),
                (11,"hearts"),
                (11,"clubs"),
                (9,"diamonds"),
                (9,"spades")])

#10.flush AKQJ9
hands.append([ (12,"spades"),
               (11,"spades"),
               (10,"spades"),
               (9,"spades"),
               (7,"spades")])

#11.flush AKQJ8
hands.append([ (12,"spades"),
               (11,"spades"),
               (10,"spades"),
               (9,"spades"),
               (6,"spades")])

#12.flush KQJ87
hands.append([ (11,"spades"),
               (10,"spades"),
               (9,"spades"),
               (6,"spades"),
               (5,"spades")])

#13.straight AKQJ10
hands.append([ (12,"spades"),
               (11,"spades"),
               (10,"spades"),
               (9,"spades"),
               (8,"hearts")])

#14.straight AKQJ10
hands.append([ (12,"hearts"),
               (11,"hearts"),
               (10,"hearts"),
               (9,"hearts"),
               (8,"spades")])

#15.straight QJ1098
hands.append([ (10,"spades"),
                (9,"spades"),
                (8,"spades"),
                (7,"spades"),
                (6,"hearts")])

#16.threes AAAKQ
hands.append([ (12,"spades"),
                (12,"hearts"),
                (12,"clubs"),
                (11,"diamonds"),
                (10,"spades")])

#17.threes AAAK9
hands.append([ (12,"spades"),
                (12,"hearts"),
                (12,"clubs"),
                (11,"diamonds"),
                (7,"spades")])

#18.threes AAAQ9
hands.append([ (12,"spades"),
                (12,"hearts"),
                (12,"clubs"),
                (10,"diamonds"),
                (7,"spades")])

#19.threes KKKQ9
hands.append([ (11,"spades"),
                (11,"hearts"),
                (11,"clubs"),
                (10,"diamonds"),
                (7,"spades")])

#20.two pairs AAKKQ
hands.append([ (12,"spades"),
                (12,"hearts"),
                (11,"clubs"),
                (11,"diamonds"),
                (10,"spades")])

#21.two pairs AAKKJ
hands.append([ (12,"spades"),
                (12,"hearts"),
                (11,"clubs"),
                (11,"diamonds"),
                (9,"spades")])

#22.two pairs AAQQJ
hands.append([ (12,"spades"),
                (12,"hearts"),
                (10,"clubs"),
                (10,"diamonds"),
                (9,"spades")])

#23.two pairs KKQQj
hands.append([ (11,"spades"),
                (11,"hearts"),
                (10,"clubs"),
                (10,"diamonds"),
                (9,"spades")])

#24.pair AAKQJ
hands.append([ (12,"spades"),
                (12,"hearts"),
                (11,"clubs"),
                (10,"diamonds"),
                (9,"spades")])

#25.pair AAKQ10
hands.append([ (12,"spades"),
                (12,"hearts"),
                (11,"clubs"),
                (10,"diamonds"),
                (8,"spades")])

#26.pair AAKJ10
hands.append([ (12,"spades"),
                (12,"hearts"),
                (11,"clubs"),
                (9,"diamonds"),
                (8,"spades")])

#27.pair AAQJ10
hands.append([ (12,"spades"),
                (12,"hearts"),
                (10,"clubs"),
                (9,"diamonds"),
                (8,"spades")])

#28.pair KKQJ10
hands.append([ (11,"spades"),
                (11,"hearts"),
                (10,"clubs"),
                (9,"diamonds"),
                (8,"spades")])

#29.nothing AKQJ9
hands.append([ (12,"spades"),
                (11,"hearts"),
                (10,"clubs"),
                (9,"diamonds"),
                (7,"spades")])

#30.nothing AKQ109
hands.append([ (12,"spades"),
                (11,"hearts"),
                (10,"clubs"),
                (8,"diamonds"),
                (7,"spades")])

#31.nothing AKJ109
hands.append([ (12,"spades"),
                (11,"hearts"),
                (9,"clubs"),
                (8,"diamonds"),
                (7,"spades")])

#32.nothing AQJ109
hands.append([ (12,"spades"),
                (10,"hearts"),
                (9,"clubs"),
                (8,"diamonds"),
                (7,"spades")])

#33.nothing KQJ98
hands.append([ (11,"spades"),
                (10,"hearts"),
                (9,"clubs"),
                (7,"diamonds"),
                (6,"spades")])

strength_test = True
for i in range(len(hands)):
    if pe.compare_strength(tuples_to_string(hands[i]),tuples_to_string(hands[i]))!=0:
        strength_test = False
        break
for i in range(len(hands)-1):
    for j in range(i+1,len(hands)):
        #print()
        if pe.compare_strength(tuples_to_string(hands[i]),tuples_to_string(hands[j]))!=1:
            strength_test = False
            break

if strength_test == True:
    print("compare strength passed")
else:
    print("compare strength test failed")

''' deprecated because uses old representation
histories = []
histories.append("c3")
histories.append("c3b3")
histories.append("c3b3a2")
histories.append("c3b3a292")
histories.append("c3b3a292ff")
histories.append("c3b3a292bbbb")
histories.append("c3b3a292cc")
histories.append("c3b3a292cc11")
histories.append("c3b3a292cc1122")
histories.append("c3b3a292cc112233")
histories.append("c3b3a292cc112233bb")
histories.append("c3b3a292bbcc112233bbff")
for i in histories:
    print(i+" parsed as ")
    tmp = pe.parse_history(i)
    print("h1:"+tmp[0]+" h2:"+tmp[1]+" preflop:"+tmp[2]+" flop:"+tmp[3])

utilities = []
utilities.append("c3b3a292bbff")
utilities.append("c3b3a292ff")
utilities.append("c3b3a292bbcc112233bbff")
utilities.append("c3b3a292bbbbcc112233bbcc")
utilities.append("c3b3a292"+"b"*16+"112233ff")
utilities.append("c3b3a292"+"b"*16+"112233"+"b"*16)

for i in utilities:
    print("utility of history "+i+" is")
    print(pe.utility(i))
'''
