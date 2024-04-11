# spacy_ner_streamlit
In this short program I have created a Named Entity Recognizer using spacy with a streamlit front-end.

There are two options as input :
  
	1.As a URL : where it will use newspaper3k to scrape the link and find the text blocks from it.
  
	2.As a direct text input : You will be able to type the text you want directly in the textbox provided in the ui

-The submit button will check which textbox has a valid input and give the processed output accordingly
  
-The url will be validated using the validators package

-The outputs can be cleared using the 'Clear Output' button

# Installation

Install spacy as it is used for the natural language processing task

	pip install spacy

Spacy requires a model to work and we are using the commonly used basic model they provide. Download it using this command in the terminal.

	python -m spacy download en_core_web_sm

Streamlit is used as the front-end for quick prototyping of this project, install it using

	pip install streamlit

Newspaper3k is used for the web scraping specifically scraping articles from the given url, install it using

	pip install newspaper3k

And finally install the Validators package for checking the URL if it is a valid one using

	pip install validators
 
# Running the program

Run the following command in the terminal where the python file has been downloaded
 
 	streamlit run spacy_ner_streamlit.py 

In Visual Studio code, Your default browser will automatically launch and display the program as a localhost webpage. Else Ctrl-Click the localhost address given in the terminal to open the page.
