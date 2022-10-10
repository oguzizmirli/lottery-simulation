# DATE: 15/12/20
# LOTTERY SIMULATION

import random
broughtForward = 0
weeklyRevenue = 0
dropBox = 0
# prizePercentage = [0, 0, 0.05, 0.1, 0.2, 0.25, 0.4]
print()
print("Starting Lottery Simulation")
print("Please wait...")
print()


# TASK 1
def draw():
    lucky_numbers = random.sample(range(1, 50), 6)
    return lucky_numbers


# TASK 2
def play_week():
    global broughtForward, weeklyRevenue, dropBox
    people = []
    for a in range(0, 7):
        a = random.randint(10000, 1000000)
        people.append(a)
    print("Daily people in a week :", people)

    totalpeople = sum(people)                                                   # CALCULATINGS
    weeklyRevenue = totalpeople * 3
    print(f"Weekly revenue: ", f"{weeklyRevenue:.2f} liras.")
    dropBox += weeklyRevenue * (45 / 100)
    weeklyRevenue = weeklyRevenue * (55 / 100)

    played_tickets = []
    for i in range(totalpeople):
        n = random.sample(range(1, 50), 6)
        played_tickets.append(n)
    print("Number of tickets: ", len(played_tickets))
    # print(f"DropBox: ", f"{dropBox:.2f} liras.")                              # PRINTS DROPBOX
    print(f"Total Prize: ", f"{weeklyRevenue:.2f} liras.")
    decide_winners(played_tickets)


# TASK 3
def decide_winners(played_tickets):
    global dropBox, broughtForward
    lucky_nums = draw()
    right_guesses = [0, 0, 0, 0, 0, 0, 0]

    for i in played_tickets:
        match = len(set(i) & set(lucky_nums))
        if match != 0:
            right_guesses[match - 1] += 1
    print("WINNING NUMBERS: ", lucky_nums)
    newlist1 = [f"{weeklyRevenue * 0.05 / x:.2f}" for x in right_guesses[2:3]]  # newlist 1: People knew 2 out of 6
    newlist2 = [f"{weeklyRevenue * 0.1 / x:,.2f}" for x in right_guesses[3:4]]  # newlist 2: People knew 3 out of 6
    newlist3 = [f"{weeklyRevenue * 0.2 / x:,.2f}" for x in right_guesses[4:5]]  # newlist 3: People knew 4 out of 6

# TASK 4
    # print("Number of right guesses 0 to 6: ", right_guesses)  # THIS PRINTS RIGHT_GUESSES AS A LIST
    print(right_guesses[0:1], "people knew 0 out of 6 earned 0 liras.")
    print(right_guesses[1:2], "people knew 1 out of 6 earned 0 liras.")
    print(right_guesses[2:3], "people knew 2 out of 6 earned", newlist1, "liras.")
    print(right_guesses[3:4], "people knew 3 out of 6 earned", newlist2, "liras.")
    print(right_guesses[4:5], "people knew 4 out of 6 earned", newlist3, "liras.")

    for i in right_guesses[5:6]:
        if i == 0:
            dropBox += dropBox + (weeklyRevenue * 0.35)
            print("Nobody knew 5 out of 6.")

        else:
            newlist4 = [f"{weeklyRevenue * 0.25 / x:,.2f}" for x in right_guesses[5:6]]
            print(right_guesses[5:6], "people knew 5 out of 6 earned", newlist4, "liras.")
    for i in right_guesses[6:7]:
        if i == 0:
            broughtForward += weeklyRevenue - (weeklyRevenue * 0.6)
            print(f"Nobody knew 6 out of 6 and the prize that will be forwarded to next week is",
                  f"{broughtForward:,.2f} ,liras.")
        else:
            print(right_guesses[6:7], "people knew 6 out of 6 earned", f"{broughtForward:,.2f}", "liras.")
            broughtForward = 0


# TASK 5
def play_year():
    global broughtForward
    month = 1
    week = 1
    while month <= 12:
        print("MONTH: ", month)
        print("WEEK: ", week)
        draw()
        play_week()
        print()
        week += 1
        if week == 5:
            week -= 4
            month += 1
        if month == 13:
            broughtForward += weeklyRevenue - (weeklyRevenue * 0.6)
            print("END OF THE YEAR")


play_year()
# MADE BY OGUZ IZMIRLI
