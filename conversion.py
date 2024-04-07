import streamlit as st

def kilogram_to_pound(weight_kg):
    return weight_kg * 2.20462

def kilometer_to_mile(distance_km):
    return distance_km * 0.621371

def celsius_to_fahrenheit(temp_c):
    return (temp_c * 9/5) + 32

def main():
    st.title("Konwerter jednostek")
    
    option = st.selectbox(
        "Wybierz konwersję:",
        ("Kilogramy na Funty", "Kilometry na Mile", "Stopnie Celsiusza na Stopnie Fahrenheita")
    )

    if option == "Kilogramy na Funty":
        weight_kg = st.number_input("Wpisz wagę w kilogramach")
        weight_lb = kilogram_to_pound(weight_kg)
        st.write(f"{weight_kg} kg = {weight_lb} lb")

    elif option == "Kilometry na Mile":
        distance_km = st.number_input("Wpisz odległość w kilometrach")
        distance_mi = kilometer_to_mile(distance_km)
        st.write(f"{distance_km} km = {distance_mi} mi")

    elif option == "Stopnie Celsiusza na Stopnie Fahrenheita":
        temp_c = st.number_input("Wpisz temperaturę w stopniach Celsiusza")
        temp_f = celsius_to_fahrenheit(temp_c)
        st.write(f"{temp_c} C = {temp_f} F")

if __name__ == "__main__":
    main()
