# NYC Taxi Trip Duration – Exploratory Data Analysis

This repository contains an exploratory data analysis (EDA) of the **New York City Taxi Trip Duration** dataset from Kaggle.  
We use Python (pandas, NumPy, Matplotlib, Seaborn) to visualize and analyze the trips.

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

We also derived additional columns such as **pickup hour**, **pickup day of week**, and **trip distance (km)** for deeper insights.

---

## 📊 Visualizations

Below are screenshots of the key charts generated during the analysis (see the `plots/` folder for PNGs):

| Chart | Screenshot |
|-------|------------|
| **Daily Ride Counts** | ![Daily Ride Counts](plots/rides_per_day.png) |
| **Pickup Hour Distribution** | ![Pickup Hour Distribution](plots/hour_distribution.png) |
| **Trip Duration Distribution (log scale)** | ![Trip Duration Distribution](plots/trip_duration_dist_log.png) |
| **Distance vs Duration Hexbin** | ![Distance vs Duration](plots/distance_vs_duration_hexbin.png) |
| **Trip Duration by Passenger Count (Boxplot)** | ![Trip Duration by Passenger Count](plots/trip_duration_by_passenger_box.png) |
| **Pickup Locations (sample scatter)** | ![Pickup Locations](plots/pickup_spatial_scatter.png) |
| **Correlation Matrix** | ![Correlation Matrix](plots/correlation_matrix.png) |
| **Avg Trip Duration by Day of Week and Hour (Heatmap)** | ![Heatmap](plots/heatmap_dow_hour_duration.png) |

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
