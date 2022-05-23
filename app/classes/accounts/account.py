class userAccount:
    def __init__(self, *args, **kwargs):
        ################################################################################################################
        self.possible_attributes = ["username", "password", "email", "first_name", "last_name", "phone_number",
                                    "address", "city", "state", "zip_code", "country", "birth_date", "about_me",
                                    "profile_picture"]
        ################################################################################################################
        self.args = args
        self.kwargs = kwargs
        ################################################################################################################
        for attribute in self.possible_attributes:
            try:
                setattr(self, attribute, kwargs[attribute])
            except:
                setattr(self, attribute, None)
        ################################################################################################################
