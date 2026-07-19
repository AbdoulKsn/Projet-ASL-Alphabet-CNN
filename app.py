import streamlit as st
import tensorflow as tf
import numpy as np
import json

from PIL import Image

# Chargement du modèle
model = tf.keras.models.load_model("mnist_cnn.h5")

# Chargement des classes
with open("class_names.json", "r") as f:
    class_names = json.load(f)

st.title("Classification d'images")

st.write("Téléversez une image pour obtenir une prédiction.")

uploaded_file = st.file_uploader(
    "Choisir une image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Image téléversée", use_container_width=True)

    # Prétraitement
    image = image.resize((64,64))

    img = np.array(image)

    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    # Prédiction
    prediction = model.predict(img)

    predicted_class = np.argmax(prediction)

    confidence = np.max(prediction)

    st.success(f"Classe prédite : {class_names[predicted_class]}")

    st.write(f"Confiance : {confidence*100:.2f}%")

    st.subheader("Probabilités")

    st.bar_chart(prediction[0])