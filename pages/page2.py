from taipy.gui import Markdown
import taipy as tp
from pathlib import Path
from sc_config import scenario_cfg
import joblib

data = joblib.load('data.pkl')
sentence = 'The quick brown fox jumps over the lazy dog'

scenario = tp.create_scenario(scenario_cfg)
scenario.sentences.write(data)
scenario.sentence_to_predict.write(sentence)

tp.submit(scenario)


def save(state):
    state.scenario.sentences.write(data)
    state.scenario.sentence_to_predict.write(state.sentence)
    state.refresh('scenario')


page2_md = Markdown(
"""


# Embetter - embeding zdjęć i tekstów dla scikit

> *Embetter implements scikit-learn compatible embeddings for computer vision and text. 
> It should make it very easy to quickly build proof of concepts using scikit-learn pipelines and, in particular, should help with bulk labelling. 
> It's a also meant to play nice with bulk and scikit-partial but it can also be used together with your favorite ANN solution like weaviate, chromadb and hnswlib.*

Mamy dwa typy embeddingów:
    - Tekstowe
    - Obrazkowe


<|{scenario}|scenario|>
<|{scenario}|scenario_dag|>

<|{sentence}|>

<|{sentence}|input|on_change=save|active={scenario}|>

<|{scenario.prediction}|data_node|>

"""
)