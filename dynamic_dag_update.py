from role_adjustment import ledger

# Initialize DAG structure
dag = {}

# Update DAG structure based on roles
def update_dag():
    global dag
    dag = {}  # Reset DAG

    for node_id, node_data in ledger.items():
        role = node_data.get("role", "Light Node")
        dag[node_id] = {"links": []}

        # Full nodes link to all other full and standby nodes
        if role == "Full Node":
            for target_id, target_data in ledger.items():
                if target_id != node_id and target_data.get("role") in ["Full Node", "Standby Node"]:
                    dag[node_id]["links"].append(target_id)

        # Light nodes link only to nearby full nodes
        elif role == "Light Node":
            full_nodes = [target_id for target_id, target_data in ledger.items() if target_data.get("role") == "Full Node"]
            if full_nodes:
                # Link light node to up to 2 full nodes
                dag[node_id]["links"].extend(full_nodes[:2])

        # Standby nodes link only to full nodes
        elif role == "Standby Node":
            for target_id, target_data in ledger.items():
                if target_id != node_id and target_data.get("role") == "Full Node":
                    dag[node_id]["links"].append(target_id)

    print("\nUpdated DAG Structure:")
    for node_id, data in dag.items():
        print(f"{node_id} (Role: {ledger[node_id]['role']}): Links -> {data['links']}")

# Function to simulate DAG updates after role adjustment
def dynamic_dag_update():
    # Call role adjustment to simulate role changes in the ledger
    from role_adjustment import adjust_roles
    adjust_roles()  # Adjust roles based on current metrics and voting

    # Update DAG structure based on new roles
    update_dag()

# Sample function to populate ledger for testing
def populate_sample_ledger():
    global ledger
    ledger = {
        "Node_001": {"latency": 120, "uptime": 0.9, "battery": 85, "throughput": 105, "role": "Full Node"},
        "Node_002": {"latency": 90, "uptime": 0.95, "battery": 60, "throughput": 115, "role": "Standby Node"},
        "Node_003": {"latency": 110, "uptime": 0.92, "battery": 45, "throughput": 85, "role": "Light Node"},
        "Node_004": {"latency": 140, "uptime": 0.85, "battery": 60, "throughput": 80, "role": "Standby Node"},
        "Node_005": {"latency": 95, "uptime": 0.88, "battery": 70, "throughput": 110, "role": "Full Node"}
    }

# Main function to test DAG updates
def main():
    # Populate the ledger with sample data
    populate_sample_ledger()

    # Run the dynamic DAG update to adjust the DAG structure based on roles
    dynamic_dag_update()

if __name__ == "__main__":
    main()
