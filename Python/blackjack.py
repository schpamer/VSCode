#card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

# def score_hand(hand):
#     print(hand)
#     sum = 0

#     non_aces = [c for c in hand if c != 'A']
#     aces = [c for c in hand if c == 'A']

    
#     for card in non_aces:
#         if card in 'JQK':
#             sum += 10
#         else:
#             sum += int(card)

#     for card in aces:
#         #print(len(aces))
#         if sum <= 10 and (len(aces) != 3) or (len(aces) == 1) or (len(aces) != 2):
#             sum += 11
#         else:
#             sum += 1
#     return sum


def score_hand(hand):
    #print(hand)
    sum = 0

    non_aces = [c for c in hand if c != 'A']
    aces = [c for c in hand if c == 'A']

    if len(aces) == 1 and non_aces[0] == 'J':
            sum = 21
            return sum

    else:
    
        for card in non_aces:
            if card in 'JQK':
                sum += 10
            else:
                sum += int(card)

        for card in aces:
            #print(len(aces))
            if sum < 10:
                sum += 11
            else:
                sum += 1
    return sum
#if sum <= 10 and (len(aces) != 0):
   


p = score_hand(['A', 'A', 'A', 'A'])     #works <=4 works <10 and <=4
print(p)
p = score_hand(['A', '2', 'A', '3', 'A']) #works <=4 <10
print(p)
p = score_hand(['A', 'A'])                #works <=4 works <10 and <=4
print(p)
p = score_hand(['A', 'A', 'A', 'J'])    #fails <=4, works <10 <=4
print(p)
p = score_hand(['J', 'A'])  #works <=10 <=4
print(p)
p = score_hand(['A', 'J'])
print(p)


    # for card in hand:
	#     if card == "J" or card == "Q" or card == "K":
	#         total+= 10
	#     elif card == "A":
	#         if total >= 11: total+= 1
	#         else: total+= 11
    # else:
    #     total += int(card)
    # return total

# def hand_total(hand):
#     print(hand)
#     total = 0
#     ace_found = False
#     soft = False

#     for card in hand:
#         if card.value >= 10:
#             total += 10
#         else:
#             total += card.value

#         if card.value == 1:
#             ace_found = True;

#     if total < 12 and ace_found:
#         total += 10
#         soft = True

#     return print(total, soft)