# rockettools

Install following packages:

```
python -m venv .venv
source .venv/bin/activate

pip install eth-ape
pip install python-dotenv
ape plugins install etherscan
```

Create .env file with the following variables:

```
PORTAL_ID="<your portal id: https://portal.pokt.network>"
ETHERSCAN_API_KEY="<your etherscan api key: https://etherscan.io>"
```

Run the following command:

```
python next_rpl_checkpoint.py
```

Sample output:

```
Current RPL checkpoint price: 0.015766 ETH
Next price update in 2708 blocks, or 9 hours and 1 minute
```
