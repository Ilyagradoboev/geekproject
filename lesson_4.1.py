import sys

def money(hours, rate, bonus):
    return hours * rate + bonus

hours = int(sys.argv[1])
rate = int(sys.argv[2])
bonus = int(sys.argv[3])

payment = money(hours, rate, bonus)

print(f'Заработная плата равна: {payment}')