from taipy.gui import Markdown
from math import cos, exp
import pandas as pd

def on_slide(state):
    state.data = compute_data(state.value)

def compute_data(decay:int)->list:
    return [cos(i/6) * exp(-i*decay/600) for i in range(100)]


value = 10

data = compute_data(value)

img_path = 'Taipy_Logo.png'

df = pd.read_csv('dataset.csv')



page1_md = Markdown(
"""
<|layout|columns=1 1 1|>

<|align-item-center logo|

<|{img_path}|image|>

# Taipy - front-end for data people

centrowałem ten element godzine :)
|>


## Dynamiczna zmiana wykresów

Value: <|{value}|text|>

<|{value}|slider|on_change=on_slide|>

<|{data}|chart|>

## Wyświetlanie zawartości tabel

<|{df}|table|>

"""
)