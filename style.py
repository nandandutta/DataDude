# Custom CSS styles
def get_custom_styles():
    return """
        <style>
            .main {
                background-color: #000000;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .icon {
                font-size: 50px;
                margin: 10px;
            }
            .button {
                background-color: #4CAF50;
                color: #fff;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .button:hover {
                background-color: #3e8e41;
            }
        </style>
    """