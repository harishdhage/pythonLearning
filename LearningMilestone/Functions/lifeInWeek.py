def life_in_weeks(age):
    total_week=4692
    burnt_week=age*52
    remaning_week = 4692 - (age*52)
    print(f"You have {remaning_week} left.")

life_in_weeks(int(input("Enter your age : ")))


def calculate_love_score(name1, name2):
    total_name = name1 + name2
    lower_names = total_name.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


calculate_love_score("harIsh", "pooja")