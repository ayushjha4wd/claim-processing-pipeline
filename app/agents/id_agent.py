def id_node(state):
    pages = state["pages"]
    ids = state["classified"].get("identity_document", [])

    data = {}

    for i in ids:
        text = pages[i].lower()

        if "name" in text:
            data["name"] = "Extracted Name"

        if "dob" in text or "date of birth" in text:
            data["dob"] = "Extracted DOB"

    state["id_data"] = data
    return state
