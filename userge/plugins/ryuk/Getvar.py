import os
from userge import userge, Message


@userge.on_cmd(
  "rvar",
   about = {
     "header" : "view vars", 
     "usage" : "{tr}rvar OWNER_ID ",
   },
)
async def view_var(message: Message):
  vname = message.input_str
  if not vname:
      await message.edit("Give a var name to vview", del_in=5)
      return
  input_name = (vname.strip()).upper()
  var = os.environ.get(input_name)
  await message.edit(var)