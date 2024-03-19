from wordcloud import WordCloud, STOPWORDS
import streamlit as st 
import pandas as pd
import numpy as np
import plotly.graph_objects as go # for plots if we want more interactive plots
import plotly.express as px # for plots of maps
import re
from collections import Counter

st.set_page_config(layout="wide")

def main():	

    c1,c2,c3=st.columns([1,1,1])

    ase=c1.text_input("ASE")
    juge=c2.text_input("Juge")
    pedopsy=c3.text_input("Pedopsy")

    all=ase+juge+pedopsy
    all_corpus = re.sub('[^A-ZÇÉÈÊÀa-zœâàéîùçôè%ê0-9 ]', ' ', all)
    all_corpus = re.sub('\s+', ' ', all_corpus)
    all_corpus = all_corpus.lower() # lower everything

    word_nb=st.slider("nombre de mots a tracer",1,100,10)

    sw=st.multiselect('Mots courrants a supprimer des analyses',
								[i[0] for i in Counter(all_corpus.split(' ')).most_common() if i[0] not in STOPWORDS][:40])
    

    all_corpus = ' '.join([i for i in all_corpus.split(' ') if i not in sw])
    

    if st.button("Analyser"):
        
        c1,c2,c3=st.columns([1,1,1])


        c1.header("ASE")
        ase_corpus = re.sub('[^A-ZÇÉÈÊÀa-zœâàéîùçôè%ê0-9 ]', ' ', ase)
        ase_corpus = re.sub('\s+', ' ', ase_corpus)
        ase_corpus = ase_corpus.lower() # lower everything
        ase_corpus = ' '.join([i for i in ase_corpus.split(' ') if i not in sw])
        if ase_corpus == ' ' or ase_corpus == '':
            ase_corpus = 'vide'
        ase_wc = WordCloud(background_color="#0E1117",min_font_size=3, repeat=False, relative_scaling=1)
        ase_wc.generate(ase_corpus)
        c1.image(ase_wc.to_array())
        ase_counter = Counter(ase_corpus.split(' ')).most_common()
        ase_words=[i[0] for i in ase_counter[:word_nb]]
        total_words_a=sum([i[1] for i in ase_counter])
        ase_freqs=[i[1]/total_words_a*100 for i in ase_counter[:word_nb]]
        c1.bar_chart(pd.DataFrame({"percent":ase_freqs,"words":ase_words}),x="words",y="percent")

        c2.header("Juges")
        juge_corpus = re.sub('[^A-ZÇÉÈÊÀa-zœâàéîùçôè%ê0-9 ]', ' ', juge)
        juge_corpus = re.sub('\s+', ' ', juge_corpus)
        juge_corpus = juge_corpus.lower() # lower everything
        juge_corpus = ' '.join([i for i in juge_corpus.split(' ') if i not in sw])
        if juge_corpus == ' ' or juge_corpus == '':
            juge_corpus = 'vide'
        juge_wc = WordCloud(background_color="#0E1117",min_font_size=3, repeat=False, relative_scaling=1)
        juge_wc.generate(juge_corpus)
        c2.image(juge_wc.to_array())
        juge_counter = Counter(juge_corpus.split(' ')).most_common()
        juge_words=[i[0] for i in juge_counter[:word_nb]]
        total_words_j=sum([i[1] for i in juge_counter])
        juge_freqs=[i[1]/total_words_j*100 for i in juge_counter[:word_nb]]
        c2.bar_chart(pd.DataFrame({"percent":juge_freqs,"words":juge_words}),x="words",y="percent")

        c3.header("Pedopsy")
        pedopsy_corpus = re.sub('[^A-ZÇÉÈÊÀa-zœâàéîùçôè%ê0-9 ]', ' ', pedopsy)
        pedopsy_corpus = re.sub('\s+', ' ', pedopsy_corpus)
        pedopsy_corpus = pedopsy_corpus.lower() # lower everything
        pedopsy_corpus = ' '.join([i for i in pedopsy_corpus.split(' ') if i not in sw])
        if pedopsy_corpus == ' ' or pedopsy_corpus == '':
            pedopsy_corpus = 'vide'
        pedopsy_wc = WordCloud(background_color="#0E1117", repeat=False, relative_scaling=1)
        pedopsy_wc.generate(pedopsy_corpus)
        c3.image(pedopsy_wc.to_array()) 
        pedopsy_counter = Counter(pedopsy_corpus.split(' ')).most_common()
        pedopsy_words=[i[0] for i in pedopsy_counter[:word_nb]]
        total_words_p=sum([i[1] for i in pedopsy_counter])
        pedopsy_freqs=[i[1]/total_words_p*100 for i in pedopsy_counter[:word_nb]]
        c3.bar_chart(pd.DataFrame({"percent":pedopsy_freqs,"words":pedopsy_words}),x="words",y="percent")

        st.header("Tous les 3 combinés")
        if all_corpus == ' ' or all_corpus == '':
            all_corpus = 'vide'
        all_wc = WordCloud(background_color="#0E1117", repeat=False, relative_scaling=1)
        all_wc.generate(pedopsy_corpus)
        st.image(all_wc.to_array()) 
        all_counter = Counter(all_corpus.split(' ')).most_common()
        all_words=[i[0] for i in all_counter[:word_nb]]
        all_words_tot=sum([i[1] for i in all_counter])
        all_freqs=[i[1]/all_words_tot*100 for i in all_counter[:word_nb]]
        st.bar_chart(pd.DataFrame({"percent":all_freqs,"words":all_words}),x="words",y="percent")


if __name__ == '__main__':
	main()

