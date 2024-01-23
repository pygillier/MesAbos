from dopplersdk import DopplerSDK
from flask import Flask
import os


class DopplerConfig:
    def __init__(self, app: Flask) -> None:
        self.init_app(app=app)

    def init_app(self, app: Flask) -> None:
        sdk = DopplerSDK()
        sdk.set_access_token(os.getenv("DOPPLER_TOKEN"))

        secrets = sdk.secrets.list(
            project=os.getenv("DOPPLER_PROJECT"),
            config=os.getenv("DOPPLER_CONFIG"),
            accepts="application/json",
        )

        for name, content in secrets.secrets.items():
            if not name.startswith("DOPPLER_"):  # Exclude doppler internal parameters
                app.config[name] = content["computed"]

        app.logger.info("Configuration loaded from doppler project")
