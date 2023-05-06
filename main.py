import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

creds = credentials.ApplicationDefault()
firebase_admin.initialize_app(creds, {
  'projectId': 'minioncheck',
})

dbase = firestore.client()
def Call_Minis(request):
    minrequest = request.args

    minref = dbase.collection("MinTable")
    minis = minref.get()
    
    list_of_minis = []
    for doc in minis:
        list_of_minis.append(doc.to_dict())

    minrequired = {}
    for m in list_of_minis:
        if m["ID"] == int(minrequest["ID"]):
            minrequired = m
            break
    if not minrequired:
        return "Given Minion ID is not available currenlty"
    
    return minrequired
