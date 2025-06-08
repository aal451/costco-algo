from AlgorithmImports import *

class BuyOpenSellProfitableClose(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2023, 11, 1)
        self.SetEndDate(2025, 5, 10)
        self.SetCash(12000)

        # Use the Charles Schwab model to model fees, since this is a brokerage retail investors would use.
        self.set_brokerage_model(BrokerageName.CHARLES_SCHWAB, AccountType.CASH)

        self.symbol = self.AddEquity("COST", Resolution.Minute).Symbol
        self.entry_price = None   # tracks what price we entered our Costco position

      
        self.SetWarmup(TimeSpan.FromMinutes(1))  

        # Set up the rules of the strategy, defined in the README to execute.
        self.Schedule.On(self.DateRules.EveryDay(self.symbol),
                         self.TimeRules.AfterMarketOpen(self.symbol, 5),
                         self.MarketOpen)

        self.Schedule.On(self.DateRules.EveryDay(self.symbol),
                         self.TimeRules.BeforeMarketClose(self.symbol, 5),
                         self.MarketClose)


    def MarketOpen(self):
        # Ensure price data is available
        if not self.Securities[self.symbol].HasData:
            self.Debug("Skipping open trade - no data")
            return

        if not self.Portfolio[self.symbol].Invested:
            self.MarketOrder(self.symbol, 10)
            self.entry_price = self.Securities[self.symbol].Price
            self.Debug(f"BUY at {self.entry_price}")

    def MarketClose(self):
        # Ensure price data is available
        if not self.Securities[self.symbol].HasData:
            self.Debug("Skipping close trade - no data")
            return

        if self.Portfolio[self.symbol].Invested:
            current_price = self.Securities[self.symbol].Price
            if current_price > self.entry_price:
                self.LimitOrder(self.symbol, -10, current_price)
                self.Debug(f"SELL at {current_price}")
