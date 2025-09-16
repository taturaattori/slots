from slotmachine import SlotMachine

slot1 = SlotMachine(3, {"777": 100, "111": 2, "222": 5, "333": 10, "444": 20, "555": 40, "666": 50, "888": 75, "999": 80})
print(slot1.simulation(100000, 20000, 2))