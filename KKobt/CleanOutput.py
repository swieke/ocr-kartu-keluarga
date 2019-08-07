import re
import json
from fuzzywuzzy import process

# def extract(id):
#         person = []
#         for k in range(int(len(splitLine))):
#                 if k+id < len(splitLine):
#                 person.append(splitLine[k+id])
#                 id+=jumlahData-1
#         print(person)
#         family.append(person)


def Clean(inputtext):
        f = inputtext
        f = inputtext.splitlines()
        

        # print(f)
        f = [line.strip() for line in f]
        # print(f)

        genders =['LAKI-LAKI', 'PEREMPUAN']
        fixed = ['Nama Lengkap', 'Tempat Lahir', 'Tanggal','Lahir','Jenis','Kelamin','Agama','Pendidikan','Jenis Pekerjaan']
        religions = ['ISLAM','KRISTEN','HINDHU','BUDHA','KATHOLIK']
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
        
        print(len(splitLine))
                

        jumlahData = int(len(splitLine)/12)

        familyList = [] 
        for i in range(0, jumlahData):
                person = []
                for k in range(i,jumlahData*12,4):   #12 -> without passport no and NIK
                        person.append(splitLine[k])
                familyList.append(person)
                print(person)

        family = {"members": []} #to be filled with familyMember

        #person = [[person1data], [person2data], .. ]

        for person in familyList:
                familyMember = {
                        "name": '',
                        "nik": '',
                        "gender": '',
                        "pob": '',
                        "dob": '',
                        "agama": '',
                        "pendidikan": '',
                        "pekerjaan": ''
            
                }

                familyMember.update({"name": person[0]})
                familyMember.update({"nik": person[1]})
                familyMember.update({"gender": process.extractOne(person[2], genders)[0]})
                familyMember.update({"pob": person[3]})
                familyMember.update({"dob": person[4]})
                familyMember.update({"agama": process.extractOne(person[5], religions)[0]})
                familyMember.update({"pendidikan": process.extractOne(person[6], listPendidikan)[0]})
                familyMember.update({"pekerjaan": process.extractOne(person[7], listPekerjaan)[0]})
                familyMember.update({"status": person[8]})
                familyMember.update({"peran": person[9]})
                familyMember.update({"ayah": person[10]})
                familyMember.update({"ibu": person[11]})
                
                family["members"].append(familyMember)
        print(family)


        attrs = {}
        for member in family['members']:
                attrs['name'] = member["name"]
                attrs['nik'] = member["nik"]
                attrs['gender'] = member["gender"]
                attrs['pob'] = member["pob"]
                attrs['dob'] = member["dob"]
                attrs['agama'] = member["agama"]
                attrs['pendidikan'] = member["pendidikan"]
                # print(attrs)
        # print(attrs)
    
                


# {'members': [{'name': 'YANUAR HERLAMBANG', 'nik': '34 13202101810001', 'gender': 'LAKHLAKI', 'pob': 'CILEGON', 'dob': '21011981', 'agama': 'ISLAM', 'pendidikan': 'ST RAT Al', 'pekerjaan': 'KARYAWAN SWASTA RI'}, {'name': 'FASIHAH OKT AFIANA', 'nik': '3273204910800001', 'gender': 'PEREMPUAN', 'pob': 'JAMBI', 'dob': '09101980', 'agama': 'ISLAM', 'pendidikan': 'DIPLOMA IV/ST RATA ', 'pekerjaan': 'KARYAWAN SWASTA'}, {'name': 'M IKAIL AZKA MUHAMMAD YAFFA', 'nik': '3273202510060001', 'gender': 'LAK LAKI', 'pob': 'BANDUNG', 'dob': '25102005', 'agama': 'ISLAM', 'pendidikan': 'BELUM TAMAT SD/SEDERAJAT', 'pekerjaan': 'PELAJAR/MAHASIS WA'}, {'name': 'GAZARYNE MARCHZA AOUILA YAFFA', 'nik': '9273208103140003', 'gender': 'PEREMPUAN', 'pob': 'BANDUNG', 'dob': '21032014', 'agama': 'ISLAM', 'pendidikan': 'TIDAK/BLM SEKOLAH', 'pekerjaan': 'BELUMIT IDAK BEKERJA'}]}


# for i in range(0, jumlahData):
#     person = []
#     for k in range(i,jumlahData*8,4):
#         person.append(splitLine[k])
#     print(person)

