# 🤟 ASL Alphabet Recognition with CNN

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-CNN-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📌 Description du projet

Ce projet consiste à développer un modèle de **Deep Learning basé sur un réseau de neurones convolutif (CNN)** capable de reconnaître les lettres de l'alphabet en **langue des signes américaine (ASL - American Sign Language)** à partir d'images.

L'objectif est de construire un système de classification d'images permettant d'identifier automatiquement un signe manuel parmi plusieurs classes correspondant aux lettres de l'alphabet ASL.

Le projet met également l'accent sur la détection et la réduction du **surapprentissage (overfitting)** grâce à différentes techniques de régularisation.

---

## 🎯 Objectifs

- Charger et préparer un dataset d'images ASL.
- Construire un modèle CNN pour la classification d'images.
- Évaluer les performances du modèle.
- Identifier les problèmes de surapprentissage.
- Appliquer des techniques d'amélioration :
  - Data Augmentation
  - Dropout
  - Batch Normalization
  - Normalisation des images
  - Early Stopping

---

# 🗂️ Structure du projet
Projet-ASL-Alphabet-CNN/
│
├── dataset/
│ ├── A/
│ ├── B/
│ ├── C/
│ └── ...
│
├── notebooks/
│ └── ASL_CNN_training.ipynb
│
├── models/
│ └── asl_cnn_model.h5
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore


---

# 🧠 Architecture du modèle CNN

Le modèle final utilise une architecture CNN composée de :


Input Image
|
Conv2D
|
Batch Normalization
|
MaxPooling
|
Conv2D
|
Batch Normalization
|
MaxPooling
|
Flatten
|
Dense Layer
|
Dropout
|
Softmax Output


### Techniques utilisées :

✅ Convolution 2D pour extraire les caractéristiques visuelles  
✅ Batch Normalization pour stabiliser l'apprentissage  
✅ Dropout pour réduire le surapprentissage  
✅ Data Augmentation pour améliorer la généralisation  

---

# 📊 Résultats

## Modèle initial (sans régularisation)

| Métrique | Résultat |
|---|---|
| Accuracy entraînement | 100% |
| Accuracy validation | 100% |
| Loss entraînement | 0.000 |
| Loss validation | 0.000 |

Ces résultats indiquaient un risque de surapprentissage ou une séparation trop facile des données.

---

## Modèle amélioré

Après ajout de :

- Data Augmentation
- Dropout
- Batch Normalization

Le modèle devient plus robuste et capable de mieux généraliser sur de nouvelles images.

---

# 🛠️ Technologies utilisées

## Langage

- Python

## Deep Learning

- TensorFlow
- Keras

## Traitement des données

- NumPy
- Pandas
- OpenCV

## Visualisation

- Matplotlib

## Environnement

- Google Colab
- Jupyter Notebook
- VS Code

---

# ⚙️ Installation

## 1. Cloner le projet

```bash
git clone https://github.com/AbdoulKsn/Projet-ASL-Alphabet-CNN.git


Améliorations futures

Quelques évolutions possibles :

Ajouter une détection en temps réel avec webcam.
Déployer le modèle avec Streamlit.
Utiliser Transfer Learning avec :
ResNet50
MobileNetV2
EfficientNet
Convertir le modèle en TensorFlow Lite pour mobile.
👨‍💻 Auteur

Abdoul Kader Koné

🎓 Master Génie Logiciel
📚 Data Science & Machine Learning
💻 Python | TensorFlow | Flutter | Firebase

📜 Licence

Ce projet est distribué sous licence MIT.


### Petit conseil pour ton GitHub :
Ajoute aussi :
- une capture d'écran des résultats (`results.png`)
- une image d'exemple ASL (`asl_demo.png`)
- ton fichier `requirements.txt`