import keyboard

def generate_table(header_labels):
    header = "|"
    for label in header_labels:
        header += f" {label} |"
    print("-" * len(header))
    print(header)
    print("-" * len(header))


def add_row(data):
    row_data = "|"
    for value in data:
        row_data += f" {value} |"
    print("-" * len(row_data))
    print(row_data)
    print("-" * len(row_data))


header_labels = ["Durchlauf", "Runde", "Einsatz", "Number", "Split", "Basket", "Corner", "SixLine", "Third", "Half", "Possible Win", "Probability", "Risk-Ratio"]
generate_table(header_labels)

def partitions(n, k):
    if k == 1:
        yield (n,)
    else:
        for i in range(n + 1):
            for result in partitions(n - i, k - 1):
                yield (i,) + result

def main():
    stopper = False
    counter = 0
    durchlauf = 1

    while not stopper:
        for rounds in partitions(31, 7): #Verteilt 30€ Einsatz auf 7 Runden
            counter = counter +1
            r1, r2, r3, r4, r5, r6, r7 = rounds
            if counter == 1:
                rx = r1
                calculate_bets(rx) #Der geplante Einsatz für Runde x wird auf die verschiedenen Wettmöglichkeiten aufgeteilt
            if counter == 2:
                rx = r2
                calculate_bets(rx)
            if counter == 3:
                rx = r3
                calculate_bets(rx)
            if counter == 4:
                rx = r4
                calculate_bets(rx)
            if counter == 5:
                rx = r5
                calculate_bets(rx)
            if counter == 6:
                rx = r6
                calculate_bets(rx)
            if counter == 7:
                rx = r7
                calculate_bets(rx)

            if counter == 8:
                #sum_math()
                counter = 0
                durchlauf = durchlauf + 1

            if keyboard.is_pressed('x'):
                stopper = True
                print("Loop stopped")
                return

            possible_win = win_math(calculate_bets(rx))
            possible_risk = risk_math(calculate_bets(rx))
            risk_ratio = combined_math()

            a = calculate_bets[0]
            b = calculate_bets[1]
            c = calculate_bets[2]
            d = calculate_bets[3]
            e = calculate_bets[4]
            f = calculate_bets[5]
            g = calculate_bets[6]

            row_values = [durchlauf, counter, rx, a, b, c, d, e, f, g, possible_win, possible_risk, risk_ratio]
            add_row(row_values)

                
def calculate_bets(rx):
    for bets_on in partitions(rx+1, 7):
        a, b, c, d, e, f, g = bets_on
        win_math(a, b, c, d, e, f, g)
        risk_math(a, b, c, d, e, f, g)
        #combined_math(win_values, risk_values)
        return a, b, c, d, e, f, g

def win_math(a, b, c, d, e, f, g):
    win_Number = a * 36
    win_Split = b * 18
    win_Basket = c * 12
    win_Corner = d * 9
    win_SixLine = e * 6
    win_Third = f * 3
    win_Half = g * 2

    possible_win = win_Number + win_Split + win_Basket + win_Corner + win_SixLine + win_Third + win_Half

    return possible_win

def risk_math(a, b, c, d, e, f, g):
    risk_Number = (1 / 37) * a if a != 0 else 1
    risk_Split = (2 / 37) * b if b != 0 else 1
    risk_Basket = (3 / 37) * c if c != 0 else 1
    risk_Corner = (4 / 37) * d if d != 0 else 1
    risk_SixLine = (6 / 37) * e if e != 0 else 1
    risk_Third = (12 / 37) * f if f != 0 else 1
    risk_Half = (18 / 37) * g if g != 0 else 1

    possible_risk = risk_Number * risk_Split * risk_Basket * risk_Corner * risk_SixLine * risk_Third * risk_Half

    return possible_risk

def combined_math():
    rr1 = win_math()
    rr2 = risk_math()
    risk_ratio = rr1 / rr2
    return risk_ratio

if __name__ == "__main__":
    main()

# wetteinsatz verändern und bis zu 10 runden spielen
#möglichen gewinn und wahrscheinlichkeit berechnen, die kombination aus höchst möglichem gewinn zu höchster wahrscheinlichkeit gewinnt