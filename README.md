# machine_learning_farm
Software que predice si el animal tendrá un bajo peso al nacer, permite ser entrenado con datos propios.
Utiliza las máquinas de vectores de soporte como conjunto de algoritmo de aprendizaje supervisado. 
Te dejo datos CSV para que puedas realizar una prueba y comprender el funcionamiento del modelo. 

El algoritmo es entrenado mediante archivos CSV con Dep's de madre y padre para obtener el resultado de si pesará más o menos de 30 kilos al nacer, 
lo cual es muy importante en el ambito ganadero.

## Funcionamiento
Pestaña "Entrenar y Ejecutar"
-  ![](https://i.imgur.com/kiBgHW0.png)
-  Porcentaje del conjunto de pruebas: Es el porcentaje que se tomará de tu archivo "data.csv" para comparar el entrenamiento del modelo y obtener un porcentaje de acierto.
-  Seleccione el archivo CSV de entrenamiento: Selecciona el archivo "data.csv", que servirá como entrenamiento para que el modelo aprenda.
-  Seleccione el archivo a predecir: Selecciona el archivo que el modelo deverá predecir. Este archivo no debe contener la última columna "menor-mayor-30". Te dejo el archivo "data_to_predict.csv" para que puedas probarlo. 
-  Ejecutar SVM: Ejecuta el modelo, se entrena y devuelve el porcentaje de acierto del algoritmo, además crea un nuevo CSV con los resultados de la predicción de los datos del archivo "data_to_predict.csv".

Pestaña "Entrenar y Ejecutar"
-  ![](https://i.imgur.com/hvi9kdg.png)
-  
