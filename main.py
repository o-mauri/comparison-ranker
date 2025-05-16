import random

K_FACTOR = 50

class comparisonItem:
    name: str
    elo: float

    def __init__(self, name, elo):
        self.name = name
        self.elo = float(elo)


def compare(item1: comparisonItem, item2: comparisonItem):
    print("What is your favourite?")
    print(f"1- {item1.name}")
    print(f"2- {item2.name}")
    result = input("Select: ")
    if not (result == "1" or result == "2"):
        print("")
        print("Please enter a valid choice")
        return compare(item1,item2)
    return result == "1"

def calculateComparison(item1: comparisonItem, item2: comparisonItem):
    win = compare(item1, item2)
    diff = item2.elo - item1.elo
    coeff = (10**(diff/400)) + 1
    expected = 1/coeff
    score = 1 if win else 0
    elo_change = (score - expected) * K_FACTOR
    item1.elo = item1.elo + elo_change
    item2.elo = item2.elo - elo_change


def readData():
    with open("data.txt") as f:
        items = f.readlines()
    all_items = []
    for item in items:
        data = item.split(":::")
        all_items.append(comparisonItem(data[0],data[1]))
    return all_items


def saveData(all_items: comparisonItem):
    all_items = sorted(all_items, key=lambda item: item.elo, reverse=True)
    lines = []
    for item in all_items:
        lines.append(item.name + ":::" + str(item.elo) + "\n")
    with open("data.txt", "w") as f:
        f.writelines(lines)


def singleCycle():
    items = readData()
    chosen = random.sample(items, 2)
    calculateComparison(chosen[0],chosen[1])
    saveData(items)


def endlessCycle():
    ranked = 1
    while True:
        print("Ranked: " + str(ranked))
        singleCycle()
        ranked += 1

endlessCycle()