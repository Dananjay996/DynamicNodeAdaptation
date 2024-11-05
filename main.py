import time
import random
import csv
from nodeStateMonitoring import simulate_monitoring, ledger
from role_adjustment import adjust_roles
from voting_mechanism import assign_neighbors
from dynamic_dag_update import update_dag, dag

# Parameters
NUM_NODES = 20  # Increase the number of nodes for a larger simulation
CYCLE_INTERVAL = 5  # Time interval (in seconds) between each monitoring and update cycle
NUM_CYCLES = 50  # Number of cycles to simulate

CSV_FILE = "simulation_results.csv"

def add_random_variability():
    for node_id, metrics in ledger.items():
        # Simulate random variations in metrics
        metrics["latency"] += random.uniform(-10, 10)  # Randomly change latency within ±10ms
        metrics["battery"] = max(0, metrics["battery"] + random.uniform(-5, 5))  # Change battery within ±5%, no negatives
        metrics["throughput"] += random.uniform(-5, 5)  # Randomly adjust throughput within ±5 transactions/sec
        metrics["uptime"] = max(0, min(1, metrics["uptime"] + random.uniform(-0.02, 0.02)))  # Small uptime fluctuations

# Function to record data to CSV for visualization
# Function to record data to CSV for visualization
def record_to_csv(cycle):
    try:
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            for node_id, data in ledger.items():
                # Debug: Print data to be recorded
                print(f"Recording to CSV - Cycle {cycle}, Node {node_id}: {data}")
                writer.writerow([
                    cycle,
                    node_id,
                    data.get("latency", "N/A"),
                    data.get("battery", "N/A"),
                    data.get("throughput", "N/A"),
                    data.get("uptime", "N/A"),
                    data.get("role", "N/A"),
                    dag.get(node_id, {}).get("links", [])
                ])
        print(f"[Cycle {cycle}] Data successfully recorded to CSV.")
    except Exception as e:
        print(f"Error recording to CSV: {e}")


# Main function with enhanced dynamics and data collection
def main():
    # Initialize CSV file for logging results
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Cycle", "Node_ID", "Latency", "Battery", "Throughput", "Uptime", "Role", "Links"])

    # Initial setup
    print("\n--- Initializing Ledger with Sample Data and Assigning Neighbors ---")
    simulate_monitoring(NUM_NODES)
    assign_neighbors()

    # Continuous simulation loop
    print("\n--- Starting Dynamic Simulation ---")
    for cycle in range(1, NUM_CYCLES + 1):
        print(f"\n[Cycle {cycle}] Collecting metrics with added variability...")
        
        # Collect new metrics with variability
        simulate_monitoring(NUM_NODES)
        add_random_variability()

        # Adjust roles and confirm through voting
        print(f"\n[Cycle {cycle}] Adjusting roles with voting confirmation...")
        adjust_roles()

        # Update the DAG structure based on new roles
        print(f"\n[Cycle {cycle}] Updating DAG structure...")
        update_dag()

        # Record data for visualization
        record_to_csv(cycle)

        # Wait for the next cycle
        time.sleep(CYCLE_INTERVAL)

    print("\nSimulation completed. Results saved to 'simulation_results.csv'.")

if __name__ == "__main__":
    main()
