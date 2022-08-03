import os

from classes.accounts.account import userAccount
import classes.server_client_conn.send as send
import data.basicData as bD
import classes.logging.log as logger


class registrationHandler:
    def __init__(self, username, email, password):
        self.account = userAccount({"username": username, "email": email, "password": password})
        self.request_registration()

    def request_registration(self):
        send.send(None, self.account, bD.MESSAGE_TYPE_ACCOUNT_CREATION)
        logger.log(os.path.basename(__file__), logger.csh, f"requested registration of {self.account.username}")