# 📊 Sales Trend Analysis Dashboard

An interactive dashboard built using **Streamlit**, **Plotly**, **Pandas**, and **Docker** to visualize and analyze sales trends over time.



## Project Overview

This project demonstrates the power of interactive dashboards in sales analytics. It allows users to:

- Track **monthly sales trends**
- Identify **top-selling products**
- View **total revenue generated**
- Filter sales by **product** and **month**
- Visualize key metrics using interactive charts



## About the Dataset

The dataset used in this project is based on a publicly available **Sales Data** CSV inspired by [Keith Galli's Sales Analysis task](https://www.kaggle.com/datasets/beekiran/sales-data-analysis).

It includes fictional order information from an electronics store with fields like:

- `Order ID` – Unique identifier for each transaction  
- `Product` – Name of the product sold  
- `Quantity Ordered` – Units sold  
- `Price Each` – Unit price  
- `Order Date` – Date of transaction  
- `Sales` – Total sale value (calculated)  
- `City` – Location of the purchase

>  I cleaned the raw data and added calculated fields like `Sales` and `Month`.

📎 [**Download Cleaned CSV**](https://raw.githubusercontent.com/Anusruthy/Sales-Trend-Analysis/main/cleaned_sales_data.csv)



## Features

- Line chart showing sales trend over time  
- KPIs:
  - Total Revenue
  - Top-Selling Product
- Top 5 Products by total sales  
- Sidebar filters by product and month  
- Auto-loads cleaned CSV — no manual upload needed



## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Docker
- Docker Compose



## Live App

👉 [Click to Open Streamlit App](https://anusruthy-sales-trend-analysis-sale-trend-view-r7xy0b.streamlit.app/)



## Run Locally with Docker

If you have Docker installed, you can run this app in seconds.

###  Step 1: Clone the Repository

```bash
git clone https://github.com/Anusruthy/Sales-Trend-Analysis.git
cd Sales-Trend-Analysis 
```

###  Step 2: Run with Docker
This builds the Docker image and runs your app locally:
```bash
docker build -t anusruthy/streamlit-app .
docker run -p 8501:8501 anusruthy/streamlit-app
```
- Then go to the localhost page.



### Run with Docker Compose
```bash
docker-compose up --build
```
This will:
- Build the image from the Dockerfile
- Start the container
- Automatically load the cleaned CSV
- Run the dashboard at localhost.

To stop the app
```bash
docker-compose down
```
### How This Was Built
- Data Cleaning: Used Pandas to remove NaNs, fix datetime formats, and compute additional fields.
- EDA: Grouped data to find monthly and product-wise sales patterns.
- Dashboard: Created with Streamlit + Plotly charts and filtering options.
- Deployment: Containerized with Docker and deployed via Docker Compose.



### Author
Anusruthy R

anusruthyraju@gmail.com


