<div align="center">
  <img src=https://github.com/noahtheprogrammer/divvybot/assets/81941019/c10a3e75-f264-493f-8646-457cdb738478 alt="divvybot_logo">
</div>

### Introduction
Divvybot is a Python-based, open-source Discord bot that I created as a side project for the Divvy.bet Discord server. This bot has the ability to check the project's market details, retrieve estimated staking revenue and display the balance of the house in real time using Alchemy's API service. This bot has the ability to be customized for other web3 project servers as well.

### Disclaimer
The creators and contributors of Divvybot are not responsible for any financial decisions made by using this tool.

### Installation
In order to use Divvybot you will need an Alchemy API key and a Discord bot token (do not share this with anyone).
Open the installation folder and create a environment file with the following code block, replacing the placeholder values with your Alchemy API key and Discord token. Both keys are required to both send and recieve information to the server.
```
DISCORD_TOKEN=YOURDISCORDTOKEN
ALCHEMY_API=YOURALCHEMYKEY
```
Next, install the dependencies for Divvybot by opening Python and running the following command. This will install automatically install the required modules and their respective versions.
```
python -m pip install -r requirements.txt
```
If Divvybot is unable to open after following the installation process, try restarting your machine, as Python occassionally requires a reboot in order to successfully import modules.

### Commands
A chart of Divvybot's available commands can be viewed below.
| Prompt | Description |
| ----------- | ----------- |
| !update | Displays the $SOL, $USDC, and $USDT balance of the accrual wallet. |
| !house | Displays the $SOL, $USDC, and $USDT balance of the house pool. |
| !market | Displays the floor price, average sale, and total volume of the Divvy collection. |
| !staking `address` | Displays staking information and estimated revenue for the given wallet address. |
| !donate | Displays the donation address of the creator. |

### Contributions
if you have any interest in contributing, fork the repository and submit a pull request to have your improvements merged into the main repository. When opening an issue or feature request, be sure to provide a clear title and description of the issue you are experiencing or the feature you would like to suggest. Once submitted, I will review the issue and respond as soon as possible.

### Donations
Divvybot is open-source and will remain free forever.
If you're feeling a bit more generous however, please donate to my $SOL address below.
```
9P8zVyaaA1rgqWjZ7hCG5w1BxL94Q248ozqyy88HQpCn
```
