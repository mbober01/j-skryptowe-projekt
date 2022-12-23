import sys

def algorytm(ciag):
    length = len(ciag)
    for x in range(length):
        temp = 0
        for index in range(x+1,(length+x)//2+1):
            temp += 1
            part1 = ciag[x:index]
            part2 = ciag[index:index+temp]
            if part1 == part2:
                return f"nie jest niepowtarzalny {part1}"

    return "jest niepowtarzalny"

def read_file(f_name):
    with open(f_name) as file:
        return file.readlines()


def make_html(inputs,outputs):
    table = "<table bgcolor='black'>\n"
    header = ["inputs","outputs"]
    table += "  <tr bgcolor='grey'>\n"
    for column in header:
        table += "    <th>{0}</th>\n".format(column.strip())
    table += "  </tr>\n"
    data = [[inputs[i],outputs[i]] for i in range(len(inputs))]
    for line in data:
        table += "  <tr bgcolor='grey'>\n"
        for column in line:
            table += "    <td>{0}</td>\n".format(column.strip())
        table += "  </tr>\n"
    table += "</table>"
    with open("raport.html", "w") as file:
        file.writelines(table)
    
def algorithm():
    files = "".join(sys.argv[1:])[:-1].split(",")
    inputs = files
    outputs = []
    print(files)
    for i,file in enumerate(files,1):
        ciag = read_file(f"input/{file}")[0]
        with open(f"output/output{i}.txt","w") as file:
            file.write(algorytm(ciag))
            outputs.append(algorytm(ciag))
    print(list(zip(inputs,outputs)))
    return [inputs, outputs]
    
data = algorithm()
make_html(data[0],data[1])
