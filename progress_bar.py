from ipywidgets import IntProgress
from IPython.display import display
import time

progress = IntProgress(min=0, max=100, value=0)
display(progress)

for i in range(100):
    time.sleep(0.05)
    progress.value = i