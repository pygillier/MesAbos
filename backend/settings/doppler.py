from dopplersdk import DopplerSDK
import os


class DopplerSettings:

    sdk: DopplerSDK = None

    def __init__(self):
        self.sdk = DopplerSDK()
        self.sdk.set_access_token(os.getenv("DOPPLER_TOKEN"))

        secrets = self.sdk.secrets.list(
            project=os.getenv("DOPPLER_PROJECT"),
            config=os.getenv("DOPPLER_CONFIG"),
            accepts="application/json"
        )
        for secret in secrets.secrets:
            self["ddd"] = secret
