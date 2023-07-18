import streamlit as st

def main():
    st.title("FilmFuse Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if validate_login(email, password):
            st.success("Login successful!")
            # Continue with your application logic or redirect to another page
        else:
            st.error("Invalid email or password")

def validate_login(email, password):
    # Here you would implement your login validation logic
    # You can check against a database or any other authentication mechanism
    # For this example, let's assume a hardcoded email and password
    valid_email = "example@example.com"
    valid_password = "password123"
    return email == valid_email and password == valid_password

if __name__ == "__main__":
    main()
