import psutil
import random
import time

# Simulated "ledger" to store node metrics
ledger = {}

# Node count for simulation (e.g., 5 nodes)
NUM_NODES = 5

# Monitoring thresholds (example values for simulation)
LATENCY_THRESHOLD = 150  # in milliseconds
BATTERY_THRESHOLD = 40   # in percentage
UPTIME_THRESHOLD = 0.8   # 80% uptime
THROUGHPUT_THRESHOLD = 100  # transactions per second

# Function to simulate latency measurement (replace with actual latency checks in real environment)
def measure_latency():
    return random.uniform(50, 200)

# Function to measure uptime as a ratio of system uptime to elapsed time since start
def measure_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    return uptime_seconds / (uptime_seconds + 1)  # Simple calculation for demo purposes

# Function to measure battery status (returns percentage, or None if not available)
def measure_battery():
    battery = psutil.sensors_battery()
    return battery.percent if battery else None

# Simulated function to measure transaction throughput (replace with actual calculations)
def measure_throughput():
    return random.uniform(80, 120)  # Simulate transactions per second

# Function to collect metrics for a single node
def collect_node_metrics(node_id):
    latency = measure_latency()
    uptime = measure_uptime()
    battery = measure_battery()
    throughput = measure_throughput()
    
    metrics = {
        "node_id": node_id,
        "latency": latency,
        "uptime": uptime,
        "battery": battery,
        "throughput": throughput
    }
    
    # Display collected metrics for each node
    print(f"\nMetrics for {node_id}:")
    print(f"Latency: {latency} ms")
    print(f"Uptime: {uptime * 100:.2f}%")
    print(f"Battery: {battery}%")
    print(f"Transaction Throughput: {throughput} transactions/second")
    
    return metrics

# Function to update the simulated ledger with node metrics
def update_ledger(node_id, metrics):
    ledger[node_id] = metrics
    print(f"\nLedger updated for {node_id}:")
    print(ledger[node_id])

# Main simulation loop to monitor and update each node
def simulate_monitoring():
    while True:
        for i in range(1, NUM_NODES + 1):
            node_id = f"Node_{i:03d}"  # Format node IDs as Node_001, Node_002, etc.
            
            # Collect metrics for the node
            metrics = collect_node_metrics(node_id)
            
            # Update the ledger with current metrics
            update_ledger(node_id, metrics)
        
        # Simulate a monitoring interval (e.g., 5 seconds here for demonstration)
        time.sleep(5)

# Run the simulation
if __name__ == "__main__":
    simulate_monitoring()
