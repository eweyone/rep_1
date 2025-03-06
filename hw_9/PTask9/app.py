import streamlit as st
from src.predict import predict_price


st.title('Прогноз стоимости квартиры 🏠')

total_square = st.number_input('Общая площадь (м²)', min_value=10.0, max_value=500.0, value=50.0)
floor = st.number_input('Этаж', min_value=1, max_value=50, value=5)

if st.button('Рассчитать стоимость'):
    predicted_price = predict_price(total_square, floor)
    st.success(f'💰 Прогнозируемая стоимость квартиры: {predicted_price:,.2f} руб.')

st.image("Images/MoscowCity.jpeg", use_container_width=True)