import streamlit as st
import firebase_admin
from firebase_admin import credentials
import json
import requests

# Firebase API key (replace with environment variable or secure method)
FIREBASE_API_KEY = "Your Key"

# Firebase REST API URLs
SIGN_UP_URL = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
SIGN_IN_URL = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
RESET_PASSWORD_URL = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"

# Initialize Firebase Admin SDK if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("medical-llm-9aa49-a2deb71ad0b9.json")
    firebase_admin.initialize_app(cred)

# Helper function for signing up
def sign_up(email, password, username=None):
    try:
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        if username:
            payload["displayName"] = username
        response = requests.post(SIGN_UP_URL, params={"key": FIREBASE_API_KEY}, json=payload)
        response_data = response.json()
        if 'email' in response_data:
            return response_data['email']
        else:
            st.warning(response_data.get('error', {}).get('message', 'Signup failed'))
    except Exception as e:
        st.warning(f'Signup failed: {e}')

# Helper function for signing in
def sign_in(email, password):
    try:
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        response = requests.post(SIGN_IN_URL, params={"key": FIREBASE_API_KEY}, json=payload)
        response_data = response.json()
        if 'email' in response_data:
            return {
                'email': response_data['email'],
                'username': response_data.get('displayName')
            }
        else:
            st.warning(response_data.get('error', {}).get('message', 'Signin failed'))
    except Exception as e:
        st.warning(f'Signin failed: {e}')

# Helper function for resetting password
def reset_password(email):
    try:
        payload = {
            "email": email,
            "requestType": "PASSWORD_RESET"
        }
        response = requests.post(RESET_PASSWORD_URL, params={"key": FIREBASE_API_KEY}, json=payload)
        if response.status_code == 200:
            return True, "Reset email sent"
        else:
            error_message = response.json().get('error', {}).get('message', 'Password reset failed')
            return False, error_message
    except Exception as e:
        return False, str(e)

# Main app function
def app():
    st.title('Welcome to :violet[Pondering] :sunglasses:')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False

    def handle_login():
        try:
            user_info = sign_in(st.session_state.email_input, st.session_state.password_input)
            if user_info:
                st.session_state.username = user_info['username']
                st.session_state.useremail = user_info['email']
                st.session_state.signedout = True
                st.session_state.signout = True
        except Exception as e:
            st.warning(f'Login failed: {e}')

    def handle_logout():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''
        st.session_state.useremail = ''

    def handle_password_reset():
        email = st.text_input('Email')
        if st.button('Send Reset Link'):
            success, message = reset_password(email)
            if success:
                st.success(message)
            else:
                st.warning(f"Password reset failed: {message}")

    if not st.session_state.signedout:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
        st.session_state.email_input = st.text_input('Email Address')
        st.session_state.password_input = st.text_input('Password', type='password')

        if choice == 'Sign up':
            st.session_state.username_input = st.text_input("Enter your unique username")
            if st.button('Create my account'):
                user = sign_up(email=st.session_state.email_input, password=st.session_state.password_input, username=st.session_state.username_input)
                if user:
                    st.success('Account created successfully!')
                    st.markdown('Please Login using your email and password')
                    st.balloons()
        else:
            st.button('Login', on_click=handle_login)
            handle_password_reset()
    else:
        st.text(f'Name: {st.session_state.username}')
        st.text(f'Email: {st.session_state.useremail}')
        st.button('Sign out', on_click=handle_logout)

if __name__ == "__main__":
    app()
