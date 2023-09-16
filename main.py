# from pathlib import Path
#
# for i in range(1,11):
#     Path(f'./file{i}.txt').touch()

from html2image import Html2Image

hti = Html2Image()
hti.screenshot(url='https://chat.openai.com/', save_as='python_org.png')


