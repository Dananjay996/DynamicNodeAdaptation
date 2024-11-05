import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data
data = pd.read_csv('simulation_results.csv')

# Set up Seaborn style for better aesthetics
sns.set_theme(style="whitegrid")

# 1. Plot Role Transition Over Time
plt.figure(figsize=(10, 6))
role_counts = data.groupby(['Cycle', 'Role']).size().unstack(fill_value=0)
role_counts.plot(kind='line', marker='o', ax=plt.gca())
plt.title("Role Transition Over Time")
plt.xlabel("Cycle")
plt.ylabel("Number of Nodes")
plt.legend(title="Role")
plt.show()

# 2. Plot DAG Connectivity Over Time (Average Links by Role)
plt.figure(figsize=(10, 6))
data['Num_Links'] = data['Links'].apply(lambda x: len(eval(x)))
avg_links_by_role = data.groupby(['Cycle', 'Role'])['Num_Links'].mean().unstack(fill_value=0)
avg_links_by_role.plot(kind='line', marker='o', ax=plt.gca())
plt.title("Average DAG Connectivity Over Time by Role")
plt.xlabel("Cycle")
plt.ylabel("Average Number of Links")
plt.legend(title="Role")
plt.show()

# 3. Plot Average Performance Metrics Over Time
plt.figure(figsize=(10, 6))
avg_metrics = data.groupby('Cycle')[['Latency', 'Throughput', 'Battery']].mean()
avg_metrics.plot(kind='line', marker='o', ax=plt.gca())
plt.title("Average Performance Metrics Over Time")
plt.xlabel("Cycle")
plt.ylabel("Metric Value")
plt.legend(["Latency (ms)", "Throughput (transactions/sec)", "Battery (%)"])
plt.show()

# 4. Correlation Between Latency, Throughput, and Role
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="Latency", y="Throughput", hue="Role", style="Role", s=100)
plt.title("Latency vs. Throughput by Role")
plt.xlabel("Latency (ms)")
plt.ylabel("Throughput (transactions/sec)")
plt.legend(title="Role")
plt.show()

# 5. Voting Approval Ratios and Success Rates (Dummy Example)
# Assuming a column 'Approval_Ratio' in data showing approval ratios, and 'Role_Change_Approved' for success rates
if 'Approval_Ratio' in data.columns and 'Role_Change_Approved' in data.columns:
    plt.figure(figsize=(10, 6))
    approval_ratios = data.groupby('Cycle')['Approval_Ratio'].mean()
    approval_ratios.plot(kind='bar', color='skyblue', ax=plt.gca())
    plt.title("Average Voting Approval Ratio Per Cycle")
    plt.xlabel("Cycle")
    plt.ylabel("Average Approval Ratio")
    plt.show()

    plt.figure(figsize=(10, 6))
    success_rates = data.groupby('Cycle')['Role_Change_Approved'].mean()
    success_rates.plot(kind='line', color='green', marker='o', ax=plt.gca())
    plt.title("Voting Success Rate Over Time")
    plt.xlabel("Cycle")
    plt.ylabel("Success Rate")
    plt.show()
