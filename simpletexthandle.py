import numpy as np
import statistics as st
import collections  as cl
import matplotlib.pyplot as plt
from wordcloud import WordCloud


while True:
    text= input("Enter Text (if you want to close then hit b): ")
    if text.lower()=="b":
        break
    mod_text = text.replace(",", "").replace(".", "").replace("?", "").replace('"', "").replace("\n", " ")
    words = mod_text.split(" ")
    mod_words=[ word  for word in words  if len(word) != 0  ]
    word_lengths = [len(x)  for x in mod_words ]
    n = len(word_lengths)
    s = sum(word_lengths)
    avg = s / n
    mean1=np.mean(word_lengths)
    sorted_lengths = sorted(word_lengths)
    n / 2
    word_freqs_1 = cl.Counter(word_lengths)
    tuples = tuple(   word_freqs_1.items()     )
    plt.plot(tuples)
    # plt.show()
    word_freqs_2 = cl.Counter(mod_words)
    word_cloud_1 = WordCloud( 
        width = 800, height = 500, background_color ='white').generate_from_frequencies(word_freqs_2)
    plt.imshow(word_cloud_1, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    word_freqs_1 = {str(k):int(v) for k,v in word_freqs_1.items()}
    word_freqs_1
    word_cloud_2 = WordCloud( 
        width = 800, height = 500, background_color ='white').generate_from_frequencies(word_freqs_1)

    plt.imshow(word_cloud_2, interpolation='bilinear')
    plt.axis("off")
    plt.show()