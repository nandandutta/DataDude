import streamlit as st

def landing_page():
    st.markdown("""
        <style>
        .centered-image img {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        .shaded-box {
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            height: 150px;  /* Fixed height */
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        .shaded-box h3 {
            color: #4CAF50;
            margin: 0;
        }
        .shaded-box p {
            margin: 0;
        }
        .text-below {
            margin-top: 10px;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Welcome to AI Analytics Platform")
    st.subheader("Unlock Insights, Drive Business Growth")
    st.markdown('<div class="centered-image"><img src="C:/Users/ndutt/OneDrive/Documents/Python_Projects/hero_image.png" width="50"></div>', unsafe_allow_html=True)

    st.header("Benefits of Our AI Analytics Platform")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div class="shaded-box">
                <h3>Faster Insights</h3>
            </div>
            <div class="text-below">
                <p>Get actionable recommendations in minutes, not months</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="shaded-box">
                <h3>Data-Driven Decisions</h3>
            </div>
            <div class="text-below">
                <p>Make informed decisions with accurate predictions and simulations</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="shaded-box">
                <h3>Improved Efficiency</h3>
            </div>
            <div class="text-below">
                <p>Automate tasks, reduce costs, and optimize resources</p>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
            <div class="shaded-box">
                <h3>Competitive Edge</h3>
            </div>
            <div class="text-below">
                <p>Stay ahead of the competition with cutting-edge AI technology</p>
            </div>
        """, unsafe_allow_html=True)

    st.header("Our AI Analytics Capabilities")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div class="shaded-box">
                <p>Predictive Analytics</p>
            </div>
            <div class="text-below">
                <p>Forecast sales, demand, and customer behavior</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="shaded-box">
                <p>Document Management</p>
            </div>
            <div class="text-below">
                <p>Streamline document processing and analysis</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="shaded-box">
                <p>Custom Connections</p>
            </div>
            <div class="text-below">
                <p>Integrate with any data source or system</p>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
            <div class="shaded-box">
                <p>Social Media Integration</p>
            </div>
            <div class="text-below">
                <p>Monitor brand sentiment and engagement</p>
            </div>
        """, unsafe_allow_html=True)

    if st.button("Get Started"):
        st.session_state.page = "Sign In"

    st.markdown("""
        <div class="footer">
            <p>Contact us: <a href="mailto:n.dutta25@gmail.com">n.dutta25@gmail.com</a> | Phone: 9903 baki mail pe | Address: 123 Baguihati</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    landing_page()
