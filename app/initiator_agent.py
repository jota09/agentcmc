import os

from dotenv import load_dotenv
from uagents import Agent, Context, Model, Protocol, Bureau
from uagents.setup import fund_agent_if_low

from llm_processing import find_symbol
from coinmarketcap import get_share_price
from response_agent import bruno_agent, bruno_protocol

# You can define your SEED_PHRASE_AGENT value as a secret or environment variable
load_dotenv()
SEED_PHRASE_AGENT = os.environ.get("SEED_PHRASE_AGENT","YOUR_SEED_PHRASE_AGENT")

class RequestMessage(Model):
    text: str
 
class ResponseMessage(Model):
    text: str
    

initiator_agent = Agent(
    name="Batman", 
    seed="initiator recovery phrase", 
)

fund_agent_if_low(initiator_agent.wallet.address())

initiator_protocol = Protocol(name="SimpleProtocol_Initiator", version="0.1.0")

@initiator_protocol.on_interval(period=10.0)
async def initiator_send_message(ctx: Context):
    await ctx.send(bruno_agent.address, RequestMessage(text="Hello I would like know how BTC is going today?"))
    
@initiator_protocol.on_message(model=ResponseMessage)
async def initiator_handle_response(ctx: Context, sender: str, msg: ResponseMessage):
    ctx.logger.info(f"Received response from {sender}: {msg.text}")
    

initiator_agent.include(initiator_protocol, publish_manifest=True)

bureau = Bureau(endpoint=["http://127.0.0.1:8000/submit"])
bureau.add(initiator_agent)
bureau.add(bruno_agent)    