# File: src/analyzer.py

def analyze_trades(trades_list):
    """
    Обрабатывает список сделок и возвращает словарь с результатами.
    """
    portfolio = {}
    last_prices = {}

    for trade in trades_list:
        ticker, operation, quantity, price = trade

        if ticker not in portfolio:
            portfolio[ticker] = {
                'position': 0,
                'cost_basis': 0.0,
                'realized_pnl': 0.0
            }
        last_prices[ticker] = price

        if operation == 'BUY':
            portfolio[ticker]['position'] += quantity
            portfolio[ticker]['cost_basis'] += quantity * price
        elif operation == 'SELL':
            if portfolio[ticker]['position'] >= quantity:
                average_price = portfolio[ticker]['cost_basis'] / portfolio[ticker]['position']
                profit = (price - average_price) * quantity
                portfolio[ticker]['realized_pnl'] += profit
                portfolio[ticker]['position'] -= quantity
                portfolio[ticker]['cost_basis'] -= average_price * quantity
            else:
                print(f"ВНИМАНИЕ: Попытка продать больше акций {ticker}, чем есть в наличии. Сделка пропущена.")
    return portfolio, last_prices

def generate_report(portfolio, last_prices):
    """
    Принимает обработанные данные и выводит отчёт.
    """
    print("--- ОТЧЁТ ПО ТОРГОВЫМ ОПЕРАЦИЯМ ---\n")
    total_pnl = 0.0
    total_portfolio_value = 0.0
    best_ticker = None
    worst_ticker = None
    max_pnl = float('-inf')
    min_pnl = float('inf')

    print("Результаты по акциям:")
    for ticker, data in portfolio.items():
        pnl = data['realized_pnl']
        total_pnl += pnl
        position = data['position']
        if pnl > max_pnl:
            max_pnl = pnl
            best_ticker = ticker
        if pnl < min_pnl:
            min_pnl = pnl
            worst_ticker = ticker
        print(f"  {ticker}: Позиция: {position} шт., Реализованный P&L: {pnl:.2f} руб.")

    print(f"\nОбщий реализованный P&L по портфелю: {total_pnl:.2f} руб.")
    if best_ticker:
        print(f"Самая прибыльная позиция: {best_ticker} ({max_pnl:.2f} руб.)")
    if worst_ticker:
        print(f"Самая убыточная позиция: {worst_ticker} ({min_pnl:.2f} руб.)")

    print("\n--- Текущая стоимость портфеля ---")
    for ticker, data in portfolio.items():
        position = data['position']
        if position > 0 and ticker in last_prices:
            current_price = last_prices[ticker]
            value = position * current_price
            total_portfolio_value += value
            print(f"  {ticker}: {position} шт. * {current_price} руб. = {value:.2f} руб.")
    print(f"Общая стоимость портфеля: {total_portfolio_value:.2f} руб.")
