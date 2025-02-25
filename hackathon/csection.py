import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data
df = pd.read_csv(r"C:\Users\SIC\Documents\Python - SIC\sic_033\hackathon\india_births_2011_2021.csv")

# Function to visualize Normal Delivery Percentage vs C-section Deliveries
def normal_vs_csection():
    delivery_type = df['Type of Delivery'].value_counts()
    delivery_type.plot(kind='bar', color=['blue', 'green', 'orange'], title="Normal Delivery vs C-Section Deliveries")
    plt.xlabel("Delivery Type")
    plt.ylabel("Number of Deliveries")
    plt.show()

# Function to determine which part of the country has more C-section deliveries
def csection_by_state():
    csection_state = df[df['Type of Delivery'] == 'C-Section']['State of Birth'].value_counts()
    csection_state.plot(kind='bar', color= 'purple', title="C-Section Deliveries by State")
    plt.xlabel("State")
    plt.ylabel("Number of C-Section Deliveries")
    plt.show()

# Function to determine which hospitals have more C-section deliveries
def csection_by_hospital():
    csection_hospital = df[df['Type of Delivery'] == 'C-Section']['Hospital'].value_counts()
    csection_hospital.plot(kind='bar', color='cyan', title="C-Section Deliveries by Hospital")
    plt.xlabel("Hospital")
    plt.ylabel("Number of C-Section Deliveries")
    plt.show()

# Function to check if C-section deliveries and seasons have any relation
def csection_by_season():
    csection_season = df[df['Type of Delivery'] == 'C-Section'].groupby('Season')['Type of Delivery'].count()
    csection_season.plot(kind='bar', color='pink', title="C-Section Deliveries by Season")
    plt.xlabel("Season")
    plt.ylabel("Number of C-Section Deliveries")
    plt.show()

# Function to determine the percentage of second child births with normal delivery when the first was a C-section
def second_child_normal_after_csection():
    second_child_normal = df[(df['Birth Order'] == 2) & 
                              (df['Type of Delivery'] == 'Normal') & 
                              (df['Parent Name'].isin(df[df['Birth Order'] == 1]['Parent Name'][df['Type of Delivery'] == 'C-Section']))]
    
    percentage = len(second_child_normal) / len(df[(df['Birth Order'] == 2) & 
                                                  (df['Parent Name'].isin(df[df['Birth Order'] == 1]['Parent Name']))]) * 100
    print(f"Percentage of second child births with normal delivery when first was a C-section: {percentage:.2f}%")

# Menu to run visualizations
def menu():
    print("\nMenu:")
    print("1. Normal Delivery Percentage vs C-section Deliveries")
    print("2. Which part of the country has more C-section deliveries")
    print("3. Which hospitals have more C-section deliveries")
    print("4. Does C-section deliveries and seasons have any relation?")
    print("5. What percentage of 2nd child birth has normal delivery when 1st delivery was by C-section")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            normal_vs_csection()
        case 2:
            csection_by_state()
        case 3:
            csection_by_hospital()
        case 4:
            csection_by_season()
        case 5:
            second_child_normal_after_csection()
        case 6:
            print("Exiting the program.")
        case _:
            print("Invalid choice! Please select again.")

# Run the program
menu()
