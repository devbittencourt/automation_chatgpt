import keyboard
import time

keyboard.send('windows')

time.sleep(2)

keyboard.write('chrome')

time.sleep(2)

keyboard.send('enter')

time.sleep(2)

site = 'https://chat.openai.com/'

time.sleep(2)

keyboard.write(site)

time.sleep(2)

keyboard.send('enter')
