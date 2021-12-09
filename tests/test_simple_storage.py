from brownie import SimpleStorage, accounts

'''
TO TEST:

run in terminal:
brownie test 

if you wanna check a specific function, then run:
brownie test -k test_deploy

to be able to have insights into the errors (if dosen't pass), then you can directly run using:
brownie test --pdb

to see exactly which one passed:
brownie test -s
'''


def test_deploy():
    # Arrange
    account = accounts[0]

    # Acting
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0

    # Assert
    assert starting_value == expected

def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Acting
    expected = 15
    simple_storage.store(expected, {"from": account})
    starting_value = simple_storage.retrieve()

    # Assert
    assert expected == simple_storage.retrieve()
