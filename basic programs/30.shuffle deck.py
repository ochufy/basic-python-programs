import random, itertools
cards=list(itertools.product(range(1,14),["spade","club","heart","diamond"]))
random.shuffle(cards)
print("Your card:")
print(cards[0][0],"of",cards[0][1])
