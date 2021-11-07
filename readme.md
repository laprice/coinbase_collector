This is a very simple script that scrapes the coinbase api for your
balances and emits a poorly formatted report of the balances with a
total for your native balance.

To use this script you will need to [create an api key pair](https://help.coinbase.com/en/exchange/managing-my-account/how-to-create-an-api-key). This script should only ever get read-only keys.

You'll need to inject the api key and secret into the environment that you run the script in.

```bash
export API_KEY="your_api_key"
export API_SECRET="your_coinbase_api_secret"
```