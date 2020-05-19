INSERT_INTO_PERMISSIONS = "insert into permissions (identificator) values ('{}');"
INSERT_INTO_HAS_PERMISSIONS = "insert into parent (parent_identificator, child_identificator) values ('{}', '{}')"

def generatePermissions():

    idsAdded = []

    with open("permissions.txt", "r") as f:
        lines = f.readlines()

    for l in lines:
        aux = l.strip().replace('-', '').strip()
        if aux not in idsAdded and aux != '':
            idsAdded.append(aux)
            print(INSERT_INTO_PERMISSIONS.format(aux))


    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            iDeep = len(lines[i].split(" ")[0])
            jDeep = len(lines[j].split(" ")[0])

            if iDeep == jDeep-1:
                print(INSERT_INTO_HAS_PERMISSIONS.format(lines[i].strip().split(" ")[1], lines[j].strip().split(" ")[1]))
            elif iDeep >= jDeep:
                break