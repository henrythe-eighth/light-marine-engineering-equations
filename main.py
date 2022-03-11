#!/usr/local/bin/python3.9
import math

global top_speed_const
top_speed_const = 1.944

global pi
pi = 3.1415

global gravity
gravity = 9.81

global theoretical_hull_speed_constant
theoretical_hull_speed_constant = 1.34

global knots
knots = "knots"

global lbs
lbs = "pounds (lbs)"

global hp
hp = "horsepower"

global tons
tons = "tons"

global init_str
init_str = "LME3 EQUATIONS SCRIPT MADE BY HENRY KORTELING OF FALMOUTH MARINE SCHOOL, ALL RIGHTS RESERVED 2022."

global issue_tracker
issue_tracker = "ANY ISSUES: SUBMIT AN ISSUE ON MY GITHUB @KRONOS3258"

# FUNCTIONS FOR BASIC CONVERSIONS AND MATHEMATICS

def square_number(num):
    num = num
    ans = num ** 2
    return (ans)


def sqrt(num):
    num = num
    ans = math.sqrt(num)
    return (ans)


def knotstokmph(knots):
    knots = knots
    kmph = knots * 1.852
    return (kmph)


def lbs_to_tons(lbs):
    lbs = lbs
    ans = lbs * 0.00045359
    return ans


# FUNCTIONS OF LME3 EQUATIONS


def horsepower(speed_in_knots, lwl_length, displacement_in_tons):
    speed_in_knots = speed_in_knots
    speed_in_kmph = knotstokmph(speed_in_knots)
    lwl_length = lwl_length
    displacement_in_tons = displacement_in_tons
    sqrt_of_lwl = sqrt(lwl_length)
    coefficent_of_effective_horsepower = sqrt_of_lwl / speed_in_kmph
    minimum_required_hp = coefficent_of_effective_horsepower * displacement_in_tons
    print(str(minimum_required_hp) + " " + str(hp))
    return minimum_required_hp


def pull_hydraulics(bore_diameter, rod_diameter, psi_def):
    bore_diameter = bore_diameter
    bore_diameter_squared = square_number(bore_diameter)
    rod_diameter = rod_diameter
    rod_diameter_squared = rod_diameter * rod_diameter
    bore_minus_rod = bore_diameter_squared - rod_diameter_squared
    psi_def = psi_def
    y = psi_def * pi * bore_minus_rod
    answer = y / 4
    print(str(answer) + " " + str(lbs))
    return answer


def push_hydraulics(bore_diameter, psi_def):
    bore_diameter = bore_diameter
    bore_diameter_squared = square_number(bore_diameter)
    psi_def = psi_def
    y = psi_def * pi * bore_diameter_squared
    answer = y / 4
    print(str(answer) + " " + str(lbs))
    return answer


def theo_hull_spd(lwl):
    lwl = lwl
    sqrt_of_lwl = sqrt(lwl)
    answer = theoretical_hull_speed_constant * sqrt_of_lwl
    print(str(answer) + " " + str(knots))
    return answer


def top_speed(lwl):
    lwl_length = lwl
    a = lwl_length * gravity
    b = 2 * pi
    c = a / b
    d = sqrt(c)
    answer = d * top_speed_const
    print(str(answer) + " " + str(knots))
    return answer


def displacement(lwl, beam):
    lwl = lwl
    beam = beam
    lwl_minus_beam = lwl - beam
    const_a = 94
    half_beam = beam / 2
    answer = lwl_minus_beam * half_beam / const_a
    print(str(answer) + " " + str(tons))
    return answer


print(init_str)
print(issue_tracker)

functions = ["Horsepower", "Pull Hydraulics", "Push Hydraulics", "Theoretical Hull Speed", "Top Speed", "Displacement"]

print("Functions:" + " " + str(functions))

print("Please write the function as it appears in the list above, otherwise the script will fail!")

choice = str(input("Which function do you want to use?" + " "))

if choice == "Horsepower":
    print("This equation tells you how much horsepower your engine has based on your top speed and boat weight and length")
    speed_in_knots = float(input("Speed in knots?" + " "))
    lwl_length = float(input("What is the waterline length?" + " "))
    displacement_in_tons = float(input("What is the displacement in tons?" + " "))
    horsepower(speed_in_knots, lwl_length, displacement_in_tons)
elif choice == "Pull Hydraulics":
    bore_diameter = float(input("What is the bore diameter?" + " "))
    rod_diameter = float(input("What is the internal diameter of the rod?" + " "))
    psi_def = float(input("What is the PSI?" + " "))
    pull_hydraulics(bore_diameter, rod_diameter, psi_def)
elif choice == "Push Hydraulics":
    bore_diameter = float(input("What is the bore diameter?" + " "))
    psi_def = float(input("What is the PSI?" + " "))
    push_hydraulics(bore_diameter, psi_def)
elif choice == "Theoretical Hull Speed":
    lwl = float(input("What is the waterline length?" + " "))
    theo_hull_spd(lwl)
elif choice == "Top Speed":
    lwl = float(input("What is the waterline length?" + " "))
    top_speed(lwl)
elif choice == "Displacement":
    lwl = float(input("What is the waterline length?" + " "))
    beam = float(input("What is the beam of the vessel?" + " "))
    displacement(lwl, beam)
else:
    print("ERROR 404 = FUNCTION NOT FOUND")
