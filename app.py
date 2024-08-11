import streamlit as st
from ui import init_session_state, create_sidebar, render_page

def main():
    init_session_state()  # Initialize session state
    
    page = create_sidebar()  # Create the sidebar and get the selected page
    render_page(page)  # Render the page based on the selection

if __name__ == "__main__":
    main()






# import streamlit as st
# from authenticator import Authenticator

# def main():
#     authenticator = Authenticator()
#     name, authentication_status, username = authenticator.login("Login", location="main")

#     if authentication_status:
#         st.write(f"Welcome {name}!")
#         show_authenticated_pages()
#     elif authentication_status is False:
#         st.error("Username/password is incorrect")
#     elif authentication_status is None:
#         st.warning("Please enter your username and password")

# def show_authenticated_pages():
#     st.sidebar.title("Navigation")
#     page = st.sidebar.selectbox("Select a page", ["Home", "Predictive Analytics", "Document Management", "Data Integration", "Logout"])

#     if page == "Home":
#         home_render()
#     elif page == "Predictive Analytics":
#         predictive_analytics_render()
#     elif page == "Document Management":
#         document_management_render()
#     elif page == "Data Integration":
#         data_integration_render()
#     elif page == "Logout":
#         logout()

# def home_render():
#     st.write("Home page logic goes here")

# def predictive_analytics_render():
#     st.write("Predictive analytics page logic goes here")

# def document_management_render():
#     st.write("Document management page logic goes here")

# def data_integration_render():
#     st.write("Data integration page logic goes here")

# def logout():
#     st.session_state["signed_in"] = False
#     st.session_state["user"] = None
#     st.experimental_rerun()

# if __name__ == "__main__":
#     main()
