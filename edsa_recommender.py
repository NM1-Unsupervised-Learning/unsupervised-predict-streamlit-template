"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# pip install streamlit

# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import base64
import random
import re

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
raw = pd.read_csv("resources/data/movies1.csv")
raw2 = pd.read_csv("resources/data/movies_sub.csv")

def callback():
    st.session_state.button_clicked = True


# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Log In or Sign Up", "Comment", "Try Something New", "About FilmFuse", "Insights", "FAQ", "Contact Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "About FilmFuse":
        st.title("About FilmFuse")
        tab1, tab2 = st.tabs(['What is FilmFuse?', 'FilmFuse Team'])
        with tab1:
            st.write(
                """
                FilmFuse is a subscription-based streaming service that allows users to enjoy movies with no ads (on an internet-connected device). \n
                FilmFuse makes use of one the best recommendation systems to provide you with a tailored movie experience like no other. You can watch from a wide variety of award-winning movies, documentaries and more. The more you watch, the better Filmic gets at recommending movies you will most likely enjoy. 
                """
                )
            st.write("")
            # st.image("enter image", use_column_width=True)
            
        with tab2:
            st.subheader("Meet the Team")
           # st.image("enter image")


    if page_selection == "Insights":
        st.subheader("Learn About Our Data")
        tab1, tab2 = st.tabs(['Data Description', 'Exploratory Data Analysis'])
        with tab1:
            st.write(
                """
                Our dataset consists of 5-star ratings obtained from users of the online MovieLens movie recommendation service. The MovieLens dataset has long been used by industry and academic researchers to improve the performance of explicitly-based recommender systems. \n
                **Source:** \n
                The data for the MovieLens dataset is maintained by the GroupLens research group in the Department of Computer Science and Engineering at the University of Minnesota. Additional movie content data was legally scraped from IMDB
                """
                )
            st.write("")

            
        with tab2:
            st.subheader("Exploratory Data Analysis")
            st.info("In this section, you will find important insights observed in our exploratory data analysis phase")
            select = st.selectbox("Insights", ("Genre with the most amount of movies","Top 15 most popular movies", "Movie Ratings", "Popular Actors", "Popular Directors"))

            if select == "Genre with the most amount of movies":
                st.image('resources\most_common_genres.png', width = None)
                st.write("The dataset has 19 unique listed genres and 5062 films have no genre listed, which accounts for 5% of the films in the dataset. Majority of the films fall into the **drama**, **comedy**, and **thriller** genres. **Drama** accounts for 23% of the films, while **comedy** and **thriller** make up 15% and 8% of the films, respectively. The **Imax** genre account for the smallest portion of the films in the dataset at less than 1%.This is due to the fact that this is a relatively new genre and the dataset goes back 50 years. ")
            if select == "Top 15 most popular movies":
                st.image('resources\pop_movies.jpg', use_column_width=True)
                st.write("Bar graph of the 15 most wached movies. Interestingly, all the movies in the top 10 were released earlier than the year 2000, we can conclude that many 'good and popular' movies in our dataset are older. The reason may be that these movies have been around longer and have been rated more as a result. The **Shawshank redemption** is the most popular movie. In the top 10 there are some good movies that some viewers may call 'classics', for example movies like **Pulp Fiction**, **Forrest Gump**, **Bravenheart** and **Fight Club**. There are also 'popular fan favourites' like **The Matrix**, **Star Wars**, and **The Lord of The Rings** in the top 15.")
            if select == "Movie Ratings":
                st.image(r'resources\ratings_dist.png', width = None)
                st.write("We observed that a high percentage of our movies were rated above average i.e above 3 and a low percentage were below 3. This could mean that people are enjoying the movies they're watching and are generous with their ratings or if they don't like the movie they don't give it a rating.")
            if select == "Popular Actors":
                st.image(r'resources\top100cast.png', width = None)
                st.write("The wordcloud above indicates a number of popular actors based on the number of movies they have appeared in (as main or supporting actors). We can observe that some of the most popular actors appearing are **Samuel L Jackson**, **Robert Deniro**, **Nicolas Cage**, **Bruce Willis**, **Gerard Depardieu** and **Johnny Depp**. The word cloud results are not surprising, most users in our have rated the **drama** and **action** genres the most, these genre's are top 3 most popular in our dataset and the actors that are appear the most are famous for their dramatic and live-action roles.")
            if select == "Popular Directors":
                st.image(r'resources\top100directors.png', width = None)
                st.write("The wordcloud above indicates a number of popular movie directors based on the number of movies they have directed. We observe that the most popular movie director as **Woody Allen**, **Luc Paul Maurice Besson** and **Stephen King**.")

        
            
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    
    if page_selection == "FAQ":
        st.title("Frequently Asked Questions")
        select = st.selectbox("FAQ",("What's the subscription cost?","Which devices are supported by FilmFuse?", "Can I share with my family?", "Can I download to watch offline?", "More questions?"))

        
        if select == "What's the subscription cost?":
            st.write("FilmFuse offers different subscription options to fit a variety of budgets and entertainment needs. There are no hidden costs, long-term commitments, or cancellation fees, and you’re able to switch plans and add-ons at any time. After a free seven-days trail, Filmic is billed on a monthly basis, unless you subscribe to a quarterly or annual plan. For full details about billing policies and procedures, please review our **Terms of Service**.")
        if select == "Which devices are supported by FilmFuse?":
            st.write("You can use FilmFuse through any internet-connected device that offers the Filmic app, including smart TVs, game consoles, streaming media players, set-top boxes, smartphones, and tablets. You can also use Filmic on your computer using an internet browser. You can review the **system requirements** for web browser compatibility, and check our **internet speed recommendations** to achieve the best performance.")
        if select == "Can I share with my family?":
            st.write("Yes. FilmFuse lets you share your subscription with up to five family members. FilmFuse allows you to stream on up to 5 screens at the same time.")
        if select == "Can I download to watch offline?":
            st.write("Absolutely. Download your movies to your to your iOS, Android, or Windows 10 device and watch them anywhere, anytime without a Wi-Fi or internet connection.")
        if select == "More questions?":
            st.write("Visit our **Contact Us** page.")
            
    if page_selection == "Try Something New":
        st.subheader("Feel like watching something out of your comfort zone?")
        st.image("resources/thrill.png")
        st.markdown("Click on 'Thrill me' for a random recommendation")
        st.write(" ")
        if st.button("Thrill me"):
            sample = raw.sample(5).reset_index()
            st.image(sample["images"][0], width = 150)
            st.subheader(sample["title"][0])
            st.subheader(sample["link"][0])
            st.subheader(" ")
            st.subheader(" ")
            
    
       
    if page_selection == "Comment":
        
        st.title("Join the discussion")
        # Comment section
        st.subheader("Leave a Comment")
        user_comment = st.text_input("Leave a comment:")
        submit_button = st.button("Submit")

        if submit_button and user_comment:
            dataset = dataset.append({'Comment': user_comment}, ignore_index=True)
            st.success("Comment submitted successfully!")
        
        # Display existing comments
            st.subheader("Comments")
            for comment in dataset['Comment']:
                st.write(comment)
        
        dataset = pd.read_csv("resources\data\IMDB Dataset.csv")
        st.subheader("IMDB Dataset")
        st.dataframe(dataset)

    if page_selection == "Contact Us":
        
        st.title("We'd love to hear from you 🙂")
        with st.form("form1", clear_on_submit=True):
            st.subheader("Get in touch with us")
            st.markdown("Fill in your details below")
            name = st.text_input("Enter full name")
            email = st.text_input("Enter email")
            message = st.text_area("Message")
            
            submit = st.form_submit_button("Submit Form")
            if submit:
                st.write("Your form has been submitted and we will be in touch 🙂")
                
    if page_selection == "Log In or Sign Up":
        # Header contents
     
        if "button_clicked" not in st.session_state:    
            st.session_state.button_clicked = False
        
            # st.image("enter image", use_column_width=True)
        
        
        genre = st.radio( "New to FilmFuse? Sign up or login in if you have an account",('login', 'sign up'))
        
        if genre == "sign up":
            email = st.text_input('Ready to watch? Enter your email to start a membership', '')
            
            if (st.button("Next", on_click = callback) or st.session_state.button_clicked): 
            
                if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)):
                    st.write('Welcome to FilmFuse', email.split("@")[0].capitalize(),","," a movie experience like no other.\n To customize your\
                    experience, please visit the **Recommender System** page to get personalized movie recommendations")
                    

                   
                else:
                    st.write("Please enter a valid email")
                    
            
                
        if genre == "login":
            
            title = st.text_input('email address', '')
            password = st.text_input('password', '', type="password")
      
         
            if (st.button("Login", on_click = callback) or st.session_state.button_clicked):
                
            
                if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',title)) and password != "":

                    st.write('Welcome back to FilmFuse', title.split("@")[0].capitalize(),",", " ", "continue watching your favourite movies or head over to the **Try Something New** page for a thrilling experience!")


                else:
                    st.write("Please enter valid login details")
        


if __name__ == '__main__':
    main()
