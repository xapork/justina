def is_over_21(card_values):
    return sum(card_values) > 21
card_str = input("введи достоинства карт через пробел: ")
cards = [int(card) for card in card_str.split()]
result = is_over_21(cards)
print(result)