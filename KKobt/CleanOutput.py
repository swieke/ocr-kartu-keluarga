import re
import json
from fuzzywuzzy import process


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
                

def CleanHeader(inputtext):
        f = inputtext
        f = inputtext.splitlines()
        

        f = [line.strip() for line in f]
        cleanLine = []
        
        for line in f:
                if int(len(line))>3 and ':' in line:
                        line = re.sub('[^ a-zA-Z0-9 -/]','',line)
                        cleanLine.append(line)
                        print(line)
                else:
                        continue

        splitLine = []
        for i in cleanLine:
                if int(len(i))>3:
                        i = i.split(' ')
                        i = [word for word in i if word]
                        splitLine.append(i)

        for i in splitLine:
                print(i)

        header= {}
        
        for info in splitLine:
                if ('Nama' or 'Kepala' or 'Keluarga') in info:
                        header["kepalaKeluarga"] = info[3]
                        print(info)
                elif ('Alamat' in info or 'alamat' in info):
                        header["alamat"] = info[1]
                elif ('RTRW' in info or 'RW' in info):
                        header["rtRW"] = info[1]
                elif ('Kode' in info or 'Pos' in info):
                        header["kodePos"] = info[2]
                elif ('Desa' in info or 'Kelurahan' in info):
                        header["desaKelurahan"] = info[1]
                elif ('kecamatan' in info or 'Kecamatan' in info):
                        header['kecamatan'] = info[1]
                elif ('Kabupaten' in info or 'kabupaten' in info):
                        header['kabupatenKota'] = info[1]
                else:
                        continue
        
        print(header)

def getKKNo(inputtext):
        f = inputtext
        f = inputtext.splitlines()
        

        f = [line.strip() for line in f]
        cleanLine = []
        
        for line in f:
                if int(len(line))>3 and ('No' in line or 'no' in line):
                        line = re.sub('[^ a-zA-Z0-9 -/]','',line)
                        cleanLine.append(line)
                        print(line)
                else:
                        continue

        splitLine = []
        for i in cleanLine:
                if int(len(i))>3:
                        i = i.split(' ')
                        i = [word for word in i if word]
                        splitLine.append(i)

                

    
                


# {'members': [{'name': 'YANUAR HERLAMBANG', 'nik': '34 13202101810001', 'gender': 'LAKHLAKI', 'pob': 'CILEGON', 'dob': '21011981', 'agama': 'ISLAM', 'pendidikan': 'ST RAT Al', 'pekerjaan': 'KARYAWAN SWASTA RI'}, {'name': 'FASIHAH OKT AFIANA', 'nik': '3273204910800001', 'gender': 'PEREMPUAN', 'pob': 'JAMBI', 'dob': '09101980', 'agama': 'ISLAM', 'pendidikan': 'DIPLOMA IV/ST RATA ', 'pekerjaan': 'KARYAWAN SWASTA'}, {'name': 'M IKAIL AZKA MUHAMMAD YAFFA', 'nik': '3273202510060001', 'gender': 'LAK LAKI', 'pob': 'BANDUNG', 'dob': '25102005', 'agama': 'ISLAM', 'pendidikan': 'BELUM TAMAT SD/SEDERAJAT', 'pekerjaan': 'PELAJAR/MAHASIS WA'}, {'name': 'GAZARYNE MARCHZA AOUILA YAFFA', 'nik': '9273208103140003', 'gender': 'PEREMPUAN', 'pob': 'BANDUNG', 'dob': '21032014', 'agama': 'ISLAM', 'pendidikan': 'TIDAK/BLM SEKOLAH', 'pekerjaan': 'BELUMIT IDAK BEKERJA'}]}


# for i in range(0, jumlahData):
#     person = []
#     for k in range(i,jumlahData*8,4):
#         person.append(splitLine[k])
#     print(person)

