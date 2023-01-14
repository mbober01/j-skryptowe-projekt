import sys
from webbrowser import open as webopen
from os import path
from datetime import datetime

# algorytm zwracajacy niepowtarzalnosc ciagu
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
# funkcja zczytujaca dane z pliku
def read_file(f_name):
    with open(f_name) as file:
        return file.readlines()
    
# funkcja tworzaca raport html i otwierajaca go w oknie przegladarki
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
    file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"raports/{file_name}.html", "w") as file:
        file.writelines(table)
    webopen(path.abspath(f"raports/{file_name}.html"))

# funkcja generujaca zczytujaca pliki input i wywolujaca nich algorytm oraz generujaca pliki output.txt   
def generate_io():
    files = "".join(sys.argv[1:])[:-1].split(",")
    inputs = []
    outputs = []
    for i,file in enumerate(files,1):
        ciag = read_file(f"input/{file}")[0]
        inputs.append(ciag)
        with open(f"output/output{i}.txt","w") as file:
            file.write(algorytm(ciag))
            outputs.append(algorytm(ciag))
    return [inputs, outputs]
  
if __name__ == "__main__":
    data = generate_io()
    make_html(data[0],data[1])
