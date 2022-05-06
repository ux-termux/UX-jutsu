from userge import Message, userge

CHANNEL = userge.getCLogger(__name__)


@userge.on_cmd(
  "jc",
  about={
      "header" : "join private chat using link",
      "usage" : "{tr}jc chatlink",
  },
)
async def jc(message: Message):
  link = message.input_str
  if not link:
     await message.edit(
            "```Bruh, Without chat name, I can't Join...^_^```", del_in=3
     )
     return
  await userge.join_chat(link)
  return await channel.send_message
    


@userge.on_cmd(
  "click",
  about={"input which button you want to press'\n defaults to 1st button"},
)
async def clck(message: Message):
  button = message.input_str
  if not button:
    press = message.replied
    await press.click(0)
  x = message.replied
  await x.click(num)
