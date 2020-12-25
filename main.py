import requests
import json

def list_cycle(hash):
    url = "https://ofmf.movapi.com/api/v1/life-cycle"
    params = {
        "tx_hash": hash
    }
    encoded_data = json.dumps(params).encode('utf-8')
    res = requests.post(url, encoded_data, auth=('summary', 'ofmf'))
    print(res.json())


def list_cycles(chain_name="", direction="", before_timestamp="", after_timestamp=""):
    url = "https://ofmf.movapi.com/api/v1/life-cycles"
    params = {}
    if chain_name != "":
        params["chain_name"] = chain_name
    if direction != "":
        params["direction"] = direction
    if before_timestamp != "":
        params["before_timestamp"] = before_timestamp
    if after_timestamp != "":
        params["after_timestamp"] = after_timestamp
    encoded_data = json.dumps(params).encode('utf-8')
    res = requests.post(url, encoded_data, auth=('summary', 'ofmf'))
    print(res.json())

def create_cross_address(chain_name, vapor_address):
    url = "https://ofmf.movapi.com/api/v1/create-cross-address"
    params = {
        "chain_name": chain_name,
        "vapor_address": vapor_address
    }
    encoded_data = json.dumps(params).encode('utf-8')
    res = requests.post(url, encoded_data, auth=('summary', 'ofmf'))
    print(res.json())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_cycle("c3b67438170a00114f32467e6097d3230bdb713b6c2fa277ad9ddde3208a07dd")

    # list_cycles(chain_name="ETH", direction="in")

    # create_cross_address("LTC", "vp1qphgfqj9wyvcnqnfts3gdtp9ecms3shdkq7zcws")

