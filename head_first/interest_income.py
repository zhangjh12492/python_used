def get_income(capital, years=[], rate=0.03):
    for i in years:
        capital += (capital * rate + capital)
        print(capital)


# get_income(10000, range(0, 25), 0.04)


def get_purchase_income1(capital, years=[], rate=0.0325):
    interest = 0
    for i in years:
        interest += capital * rate
        print(interest)


# 利息计算
def get_purchase_income_2(capital, incr, len, rate=0.05):
    years = range(0, len)
    total_interest = 0
    for i in years:
        interest = capital * rate
        total_interest += interest
        capital = capital - incr + interest
        print(int(total_interest), int(interest), int(capital))


# get_purchase_income1(370000, range(15))

def get_purchage_income_by_discount(capital, discount, month_deduct):
    year_deduce = month_deduct * 12
    # 10年
    print("10年，" + str(discount) + "成")
    get_purchase_income_2(capital, year_deduce, 10)
    print('\n\n')
    # 15年
    print("15年，" + str(discount) + "成")
    get_purchase_income_2(capital, year_deduce, 15)
    print('\n\n')
    # 20年
    print("20年，" + str(discount) + "成")
    get_purchase_income_2(capital, year_deduce, 20)
    print("\n\n")
    # 25年
    print("25年，" + str(discount) + "成")
    get_purchase_income_2(capital, year_deduce, 25)
    print('\n\n')
    # 30年
    print("30年，" + str(discount) + "成")
    get_purchase_income_2(capital, year_deduce, 30)
    print('\n\n')


get_purchage_income_by_discount(666000, 1, 2898)

