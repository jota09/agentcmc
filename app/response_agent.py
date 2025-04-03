import os

from dotenv import load_dotenv
from uagents import Agent, Context, Model, Bureau, Protocol
from uagents.setup import fund_agent_if_low

from llm_processing import find_symbol
from coinmarketcap import get_share_price

# You can define your SEED_PHRASE_AGENT value as a secret or environment variable
load_dotenv()
SEED_PHRASE_AGENT = os.environ.get("SEED_PHRASE_AGENT","YOUR_SEED_PHRASE_AGENT")

class RequestMessage(Model):
    text: str
 
class ResponseMessage(Model):
    text: str
    
bruno_agent = Agent(
    name="Bruno",
    port=8000,
    seed=SEED_PHRASE_AGENT,
    endpoint=["http://localhost:8000/submit","http://localhost:8001/submit"],
    readme_path="README.md"
)

fund_agent_if_low(bruno_agent.wallet.address())

bruno_protocol = Protocol(name="Protocol_Response", version="0.1.0")

@bruno_protocol.on_message(RequestMessage, replies=ResponseMessage)
async def responder_handle_message(ctx: Context, sender: str, msg: RequestMessage):
    ctx.logger.info(f"Received message from {sender}: {msg.text}")
    symbol = find_symbol(msg.text)
    response = await get_share_price(symbol)
    await ctx.send(sender, ResponseMessage(text=response))
 
bruno_agent.include(bruno_protocol, publish_manifest=True)