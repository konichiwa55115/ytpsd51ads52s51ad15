import logging

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
TgFileDownloadlist = {}


import pyrogram, os

if __name__ == "__main__":
    plugins = dict(root="plugins")
    app = pyrogram.Client(
        "bot",
        bot_token="5393596540:AAF5Ps0KbzFmO9GogkAGzzFvtD2E7T5YR9g",
        api_id=int(17983098),
        api_hash="ee28199396e0925f1f44d945ac174f64",
        plugins=plugins,
    )
    app.run()
