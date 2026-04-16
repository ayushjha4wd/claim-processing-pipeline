from langgraph.graph import StateGraph
from app.agents.segregator import segregator_node
from app.agents.id_agent import id_node
from app.agents.discharge_agent import discharge_node
from app.agents.bill_agent import bill_node


def run_workflow(file_path, claim_id):

    # Initial state
    state = {
        "file_path": file_path,
        "claim_id": claim_id
    }

    # Create graph
    graph = StateGraph(dict)

    # Add nodes
    graph.add_node("segregator", segregator_node)
    graph.add_node("id_agent", id_node)
    graph.add_node("discharge_agent", discharge_node)
    graph.add_node("bill_agent", bill_node)

    # Define flow
    graph.set_entry_point("segregator")

    graph.add_edge("segregator", "id_agent")
    graph.add_edge("segregator", "discharge_agent")
    graph.add_edge("segregator", "bill_agent")

    # Final node
    graph.set_finish_point("bill_agent")

    # Compile graph
    app = graph.compile()

    # Execute
    final_state = app.invoke(state)

    # Return structured output
    return {
        "claim_id": claim_id,
        "identity": final_state.get("id_data"),
        "discharge_summary": final_state.get("discharge_data"),
        "billing": final_state.get("bill_data")
    }
