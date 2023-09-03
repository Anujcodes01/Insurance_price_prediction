# Insurance Premium Prediction

## How To Start
### Creat Environment
```
conda create -p venv python==3.8 -y
```
### Activate Environment
```
conda activate venv/
```
### Install Requirements 
```
pip install -r requirements.txt
```

## Problem Statement

The goal of this project is to give people an estimate of how much they need based on
their individual health situation. After that, customers can work with any health
insurance carrier and its plans and perks while keeping the projected cost from our
study in mind. This can assist a person in concentrating on the health side of an
insurance policy rather han the ineffective part.



**Project Goal: Enhancing Informed Health Insurance Decisions**

1. **Personalized Health Cost Estimation:** The project aims to provide individuals with a tailored estimate of how much health coverage they need based on their unique health situation. This personalized approach takes into account factors such as age, health status, lifestyle, and family composition. By offering a precise estimate, individuals can better understand their insurance needs.

2. **Open Access to Insurance Options:** Beyond estimating insurance needs, the project aims to empower customers by providing them the flexibility to explore health insurance carriers, their plans, and associated benefits comprehensively. This approach ensures that individuals can choose insurance providers that align with their specific health requirements and preferences.

3. **Cost Awareness:** By keeping the projected cost from the study in mind, the project promotes cost-conscious decision-making. Individuals can focus on optimizing their health coverage based on their estimated needs, avoiding overpayment for unnecessary features or underinsurance.

4. **Health-Centric Approach:** The project encourages individuals to concentrate on the health-related aspects of their insurance policies. This shift in focus ensures that individuals prioritize the adequacy of their coverage, ensuring they receive the necessary medical care when needed, rather than being preoccupied with extraneous or ineffective policy elements.

In summary, the primary aim of this project is to demystify the health insurance landscape, making it more accessible and transparent for individuals. By providing personalized estimates, access to diverse insurance options, and a heightened focus on health-centric decision-making, the project equips individuals with the tools they need to secure insurance coverage that genuinely meets their health needs, ultimately fostering a healthier and more financially secure population.

## Dataset:-
```
https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction
```
## Project Various Steps:-
### Data Ingestion
The cornerstone of our data-driven project was established through a systematic process of data acquisition and ingestion. Utilizing Kaggle, a reputable platform renowned for its high-quality datasets, we identified and acquired the crucial data required for our price prediction project. This dataset, integral to our goal of accurate price forecasting, was meticulously downloaded and securely stored within our local system infrastructure. Subsequently, we initiated the data ingestion phase, where the dataset seamlessly integrated into our project's data pipeline. This meticulous approach ensures that our project is built upon a solid foundation, setting the stage for robust and precise price prediction models and analysis.

### Data transformation
Steps performed in pre-processing are:
- • First read data from Artifact folder
- • Checking unnecessary columns
- • One column has product id which is unique for every product so I deleted that column.
- • Checked for null values
- • there are too many null values are present in two columns that’s why I deleted them
- • Performed one-hot encoder on categorical columns.
- • Scaling is performed for needed information.
- • And, the info is prepared for passing to the machine learning formula

### Modelling
The pre-processed information is then envisioned and every one the specified insights are being drawn. though from the drawn insights, the info is at random unfold however still modelling is performed with completely different machine learning algorithms to form positive we tend to cowl all the chances. and eventually, Gradient Boosting performed well .

### Batch Prediction

In the pursuit of creating a comprehensive and efficient system, we have successfully executed batch prediction as a pivotal component of our project. Leveraging a meticulously designed data transformation pipeline, we have harnessed the power of our predictive model to generate accurate and timely batch predictions. This milestone signifies the culmination of our efforts in seamlessly processing and analyzing data, resulting in actionable insights that drive informed decision-making. As we prepare our Low-Level Design Document, this achievement underscores the significance of our data transformation pipeline and predictive model, which will be elaborately detailed to ensure clarity and scalability in our system architecture.

### Training And Prediction Pipeline

In our endeavor to create a robust and end-to-end data-driven solution, we have meticulously crafted both a training pipeline and a prediction pipeline. The training pipeline serves as the backbone for developing our predictive models, allowing us to iteratively train and fine-tune them with the highest precision possible. Meanwhile, the prediction pipeline enables us to seamlessly apply these trained models to new data, ensuring that our insights and forecasts remain consistently accurate and adaptable to real-world scenarios. This dual pipeline approach embodies our commitment to providing a comprehensive, data-driven solution that empowers decision-makers with the most reliable and up-to-date information. As we delve into the creation of our Low-Level Design Document, we will intricately detail these pipelines, showcasing their sophistication and efficiency in our system architecture.

### UI Integration

Both CSS and HTML files are being created and are being integrated with the created machine learning model. All the required files are then integrated to the app.py(For localhost), Application.py(For Streamlit) file and tested locally

## Project Link - 
```

```

## Vedio Url - 

```
https://youtu.be/FjbVNcU9_nw?si=LwGuBgbq3Gwaq03j

```