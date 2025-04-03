from uagents import Agent, Context, Field, Model, Protocol
from ai_engine import UAgentResponse, UAgentResponseType
from coinmarketcap import get_share_price
from llm_processing import find_symbol
from uagents.setup import fund_agent_if_low

agentDeltaV = Agent(
    name="Tester", 
    seed="TesterSecretPhrase", 
    port=8000,
    mailbox=True,
    readme_path="README.md",
    publish_agent_details=True
)

fund_agent_if_low(agentDeltaV.wallet.address())

class TestingCMCPriceTrackerRequest(Model):
    symbol: str = Field(description="The symbol of the currency, for example: fetch, bitcoin, ethereum, etc.")

    class Config:
        allow_population_by_field_name = True

tester_protocol = Protocol("TestingCMCPriceTrackerProtocol")

@tester_protocol.on_message(model=TestingCMCPriceTrackerRequest, replies={UAgentResponse})
async def coinmarketcap_share(ctx: Context, sender: str, msg: TestingCMCPriceTrackerRequest):
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

# Include protocol in agent
agentDeltaV.include(tester_protocol, publish_manifest=True)
