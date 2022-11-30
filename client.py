from models import Account
from access_create_acc.access_create_acc import user_account

connection_string = "sqlite:///accounts.db"

if __name__ == '__main__':
    user_account(connection_string, Account)
