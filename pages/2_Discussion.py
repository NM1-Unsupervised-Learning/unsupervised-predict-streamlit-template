import streamlit as st
import pandas as pd

def main():
    st.title("Join the Discussion")
    dataset = pd.read_csv("resources/data/IMDB_Dataset.csv")  # Load the dataset
    
    st.header("")
    
    # Comment section
    st.subheader("Leave a Comment")
    user_comment = st.text_input("Leave a comment:")
    submit_button = st.button("Submit")

    if submit_button and user_comment:
        dataset = dataset.append({'review': user_comment}, ignore_index=True)
        st.success("Comment submitted successfully!")

    dataset = pd.read_csv("resources\data\IMDB_Dataset.csv")
    st.subheader("IMDB Dataset")
    st.dataframe(dataset)

if __name__ == "__main__":
    main()
