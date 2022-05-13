class user_account:
    def __init__(self, *args, **kwargs):
        ################################################################################################################
        self.possible_attributes = ["username", "password", "email", "first_name", "last_name", "phone_number",
                                    "address", "city", "state", "zip_code", "country", "birth_date", "about_me",
                                    "profile_picture"]
        ################################################################################################################
        self.args = args
        self.kwargs = kwargs
        ################################################################################################################
        self.username = self.kwargs.get("username")
        self.password = self.kwargs.get("password")

        self.email = self.kwargs.get("email")
        self.phone_number = self.kwargs.get("phone_number")

        self.first_name = self.kwargs.get("first_name")
        self.last_name = self.kwargs.get("last_name")
        self.birth_date = self.kwargs.get("birth_date")

        self.country = self.kwargs.get("country")
        self.city = self.kwargs.get("city")
        self.address = self.kwargs.get("address")

        self.about_me = self.kwargs.get("about_me")
        self.profile_picture = self.kwargs.get("profile_picture")
        ################################################################################################################
