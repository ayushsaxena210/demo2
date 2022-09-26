from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

"""
data_name = "14res" #@param ["14lap", "14res", "15res", "16res"]

import sys
sys.path.append("aste")
from data_utils import Data

path = f"aste/data/triplet_data/{data_name}/train.txt"
data = Data.load_from_full_path(path)
from pathlib import Path
from data_utils import Data, Sentence, SplitEnum
from wrapper import SpanModel

model = SpanModel(save_dir="pretrained_14res", random_seed=0)

def predict_sentence(text: str, model: SpanModel) -> Sentence:
    path_in = "temp_in.txt"
    path_out = "temp_out.txt"
    sent = Sentence(tokens=text.split(), triples=[], pos=[], is_labeled=False, weight=1, id=0)
    data = Data(root=Path(), data_split=SplitEnum.test, sentences=[sent])
    data.save_to_path(path_in)
    model.predict(path_in, path_out)
    data = Data.load_from_full_path(path_out)
    sent = data.sentences[0]
    result=[]
    for t in sent.triples:
        target = " ".join(sent.tokens[t.t_start:t.t_end+1])
        opinion = " ".join(sent.tokens[t.o_start:t.o_end+1])
        
        result.append(dict(target=target, opinion=opinion))
"""

@api_view(['POST'])
def sentiment_analysis(request):
    news = request.data["news"]
    result = None
    #result = predict_sentence(news, model)
    return Response({"result": result})
