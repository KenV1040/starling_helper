class StarlingCtrl:
    __request_string = "Authorization: Bearer "

    def __init__(self) -> None:
        self.authorised = None
        self.session_token = None

    def pat(self, pat):
        self.session_token = pat
