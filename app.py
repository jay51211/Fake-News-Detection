import streamlit as st
import pickle

st.set_page_config(
    page_title = "Fake news"
)

st.title("Fake News Finder")
st.caption("Trained on knn model")

model = pickle.load( open("fake_news_model.pkl", "rb") )
vector = pickle.load(open("vectorizer.pkl", "rb"))

news = st.text_area("Enter a news title")
if st.button("Predict"):
    vect = vector.transform([news])
    prediction = model.predict(vect)[0]

    if prediction == 1:
        st.success("The news is real.")
    else:
        st.error("The news is fake.")

