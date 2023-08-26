import os
import json
from dotenv import load_dotenv

from solders.pubkey import Pubkey
from solana.rpc.api import Client
from solana.rpc.types import TokenAccountOpts

load_dotenv()
api = os.getenv('ALCHEMY_KEY')
client = Client(f"https://solana-mainnet.g.alchemy.com/v2/{api}")

# Public address string created using accrual wallet address
accrual = "3D3whwTbRYzr2b6yY8hXE6EVGRJVGYyGC7jFrTxHVhbK"

# Token arrays organized with house authority [0] and token [1] public address strings
sol = ["B98A4BxgrpmkXvKHSFyYPwp3GqrmFBN7Na1vCwtPDfvd", None]
usdc = ["GBgg4DxDAx18zjTbdfv1LgdX5VNGprKomeDyRJrQYX3t", "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"]
usdt = ["HXjwCrCKWR6EyrVYSUPcFfnPitWKy2xLhasE9Ak4BdxY", "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB"]
bonk = ["5oqHf5xbaV5hTUXFaadMu8SPkE4QLWPh661WHYyek58t", "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263"]
prnt = ["9gmnQF1zvZs858svdfv5gTJjhYH6CEGHgnQXMhk1xjEx", "4TUNzcgp2fPD48fcW4seRjyqyDZMrPj4ZubnXFEsKeYk"]


def token_balance(address: str, token: str) -> float:
    response = client.get_token_accounts_by_owner_json_parsed(Pubkey.from_string(address), TokenAccountOpts(mint = Pubkey.from_string(token))).to_json()
    json_response = json.loads(response)
    balance = json_response["result"]["value"][0]["account"]["data"]["parsed"]["info"]["tokenAmount"]["uiAmount"]
    return(balance)

def sol_balance(address: str) -> float:
    balance_response = client.get_balance(Pubkey.from_string(address)).value
    balance_response = balance_response / (10**9)
    return(balance_response)

def find_pass_count(address: str) -> list:
    response = client.get_token_accounts_by_owner_json_parsed(Pubkey.from_string(address), TokenAccountOpts(program_id = Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"))).to_json()
    json_response = json.loads(response)
    hashlist = json.load(open("hashlist.json"))
    token_count = len(json_response["result"]["value"])
    passes = 0
    staked_passes = 0
    for i in range(token_count):
        info = json_response["result"]["value"][i]["account"]["data"]["parsed"]["info"]
        if info["mint"] in hashlist:
            passes = passes + 1
            if info["state"] == "frozen":
                staked_passes = staked_passes + 1
    return [passes, staked_passes]