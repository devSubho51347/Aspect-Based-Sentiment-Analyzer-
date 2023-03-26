import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import openai

st.title("Aspect Based Sentiment Analysis Of Glassdoor Reviews")

st.subheader("Provide your Input Here")
review = st.text_area("Enter Review")

button1 = st.button("Generate positive aspects")
button2 = st.button("Generate negative aspects")

openai.api_key = "Enter your API Key"

if button1:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Find positive aspects from the below text\n\nText: Employee Friendly Diversity and Inclusion Compensation Benefits Perks\n\nPositive\n\nEmployee Friendly\nDiversity\n Compensation Benefits\n\n##\n\nText: Education funds. Employee wellbeing. Great culture.\n\nPositive\nEducation funds\nEmployee wellbeing\nGreat culture\n\n##\n\nText:{review}\n\n",
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text = response['choices'][0]['text']

    st.success("Positive Aspects have been successfully generated")

    st.write(text)

if button2:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Find negative aspects from the below text\nText: long work hours frequently. nothing more that I can think of.\n\nlong work hours\n\n##\nText: U might suffer due to politics.\n\npolitics\n##\n\nText: Salary is literally peanuts .\n\nlow salary\n##\n\nText: None to report from my experience.\n\nnone\n##\n\nText: {review}\n",
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text = response['choices'][0]['text']

    st.success("Negative Aspects have been successfully generated")

    st.write(text)



