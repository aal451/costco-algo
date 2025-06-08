# Costco Trading Algorithm

This is a stock trading algorithm designed to trade Costco (COST) through the QuantConnect Platform, using the Charles Schwab as the underlying brokerage.

## Inspiration

With the advent of technology platforms such as QuantConnect, it is now possible to trade algorithmically using Python code through brokerage integrations such as Charles Schwab using standard retail trading accounts. 

Along with the explosion in zero-commission trading being generally available to retail traders, this provides an interesting opportunity: 

1. Algorithmic trading allows retail traders to effectively automate their trades, allowing them to ensure portfolio growth without the time demands of active trading.
2. Zero-commission brokerage allows retail to take advantage of extremely small gains, which have the potential to compound into significant portfolio growth.
3. Automatic trading has the potential to reduce "panic trades", which lead to degraded long-term performance.
4. Retail trading is generally done on a smaller scale than institutional trading, which allows retail to take advantage of the smaller opportunities institutions would not normally be able to take advantage of, due to the scale institutional strategies require to be successful.

Therefore, considering these potential advantages, I decided to create an algorithm on QuantConnect to take advantage of all four of the above points, being a retail trader myself.

## Thesis

As I was researching a potential strategy to develop a QuantConnect algorithm on, I decided to model my strategy around the largest advantage that a retail investor has: time. Specifically, as a retail investor does not have to meet quarterly performance requirements, this means the strategy has an advantage, in that it can hold investments for a long as necessary to achieve the outsized returns it was developed to create.

With this in mind, I figured that with the advantage of time, I should choose a strong underlying stock to serve as the basis of my strategy. This was because I believed that:

1. For a successful long strategy, like the one I would try to implement, strong stock appreciation is necessary.
2. A strong underlying stock would provide a good level of assurance that in the event of a misplaced trade (due to unexpected economic events, e.g. recessions), the stock would eventually rebound, so with the advantage of time, the strategy should always come out with positive returns, the overall goal.

After a few weeks of research, I determined that Costco (COST) would be the best stock to serve this purpose for the following reasons:
1. Excellent Financial Fundamentals
    * Exceptional Return on Invested Capital: over 25% since 2022, indicating consistent focus on effectively allocating capital to deliver returns for shareholders.
    * Consistently Increasing Earnings Per Share and Net Income: indicating continued and improving financial success, likely to translate to high-quality returns.
    * Extraordinary Financial resilience: even during times of significant headwinds, such as the COVID-19 pandemic, COST succeeded in increasing profitability year over year.
2. Strong Underlying Business Model
    * Membership Model: the high membership renewal rate (consistently >90%) and consistently increasing membership numbers provides exceptional, stable capital for the company to deploy in service of consistently improving its underlying business, while also reducing the profit margins the company needs to take on its products, allowing it to consistently undercut other retailers price-wise, driving outsized returns.
    * International Success: Costco has proven successful in expanding its highly successful business model abroad, creating strong avenues for future growth likely to drive outsized returns in the future. For example, since 2015, the comparable sales growth of stores abroad has, on average, been ~8%, with average return on invested capital being 17%, indicating resounding success in expansion abroad.
    * Pricing Power: by leveraging the highly successful, in-house, private-label Kirkland Signature Brand, as well as its scale and prestige, Costco has demonstrated extraordinary leverage with suppliers in terms of pricing, allowing it to consistently protect and grow its profits.


With this in mind, I decided to create simple strategy to automatically trade COST.

This strategy consisted of three main ideas:
1. Buy COST 5 minutes after open if there is not an established position already.
    * In this strategy, I traded 10 shares with 12K of capital to realistically simulate the capital a retail investor might have at their disposal.
2. Sell COST 5 minutes before close if there is already an established position.
3. If the price 5 minutes before close is not greater than the price the position was bought at, the position is held until the next day.

My thesis is that this strategy would work, since via the reasons above, there would be good reason to believe that while the value of COST would increase over time, due to strong fundamentals and financials, which would ultimately power the strategy's returns, capturing profit from the normal day-to-day fluctuations of the market would provide opportunities to generate even larger returns. Moreover, the nature of the algorithm, in which the position is never sold at a loss, would provide high certainty to the investor that there would be no loss in capital over time*, making the strategy exceptional for the retail investor, as the loss-aversion of the retail investor on strategies that are profitable, even with occassional losses, might degrade the performance of the algorithm (since the investor may be tempted to intervene).

\* Of course, this strategy cannot guarantee no losses, since there is the possibility the stock may never come back up after a position is entered. However, this idea was also a part of what influenced my strategy development to select Costco. Specifically, I determined that as long as a high-quality enough stock was chosen to trade on, such as Costco, which we could determine via quantitative and fundamental analysis, the probability of this scenario would be extremely low, making this a superior strategy.


With all of this development in mind, I then decided to study the QuantConnect platform, and ultimately, I used my knowledge of Python via my coursework and personal experience to code the strategy for execution on QuantConnect. I also chose to use the Charles Schwab Brokerage model to model the fees associated with trading in QuantConnect. This was because (1) Schwab offers zero-commission trading (which would be necessary, since trading on a day-to-day timeframe with fees would signficantly impact this strategy's returns) and (2) most retail investors would have access to this brokerage, and (3) QuantConnect Schwab integration would allow retail investors to live deploy this strategy, if desired.

## Results

To evaluate this strategy, since I did not have enough capital on my own at the time to execute live, I decided to use QuantConnect's backtesting feature.

If you want to take a look at the results for yourself through official QuantConnect reports hosted on the platform:
For a report with nicer, interactive charts: https://www.quantconnect.cloud/backtest/744b34ce7bab835c69727e7c26a73924/?theme=chrome
For a report with more in-depth statistics (click the "statistics" tab at the top): https://www.quantconnect.com/terminal/cache/embedded_backtest_e0406d06d2b8f01e8abe86a14f4c9b14.html


Results from running the backtest:
<img width="1450" alt="Screenshot 2025-06-08 at 1 08 56 PM" src="https://github.com/user-attachments/assets/01dedb34-3f6c-42e6-b679-66bc65dde084" />

As we can see in the above image, I determined that the strategy had excellent returns: achieving a whopping **32.34%** return when run from November 2023 through May 2025. Considering that the average retail investor loses money [source](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6AAA9078F50C2597F44D73FA6A8E3F0D/S0022109023000601a.pdf/resolving-a-paradox-retail-trades-positively-predict-returns-but-are-not-profitable.pdf), especially via active trading, this strategy, which runs fully automated and generates exceptional returns would be wonderful for the retail investor.

<img width="1220" alt="Screenshot 2025-06-08 at 1 24 23 PM" src="https://github.com/user-attachments/assets/7a9bce29-2617-4d28-8c03-c339c1e5b0ec" />

Further, taking a look a the statistics for the strategy, we can see the strategy has several attractive aspects in addition to its exceptional returns. First, drawdown is only **7.3%**. This implies that the strategy, at any given point, the max decline in the portfolio value is just 7.3%, which is relatively minimal. This is especially atttractive, because retail investors in particular may be tempted to panic trade, interfering with the algorithm's performance, so maintaining as minimal as possible drawdown is critical for preventing this situation, ensuring this algorithm is a viable strategy for retail. Second, the algorithm delivers an acceptable Sharpe Ratio of 1.162, indicating that the strategy delivers good returns on a risk-adjusted basis. Third, the Sortino ratio is also acceptable at 1.287, indicating that the strategy delivers good returns relative to downside risk (especially important for the risk averse retail investor).

**Finally, the strategy is attractive in that it is easily explainable, simple, and logically sound while generating good risk-adjusted returns.** This not only makes it easier psychologically to implement, but also reduces the risk of improper financial analysis leading to the strategy breaking down. Additionally, it works with reasonable amounts of capital that a retail investor could be expected to have, making it a realistic strategy to use.

## Limitations

1. Of course, there is a risk that the underlying may experience fundamentals shift that destroy the underlying thesis that the stock will deliver strong returns over time, eroding the algorithm's underlying thesis. This can be mitigated by adapting the strategy to trade a few different, equally strong stocks.
2. The strategy performs a large amount of trades (in the backtest, it performed 189). This means it **must** be executed in a commission-free account to be successful, as fees could significantly erode its performance.
3. Because the strategy trades daily, within the timespan of a week, it is possible that the strategy can execute 4 or more trades within the span of 5 trading days, and if this is the only strategy running, this would account for more than 6% of the volume of trading on the account. Therefore, the strategy could trigger the pattern day trading rule. This could, however, be mitigated by using a cash account (which would probably be fine for the average retail investor anyway, and definitely fine for this strategy, which doesn't use margin), requiring over 25K in the margin account, or adjusting the timeframe for position holding to be a week-long (which would still preserve the underlying algorithm thesis).
4. Since this strategy makes frequent trades, it will perform best in tax-advantaged accounts, such as Roth IRAs.





