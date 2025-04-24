import streamlit as st
import pickle
import pandas as pd

# Cargar el modelo
with open(r'C:\Users\cuell\Downloads\Regresiones_lineales\modelo_precio_auto.pkl', 'rb') as f:
    modelo_info = pickle.load(f)


model = modelo_info['model']
features = modelo_info['features']

# Layout de la app
st.title('Predicción de precio de autos usados')
st.write('Este es un modelo de predicción de precios de autos usados basado en características como el año del modelo, el kilometraje, el tamaño del motor, los caballos de fuerza y el tipo de combustible.')
st.write('Por favor, ingrese las características del auto para predecir su precio.')



# Inputs del usuario para el automóvil

brand = st.selectbox('Marca', ['Toyota', 'Honda', 'Ford', 'BMW', 'Audi', 'Hyundai', 'Kia'])
fuel_type = st.selectbox('Tipo de combustible', ['Gasoline', 'Diesel', 'Hybrid', 'Electric'])
model_year = st.slider('Año del modelo', 2005, 2024, 2015)
mileage = st.number_input('Kilometraje (en miles)', min_value=0.0, step=0.5)
engine_size = st.slider('Tamaño del motor (litros)', 1.0, 5.0, 2.0)
horsepower = st.slider('Caballos de fuerza', 70, 400, 150)

# Input para el nombre del usuario
user_name = st.text_input('Ingrese su nombre:')


# Diccionario de modificación para el tipo de combustible
fuel_modifier = {'Gasoline': 0, 'Diesel': 1000, 'Hybrid': 3000, 'Electric': 5000}

# Crear entrada con las características correctas
input_data = {col: 0 for col in features}
input_data.update({
    'model_year': model_year,
    'mileage': mileage,
    'engine_size': engine_size,
    'horsepower': horsepower,
    'fuel_modifier': fuel_modifier[fuel_type],
})

# Codificación one-hot de la marca
brand_col = f'brand_{brand}'
if brand_col in features:  # Verificamos si la columna de la marca existe
    input_data[brand_col] = 1

# Convertir a DataFrame
input_df = pd.DataFrame([input_data])

# Variable para almacenar los autos más caros en la sesión
if 'expensive_cars' not in st.session_state:
    st.session_state.expensive_cars = []

# Predecir el precio
if st.button('Predecir precio'):
    try:
        pred = model.predict(input_df)[0]
        st.success(f'Precio estimado para {user_name}: ${pred:,.2f}')
        
        # Almacenar el auto más caro en la lista
        st.session_state.expensive_cars.append({
            'nombre': user_name,
            'modelo': brand,
            'precio': pred
        })
        
        # Mostrar la lista de los autos más caros
        st.write("### Vehículos más caros:")
        expensive_cars_df = pd.DataFrame(st.session_state.expensive_cars)
        expensive_cars_df = expensive_cars_df.sort_values(by='precio', ascending=False)  # Ordenar por precio
        st.write(expensive_cars_df[['nombre', 'modelo', 'precio']])

    except Exception as e:
        st.error(f'Error al hacer la predicción: {str(e)}')

