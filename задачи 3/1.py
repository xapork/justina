def determine_winner(player1, player2):
    if player1 == player2:
        return 0  
    elif (player1 == 'R' and player2 == 'S') or (player1 == 'S' and player2 == 'P') or (player1 == 'P' and player2 == 'R'):
        return 1 
    else:
        return 2  

player1 = input("Игрок 1 выбирает (R - камень, S - ножницы, P - бумага): ")
player2 = input("Игрок 2 выбирает (R - камень, S - ножницы, P - бумага): ")

result = determine_winner(player1, player2)

if result == 0:
    print("Ничья!")
elif result == 1:
    print("Игрок 1 побеждает!")
else:
    print("Игрок 2 побеждает!")