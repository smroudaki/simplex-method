"""
Equation Format:
Main Profit(MP): Z = 7X + 5Y
St1:    2X + 1Y <= 100
St2:    4X + 3Y <= 240
        stop
=======================
Cj = coefficient in profit for each variable
Zj = sum of basis variables * non basis variables in each St
Cj - Zj = profit per unit (PPU)
this is called optimal profit testing
-----------------------
we put the highest profit(PPU) as a basis variable to effect the Main Profit(MP) that we are optimizing for.

when the problem is maximisation, and we get positive results in PPU; and if it is minimization and we get negative results in PPU,
then it means we need to calculate one or more steps to reach the optimal optimization
=======================
initial feasible solution:
X0, X1, ... = 0 then Slack variables will be counted
=======================
RHS should not be negative
=======================
Minimum Test: to find the pivot row, by dividing RHS to the Positive! pivot column variables

"""


def main():
    # profit = get_input()
    main_equality = get_input()
    print("\nMain Equality: ", main_equality)
    cos = coefficients(main_equality)
    print("cos: ", cos)
    cos_slk = standard_form(cos)
    cos = cos_slk[0]
    slk = cos_slk[1]
    print("cos: ", cos)
    print("slk: ", slk)
    count_zj(cos)
    get_answer(cos)


def get_profit():
    return input("Enter maximisation: ")


def get_input():
    inequality = []

    maximisation = input("Enter maximisation: ")
    inequality.append(maximisation)

    while True:
        user_input = input("Enter inequality or enter 'stop' to stop adding: ")
        if user_input == "stop":
            break
        inequality.append(user_input)
    return inequality


def coefficients(equ):
    parts = [0, 0, 0]
    cos = [0, 0, 0]
    co_x = co_y = rhs = 0

    for j in range(len(equ)):
        parts[j] = equ[j].split(' ')

    print(parts)

    for j in range(len(parts)):
        for i in range(len(parts[j])):
            if (parts[j][i] != 'Z'
                    and parts[j][i] != '='
                    and parts[j][i] != '+'
                    and parts[j][i] != '<='
                    and parts[j][i] != '>='):

                if 'X' in parts[j][i]:
                    co_x = int(parts[j][i].split('X')[0])
                elif 'Y' in parts[j][i]:
                    co_y = int(parts[j][i].split('Y')[0])
                else:
                    rhs = int(parts[j][i])

        cos[j] = [co_x, co_y, rhs]

    return cos


def standard_form(equ):
    slacks_length = len(equ)
    solution = []

    for i in range(slacks_length - 1):
        equ[0].insert(-1, 0)

    for i in range(1, slacks_length):
        solution.append([])
        for j in range(1, slacks_length):
            if i == j:
                equ[i].insert(-1, 1)
                solution[i - 1].append(1)
            else:
                equ[i].insert(-1, 0)
                solution[i - 1].append(0)
    # print(solution)

    return equ, solution


def count_zj(equ):
    solution = 0


def get_answer(equ):
    print("answer")


main()
# Cos = Coefficients
# in = inequality
# maxCos = coefficients(maximisation)
# inCos = []
# for i in range(len(inequality)):
#     inCos.append(coefficients(inequality[i]))
#
# print("Max Coefficients: " + str(maxCos))
# print("Inequality1 Coefficients: " + str(inCos[0]))
# print("Inequality2 Coefficients: " + str(inCos[1]))
#
# # STF = Standard Form # Needs lots of work
# inCos[0].insert(-1, 1)
# inCos[0].insert(-1, 0)
# inCos[1].insert(-1, 0)
# inCos[1].insert(-1, 1)
# maxCos.insert(len(maxCos), 0)
# maxCos.insert(len(maxCos), 0)
#
# slackVariablesLength = len(inCos)
# for i in range(slackVariablesLength):
#     for j in range(slackVariablesLength):
#         inCos[i].insert(-1, 1) if i == j else inCos[i].insert(-1, 0)
#     maxCos.append(0)
#     print(inCos[i])
#
# print(inCos[0])
# print(inCos[1])
# print(maxCos)
# maxMCos = max(maxCos)
# pivotCol = maxCos.index(maxMCos)
# print("Pivot Column = " + str(pivotCol))
#
# if inCos[0][-1] / inCos[0][pivotCol] <= inCos[1][-1] / inCos[1][pivotCol]:
#     pivotRow = 0
# else:
#     pivotRow = 1
# print("Pivot Row = " + str(pivotRow))
#
# pivotNum = inCos[pivotRow][pivotCol]
# for i in range(len(inCos[0])):
#     inCos[pivotRow][i] /= pivotNum
# pivotNum /= pivotNum
#
# print("Pivot Number = " + str(pivotNum))
# print(inCos)
# if (inCos[pivotRow] == 1):
#     print('true')
#
# CosPivotCol = []
# for i in range(len(inCos)):
#     if (i != pivotRow):
#         CosPivotCol[i] = inCos[i][pivotCol]
#     else:
#         CosPivotCol[i] = 0
#
# inCos[pivotRow][pivotCol]
# for i in range(len(inCos)):
#     for j in range(len(inCos[0])):
#         if (inCos[i][j] == inCos[pivotRow][pivotCol]):
#             break
#         inCos[i][j] = pivotNum
