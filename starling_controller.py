import requests as r


class StarlingCtrl:
    _base_endpoint = "https://api.starlingbank.com/api/v2"
    _header = ""

    def __init__(self, authorised, session_token) -> None:
        self.authorised = authorised
        self.session_token = session_token
        self._header = {'Authorization': 'Bearer ' + self.session_token}

    def _call(self, method, endpoint, body=None):
        try:
            response = None
            if method == 'GET':
                response = r.get(self._base_endpoint + endpoint, headers=self._header, verify='./certs/starling-prod'
                                                                                              '-api-certificate.crt')
            elif method == 'POST':
                response = r.post(self._base_endpoint + endpoint, headers=self._header, data=body,
                                  verify='./certs/starling-prod'
                                         '-api-certificate.crt')
            response.raise_for_status()
            return response
        except r.exceptions.HTTPError as errh:
            return "An Http Error occurred:" + repr(errh)
        except r.exceptions.ConnectionError as errc:
            return "An Error Connecting to the API occurred:" + repr(errc)
        except r.exceptions.Timeout as errt:
            return "A Timeout Error occurred:" + repr(errt)
        except r.exceptions.RequestException as err:
            return "An Unknown Error occurred" + repr(err)

    def get_accounts(self):
        res = self._call('GET', '/accounts')
        print(res.text)
        return res
