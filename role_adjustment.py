# Thresholds and role criteria
LATENCY_THRESHOLD = 150     # in milliseconds
BATTERY_THRESHOLD = 40      # in percentage
UPTIME_THRESHOLD = 0.8      # 80% uptime
THROUGHPUT_THRESHOLD = 100  # transactions per second

# Role labels
FULL_NODE = "Full Node"
LIGHT_NODE = "Light Node"
STANDBY_NODE = "Standby Node"

# Sample ledger, to be populated by the Node State Monitoring Module
# Example format:
# ledger = {
#     "Node_001": {"latency": 120, "uptime": 0.9, "battery": 85, "throughput": 105},
#     "Node_002": {"latency": 160, "uptime": 0.7, "battery": 30, "throughput": 90},
# }
ledger = {}  # This would be populated by the monitoring module

# Function to determine the role of a node based on its metrics
def determine_role(metrics):
    latency = metrics['latency']
    uptime = metrics['uptime']
    battery = metrics['battery']
    throughput = metrics['throughput']
    
    # Decision logic for role assignment
    if latency < LATENCY_THRESHOLD and uptime >= UPTIME_THRESHOLD and battery > BATTERY_THRESHOLD and throughput >= THROUGHPUT_THRESHOLD:
        return FULL_NODE
    elif latency >= LATENCY_THRESHOLD or battery <= BATTERY_THRESHOLD or uptime < UPTIME_THRESHOLD:
        return LIGHT_NODE
    else:
        return STANDBY_NODE

# Function to adjust roles for each node based on current metrics in the ledger
def adjust_roles():
    for node_id, metrics in ledger.items():
        # Determine the role for each node
        role = determine_role(metrics)
        
        # Update the ledger with the new role
        ledger[node_id]['role'] = role
        
        # Output the new role assignment for the node
        print(f"Node ID: {node_id} | Assigned Role: {role}")

# Simulated function to populate the ledger with sample metrics
# (This simulates output from the Node State Monitoring Module)
def populate_sample_ledger():
    global ledger
    ledger = {
        "Node_001": {"latency": 120, "uptime": 0.9, "battery": 85, "throughput": 105},
        "Node_002": {"latency": 160, "uptime": 0.7, "battery": 30, "throughput": 90},
        "Node_003": {"latency": 110, "uptime": 0.95, "battery": 50, "throughput": 115},
        "Node_004": {"latency": 140, "uptime": 0.85, "battery": 60, "throughput": 80},
        "Node_005": {"latency": 180, "uptime": 0.75, "battery": 45, "throughput": 95}
    }

# Main function to simulate the role adjustment process
def main():
    # Simulate populating the ledger with initial metrics
    populate_sample_ledger()
    
    # Adjust roles based on the current metrics
    adjust_roles()
    
    # Print final ledger status for each node
    print("\nFinal Ledger State:")
    for node_id, data in ledger.items():
        print(f"{node_id}: {data}")

# Run the role adjustment process
if __name__ == "__main__":
    main()
