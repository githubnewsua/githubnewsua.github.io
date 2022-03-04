# import typer
# from telethon import TelegramClient, events, sync
# from telethon.errors import SessionPasswordNeededError
# from telethon.tl.functions.messages import GetHistoryRequest
#
# from parser.app.config import CONFIG
#
#
# def tg(channel):
#     conf = CONFIG["config"]["telegram"]
#     client = TelegramClient(conf["username"], conf["api_id"], conf["api_hash"])
#     client.start()
#     typer.echo("Client Created")
#
#     offset_id = 0
#     limit = 100
#     total_messages = 0
#
#     my_channel = client.get_entity(channel)
#
#     while True:
#         typer.echo(f"Current Offset ID is:{offset_id}; Total Messages:{total_messages}")
#         history = client(GetHistoryRequest(
#             peer=my_channel,
#             offset_id=offset_id,
#             offset_date=None,
#             add_offset=0,
#             limit=limit,
#             max_id=0,
#             min_id=0,
#             hash=0
#         ))
#         if not history.messages:
#             break
#         messages = history.messages
#         for message in messages:
#             all_messages.append(message.to_dict())
#         offset_id = messages[len(messages) - 1].id
#         total_messages = len(all_messages)
#         if total_count_limit != 0 and total_messages >= total_count_limit:
#             break
#
#     # history = client(GetHistoryRequest(
#     #     peer=my_channel,
#     #     offset_id=offset_id,
#     #     offset_date=None,
#     #     add_offset=0,
#     #     limit=limit,
#     #     max_id=0,
#     #     min_id=0,
#     #     hash=0
#     # ))
#     # # Ensure you're authorized
#     # if not client.is_user_authorized():
#     #     print("Not authorized")
#     #     client.send_code_request("phone")
#     #     try:
#     #         client.sign_in("phone", input('Enter the code: '))
#     #     except SessionPasswordNeededError:
#     #         client.sign_in(password=input('Password: '))
