import config, requests


async def notify_tech(msg):
    try:
        msg = f"*OpenSeller Bot*\n{str(msg)}"

        msg = msg.replace("_", "\_").replace("<b>", "").replace("</b>", "")
        for i in config.admin_id:
            url = "https://api.telegram.org/bot%s/sendMessage" % (
                config.ADMIN_API_TOKEN
            )
            params = {
                "chat_id": i,
                "parse_mode": "Markdown",
                "text": str(msg),
            }
            res = requests.post(url, data=params)
            if res.ok:
                print("Successfully sent message from Technical Bot")
            else:
                raise Exception(res)
    except Exception as err:
        print(f"Error sending message from Technical Bot. {err}")
