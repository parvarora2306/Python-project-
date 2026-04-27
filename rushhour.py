import os
import random
import time

money = 100
GRID = 17
MID = GRID // 2


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def read_int(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Enter a number >= {minimum}")
                continue
            if maximum is not None and value > maximum:
                print(f"Enter a number <= {maximum}")
                continue
            return value
        except ValueError:
            print("Enter a valid number")


def generate_lane_counts():
    return {
        "North": random.randint(0, 5),
        "South": random.randint(0, 5),
        "East": random.randint(0, 5),
        "West": random.randint(0, 5),
    }


def build_cars(lane_counts):
    cars = []

    for i in range(lane_counts["North"]):
        cars.append({"r": -1 - (i * 2), "c": MID, "dr": 1, "dc": 0, "sym": "↓"})

    for i in range(lane_counts["South"]):
        cars.append({"r": GRID + (i * 2), "c": MID, "dr": -1, "dc": 0, "sym": "↑"})

    for i in range(lane_counts["West"]):
        cars.append({"r": MID, "c": -1 - (i * 2), "dr": 0, "dc": 1, "sym": "→"})

    for i in range(lane_counts["East"]):
        cars.append({"r": MID, "c": GRID + (i * 2), "dr": 0, "dc": -1, "sym": "←"})

    return cars


def render(cars, tick, lane_counts, total):
    grid = [[" " for _ in range(GRID)] for _ in range(GRID)]

    for i in range(GRID):
        grid[MID][i] = "─"
        grid[i][MID] = "│"
    grid[MID][MID] = "┼"

    for car in cars:
        r, c = car["r"], car["c"]
        if 0 <= r < GRID and 0 <= c < GRID:
            grid[r][c] = car["sym"]

    clear_screen()
    print(f"Rush Hour Bet Game")
    print(f"Balance: {money}")
    print(f"Tick: {tick}")
    print(f"Traffic total: {total}")
    print(f"North: {lane_counts['North']}  South: {lane_counts['South']}  East: {lane_counts['East']}  West: {lane_counts['West']}")
    print()

    for row in grid:
        print("".join(row))


def simulate_round(lane_counts, total):
    cars = build_cars(lane_counts)

    for tick in range(1, 19):
        render(cars, tick, lane_counts, total)
        time.sleep(0.25)

        for car in cars:
            car["r"] += car["dr"]
            car["c"] += car["dc"]

    render(cars, 19, lane_counts, total)
    time.sleep(0.4)


def resolve_bet(mode, line_low, line_high, total):
    if mode == "over":
        return total > line_low
    if mode == "under":
        return total < line_low
    if mode == "range":
        return line_low <= total <= line_high
    return False


print("Rush Hour Text Game Started")

while money > 0:
    print(f"\nBalance: {money}")
    bet = read_int("Enter bet amount: ", 1)
    if bet > money:
        print("Not enough balance")
        continue

    mode = input("Choose mode (over / under / range): ").strip().lower()

    if mode not in {"over", "under", "range"}:
        print("Invalid mode")
        continue

    if mode in {"over", "under"}:
        line = read_int("Enter the line number: ", 0)
        low = line
        high = line
    else:
        low = read_int("Enter range low: ", 0)
        high = read_int("Enter range high: ", low)

    lane_counts = generate_lane_counts()
    total = sum(lane_counts.values())

    print("\nSimulating traffic...")
    time.sleep(1)
    simulate_round(lane_counts, total)

    win = resolve_bet(mode, low, high, total)

    if win:
        if mode == "range":
            profit = bet * 2
            money += profit
            print(f"\nYou won! Total traffic was {total}. Payout: +{profit}")
        else:
            profit = bet
            money += profit
            print(f"\nYou won! Total traffic was {total}. Payout: +{profit}")
    else:
        money -= bet
        print(f"\nYou lost! Total traffic was {total}. Loss: -{bet}")

    print(f"New balance: {money}")

    again = input("\nPlay again? (y/n): ").strip().lower()
    if again != "y":
        break

print(f"\nGame over. Final balance: {money}")
