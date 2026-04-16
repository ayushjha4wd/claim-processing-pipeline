from app.services.pdf_service import extract_pages

def segregator_node(state):
    pages = extract_pages(state["file_path"])

    classified = {
        "identity_document": [],
        "discharge_summary": [],
        "itemized_bill": []
    }

    for i, text in enumerate(pages):
        t = text.lower()

        if "patient" in t or "id" in t:
            classified["identity_document"].append(i)

        elif "discharge summary" in t:
            classified["discharge_summary"].append(i)

        elif "bill" in t or "amount" in t:
            classified["itemized_bill"].append(i)

    state["pages"] = pages
    state["classified"] = classified

    return state
