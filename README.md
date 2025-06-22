
# 📊 Sales Trend Analysis Dashboard

This is a simple interactive dashboard built using **Streamlit** to visualize and analyze sales trends over time.

## About the Dataset
The dataset used in this project is based on a publicly available **Sales Data** CSV inspired by [Keith Galli's Sales Analysis task](https://www.kaggle.com/datasets/beekiran/sales-data-analysis).

It includes fictional order information from an electronics store and contains fields like:

- `Order ID` – Unique identifier for each transaction  
- `Product` – Name of the product sold  
- `Quantity Ordered` – Units sold  
- `Price Each` – Unit price  
- `Order Date` – Date of transaction  
- `Sales` – Total sale value (calculated)  
- `City` – Location of the purchase

  ###  What We Did with the Data

- Cleaned the dataset (removed NaNs, converted date columns)
- Added new columns (like `Sales` and `Month`)
- Built an interactive **Streamlit dashboard** to:
  - Visualize total sales over time
  - Track top-selling products
  - Display KPIs like total sales and best city
  - Allow dynamic filtering by product and month
    
### A cleaned sample of the dataset is available in this repo:
[📎 Download Cleaned CSV](https://raw.githubusercontent.com/Anusruthy/sales-trend-streamlit/main/cleaned_sales_data.csv)

## Features

- Upload cleaned CSV sales data
- Interactive line chart for sales over time
-  Key Metrics:
  - Total Sales
  - Top Selling Product
- Top 5 Products by Total Sales
- Filters using sidebar which will give details about each products trend in each month.

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly

## How to Use ?

1. Clone this repo or open it in Streamlit Cloud.
2. Upload your cleaned sales CSV file.
3. Use the sidebar to filter the data.
4. Explore KPIs and visualizations.

##  Live App

👉 [Click to Open Streamlit App] (https://anusruthy-sales-trend-analysis-sale-trend-view-r7xy0b.streamlit.app/)
