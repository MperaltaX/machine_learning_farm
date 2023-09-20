# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:44:28 2023

@author: Mattias
"""
import numpy as np
np.seterr(all='raise')
import tkinter as tk
from tkinter import ttk
import os
from tkinter import filedialog
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score





def trainingSVM():
    testsize = float(test_var.get())
    # Obtener la ruta del archivo seleccionado
    ruta_archivo = ruta_archivo_var.get()
    # Obtener la ruta del archivo seleccionado
    nuevos_datos_file = ruta_archivo_var_test.get()
    try:
        # Cargar los nuevos datos desde el archivo CSV
        nuevos_datos = pd.read_csv(nuevos_datos_file, delimiter=';')
    except pd.errors.ParserError:
        mensaje_label.config(text='No se pudo cargar el archivo de nuevos datos.')
        return
    
    # Cargar los datos desde el archivo CSV
    data = pd.read_csv(ruta_archivo, delimiter=';')

    # Separar las características (X) y las etiquetas (y)
    X = data.iloc[:, :-1]  # Todas las columnas excepto la última
    y = data['menor-mayor-30']  # La columna de etiquetas

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testsize, random_state=42)

    # Crear un modelo SVM (puedes ajustar los hiperparámetros según sea necesario)
    svm_model = SVC(kernel='linear', C=1.0)

    # Entrenar el modelo en los datos de entrenamiento
    svm_model.fit(X_train, y_train)

    # Realizar predicciones en el conjunto de prueba
    y_pred = svm_model.predict(X_test)

    # Calcular la precisión del modelo en el conjunto de prueba
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Precisión del modelo SVM: {accuracy * 100:.2f}%')
    # Mostrar mensaje
    mensaje_label.config(text=f'Precisión del modelo SVM: {accuracy * 100:.2f}%', wraplength=230)
    
    
    # Hacer predicciones en los nuevos datos
    nuevas_predicciones = svm_model.predict(nuevos_datos)
    
    # Crear un DataFrame con las predicciones y agregarlo a los nuevos datos
    nuevos_datos_con_predicciones = nuevos_datos.copy()
    nuevos_datos_con_predicciones['menor-mayor-30'] = nuevas_predicciones
    
    # Obtener la ruta del directorio donde se encuentra este script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Combinar la ruta del directorio actual con el nombre del archivo de salida
    ruta_salida = os.path.join(directorio_actual, 'nuevas_predicciones.csv')
    
    # Guardar el DataFrame con las predicciones en un nuevo archivo CSV
    nuevos_datos_con_predicciones.to_csv(ruta_salida, sep=';', index=False)
    
    mensaje_label0.config(text='Predicciones exportadas a ' + ruta_salida, wraplength=230)
            
 
def trainingSVMTest():  
    testsize = float(test_var2.get())
    # Obtener la ruta del archivo seleccionado
    ruta_archivo = ruta_archivo_var2.get()
    # Obtener la ruta del archivo seleccionado Test
    nuevos_datos_file2 = ruta_archivo_var_test2.get()

    
    # Cargar los datos desde el archivo CSV
    data = pd.read_csv(ruta_archivo, delimiter=';')
    
    # Separar las características (X) y las etiquetas (y)
    X = data.iloc[:, :-1]  # Todas las columnas excepto la última
    y = data['menor-mayor-30']  # La columna de etiquetas

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testsize, random_state=42)

    # Crear un modelo SVM (puedes ajustar los hiperparámetros según sea necesario)
    svm_model = SVC(kernel='linear', C=1.0)

    # Entrenar el modelo en los datos de entrenamiento
    svm_model.fit(X_train, y_train)

    # Realizar predicciones en el conjunto de prueba
    y_pred = svm_model.predict(X_test)

    # Calcular la precisión del modelo en el conjunto de prueba
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Precisión del modelo SVM: {accuracy * 100:.2f}%')
    # Mostrar mensaje
    mensaje_label1.config(text=f'Precisión del modelo SVM: {accuracy * 100:.2f}%', wraplength=230)
    
    # Cargar los datos de prueba desde otro archivo CSV
    data_test = pd.read_csv(nuevos_datos_file2, delimiter=';')
    
    X_test = data_test.iloc[:, :-1]  # Todas las columnas excepto la última
    y_test = data_test['menor-mayor-30']  # La columna de etiquetas

    # Realizar predicciones en el conjunto de prueba
    y_pred_test = svm_model.predict(X_test)

    # Calcular la precisión del modelo en el conjunto de prueba de prueba
    accuracy_test = accuracy_score(y_test, y_pred_test)
    print(f'Precisión del modelo SVM en el conjunto de prueba: {accuracy_test * 100:.2f}%')
    mensaje_label2.config(text=f'Precisión del modelo SVM en el conjunto de prueba: {accuracy_test * 100:.2f}%', wraplength=230)
    
    

    
    
        
def ejecutar_svm():
    try:
        trainingSVM()
    except Exception as e:
        mensaje_label.config(text=f'Ocurrió un error: {str(e)}', wraplength=230)

def ejecutar_svm_test():
    try:
        trainingSVMTest()
    except Exception as e:
        mensaje_label2.config(text=f'Ocurrió un error: {str(e)}', wraplength=230)

# Función para obtener la ruta del archivo
def obtener_ruta():
    ruta_archivo = filedialog.askopenfilename()
    ruta_archivo_var.set(ruta_archivo)
    
def obtener_ruta_test():
    ruta_archivo_test = filedialog.askopenfilename()
    ruta_archivo_var_test.set(ruta_archivo_test)  
    
    
def obtener_ruta2():
    ruta_archivo2 = filedialog.askopenfilename()
    ruta_archivo_var2.set(ruta_archivo2)
    
def obtener_ruta_test2():
    ruta_archivo_test2 = filedialog.askopenfilename()
    ruta_archivo_var_test2.set(ruta_archivo_test2)  
    
    
# Funciones para alternar entre las pestañas
def mostrar_ventana1():
    notebook.select(tab1)

def mostrar_ventana2():
    notebook.select(tab2)
    
    


# Crear ventana
ventana = tk.Tk()

# Configurar ventana
ventana.title("Machine Learning")
ventana.geometry("300x450")

# Crear un Notebook (pestañas)
notebook = ttk.Notebook(ventana)
notebook.pack(pady=10)

# Crear pestaña 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Entrenar y ejecutar")

# Contenido de la pestaña 1
# Agregar un Frame para salto de linea
frame = tk.Frame(tab1)
frame.pack(pady=10)


# Crear etiqueta y campo de entrada para la cantidad
etiqueta_test = tk.Label(tab1, text=" Porcentaje del conjunto de pruebas (valor de 0 a 1) ")
etiqueta_test.pack()
test_var = tk.StringVar()
entrada_test = tk.Entry(tab1, textvariable=test_var)
entrada_test.pack()


# Crear botón para seleccionar archivo
ruta_archivo_var = tk.StringVar()
ruta_archivo_label = tk.Label(tab1, text='Seleccione el archivo CSV de entrenamiento')

# Agregar un Frame para salto de linea
frame = tk.Frame(tab1)
frame.pack(pady=10)
ruta_archivo_label.pack()
ruta_archivo_entry = tk.Entry(tab1, textvariable=ruta_archivo_var)
ruta_archivo_entry.pack()

# Agregar un Frame para salto de linea
frame = tk.Frame(tab1)
frame.pack(pady=10)

# Crear botón para seleccionar archivo
seleccionar_archivo_button = tk.Button(tab1, text='Seleccionar', command=obtener_ruta)
seleccionar_archivo_button.pack()



# Crear botón para seleccionar archivo
ruta_archivo_var_test = tk.StringVar()
ruta_archivo_label_test = tk.Label(tab1, text='Seleccione el archivo CSV a Predecir')

# Agregar un Frame para salto de linea
frame_test = tk.Frame(tab1)
frame_test.pack(pady=10)
ruta_archivo_label_test.pack()
ruta_archivo_entry_test = tk.Entry(tab1, textvariable=ruta_archivo_var_test)
ruta_archivo_entry_test.pack()

# Agregar un Frame para salto de linea
frame = tk.Frame(tab1)
frame.pack(pady=10)

# Crear botón para seleccionar archivo
seleccionar_archivo_button_test = tk.Button(tab1, text='Seleccionar', command=obtener_ruta_test)
seleccionar_archivo_button_test.pack()

# Agregar un Frame para salto de linea
frame = tk.Frame(tab1)
frame.pack(pady=10)

# Crear botón para ejecutar SVM
ejecutar_button = tk.Button(frame, text='Ejecutar SVM', command=ejecutar_svm)
ejecutar_button.pack(side="left", padx=10)




# Crear etiqueta para mensaje
mensaje_label = tk.Label(tab1, text='')
mensaje_label.pack()

# Crear etiqueta para mensaje
mensaje_label0 = tk.Label(tab1, text='')
mensaje_label0.pack()

# Agregar un Frame para salto de linea
frame = tk.Frame(tab1)
frame.pack(pady=50)


# Crear pestaña 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Entrenar y comparar")


# Contenido de la pestaña 2
# Agregar un Frame para salto de linea
frame = tk.Frame(tab2)
frame.pack(pady=10)


# Crear etiqueta y campo de entrada para la cantidad
etiqueta_test = tk.Label(tab2, text=" Porcentaje del conjunto de pruebas (valor de 0 a 1) ")
etiqueta_test.pack()
test_var2 = tk.StringVar()
entrada_test = tk.Entry(tab2, textvariable=test_var2)
entrada_test.pack()

# Crear botón para seleccionar archivo
ruta_archivo_var2 = tk.StringVar()
ruta_archivo_label = tk.Label(tab2, text='Seleccione el archivo CSV de entrenamiento')

# Agregar un Frame para salto de linea
frame = tk.Frame(tab2)
frame.pack(pady=10)
ruta_archivo_label.pack()
ruta_archivo_entry = tk.Entry(tab2, textvariable=ruta_archivo_var2)
ruta_archivo_entry.pack()

# Agregar un Frame para salto de linea
frame = tk.Frame(tab2)
frame.pack(pady=10)

# Crear botón para seleccionar archivo
seleccionar_archivo_button = tk.Button(tab2, text='Seleccionar', command=obtener_ruta2)
seleccionar_archivo_button.pack()



# Crear botón para seleccionar archivo
ruta_archivo_var_test2 = tk.StringVar()
ruta_archivo_label_test = tk.Label(tab2, text='Seleccione el archivo CSV de Test a comparar')

# Agregar un Frame para salto de linea
frame_test = tk.Frame(tab2)
frame_test.pack(pady=10)
ruta_archivo_label_test.pack()
ruta_archivo_entry_test = tk.Entry(tab2, textvariable=ruta_archivo_var_test2)
ruta_archivo_entry_test.pack()

# Agregar un Frame para salto de linea
frame = tk.Frame(tab2)
frame.pack(pady=10)

# Crear botón para seleccionar archivo
seleccionar_archivo_button_test = tk.Button(tab2, text='Seleccionar', command=obtener_ruta_test2)
seleccionar_archivo_button_test.pack()

# Agregar un Frame para salto de linea
frame = tk.Frame(tab2)
frame.pack(pady=10)

# Crear botón para ejecutar SVM
ejecutar_button = tk.Button(frame, text='Ejecutar SVM', command=ejecutar_svm_test)
ejecutar_button.pack(side="left", padx=10)




# Crear etiqueta para mensaje
mensaje_label1 = tk.Label(tab2, text='')
mensaje_label1.pack()

# Crear etiqueta para mensaje
mensaje_label2 = tk.Label(tab2, text='')
mensaje_label2.pack()

# Agregar un Frame para salto de linea
frame = tk.Frame(tab2)
frame.pack(pady=50)


# Ejecutar ventana
ventana.mainloop()
