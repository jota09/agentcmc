import os

#from cosmpy.aerial.wallet import LocalWallet
from cosmpy.aerial.client import LedgerClient, NetworkConfig
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from dotenv import load_dotenv

# You can define your COINMARKETCAP_API_KEY value as a secret or environment variable
load_dotenv()
SEED_PHRASE_WALLET = os.environ.get("SEED_PHRASE_WALLET","YOUR_SEED_PHRASE_WALLET")

# Recovering an existing private key
#my_wallet = LocalWallet.from_mnemonic(SEED_PHRASE_WALLET)

#print(my_wallet.address()) will print the address for the wallet

agent = Agent(
    name="Default",
    port=8000,
#    wallet=my_wallet,
    seed="DefaultSeedPhrase",
    endpoint=["http://127.0.0.1:8000/submit","http://127.0.0.1:8001/submit"]
)

fund_agent_if_low(agent.wallet.address())

@agent.on_event("startup")
async def introduce_agent(ctx: Context):
    ctx.logger.info(f"ASI network address:{agent.wallet.address()}")
    ledger_client = LedgerClient(NetworkConfig.fetch_mainnet())
    address: str = agent.wallet.address()
    balances = ledger_client.query_bank_all_balances(address)
    ctx.logger.info(f"Balance of addr: {balances}")

@agent.on_event("startup")
async def introduce_agent(ctx: Context):
    ctx.logger.info(f"Hello, I'm agent {agent.name} and my address is {agent.address}. ASI network address:{agent.wallet.address()}")

if __name__ == "__main__":
    agent.run()
   