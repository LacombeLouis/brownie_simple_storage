from brownie import accounts, config, SimpleStorage, network

"""
To see what happens and deploy contracts use:

brownie console

then you can run:
account = accounts[0]
simple_storage = SimpleStorage.deploy({"from": account})
simple_storage.retrieve()


You can specify your accounts specifically and always have them included in the accounts created by ganache
account = accounts.add(config["wallets"]["from_key"])
"""
def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)

    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()
