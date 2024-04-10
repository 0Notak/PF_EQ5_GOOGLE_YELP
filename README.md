# PF_EQ5_GOOGLE_YELP

[![image](https://github.com/0Notak/PF_EQ5_GOOGLE_YELP/assets/149798101/3e7b0ccc-84a4-4bba-bfab-8be18e294c2a)](https://camo.githubusercontent.com/953e3aeda5322462b234c4dace6aa8796f4bc6e250efc943c4091b189a6b237e/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f612f61642f59656c705f4c6f676f2e7376672f3235363070782d59656c705f4c6f676f2e7376672e706e67)
 
 

 # PROYECTO DE SISTEMA DE RECOMENDACIONES GOOGLE YELP

 Descripción del Proyecto: Pipeline en GCP para ETL y Modelado de Machine Learning
Introducción

Este repositorio contiene el código y la documentación asociada a un proyecto de pipeline en Google Cloud Platform (GCP) destinado a realizar el proceso de Extracción, Transformación y Carga (ETL) de varios conjuntos de datos en formato Parquet. El objetivo principal del proyecto es llevar a cabo la preparación de datos y el entrenamiento de modelos de Machine Learning utilizando servicios nativos de GCP, como Cloud Storage, Cloud Functions, Cloud SQL y Vertex AI.
Stack Tecnológico

## El stack tecnológico utilizado en este proyecto incluye:
Descripcion visual del Stack tecnologico:

<img src="https://i.ibb.co/xhpWckt/STACK.png" alt="STACK" border="0">



    - Google Cloud Storage: Se utiliza como almacenamiento centralizado para los conjuntos de datos en formato Parquet.

    - Google Cloud Functions: Se implementan funciones en la nube para automatizar tareas específicas dentro del pipeline, como la activación de flujos de trabajo en respuesta a eventos.

    - Google Cloud SQL: Se emplea como base de datos relacional para almacenar metadatos y realizar consultas sobre los datos procesados.

    - Google Vertex AI: Se utiliza para el entrenamiento y la implementación de modelos de Machine Learning, aprovechando la infraestructura y las herramientas de Google para la creación de modelos eficientes y escalables.




## Descripción del Pipeline

El pipeline de datos consta de varias etapas, que se detallan a continuación:

    - Extracción de Datos: Los conjuntos de datos en formato Parquet son extraídos de la aplicación de GCP y almacenados en Google Cloud Storage para su posterior procesamiento.

    - Transformación de Datos: Se aplican transformaciones ETL a los datos almacenados en Cloud Storage, incluyendo limpieza, filtrado y manipulación de datos para prepararlos adecuadamente para el modelado de Machine Learning.

    - Carga de Datos: Los datos transformados se cargan en una base de datos Cloud SQL para su almacenamiento y posterior análisis.

    - Entrenamiento de Modelos: Utilizando los datos almacenados en Cloud SQL, se entrenan modelos de Machine Learning en Google Vertex AI. Se exploran diferentes algoritmos y técnicas de modelado para obtener los mejores resultados posibles.

    - Evaluación y Despliegue de Modelos: Una vez entrenados, los modelos se evalúan utilizando métricas de rendimiento específicas y se despliegan en producción para su uso en la aplicación de GCP.



## **Cronograma**

El proyecto se desarrollará en un período de 3 semanas, con tres sprint que son los siguientes:
- Sprint 1: Puesta en macha del proyecto. 1 Semana
- Sprint 2: Data Engineering. 1 Semana
- Sprint 3: Data Analitics y Machine learning. 1 Semana

.

Revisar: [Cronograma o Modelo de Grantt](https://github.com/0Notak/PF_EQ5_GOOGLE_YELP/blob/rama_Daniel/EXTRA/MODELO%20GRANTT%20EQ5.pdf)
<p align="right">(<a href="#readme-top">ir arriba</a>)</p>

## **Fuentes de datos**

+   [Diccionario de Datos](https://docs.google.com/document/d/1ASLMGAgrviicATaP1UJlflpmBCXtuSTHQGWdQMN6_2I/edit)

Fuentes de datos obligatorias:
+   [Dataset de Google Maps](https://drive.google.com/drive/folders/1Wf7YkxA0aHI3GpoHc9Nh8_scf5BbD4DA?usp=share_link)
+   [Dataset de Yelp!](https://drive.google.com/drive/folders/1TI-SsMnZsNP6t930olEEWbBQdo_yuIZF?usp=sharing)
<p align="right">(<a href="#readme-top">ir arriba</a>)</p>

## Integrantes

- Hevert Daniel Martinez Dominguez | Data Engineer | [Link Github](https://github.com/0Notak)
- Marko Misael Sotola | Machine Learning Engineer | [Link Github](https://github.com/marko7768) 
- Max Enoc Moreno Navarrete |  Data Analyst | [Link Github](https://github.com/MENM-HRRY)


