from taipy import Config
import numpy as np
import pandas as pd
from embetter.grab import ColumnGrabber
from embetter.multi import ClipEncoder
from embetter.text import SentenceEncoder
from embetter.vision import ImageLoader
from sklearn.linear_model import (LogisticRegression, Perceptron,
                                  QuantileRegressor)
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline

sentences_cfg = Config.configure_data_node("sentences")
sentence_to_predict_cfg = Config.configure_data_node("sentence_to_predict")
predictions_cfg = Config.configure_data_node("prediction")


def predict(sentetnces, sentence_to_predict):
    rura_text2 = make_pipeline(
    SentenceEncoder()
    )
    # model.fit(rura_text2.transform(sentetnces), sentetnces['language'])
    
    model = LogisticRegression(max_iter=1000)
    model.fit(sentetnces[0], sentetnces[1])
    return model.predict(rura_text2.transform(sentence_to_predict).reshape(1, -1))[0]



task_predict_cfg = Config.configure_task(id="predict",
                                    function=predict,
                                    input=[sentences_cfg, sentence_to_predict_cfg],
                                    output=predictions_cfg)

scenario_cfg = Config.configure_scenario(id="sentence_prediction",
                                         task_configs=[task_predict_cfg])