import pandas as pd
import numpy as np
import random
from datetime import datetime

# Definir datos de ejemplo
nombres = ["Juan", "María", "Carlos", "Ana", "Pedro", "Laura", "Diego", "Sofia", "Luis", "Carmen"]
apellidos = ["García", "Martínez", "López", "González", "Rodríguez", "Fernández", "Pérez", "Sánchez", "Torres", "Ramírez"]
niveles_educativos = ["Licenciatura", "Posgrado", "Doctorado", "Maestría"]
carreras = [
    "Ingeniería en Sistemas", "Medicina", "Administración", "Psicología",
    "Arquitectura", "Derecho", "Biología", "Economía", "Física", "Química"
]
instituciones = [
    "Universidad Nacional de Colombia", "Universidad de Antioquia", "Universidad del Valle",
    "Universidad Industrial de Santander", "Universidad de los Andes"
]
departamentos = [
    "Antioquia", "Cundinamarca", "Valle del Cauca", "Santander", "Atlántico",
    "Boyacá", "Caldas", "Risaralda", "Bolívar", "Norte de Santander"
]

# Generar 50 registros
data = []
for _ in range(50):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    edad = random.randint(18, 45)
    nivel = random.choice(niveles_educativos)
    carrera = random.choice(carreras)
    institucion = random.choice(instituciones)
    departamento = random.choice(departamentos)
    promedio = round(random.uniform(3.0, 5.0), 2)  # Ajustado a escala colombiana
    
    data.append({
        'Nombre': f"{nombre} {apellido}",
        'Edad': edad,
        'Nivel educativo': nivel,
        'Carrera': carrera,
        'Institución': institucion,
        'Departamento': departamento,
        'Promedio': promedio
    })

# Crear DataFrame
df = pd.DataFrame(data)

# Asegurar que haya suficientes estudiantes de posgrado para el análisis
posgrado_count = len(df[df['Nivel educativo'] == 'Posgrado'])
if posgrado_count < 10:
    indices = df[df['Nivel educativo'] != 'Posgrado'].index[:10-posgrado_count]
    df.loc[indices, 'Nivel educativo'] = 'Posgrado'

# Guardar el DataFrame en un archivo CSV
df.to_csv('educacion.csv', index=False)

# Mostrar las primeras filas del DataFrame generado
print(df.head())