def discharge_node(state):
    pages = state["pages"]
    ids = state["classified"].get("discharge_summary", [])

    data = {}

    for i in ids:
        text = pages[i].lower()

        if "diagnosis" in text:
            data["diagnosis"] = "Extracted Diagnosis"

        if "admission" in text:
            data["admission_date"] = "Extracted Admission Date"

        if "discharge" in text:
            data["discharge_date"] = "Extracted Discharge Date"

    state["discharge_data"] = data
    return state
