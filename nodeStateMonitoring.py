import psutil
import random
import time

# Simulated "ledger" to store node metrics
ledger = {}

LATENCY_THRESHOLD = 150  # in milliseconds
BATTERY_THRESHOLD = 40   # in percentage
UPTIME_THRESHOLD = 0.8   # 80% uptime
THROUGHPUT_THRESHOLD = 100  # transactions per second

# Function to simulate latency measurement
def measure_latency():
    return random.uniform(50, 200)

# Function to measure uptime as a ratio of system uptime to elapsed time since start
def measure_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    return uptime_seconds / (uptime_seconds + 1)

# Function to measure battery status (returns percentage, or None if not available)
def measure_battery():
    battery = psutil.sensors_battery()
    return battery.percent if battery else None

# Simulated function to measure transaction throughput
def measure_throughput():
    return random.uniform(80, 120)

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

# Function to monitor and update each node for a single cycle
def simulate_monitoring(num_nodes):
    for i in range(1, num_nodes + 1):
        node_id = f"Node_{i:03d}"
        
        # Collect metrics for the node
        metrics = collect_node_metrics(node_id)
        
        # Update the ledger with current metrics
        update_ledger(node_id, metrics)
