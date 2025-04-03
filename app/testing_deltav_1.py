from uagents import Agent, Context, Field, Model, Protocol
from ai_engine import UAgentResponse, UAgentResponseType
from coinmarketcap import get_share_price
from llm_processing import find_symbol

class CoinMarketCapPriceTrackerRequest(Model):
    symbol: str = Field(description="The symbol of the currency, for example: fetch, bitcoin, ethereum, etc.")

    class Config:
        allow_population_by_field_name = True

coinmarketcap_protocol = Protocol("CoinMarketCapPriceTrackerProtocol")

@coinmarketcap_protocol.on_message(model=CoinMarketCapPriceTrackerRequest, replies={UAgentResponse})
async def coinmarketcap_share(ctx: Context, sender: str, msg: CoinMarketCapPriceTrackerRequest):
    """Handles cryptocurrency price requests by retrieving and sending the cryptocurrency price"""
    ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")

    try:
        #Hard coding question What is the price of ETHEREUM today? to test LLM processor
        #symbol = find_symbol("What is the price of ETHEREUM today?")
        #ctx.logger.info(f"THE SYMBOL GETTING BY LLM IS: {symbol}")
        symbol = msg.symbol
        message = await get_share_price(symbol)
        ctx.logger.info(f"message from endpoint: {message}")

        await ctx.send(sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL))
    except Exception as ex:
        ctx.logger.warn(ex)
        await ctx.send(sender, UAgentResponse(message=str(ex), type=UAgentResponseType.ERROR))
