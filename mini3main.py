#!/usr/bin/env python3
"""
NYC Taxi Trip Duration EDA
Reads NYC.csv, performs exploratory data analysis, and saves plots to ./plots
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import argparse

sns.set(style="whitegrid")

def main(args):
    # Create output directory
    os.makedirs(args.out, exist_ok=True)

# Load dataset
    csv_path = "/Users/mariya/Downloads/NYC.csv"   # <-- your file path
    print(f"Loading {csv_path}...")
    df = pd.read_csv(csv_path, nrows=args.nrows if args.nrows else None)
    print(f"Loaded {len(df):,} rows")
    
    # Convert datetime columns
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])

    # Basic features
    df['pickup_date'] = df['pickup_datetime'].dt.date
    df['pickup_hour'] = df['pickup_datetime'].dt.hour
    df['pickup_dayofweek'] = df['pickup_datetime'].dt.day_name()

    # Trip distance (rough haversine)
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371  # km
        phi1, phi2 = np.radians(lat1), np.radians(lat2)
        dphi = np.radians(lat2 - lat1)
        dlambda = np.radians(lon2 - lon1)
        a = np.sin(dphi/2)**2 + np.cos(phi1)*np.cos(phi2)*np.sin(dlambda/2)**2
        return 2*R*np.arcsin(np.sqrt(a))

    df['trip_distance_km'] = haversine(df['pickup_latitude'], df['pickup_longitude'],
                                       df['dropoff_latitude'], df['dropoff_longitude'])

    # Plot 1: Daily rides
    rides_per_day = df.groupby('pickup_date').size()
    plt.figure(figsize=(12, 5))
    rides_per_day.plot()
    plt.title("Daily Ride Counts")
    plt.xlabel("Date")
    plt.ylabel("Number of rides")
    plt.tight_layout()
    plt.savefig(os.path.join(args.out, "rides_per_day.png"))
    plt.close()

    # Plot 2: Pickup hour distribution
    plt.figure(figsize=(8, 5))
    sns.countplot(x='pickup_hour', data=df, color='skyblue')
    plt.title("Pickup Hour Distribution")
    plt.tight_layout()
    plt.savefig(os.path.join(args.out, "hour_distribution.png"))
    plt.close()

    # Plot 3: Trip duration distribution (seconds)
    plt.figure(figsize=(8, 5))
    sns.histplot(df['trip_duration'], bins=100, log_scale=(False, True))
    plt.title("Trip Duration Distribution (log y)")
    plt.xlabel("Trip duration (seconds)")
    plt.ylabel("Frequency (log)")
    plt.tight_layout()
    plt.savefig(os.path.join(args.out, "trip_duration_dist_log.png"))
    plt.close()

    # Plot 4: Distance vs Duration hexbin
    plt.figure(figsize=(8, 6))
    plt.hexbin(df['trip_distance_km'], df['trip_duration']/60, gridsize=50, cmap='viridis', bins='log')
    plt.xlabel("Distance (km)")
    plt.ylabel("Duration (minutes)")
    plt.title("Distance vs Duration")
    cb = plt.colorbar()
    cb.set_label('log10(N)')
    plt.tight_layout()
    plt.savefig(os.path.join(args.out, "distance_vs_duration_hexbin.png"))
    plt.close()

    # Plot 5: Trip duration by passenger count
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='passenger_count', y='trip_duration', data=df)
    plt.yscale('log')
    plt.title("Trip Duration by Passenger Count (log scale)")
    plt.tight_layout()
    plt.savefig(os.path.join(args.out, "trip_duration_by_passenger_box.png"))
    plt.close()

    # Plot 6: Pickup location scatter (sampled)
    sample = df.sample(n=min(5000, len(df)), random_state=42)
    plt.figure(figsize=(6, 6))
    plt.scatter(sample['pickup_longitude'], sample['pickup_latitude'], s=1, alpha=0.5)
    plt.title("Pickup Locations (sample)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.tight_layout()
    plt.savefig(os.path.join(args.out, "pickup_spatial_scatter.png"))
    plt.close()

    # Plot 7: Correlation matrix
    plt.figure(figsize=(8, 6))
    numeric_cols = ['trip_duration', 'passenger_count', 'trip_distance_km']
    corr = df[numeric_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.savefig(os.path.join(args.out, "correlation_matrix.png"))
    plt.close()

    # Plot 8: Average duration by day-of-week and hour
    pivot = df.groupby(['pickup_dayofweek', 'pickup_hour'])['trip_duration'].mean().reset_index()

# ✅ fixed pivot syntax for new pandas
    pivot_table = pivot.pivot(index='pickup_dayofweek', columns='pickup_hour', values='trip_duration')
    
    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot_table, cmap='YlOrRd')
    plt.title("Avg Trip Duration by Day of Week and Hour")
    plt.xlabel("Hour")
    plt.ylabel("Day of Week")
    plt.tight_layout()
    plt.savefig(os.path.join(args.out, "heatmap_dow_hour_duration.png"))
    plt.close()
    
    
    print(f"All plots saved in {args.out}/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", default="NYC.csv", help="Path to NYC.csv")
    parser.add_argument("--out", default="plots", help="Output folder for plots")
    parser.add_argument("--nrows", type=int, default=None, help="Read only first N rows")
    args = parser.parse_args()
    main(args)
