from jieba_text import *
from read import read_inputtxt
from prolog_input import prolog_input_rule

prolog = prolog_input_rule()
test = read_inputtxt()

def build_dictionary():
    store = dict()
    Name = "Name"
    Position = "Position"
    Address = "Address"
    Address1 = "Address1"
    Address2 = "Address2"
    Salary = "Salary"
    reSalary = "reSalary"
    Exp = "Exp"
    Edu = "Edu"
    why = "why"
    wa = "wa"
    wt = "wt"
    wq = "wq"
    orr = "Or"
    perhaps = "perhaps"
    rT = "待遇面議"
    profession = "profession"
    business = "business"

    Prodata = ["soln[Name]", "soln[Position]", "soln[Address]", "soln[Address]", "soin[Address2]", "soln[Salary]",
           "soln[Exp]", "soln[Edu]"]
    words = pseg.cut(test)

    f2 = open('result.txt', 'w')
    for w, f in words:
        store[f] = w
        if f == "or":
            for n in store.keys():
                if n == "name":
                    Name = store.get(n)
                    Prodata[0] = store.get(n)
                elif n == "position":
                    Position = store.get(n)
                    Prodata[1] = store.get(n)
                elif n == "address":
                    Address = store.get(n)
                    Prodata[2] = store.get(n)
                elif n == "address1":
                    Address = store.get(n)
                    Prodata[3] = store.get(n)
                elif n == "address2":
                    Address = store.get(n)
                    Prodata[4] = store.get(n)
                elif n == "m":
                    reSalary = store.get(n)
                    Prodata[5] = store.get(n)
                elif n == "exp":
                    Exp = store.get(n)
                    Prodata[6] = store.get(n)
                elif n == "edu":
                    Edu = store.get(n)
                    Prodata[7] = store.get(n)
                elif n == "why":
                    why = store.get(n)
                elif n == "wa":
                    wa = store.get(n)
                elif n == "wt":
                    wt = store.get(n)
                elif n == "wq":
                    wq = store.get(n)
                elif n == "perhaps":
                    perhaps = store.get(n)
                elif n == "profession":
                    profession = store.get(n)
                elif n == "business":
                    business = store.get(n)
            # 規則
            if why != "why" and Address != "Address" and Address1 != "Address1":
                for soln in prolog.query(
                        "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
                    f2.write(
                        soln[Name] + soln[Position] + Address + Address1 + soln[Address2] + str(soln[Salary]) + str(
                            soln[Exp]) +
                        soln[Edu] + "\n")
                    print("123")
                # 規則 地區加上錢
            elif why != "why" and Address != "Address" and wq != "wq" and reSalary != "reSalary":
                for soln in prolog.query(
                        "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
                    if soln[Salary] > reSalary:
                        f2.write(soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(
                            soln[Salary]) + str(
                            soln[Exp]) + soln[Edu] + "\n")
            elif profession != "profession" and perhaps != "perhaps":
                for soln in prolog.query(
                        "粗集職業(" + Name + "," + "Position" + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + profession + ")"):
                    f2.write(soln[Name] + soln["Position"] + soln[Address] + soln[Address1] + soln[Address2] + str(
                        soln[Salary]) + str(soln[Exp]) + soln[Edu] + "\n")
            elif business != "business" and perhaps != "perhaps":
                for soln in prolog.query(
                        "粗集職業二(" + Name + "," + "Position" + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + business + ")"):
                    f2.write(soln[Name] + soln["Position"] + soln[Address] + soln[Address1] + soln[Address2] + str(
                        soln[Salary]) + str(soln[Exp]) + soln[Edu] + "\n")
            elif Address != "Address" and Name != "Name":
                for soln in prolog.query(
                        "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
                    f2.write(
                        Name + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                            soln[Exp]) +
                        soln[Edu] + "\n")
            elif why != "why" and Address != "Address":
                for soln in prolog.query(
                        "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
                    f2.write(
                        soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                            soln[Exp]) + soln[Edu] + "\n")

            elif Name != "Name":
                for soln in prolog.query(
                        "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
                    f2.write(
                        Name + soln[Position] + soln[Address] + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                            soln[Exp]) + soln[Edu] + "\n")
            elif Name != "Address":
                for soln in prolog.query(
                        "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
                    f2.write(
                        soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                            soln[Exp]) + soln[Edu] + "\n")

    for n in store.keys():
        if n == "name":
            Name = store.get(n)
            Prodata[0] = store.get(n)
        elif n == "position":
            Position = store.get(n)
            Prodata[1] = store.get(n)
        elif n == "address":
            Address = store.get(n)
            Prodata[2] = store.get(n)
        elif n == "address1":
            Address = store.get(n)
            Prodata[3] = store.get(n)
        elif n == "address2":
            Address = store.get(n)
            Prodata[4] = store.get(n)
        elif n == "m":
            reSalary = store.get(n)
            Prodata[5] = store.get(n)
        elif n == "exp":
            Exp = store.get(n)
            Prodata[6] = store.get(n)
        elif n == "edu":
            Edu = store.get(n)
            Prodata[7] = store.get(n)
        elif n == "why":
            why = store.get(n)
        elif n == "wa":
            wa = store.get(n)
        elif n == "wt":
            wt = store.get(n)
        elif n == "wq":
            wq = store.get(n)
        elif n == "perhaps":
            perhaps = store.get(n)
        elif n == "profession":
            profession = store.get(n)
        elif n == "business":
            business = store.get(n)

    # 規則
    if why != "why" and Address != "Address" and Address1 != "Address1":
        for soln in prolog.query(
                "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
            f2.write(
                soln[Name] + soln[Position] + Address + Address1 + soln[Address2] + str(soln[Salary]) + str(soln[Exp]) +
                soln[Edu] + "\n")
            print("123")
    # 規則 地區加上錢
    elif why != "why" and Address != "Address" and wq != "wq" and reSalary != "reSalary":
        for soln in prolog.query(
                "公司價格(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + reSalary + "," + rT + ")"):
            f2.write(soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                soln[Exp]) + soln[Edu] + "\n")
    elif profession != "profession" and perhaps != "perhaps":
        print(profession + perhaps)
        for soln in prolog.query(
                "粗集職業(" + Name + "," + "Position" + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + profession + ")"):
            f2.write(
                soln[Name] + soln["Position"] + soln[Address] + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                    soln[Exp]) + soln[Edu] + "\n")
    elif business != "business" and perhaps != "perhaps":
        print(profession + perhaps)
        for soln in prolog.query(
                "粗集職業二(" + Name + "," + "Position" + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + business + ")"):
            f2.write(
                soln[Name] + soln["Position"] + soln[Address] + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                    soln[Exp]) + soln[Edu] + "\n")

    elif Address != "Address" and perhaps != "perhaps":
        for soln in prolog.query(
                "粗集公司(" + Name + "," + Position + "," + "Adress" + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + Address + ")"):
            f2.write(soln[Name] + "," + soln[Position] + "," + soln["Adress"] + soln[Address1] + soln[Address2] + "," + str(
                soln[Salary]) + "," + str(soln[Exp]) + "," + soln[Edu] + "\n")
    elif Address != "Address" and Name != "Name":
        for soln in prolog.query(
                "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
            f2.write(Name + "," + soln[Position] + "," + Address + soln[Address1] + soln[Address2] + "," + str(
                soln[Salary]) + "," + str(soln[Exp]) + "," + soln[Edu] + "\n")
    elif why != "why" and Address != "Address":
        for soln in prolog.query(
                "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
            f2.write(soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                soln[Exp]) + soln[Edu] + "\n")
    elif reSalary != "reSalary" and wq != "wq":
        for soln in prolog.query(
                "公司價格(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + "," + reSalary + "," + rT + ")"):
            f2.write(soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                soln[Exp]) + soln[Edu] + "\n")
    elif Name != "Name":
        for soln in prolog.query(
                "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
            f2.write(Name + soln[Position] + soln[Address] + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                soln[Exp]) + soln[Edu] + "\n")
    elif Address != "Address":
        for soln in prolog.query(
                "公司(" + Name + "," + Position + "," + Address + "," + Address1 + "," + Address2 + "," + Salary + "," + Exp + "," + Edu + ")"):
            f2.write(soln[Name] + soln[Position] + Address + soln[Address1] + soln[Address2] + str(soln[Salary]) + str(
                soln[Exp]) + soln[Edu] + "\n")
