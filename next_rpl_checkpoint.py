from ape import networks, api, Contract, chain
from dotenv import load_dotenv

load_dotenv()

ETH_SECONDS_PER_BLOCK = 12
ROCKET_STORAGE_ADDRESS = "0x1d8f8f00cfa6758d7bE78336684788Fb0ee0Fa46"
RPL_CHECKPOINT_BLOCKS = 5760

Web3 = api.providers.Web3


def main():
    with networks.ethereum.mainnet.use_provider("infura"):
        rocket_storage = Contract(ROCKET_STORAGE_ADDRESS)

        rocket_network_prices_abi = Web3.solidity_keccak(
            ["string", "string"], ["contract.address", "rocketNetworkPrices"]
        )
        rocket_network_prices = Contract(
            rocket_storage.getAddress(rocket_network_prices_abi)
        )

        rpl_price = rocket_network_prices.getRPLPrice() / 10**18
        print(f"Current RPL checkpoint price: {rpl_price:.6f} ETH")

        blocks_until_next_price_update = RPL_CHECKPOINT_BLOCKS - (
            chain.blocks.height - rocket_network_prices.getPricesBlock()
        )
        hours_until_next_price_update = int(
            blocks_until_next_price_update * ETH_SECONDS_PER_BLOCK / 60 / 60
        )
        minutes_until_next_price_update = int(
            blocks_until_next_price_update * ETH_SECONDS_PER_BLOCK / 60
            - hours_until_next_price_update * 60
        )

        if minutes_until_next_price_update == 1:
            minutes = "minute"
        else:
            minutes = "minutes"
        print(
            f"Next price update in {blocks_until_next_price_update} blocks, or {hours_until_next_price_update} hours and {minutes_until_next_price_update} {minutes}"
        )


if __name__ == "__main__":
    main()
