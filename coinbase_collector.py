"""Collects balance from coinbase emits report."""
import os
from coinbase.wallet.client import Client

def filter_accounts(data):
    """Returns a list of only accounts that have a balance."""
    return { acct.currency : acct for acct in data if float(acct.balance.amount) > 0.0 }

if __name__=='__main__':
    api_key = os.environ['API_KEY']
    api_secret = os.environ['API_SECRET']
    client = Client(api_key,api_secret)
    user = client.get_current_user()
    accounts = client.get_accounts()
    portfolio = filter_accounts(accounts.data)
    order = list(portfolio.keys())
    order.sort()
    lines = [ F"{str(portfolio[i].balance):<18}    {str(portfolio[i].native_balance):<18}"
              for i in order ]
    _ = [print(line) for line in lines]
    total_native = sum([ float(portfolio[i].native_balance.amount) for i in order])
    print(F"total usd: {total_native:.2f}")
