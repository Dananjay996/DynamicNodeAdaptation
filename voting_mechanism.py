import random
ledger = {}  # This would be populated by monitoring module

# Voting thresholds
MAJORITY_THRESHOLD = 0.6  # 60% majority to approve role change

# Function to assign neighbors to each node (for simulation)
def assign_neighbors():
    node_ids = list(ledger.keys())
    for node_id in node_ids:
        # Assign random neighbors from the other nodes
        neighbors = random.sample([n for n in node_ids if n != node_id], k=min(3, len(node_ids) - 1))
        ledger[node_id]["neighbors"] = neighbors

# Function to calculate vote weight based on a node's performance metrics
def calculate_vote_weight(metrics):
    # Weight is based on uptime and inverse of latency
    uptime_weight = metrics["uptime"]
    latency_weight = 1 / (metrics["latency"] + 1)  # Adding 1 to avoid division by zero
    return uptime_weight * latency_weight

# Voting mechanism for role change
def vote_on_role_change(node_id, proposed_role):
    node = ledger[node_id]
    neighbors = node["neighbors"]
    
    # Tally the votes
    total_weight = 0
    approval_weight = 0
    
    for neighbor_id in neighbors:
        neighbor_metrics = ledger[neighbor_id]
        weight = calculate_vote_weight(neighbor_metrics)
        total_weight += weight
        
        # Simulate neighbor vote: Randomly approve/reject based on neighbor's current metrics
        if neighbor_metrics["throughput"] >= 100:  # For example, high-throughput neighbors tend to approve
            approval_weight += weight

    # Calculate approval ratio
    approval_ratio = approval_weight / total_weight if total_weight > 0 else 0

    # Determine if majority approves the proposed role change
    approved = approval_ratio >= MAJORITY_THRESHOLD
    print(f"Node {node_id} | Proposed Role: {proposed_role} | Approval Ratio: {approval_ratio:.2f} | Approved: {approved}")
    
    return approved

# Function to adjust role with voting mechanism
def adjust_roles_with_voting():
    for node_id, node_data in ledger.items():
        # Simulate a proposed role change (based on hypothetical metrics here)
        proposed_role = "Full Node" if node_data["latency"] < 100 else "Light Node"
        
        # Neighbors vote to confirm role change
        if vote_on_role_change(node_id, proposed_role):
            ledger[node_id]["role"] = proposed_role
            print(f"Node {node_id} role updated to: {proposed_role}")
        else:
            print(f"Node {node_id} role change to {proposed_role} was not approved")

# Simulated function to populate the ledger with sample metrics
def populate_sample_ledger():
    global ledger
    ledger = {
        "Node_001": {"latency": 120, "uptime": 0.9, "battery": 85, "throughput": 105, "role": "Standby Node"},
        "Node_002": {"latency": 90, "uptime": 0.95, "battery": 60, "throughput": 115, "role": "Full Node"},
        "Node_003": {"latency": 110, "uptime": 0.92, "battery": 45, "throughput": 85, "role": "Light Node"},
        "Node_004": {"latency": 140, "uptime": 0.85, "battery": 60, "throughput": 80, "role": "Standby Node"},
        "Node_005": {"latency": 95, "uptime": 0.88, "battery": 70, "throughput": 110, "role": "Full Node"}
    }

# Main function to simulate the voting-based role adjustment
def main():
    populate_sample_ledger()
    
    assign_neighbors()
    adjust_roles_with_voting()
    
    # Print final ledger status
    print("\nFinal Ledger State:")
    for node_id, data in ledger.items():
        print(f"{node_id}: {data}")

if __name__ == "__main__":
    main()
