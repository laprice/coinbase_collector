import os
from coinbase.wallet.client import Client
from coinbase.wallet.model import Money


def filter_accounts(data):
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
    f = "{:<18}    {:<18}" 
    lines = [ print(f.format(str(portfolio[i].balance),str(portfolio[i].native_balance)))
              for i in order ]
    total_native = sum([ float(portfolio[i].native_balance.amount) for i in order])
    print("total usd: {:.2f}".format(total_native))
    
