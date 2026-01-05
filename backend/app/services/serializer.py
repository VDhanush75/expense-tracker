from bson import ObjectId

def serialize(doc):
    if isinstance(doc, list):
        return [serialize(d) for d in doc]

    if isinstance(doc, dict):
        new_doc = {}
        for k, v in doc.items():
            if isinstance(v, ObjectId):
                new_doc[k] = str(v)
            else:
                new_doc[k] = v
        return new_doc

    return doc
