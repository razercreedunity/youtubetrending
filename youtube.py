import pickle
import streamlit as st

# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

pickle_in_second = open('classifier_second.pkl', 'rb')
classifier_second = pickle.load(pickle_in_second)

pickle_in_third = open('classifier_third.pkl', 'rb')
classifier_third = pickle.load(pickle_in_third)

import base64


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


set_png_as_page_bg('background.jpg')

@st.cache()
# defining the function which will make the prediction using the data which the user inputs
#Random Forest
def prediction(category_id, views, likes, dislikes, comment_count, country):
    # Pre-processing user input
    if country == "France":
        country = 1
    elif country == "United Kingdom":
        country = 2

    if category_id == "Entertainment":
        category_id = 1
    elif category_id == "Music":
        category_id = 2
    elif category_id == "People & Blogs":
        category_id = 3

    # Making predictions
    prediction = classifier.predict([[category_id, views, likes, dislikes, comment_count, country]])

    if prediction == 0:
        pred = 'Worst Trending'
    elif prediction == 1:
        pred = 'Best Trending'
    else:
        pred = 'Moderate Trending'
    return pred

#Naive Bayes
def prediction_second(category_id, views, likes, dislikes, comment_count, country):
    # Pre-processing user input
    if country == "France":
        country = 1
    elif country == "United Kingdom":
        country = 2

    if category_id == "Entertainment":
        category_id = 1
    elif category_id == "Music":
        category_id = 2
    elif category_id == "People & Blogs":
        category_id = 3

    # Making predictions
    prediction_second = classifier_second.predict([[category_id, views, likes, dislikes, comment_count, country]])

    if prediction_second == 0:
        pred = 'Worst Trending'
    elif prediction_second == 1:
        pred = 'Best Trending'
    else:
        pred = 'Moderate Trending'

    return pred

#k-NN
def prediction_third(category_id, views, likes, dislikes, comment_count, country):
    # Pre-processing user input
    if country == "France":
        country = 1
    elif country == "United Kingdom":
        country = 2

    if category_id == "Entertainment":
        category_id = 1
    elif category_id == "Music":
        category_id = 2
    elif category_id == "People & Blogs":
        category_id = 3

    # Making predictions
    prediction_third = classifier_third.predict([[category_id, views, likes, dislikes, comment_count, country]])

    if prediction_third == 0:
        pred = 'Worst Trending'
    elif prediction_third == 1:
        pred = 'Best Trending'
    else:
        pred = 'Moderate Trending'
    return pred

# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:Red;width: 700px; height: 70px; border-radius: 100px / 50px"> 
    <h1 style ="color:black;text-align:center;">Youtube Trending Prediction</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction

    model = st.selectbox('Machine Learning Model', ("Random Forest", "Naive Bayes", "k-NN"))
    country = st.selectbox('Country', ("France", "United Kingdom"))
    category_id = st.selectbox('Category', ("Entertainment", "Music", "People & Blogs"))
    views = st.sidebar.slider("View", 100053, 999966)
    likes = st.sidebar.slider("Likes", 91, 176713)
    dislikes = st.sidebar.slider("Dislikes", 8, 28372)
    comment_count = st.sidebar.slider("Comments", 3, 31749)

    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        if model == "Random Forest":
            result = prediction(category_id, views, likes, dislikes, comment_count, country)
            st.success('Your Video Is On The {}'.format(result))
        elif model == "Naive Bayes":
            result = prediction_second(category_id, views, likes, dislikes, comment_count, country)
            st.success('Your Video Is On The {}'.format(result))
        elif model == "k-NN":
            result = prediction_third(category_id, views, likes, dislikes, comment_count, country)
            st.success('Your Video Is On The {}'.format(result))
        print("Done!")

if __name__ == '__main__':
    main()
