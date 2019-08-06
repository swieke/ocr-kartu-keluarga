import re
from fuzzywuzzy import process


def Clean(inputtext):
        f = inputtext
        f = inputtext.splitlines()
        

        # print(f)
        f = [line.strip() for line in f]
        # print(f)

        fixed = ['Nama Lengkap', 'Tempat Lahir', 'Tanggal','Lahir','Jenis','Kelamin','Agama','Pendidikan','Jenis Pekerjaan']
        listPekerjaan = [line.rstrip('\n').upper() for line in open('pekerjaan.txt')]
        listPendidikan = [line.rstrip('\n').upper() for line in open('pendidikan.txt')]
        cleanLine = []
        splitLine = []
     
        for line in f:
        
                if int(len(line))>3:
                        line = re.sub('[^ a-zA-Z0-9 - /]','',line)
                        # line = line.strip()
                        cleanLine.append(line)
                else:
                        continue

        for i in cleanLine:
                if i not in fixed and int(len(i))>3:
                        splitLine.append(i)

        for i in splitLine:
                print(i)
                

# jumlahData = int(len(splitLine)/8)


# family = []

# def extract(id):
#     person = []
#     for k in range(int(len(splitLine))):
#         if k+id < len(splitLine):
#             person.append(splitLine[k+id])
#             id+=jumlahData-1
#     # print(person)
#     family.append(person)


# for k in range(jumlahData):
#     extract(k)

# for i in range(0, jumlahData):
#     person = []
#     for k in range(i,jumlahData*8,4):
#         person.append(splitLine[k])
#     print(person)



# familyDict = {"members": None}

# orang = {
#                 "name": '',
#                 "nik": '',
#                 "gender": '',
#                 "pob": '',
#                 "dob": '',
#                 "agama": '',
#                 "pendidikan": '',
#                 "pekerjaan": ''
            
#         }

# for member in family:
#     orang = {
#                 "name": '',
#                 "nik": '',
#                 "gender": '',
#                 "pob": '',
#                 "dob": '',
#                 "agama": '',
#                 "pendidikan": '',
#                 "pekerjaan": ''
            
#         }

#     orang["name"] = member[0]
#     orang["nik"] = member[1]
#     orang["gender"] = member[2]
#     orang["pob"] = member[3]
#     orang["dob"] = member[4]
#     orang["agama"] = member[5]
#     orang["pendidikan"] = member[6]
#     orang["pekerjaan"] = member[7]

#     familyDict.update({"members":orang})

# print(familyDict)






