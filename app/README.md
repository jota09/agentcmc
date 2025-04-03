# agentcmc
This agent fetches real-time prices of top cryptocurrencies via CoinMarketCap API for accurate, live market data


<img src="https://img.shields.io/badge/crypto-colorcode" alt="tag:crypto"> <img src="https://img.shields.io/badge/prices-red" alt="tag:prices"> <img src="https://img.shields.io/badge/tracker-red" alt="tag:tracker"> <img src="https://img.shields.io/badge/USD-red" alt="tag:USD"> <img src="https://img.shields.io/badge/CoinMarketCap-3D8BD3" alt="tag:CoinMarketCap"> <img src="https://img.shields.io/badge/tracker-3D8BD3" alt="tag:tracker">

![image](https://logowik.com/content/uploads/images/coinmarketcap6426.jpg)

The CoinMarketCap Price Agent is designed to retrieve real-time cryptocurrency prices using their respective ticker symbols. Integrated with the CoinMarketCap API, this agent provides accurate, up-to-date prices for requested cryptocurrencies, including major cryptocurrencies like Bitcoin, Ethereum, and Fetch.ai.


Key features and benefits of this agent include:


- Utilizing the CoinMarketCap API to fetch cryptocurrency price data
- Secure data exchange via HTTPS protocol
- Providing accurate, up-to-date prices for requested cryptocurrencies
- Optimized for fast response times, because interact directly with CoinMarketCap API

By leveraging the CoinMarketCap API, this agent ensures reliable, high-quality data for informed decision-making. It is an ideal solution for those seeking real-time cryptocurrency price information.

The CoinMarketCap Agent uses the CoinMarketCap API to search for and retrieve information about cryptocurrencies. It accepts a search query and returns a summary of relevant coins, exchanges, categories, and NFTs.

This agent retrieves the current prices of cryptocurrencies from CoinMarketCap based on a specified currency symbol. By providing a currency symbol, such as "bitcoin" or "ethereum," users can access up-to-date pricing information for their chosen cryptocurrency. This functionality is crucial for individuals and businesses seeking to monitor market trends, make informed investment decisions, or analyze the performance of various cryptocurrencies.

Input Data Model

```
class CoinMarketCapPriceTrackerRequest(Model):
    symbol: str = Field(description="The symbol of the currency, for example: fetch, bitcoin, ethereum, etc.")

    class Config:
        allow_population_by_field_name = True

```
