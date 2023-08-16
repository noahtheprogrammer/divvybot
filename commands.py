import json

from solders.pubkey import Pubkey
from solana.rpc.api import Client
from solana.rpc.types import TokenAccountOpts

client = Client("https://api.mainnet-beta.solana.com/")
payout_address = Pubkey.from_string("3D3whwTbRYzr2b6yY8hXE6EVGRJVGYyGC7jFrTxHVhbK")

def token_balance(address: str) -> float:
    response = client.get_token_accounts_by_owner_json_parsed(payout_address, TokenAccountOpts(mint = Pubkey.from_string(address))).to_json()
    json_response = json.loads(response)
    balance = json_response["result"]["value"][0]["account"]["data"]["parsed"]["info"]["tokenAmount"]["uiAmount"]
    return(balance)

def sol_balance():
    balance_response = client.get_balance(payout_address).value
    balance_response = balance_response / (10**9)
    return(balance_response)