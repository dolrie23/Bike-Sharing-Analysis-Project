# Data Analysis Project with Streamlit
This repository contains a data analysis project built using Streamlit, 
Python libraries that allows for the creation of useful analysis and intuitive 
web applications for data visualization.

## Introduction
The goal of this project is to implement:
1. The Basic of Data  Analysis
3. Application of Basics Descriptive Statistics 
4. Considerations in Data Processing 
5. Data Wrangling 
6. Exploratory Data Analysis 
7. Data Visualization 
8. Dashboard Development (Streamlit)

## Table of Contents
- **[Introduction](#Introduction)**
- **[Features](##Features)**
- **[Installation Step](#Installation-Step)**
- **[Dashboard](#Dashboard)**
- **[Project Structures](#Project-Structures)**
- **[Library](#Library)**

## Features

- Usefull data visualizations
- Filtered data and explored data
- Uploadable dataset
- Intuitive dashboard

## Installation Step
### Clone this Repository to your local
If you have git, use this code:
```shell
git clone https://github.com/dolrie23/Bike-Sharing-Analysis-Dicoding.git
cd Bike-Sharing-Analysis-Dicoding
```
or just install manually from download button above.

Create new virtual environment
```shell
python -m venv venv
source venv/bin/activate
```

### Install Dependencies
```shell
pip install -r requirements.txt
```

## Dashboard
### Run the Dashboard
Type on your cmd or terminal:
```shell
cd dashboard
streamlit run Dashboard.py
```

### Deployed Dashboard
Here is the link 💁‍♂️ [Data_Analysis_Project](https://bike-sharing-analysis-project.streamlit.app/)

## Project Structures
```bash
.
├── dashboard
│   ├── Dashboard.py
│   ├── day_dataset.csv
│   ├── hour_dataset.csv
├── data
│   ├── hour.csv
│   ├── day.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Library
- Streamlit: For building the web interface. 
- Numpy & Pandas: For data manipulation.
- Matplotlib & Seaborn: For data visualization.