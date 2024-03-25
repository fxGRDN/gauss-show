from taipy.gui import Markdown
from pathlib import Path

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





page2_md = Markdown(
"""


# Embetter - embeding zdjęć i tekstów dla scikit

> *Embetter implements scikit-learn compatible embeddings for computer vision and text. 
> It should make it very easy to quickly build proof of concepts using scikit-learn pipelines and, in particular, should help with bulk labelling. 
> It's a also meant to play nice with bulk and scikit-partial but it can also be used together with your favorite ANN solution like weaviate, chromadb and hnswlib.*

```python
rura_img = make_pipeline(
    ImageLoader(convert="RGB"),
    ClipEncoder(),
)

rura_text = make_pipeline(
    ColumnGrabber("text"),
    SentenceEncoder()
)
rura_text2 = make_pipeline(
    ColumnGrabber("Text"),
    SentenceEncoder()
)
```

"""
)