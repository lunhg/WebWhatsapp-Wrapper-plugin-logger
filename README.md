# Logger 
Plugin utility for [lunhg/WebWhatsapp-Wrapper](https://www.github.com/lunhg/WebWhatsapp-Wrapper)

# Download

```
$ git clone https://github.com/lunhg/WebWhatsapp-Wrapper-plugin-logger <path-to-clone>
```

# Usage

Create a class that implements [lunhg/WebWhatsapp-Wrapper-bot](https://www.github.com/lunhg/WebWhatsapp-Wrapper-bot)


```python
import sys
import os
import json
sys.path.append('<path-to-lunhg/WebWhatsapp-Wrapper-bot>')
import bot

# Implement a abstract bot
class Whatsapp(bot.Bot):

  def __init__(self, **kwargs):
    super(Foo, self).__init__(**kwargs)
    # Open and loads configuration for each
    # plugin
    self.plugin(name='logger', path='<path-to-lunhg/WebWhatsapp-Wrapper-plugin-logger>')
    ...
    
  # A simple implementation of setup
  # loaded form configuration readed by a json file
  def setup(self):
    super.setup(self.config)
    ...

  # A simple implementation of run with 0.1 seconds
  # between a call and another call, with
  # implementation of handle methods of logger plugin
  def run(self, handles=[]):
    super.run(frameTime=0.1, callbacks=handles)
 
  # self.attributes and self.
  def logger(self):
    return self.getattribute('logger')

if __name__ is '__main__':
  foobarbaz = Whatsapp(client='firefox', )
  
  # { "logger": {"logdir": "<path-to-log>"} }
  with open('<path-to-config>') as json_data:
    data = json.load(json_data)
    foobarbaz.setup(data)
  
  handleLog = foobarbaz.logger().handle
  foobarbaz.run(handles=[handleLog])

```

