import json

from solders.pubkey import Pubkey
from solana.rpc.api import Client
from solana.rpc.types import TokenAccountOpts

client = Client("https://api.mainnet-beta.solana.com/")


# Pubkey created using accrual wallet address
accrual = Pubkey.from_string("3D3whwTbRYzr2b6yY8hXE6EVGRJVGYyGC7jFrTxHVhbK")

# Token array organized in order of house authority [0] and token pubkeys [1]
sol = [Pubkey.from_string("B98A4BxgrpmkXvKHSFyYPwp3GqrmFBN7Na1vCwtPDfvd"), None]
usdc = [Pubkey.from_string("GBgg4DxDAx18zjTbdfv1LgdX5VNGprKomeDyRJrQYX3t"), Pubkey.from_string("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v")]
usdt = [Pubkey.from_string("HXjwCrCKWR6EyrVYSUPcFfnPitWKy2xLhasE9Ak4BdxY"), Pubkey.from_string("Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB")]
bonk = [Pubkey.from_string("5oqHf5xbaV5hTUXFaadMu8SPkE4QLWPh661WHYyek58t"), Pubkey.from_string("DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263")]
prnt = [Pubkey.from_string("9gmnQF1zvZs858svdfv5gTJjhYH6CEGHgnQXMhk1xjEx"), Pubkey.from_string("4TUNzcgp2fPD48fcW4seRjyqyDZMrPj4ZubnXFEsKeYk")]


def token_balance(address: Pubkey, token: Pubkey) -> float:
    response = client.get_token_accounts_by_owner_json_parsed(address, TokenAccountOpts(mint = token)).to_json()
    json_response = json.loads(response)
    balance = json_response["result"]["value"][0]["account"]["data"]["parsed"]["info"]["tokenAmount"]["uiAmount"]
    return(balance)

def sol_balance(address: Pubkey):
    balance_response = client.get_balance(address).value
    balance_response = balance_response / (10**9)
    return(balance_response)