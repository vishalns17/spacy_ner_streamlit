import streamlit as st
import spacy
from spacy import displacy
import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint
from newspaper import Article
import validators

st.title("Named Entity Recognizer")

st.info("This app will take an input from the user and then prints the named entities\n\nChoose any one method")
url=st.text_area("Enter the URL of the article")
text = st.text_area("Enter a paragraph")
doc=""

if(st.button("Submit")):
    if (url=="") & (text==""):
        st.warning("Please enter an input")
    elif (url!="" )& (text==""):
        if validators.url(url)==True:
            article = Article(url)
            article.download()
            article.parse()
            doc=nlp(article.text)
        else:
            st.warning("Please enter a valid URL")
    elif (url=="") & (text!="") :
        doc=nlp(text)

    elif (url!="" )& (text!=""):
        st.warning("Please enter any one input only")
    #elif (url=="") & (text!="") :
    #doc = nlp(text)
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    # Display the entity visualization in the browser:
    st.markdown(ent_html, unsafe_allow_html=True)

def clear_text():
    st.session_state["text"] = ""
st.button("Clear Output", on_click=clear_text)
