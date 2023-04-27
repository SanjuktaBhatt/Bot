import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from wordcloud import WordCloud
import plotly.express as px
import openai
openai.api_key = "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"

movies_df_path="https://s3-whjr-curriculum-uploads.whjr.online/24f0d878-6a68-41e8-a4c5-88de15e55b0d.csv"
df=pd.read_csv(movies_df_path)
df.sort_values(by="rating",ascending=False,inplace=True,ignore_index=True)


def talk(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    response_list=message.split(". ")
    response_final=".\n".join(response_list)
    print(response_final)


def recommend(genre):
    global df
    return(df[df["genre"]==genre])["title"].unique()[:10]

def bubblechart(genre):
    global df
    data=df[df["genre"]==genre].head(25)
    fig = px.scatter( data,x='rating', y='revenue', size='revenue', color='rating',hover_name='title', size_max=75)
    fig.show()

def wordcloud(column):
    global df
    data = df[column].value_counts()
    wc = WordCloud(background_color="white").generate_from_frequencies(data)
    plt.axis('off')
    plt.imshow(wc)