import streamlit as st
from sign_in import verify_password
from style import get_custom_styles
from home import home_page
from predictive_analytics import predictive_analytics
from campaign_management import campaign_management
from content_calendar import content_calendar
from social_media_management import social_media_management
from email_marketing import email_marketing
from analytics_and_reporting import analytics_and_reporting
from team_collaboration import team_collaboration




def init_session_state():
    if "signed_in" not in st.session_state:
        st.session_state["signed_in"] = False
    if "user" not in st.session_state:
        st.session_state["user"] = None

def create_sidebar():
    if st.session_state["signed_in"]:
        nav = st.sidebar.selectbox("Select a page", ["Home", "Predictive Analytics","Campaign Management", "Content Calendar", "Social Media Management", "Email Marketing", "Analytics and Reporting", "Team Collaboration", "Document Management", "Data Integration", "Logout"], key="nav_menu_signed_in")
    else:
        nav = st.sidebar.selectbox("Select a page", ["Sign In", "Reset Password"], key="sign_in_nav_not_signed_in")
    return nav

def render_page(page):
    if page == "Sign In":
        sign_in_render()
    elif page == "Home":
        home_render()
    elif page == "Predictive Analytics":
        predictive_analytics_render()
    elif page == "Campaign Management":
        campaign_management_render()
    elif page == "Content Calendar":
        content_calendar_render()
    elif page == "Social Media Management":
        social_media_management_render()
    elif page == "Email Marketing":
        email_marketing_render()
    elif page == "Analytics and Reporting":
        analytics_and_reporting_render()
    elif page == "Team Collaboration":
        team_collaboration_render()
    elif page == "Document Management":
        document_management_render()
    elif page == "Data Integration":
        data_integration_render()
    elif page == "Logout":
        logout()
    elif page == "Reset Password":
        reset_password()

def logout():
    st.session_state["signed_in"] = False
    st.session_state["user"] = None
    st.experimental_rerun()

def reset_password():
    # Add your password reset logic here
    st.write("Reset password logic goes here")

def sign_in_render():
    if st.session_state["signed_in"]:
        st.write(f"Welcome back, {st.session_state['user']}!")
        return

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign In", key="sign_in_button"):
        if verify_password(username, password):
            st.session_state["signed_in"] = True
            st.session_state["user"] = username
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")

def home_render():
    st.markdown(get_custom_styles(), unsafe_allow_html=True)
    home_page()
    st.write("Home page logic goes here")

def predictive_analytics_render():
    predictive_analytics()
    st.write("Predictive analytics page logic goes here")

def document_management_render():
    # Add your document management page logic here
    st.write("Document management page logic goes here")

def data_integration_render():
    # Add your data integration page logic here
    st.write("Data integration page logic goes here")

def campaign_management_render():
    # Add your campaign management page logic here
    st.write("Campaign management page logic goes here")

def content_calendar_render():
    # Add your content calendar page logic here
    st.write("Content calendar page logic goes here")

def social_media_management_render():
    # Add your social media management page logic here
    st.write("Social media management page logic goes here")

def email_marketing_render():
    # Add your email marketing page logic here
    st.write("Email marketing page logic goes here")

def analytics_and_reporting_render():
    # Add your analytics and reporting page logic here
    st.write("Analytics and reporting page logic goes here")

def team_collaboration_render():
    # Add your team collaboration page logic here
    st.write("Team collaboration page logic goes here")






if __name__ == "__main__":
    init_session_state()
    page = create_sidebar()
    render_page(page)































# import streamlit as st
# from auth_logic import store_password, user_exists, verify_password

# def init_session_state():
#     if "signed_in" not in st.session_state:
#         st.session_state["signed_in"] = False
#     if "user" not in st.session_state:
#         st.session_state["user"] = None

# def create_sidebar():
#     if st.session_state["signed_in"]:
#         nav = st.sidebar.selectbox("Select a page", ["Home", "Predictive Analytics", "Document Management", "Data Integration", "Logout"], key="nav_menu_signed_in")
#     else:
#         nav = st.sidebar.selectbox("Select a page", ["Sign In", "Sign Up", "Reset Password"], key="sign_in_nav_not_signed_in")
#     return nav

# def render_page(page):
#     if page == "Sign In":
#         sign_in_render()
#     elif page == "Sign Up":
#         sign_up_render()
#     elif page == "Home":
#         home_render()
#     elif page == "Predictive Analytics":
#         predictive_analytics_render()
#     elif page == "Document Management":
#         document_management_render()
#     elif page == "Data Integration":
#         data_integration_render()
#     elif page == "Logout":
#         logout()
#     elif page == "Reset Password":
#         reset_password()

# def logout():
#     st.session_state["signed_in"] = False
#     st.session_state["user"] = None
#     st.experimental_rerun()

# def reset_password():
#     # Add your password reset logic here
#     st.write("Reset password logic goes here")

# def sign_in_render():
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     if st.button("Sign In", key="sign_in_button"):
#         if verify_password(username, password):
#             st.session_state["signed_in"] = True
#             st.session_state["user"] = username
#             st.experimental_rerun()
#         else:
#             st.error("Invalid credentials")

# def sign_up_render():
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")
#     if st.button("Sign Up", key="sign_up_button"):
#         if password == confirm_password:
#             if user_exists(username):
#                 st.error("Username already exists")
#             else:
#                 store_password(username, password)
#                 st.success("Account created successfully. You can now sign in.")
#                 st.session_state["signed_in"] = False
#                 st.session_state["user"] = None
#                 st.experimental_rerun()
#         else:
#             st.error("Passwords do not match")

# def home_render():
#     # Add your home page logic here
#     st.write("Home page logic goes here")

# def predictive_analytics_render():
#     # Add your predictive analytics page logic here
#     st.write("Predictive analytics page logic goes here")

# def document_management_render():
#     # Add your document management page logic here
#     st.write("Document management page logic goes here")

# def data_integration_render():
#     # Add your data integration page logic here
#     st.write("Data integration page logic goes here")
