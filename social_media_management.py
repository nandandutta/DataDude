import streamlit as st
import requests

# Define the API endpoint for generating post content
API_URL = 'http://localhost:5000/generate_post'

# Function to generate post content by calling the external script
def generate_post_content(prompt, context=''):
    response = requests.post(API_URL, json={'prompt': prompt, 'context': context})
    if response.status_code == 200:
        return response.json().get('content', '')
    else:
        st.error('Failed to generate post content')
        return ''

def social_media_management():
    # Set page title
    st.title('Social Media Posting Interface')

    # Custom CSS for button styling
    st.markdown("""
        <style>
        .button-container {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }
        .button-container .stButton {
            width: 200px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Button container
    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    # Social media buttons
    with col1:
        if st.button('Connect Facebook'):
            st.write(f'[Login with Facebook](http://localhost:5000/login/facebook)')

    with col2:
        if st.button('Connect Instagram'):
            st.write(f'[Login with Instagram](http://localhost:5000/login/instagram)')

    with col3:
        if st.button('Connect Twitter'):
            st.write(f'[Login with Twitter](http://localhost:5000/login/twitter)')

    with col4:
        if st.button('Connect LinkedIn'):
            st.write(f'[Login with LinkedIn](http://localhost:5000/login/linkedin)')

    st.markdown('</div>', unsafe_allow_html=True)

    # Post creation section
    st.header('Create a New Post')

    # Multi-select dropdown to choose social media platforms
    selected_platforms = st.multiselect(
        'Select Social Media Platforms',
        ['facebook', 'instagram', 'twitter', 'linkedin']
    )

    # Text input for generating post content
    prompt = st.text_area('Enter a prompt for the model to generate post content', '')
    context = st.text_area('Enter additional context', '')

    if st.button('Generate Post Content'):
        if prompt:
            generated_content = generate_post_content(prompt, context)
            st.write('Generated Post Content:')
            st.write(generated_content)
        else:
            st.error('Please enter a prompt to generate content.')

    post_text = st.text_area('Or enter your own text for the post', '')

    uploaded_file = st.file_uploader('Upload an image or video', type=['jpg', 'jpeg', 'png', 'mp4', 'mov'])

    post_category = st.selectbox(
        'Select Post Category (LinkedIn only)',
        ['None', 'Reel', 'Story', 'Article']
    )

    if st.button('Post'):
        if post_text or uploaded_file:
            if selected_platforms:
                for platform in selected_platforms:
                    st.write(f'Posting to {platform}...')
                    # Add code here to handle posting the content to the selected social media
                    files = {'file': uploaded_file} if uploaded_file else {}
                    data = {
                        'text': post_text or generated_content,
                        'category': post_category if platform == 'linkedin' else 'None'
                    }
                    # Ensure you have the correct URL to handle posting
                    response = requests.post(f'http://localhost:5000/post/{platform}', files=files, data=data)
                    
                    if response.status_code == 200:
                        st.success(f'Your post has been submitted to {platform}!')
                    else:
                        st.error(f'Failed to post to {platform}.')
            else:
                st.error('Please select at least one social media platform.')
        else:
            st.error('Please provide some content to post.')

if __name__ == "__main__":
    social_media_management()
