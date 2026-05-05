import pandas as pd
import numpy as np
import hashlib

# Cargar la base de datos
df = pd.read_excel("Base de Datos.xlsx")

# -----------------------------
# 0. SUPRESIÓN
# -----------------------------
df = df.drop(columns=['Nombre completo', 'Teléfono'])

# -----------------------------
# 1. GENERALIZACIÓN DE EDAD
# -----------------------------
df['Edad'] = pd.cut(df['Edad'],
                    bins=[0,18,30,50,100],
                    labels=['0-18','19-30','31-50','51+'])

# -----------------------------
# 2. CODIFICACIÓN DE GÉNERO
# -----------------------------
df['Género'] = df['Género'].map({
    'Masculino': 1,
    'Femenino': 2
})

# -----------------------------
# 3. GENERALIZACIÓN CÓDIGO POSTAL
# -----------------------------
df['Código postal'] = df['Código postal'].astype(str).str[:3] + "XX"

# -----------------------------
# 4. GENERALIZACIÓN DE DIAGNÓSTICO
# -----------------------------
def clasificar_diagnostico(x):
    if 'Diabetes' in x or 'Obesidad' in x:
        return 'Enfermedad metabólica'
    elif 'Cáncer' in x:
        return 'Enfermedad oncológica'
    elif 'Asma' in x or 'pulmonar' in x:
        return 'Enfermedad respiratoria'
    elif 'cardíaca' in x or 'Infarto' in x or 'Hipertensión' in x:
        return 'Enfermedad cardiovascular'
    elif 'Depresión' in x or 'ansiedad' in x or 'bipolar' in x or 'obsesivo' in x:
        return 'Trastorno mental'
    elif 'Alzheimer' in x or 'Parkinson' in x:
        return 'Enfermedad neurológica'
    else:
        return 'Otra condición'

df['Diagnóstico'] = df['Diagnóstico'].apply(clasificar_diagnostico)

# -----------------------------
# 5. PERTURBACIÓN (RUIDO ALEATORIO)
# -----------------------------
df['Ingresos anuales'] = df['Ingresos anuales'] + np.random.normal(0, 5, len(df))

# -----------------------------
# 6. SEUDONIMIZACIÓN (ID HASH)
# -----------------------------
df['ID'] = [hashlib.sha256(str(i).encode()).hexdigest() for i in df.index]

# -----------------------------
# GUARDAR BASE ANONIMIZADA
# -----------------------------
df.to_excel("Base_Anonimizada.xlsx", index=False)

print("Anonimización completa correctamente.")