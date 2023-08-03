import keyboard

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
                counter = 0

            if keyboard.is_pressed('x'):
                stopper = True
                print("Loop stopped")
                return

                
def calculate_bets(rx):
    for bets_on in partitions(rx+1, 7):
        a, b, c, d, e, f, g = bets_on
        win_values = win_math(a, b, c, d, e, f, g)
        risk_values = risk_math(a, b, c, d, e, f, g)
        combined_math(win_values, risk_values)

def win_math(a, b, c, d, e, f, g):
    win_Number = a * 36
    win_Split = b * 18
    win_Basket = c * 12
    win_Corner = d * 9
    win_SixLine = e * 6
    win_Third = f * 3
    win_Half = g * 2

    possible_win = win_Number + win_Split + win_Basket + win_Corner + win_SixLine + win_Third + win_Half

    return [possible_win, win_Number, win_Split, win_Basket, win_Corner, win_SixLine, win_Third, win_Half]

def risk_math(a, b, c, d, e, f, g):
    risk_Number = (1 / 37) * a if a != 0 else 1
    risk_Split = (2 / 37) * b if b != 0 else 1
    risk_Basket = (3 / 37) * c if c != 0 else 1
    risk_Corner = (4 / 37) * d if d != 0 else 1
    risk_SixLine = (6 / 37) * e if e != 0 else 1
    risk_Third = (12 / 37) * f if f != 0 else 1
    risk_Half = (18 / 37) * g if g != 0 else 1

    possible_risk = risk_Number * risk_Split * risk_Basket * risk_Corner * risk_SixLine * risk_Third * risk_Half

    return [possible_risk, risk_Number, risk_Split, risk_Basket, risk_Corner, risk_SixLine, risk_Third, risk_Half]

def combined_math(win_values, risk_values):
    rr1 = win_values[0]
    rr2 = risk_values[0]
    risk_ratio = rr1 / rr2
    print(risk_ratio)

if __name__ == "__main__":
    main()

# wetteinsatz verändern und bis zu 10 runden spielen
#möglichen gewinn und wahrscheinlichkeit berechnen, die kombination aus höchst möglichem gewinn zu höchster wahrscheinlichkeit gewinnt