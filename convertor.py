import streamlit as st

def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Inches": 39.3701,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Miles": 0.000621371,
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Grams": 1,
        "Kilograms": 0.001,
        "Milligrams": 1000,
        "Pounds": 0.00220462,
        "Ounces": 0.035274,
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

def main():
    st.title("Unit Converter")
    
    option = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
    
    if option == "Length":
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"])
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"])
        value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
        if st.button("Convert"):
            result = convert_length(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    
    elif option == "Weight":
        from_unit = st.selectbox("From", ["Grams", "Kilograms", "Milligrams", "Pounds", "Ounces"])
        to_unit = st.selectbox("To", ["Grams", "Kilograms", "Milligrams", "Pounds", "Ounces"])
        value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
        if st.button("Convert"):
            result = convert_weight(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    
    elif option == "Temperature":
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
        value = st.number_input("Enter Value", format="%.2f")
        if st.button("Convert"):
            result = convert_temperature(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

if __name__ == "__main__":
    main()
