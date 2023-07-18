import streamlit as st
import requests
import base64
import os


def display_team_member(name, description, designation, image_path):
    st.image(image_path, caption=name, width=200)
    st.markdown(f"<h1 style='font-size:25px'><b>{name}</b></h1>", unsafe_allow_html=True)
    st.write(f"*{designation}*")
    st.write(description)
    st.write("---")

def main():
    st.title("Meet The Team")
    st.write("")  # creating an empty space

    sentence = "We are a young and multicultural data science team, working diligently to analyze data from around the world, one dataframe at a time!"
    st.write("")  # creating an empty space

    st.subheader(sentence)
    st.write("")  # creating an empty space
    st.write("")  # creating an empty space
    team_members = [
        {"name": "Palesa Motsoahae", "description": "Palesa is an experienced data scientist with a Ph.D. in Machine Learning and a passion for extracting valuable insights from complex datasets. With over a decade of industry experience, she has led numerous successful data science projects across various domains. Driven by her curiosity and analytical mindset, Palesa specializes in developing advanced algorithms and statistical models to solve challenging problems.", "designation": "Lead Data Scientist"},
        {"name": "Fortune Makgakga", "description": "Fortune is a seasoned data scientist with a strong background in predictive analytics and data mining. With a master's degree in Data Science, he brings expertise in developing scalable and efficient machine learning models. Fortune excels in feature engineering, algorithm selection, and model validation, ensuring the team delivers accurate and actionable insights to drive informed decision-making.", "designation": "Senior Data Scientist"},
        {"name": "Ayanda Shilakoe", "description": "Ayanda is a skilled data scientist who thrives on translating complex data into meaningful business solutions. With a bachelor's degree in Statistics and a keen eye for detail, she excels in exploratory data analysis, data visualization, and statistical modeling. Ayanda ability to identify patterns and trends allows her to uncover valuable insights that empower organizations to make data-driven decisions.", "designation": "Data Scientist II"},
        {"name": "Gift Mphahlele", "description": "Gift holds a Ph.D. in Computer Science, specializing in Natural Language Processing and Text Mining. He is an expert in extracting information from unstructured textual data and developing cutting-edge language models. Gift's research background and expertise in deep learning techniques enable him to build robust solutions for text analysis, sentiment analysis, and document classification.", "designation": "Data Scientist II"},
        {"name": "Dumisani Ncubeni", "description": "Dumisani is a detail-oriented data scientist who enjoys diving into complex datasets to uncover hidden patterns. With a bachelor's degree in Mathematics and a strong programming background, he excels in building and optimizing machine learning models. Dumisani's expertise lies in data wrangling, algorithm implementation, and model tuning, ensuring robust and efficient solutions.", "designation": "Data Scientist I"},
        {"name": "Boitumelo Mphahlele", "description": "Boitumelo is a highly motivated data scientist with a passion for leveraging data to drive innovation. With a master's degree in Data Analytics, she possesses a solid foundation in statistical analysis and machine learning algorithms. Boitumelo excels in data preprocessing, feature selection, and model evaluation, playing a vital role in delivering accurate and actionable insights to support business objectives.", "designation": "Data Scientist I"},
        {"name": "Mantsho Molepo", "description": "Mantsho is an emerging talent in the field of data science, bringing enthusiasm and a fresh perspective to the team. Currently pursuing a master's degree in Data Science, she demonstrates a strong aptitude for data manipulation, exploratory analysis, and model development. Mantsho's dedication and willingness to learn make her a valuable asset, contributing to the team's success.", "designation": "Natural Language Processing Expert and Bookworm:"},
    ]

    num_members = len(team_members)
    rows = num_members // 3 + (num_members % 3 > 0)

    for i in range(rows):
        cols = st.columns(3)
        for j in range(3):
            index = i * 3 + j
            if index < num_members:
                with cols[j]:
                    image_filename = team_members[index]['name'].replace(' ', '_').lower() + ".jpg"
                    image_path = os.path.join("team_images", image_filename)
                    permissions = 0o644  # Example: read and write for the owner, read for others
                    os.chmod(image_path, permissions)  # Change file permissions
                    display_team_member(
                        team_members[index]["name"],
                        team_members[index]["description"],
                        team_members[index]["designation"],
                        image_path
                    )

if __name__ == "__main__":
    main()