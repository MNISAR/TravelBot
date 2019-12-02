# TravelBot
Chatbot for travel domain

Abstract:
Chatbot is a computer application that interacts with users using natural language in a similar way to imitate a human travel agent. In most cases, it can provide better user-centric recommendations. Hence, the chatbot is becoming an integral part of the future consumer services.
This project deals with answering travel query of the user. The Chatbot provides an interface to interact with the user. As the number of people using messaging platforms is increasing exponentially, developing such a comfortable service will help the user to avoid getting used to some new interface. The Chatbot takes the user’s input query and then uses various tools of Natural Language Processing to process the input and then generate the answer to the user’s query according to the requirements.


Working: 
The user will enter the questions through the console.
The question will be fetched from the console and will be passed to eval function.
The eval function will classify the tokens and identify the meaning of a sentence.
After the recognition of tokens, the appropriate query is being fired onto the database.
The result obtained from the database will be formatted and displayed to the user.


Technologies used:
  Database: 
    MongoDB, Wikipedia live
  Server(backend): 
    Flask Framework
  Other technologies: 
    Python – complete implementation
    SPACY – For Natural Language Processing
    Sci-kit Learn – for Query Processing
    Geopy – for weather related data
    G Map API – for location and nearby processing
    Gensim – for summarization
    Wikipedia – to get data whenever necessary
    Bing-map API – to get distance, time from place to place
