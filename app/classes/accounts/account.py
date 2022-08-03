class userAccount:
    def __init__(self, **kwargs):
        ################################################################################################################
        self.possible_attributes = ["username", "password", "email", "first_name", "last_name", "phone_number",
                                    "address", "city", "state", "zip_code", "country", "birth_date", "about_me",
                                    "profile_picture"]
        ################################################################################################################
        self.kwargs = kwargs
        self.activated = False
        self.id = None
        ################################################################################################################
        for attribute in self.possible_attributes:
            try:
                setattr(self, attribute, kwargs[attribute])
            except:
                setattr(self, attribute, None)
        ################################################################################################################
    def activate(self):
        self.activated = True
