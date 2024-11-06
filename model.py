import streamlit as st
import joblib



Lbl_brand = joblib.load('Lbl_brand.joblib')
Lbl_fuel = joblib.load('Lbl_fuel.joblib')
Lbl_transmission = joblib.load('Lbl_tran.joblib')
Lbl_owner = joblib.load('Lbl_owner.joblib')

scalerX = joblib.load('scalerX.joblib')
scalery = joblib.load('scalery.joblib')
reg_moduel = joblib.load('Rf.joblib')


st.title("Car Price Prediction")


brand = st.selectbox('Select Brand', ['Toyota', 'Honda', 'Ford', 'Maruti', 'Hyundai', 'Tata', 'Mahindra', 'Volkswagen', 'Audi', 'BMW', 'Mercedes'])
fuel = st.selectbox('Select Fuel Type', ['Petrol', 'Diesel'])
transmission = st.selectbox('Select Transmission Type', ['Manual', 'Automatic'])
owner_type = st.selectbox('Select Owner Type', ['First', 'Second', 'Third'])
year = st.number_input('Year of Manufacture', min_value=2000, max_value=2024, value=2018)
km_driven = st.number_input('Kilometers Driven', min_value=0, max_value=300000, value=28000)
mileage = st.number_input('Mileage (kmpl)', min_value=5.0, max_value=30.0, value=14.0)
engine_size = st.number_input('Engine Size (cc)', min_value=500, max_value=5000, value=2298)
power = st.number_input('Power (BHP)', min_value=50, max_value=1000, value=335)
seats = st.number_input('Number of Seats', min_value=2, max_value=10, value=5)


Brand = Lbl_brand.transform([brand])[0]
Fuel = Lbl_fuel.transform([fuel])[0]
Tran = Lbl_transmission.transform([transmission])[0]
Sell = Lbl_owner.transform([owner_type])[0]


input_data = [Brand, year, km_driven, Fuel, Tran, Sell, mileage, engine_size, power, seats]

if st.button('Predict Price'):
   
    scaled_input = scalerX.transform([input_data])
    
    
    predicted_value = reg_moduel.predict(scaled_input)
    
    
    predicted_price = scalery.inverse_transform([predicted_value])
    
    st.write(f"Predicted Price: ₹ {predicted_price[0][0]:,.2f}")
