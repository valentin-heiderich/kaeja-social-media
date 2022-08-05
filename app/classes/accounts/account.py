class userAccount:
    def __init__(self, *args, **kwargs):
        ################################################################################################################
        self.possible_attributes = ["username", "password", "email"]
        self.account_attributes = {
            "house": None,
            "group": None,
            "daily_score": 0,
            "weekly_score": 0,
            "monthly_score": 0,
            "yearly_score": 0,
            "total_score": 0
        }
        ################################################################################################################
        self.kwargs = args[0]
        ################################################################################################################
        self.activated = False
        self.id = None
        ################################################################################################################
        self.username = self.kwargs["username"]
        self.password = self.kwargs["password"]
        self.email = self.kwargs["email"]
        ################################################################################################################
        for attribute, value in self.account_attributes.items():
            setattr(self, attribute, value)
        ################################################################################################################
    def activate(self):
        self.activated = True