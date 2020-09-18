import os

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

variables_file = find_all("variables.tf","C:\\Users\\pmalkapuram\\Downloads\\mycode\\Matilda\\matilda-plugin-v3\\matilda_plugin\\operators\\terraform_cloud\\aws")

def find(text):      
  import re
  matches=re.findall(r'\"(.+?)\"',text)
  # matches is now ['String 1', 'String 2', 'String3']
  return ",".join(matches)

found = 0
variable = None
description = "description"
for i in variables_file:
    print(i)
    if "services" in i:
        x =input("Do you want to generate variables, desc for above file y/n: ")
        if x == "y":
            print("\n","\n")
            print("# Inputs")
            print("\n")
            print('| Name | Description |')
            print('| ------------- | ------------- |')
            f = open(i, "r")
            #print(doit(f.read()))
            with open(i) as f:
                for line in f:
                    if line.strip().startswith("variable"):
                        found += 1
                        if found >1:
                            print(" ")
                            found =0
                        print("|",line.partition("variable")[2].replace('{', '').replace('"','').replace("\n","|"), end ="")
                        
                    if found == 1:
                        if line.strip().startswith("description"):
                            print(find(line),"|")
                            found =0
        else:
            break