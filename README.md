# BSB Mini Task-3 | NYC Taxi Trip Duration – Exploratory Data Analysis

This repository contains an exploratory data analysis (EDA) of the **New York City Taxi Trip Duration** dataset from Kaggle.  
I have used Python (pandas, NumPy, Matplotlib, Seaborn) to visualize and analyze the trips.

---

## 📄 Dataset Description

The dataset contains more than **1.45 million taxi trips** collected in New York City.  
Each record includes:

- `id`: Unique identifier for each trip  
- `vendor_id`: Taxi company identifier (1 or 2)  
- `pickup_datetime` & `dropoff_datetime`: Timestamps of the trip  
- `passenger_count`: Number of passengers  
- `pickup_longitude`, `pickup_latitude`: Pickup coordinates  
- `dropoff_longitude`, `dropoff_latitude`: Drop-off coordinates  
- `store_and_fwd_flag`: Whether the trip record was stored before being sent  
- `trip_duration`: Duration of the trip in seconds  

I also derived additional columns such as **pickup hour**, **pickup day of week**, and **trip distance (km)** for deeper insights.

---

## 📊 Visualizations

Below are screenshots of the key charts generated during the analysis (see the `plots/` folder for PNGs):

| Chart | Screenshot |
|-------|------------|
| **Daily Ride Counts** | ![Daily Ride Counts]<img width="1200" height="500" alt="image" src="https://github.com/user-attachments/assets/2fedd3bd-abae-45e1-8e05-cb79556f73ba" />|
| **Pickup Hour Distribution** | ![Pickup Hour Distribution]<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/1a801926-6a4f-4771-bd31-a07b62c766d3" />|
| **Trip Duration Distribution (log scale)** | ![Trip Duration Distribution]<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/7ba82102-f95e-4c57-93a4-b699075c155c" />|
| **Distance vs Duration Hexbin** | ![Distance vs Duration]<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/9b7f0415-c216-4daa-afb6-85c7df66ce0d" />|
| **Trip Duration by Passenger Count (Boxplot)** | ![Trip Duration by Passenger Count]<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/326063fe-4c50-4449-a07b-d1bcc5c425dc" />|
| **Pickup Locations (sample scatter)** | ![Pickup Locations]<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/2e442ef9-4a73-4b65-bb4e-fc7ab8113a12" />|
| **Correlation Matrix** | ![Correlation Matrix]<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/84978b64-92c4-4856-acb9-c40f49fce15f" />|
| **Avg Trip Duration by Day of Week and Hour (Heatmap)** | ![Heatmap]<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/c249587e-26e6-4465-9efe-9c83a40a15bd" />|

---

## 📝 Insights & Observations

- **Ride Volume Over Time**: The number of trips varies by day, with noticeable dips on some holidays/weekends.  
- **Peak Hours**: Most pickups occur during **morning rush (7–9 AM)** and **evening rush (5–8 PM)**.  
- **Trip Duration Distribution**: The majority of trips last under 20 minutes; a long tail indicates a small number of very long trips.  
- **Distance vs Duration**: Strong positive relationship for normal trips; outliers may represent traffic congestion or unusual routes.  
- **Passenger Count**: Most rides have 1 passenger; median trip duration does not change much for higher counts.  
- **Spatial Patterns**: Pickup scatterplot shows dense clusters in Manhattan, JFK, and LaGuardia areas.  
- **Correlations**: Trip distance correlates moderately with trip duration; passenger count shows little correlation.  
- **Heatmap by Day & Hour**: Trips tend to last longer during **rush hours** across all weekdays.  

---

## 🛠️ How to Reproduce

1. Clone this repository.
2. Install dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn
