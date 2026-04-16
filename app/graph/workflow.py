from app.agents.segregator import segregator_node
from app.agents.id_agent import id_node
from app.agents.discharge_agent import discharge_node
from app.agents.bill_agent import bill_node

def run_workflow(file_path, claim_id):

    state = {
        "file_path": file_path,
        "claim_id": claim_id
    }

    state = segregator_node(state)
    state = id_node(state)
    state = discharge_node(state)
    state = bill_node(state)

    return {
        "claim_id": claim_id,
        "identity": state.get("id_data"),
        "discharge_summary": state.get("discharge_data"),
        "billing": state.get("bill_data")
    }
