def bill_node(state):
    pages = state["pages"]
    ids = state["classified"].get("itemized_bill", [])

    total = 0

    for i in ids:
        total += 100  # dummy logic

    state["bill_data"] = {
        "total_amount": total
    }

    return state
