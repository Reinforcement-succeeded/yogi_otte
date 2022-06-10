import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import urllib.request
from konlpy.tag import Okt
from tqdm import tqdm
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

loaded_model = tf.keras.models.load_model('static/model/best_model.h5')

okt = Okt()
okt.morphs('고기도 맛있고 서비스는 더 최고입니다', stem=True)
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
tokenizer = Tokenizer()
max_len = 30

import pickle

with open('static/model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def sentiment_predict(new_sentence):
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', new_sentence)
    print("new_sentence_1 = ", end=""), print(new_sentence)

    new_sentence = okt.morphs(new_sentence, stem=True)  # 토큰화
    print("new_sentence_2 = ", end=""), print(new_sentence)

    new_sentence = [word for word in new_sentence if not word in stopwords]  # 불용어 제거
    print("new_sentence_3 = ", end=""), print(new_sentence)

    encoded = tokenizer.texts_to_sequences([new_sentence])  # 정수 인코딩
    print("encoded = ", end=""), print(encoded)

    pad_new = pad_sequences(encoded, maxlen=max_len)  # 패딩
    score = float(loaded_model.predict(pad_new))  # 예측
    if (score > 0.5):
        print("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(score * 100))
    else:
        print("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 - score) * 100))

sentiment_predict('고기도 맛있고 양 많다')

sentiment_predict('일단 양꼬치 양많은거 좋구 맛두 좋구')

sentiment_predict('맛없다 다신 안간다 더럽다')