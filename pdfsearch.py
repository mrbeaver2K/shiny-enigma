import os, json, pymupdf4llm

indexNeeded = True
targetDirectory = input("Enter target directory: ")
if targetDirectory == "": targetDirectory = "."
if os.path.exists(targetDirectory + ".pdfsearchindex.json"):
    print("Cache detected.")
    indexNeeded = False
    with open(targetDirectory + ".pdfsearchindex.json", "r") as cache:
        cacheOut = json.load(cache)
    contentKeys = cacheOut["keys"]
    validation = set()
    for file in os.listdir(targetDirectory):
        if file.endswith(".pdf"):
            validation.add(file)
            if not file in contentKeys:
                indexNeeded = True
    contentValues = cacheOut["values"]
    for i in range(len(contentKeys)):
        if not contentKeys[i] in validation:
            contentKeys.pop(i)
            contentValues.pop(i)
    if not indexNeeded:
        print("Cache integrity good.")
    else:
        print("Files have been added. Reindex required.")
else:
    print("Please wait while indexing.")
    contentKeys = []
    contentValues = []
if indexNeeded:
    for file in os.listdir(targetDirectory):
        if file.endswith(".pdf"):
            if not file in contentKeys:
                contentKeys.append(file)
                contentValues.append(pymupdf4llm.to_markdown(file))
                print("Indexed " + file)
            else:
                print("Found " + file)
    print("Indexing complete.")
    if len(contentKeys) == 0:
        print("Warning: No PDFs found.")
    else:
        with open(targetDirectory + ".pdfsearchindex.json", "w") as cache:
            json.dump({"keys": contentKeys, "values": contentValues}, cache)
        print("Cache created.")

while True:
    query = input("Enter query: ")
    if query == "":
        break
    matches = {}
    for i in range(len(contentKeys)):
        counts = contentValues[i].count(query)
        if counts != 0:
            matches[contentKeys[i]] = counts
    if matches == {}:
        print("Search complete. No matches found.")
    else:
        print("Search complete. Query matched:")
        for k, v in matches.items():
            print(v, "match" + ("es" if v != 1 else "") + " in " + k)
