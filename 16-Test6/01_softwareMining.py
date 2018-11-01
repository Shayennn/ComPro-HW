#std35: Phitchawat Lukkanathiti
#date: 01NOV2018
#program: 01_softwareMining.py
#description: too long to descript.

def loadSMCSV():
    f = open('Sample.csv')
    data = {}
    head = f.readline().strip().split()
    while True:
        line = f.readline().strip()
        if line=='':
            break
        row = line.split()
        data[row[0]] = {}
        for i in range(0,len(row)):
            data[row[0]][head[i]] = row[i]
    return data

def fetchRowGroup( data, rowname ):
    returnrow = {}
    for row in data.values():
        if row[rowname] not in returnrow:
            returnrow[row[rowname]] = 1
        else:
            returnrow[row[rowname]] += 1
    return returnrow

def fetchSomeRow( data, rowname):
    returnrow = []
    for name, row in data.items():
        returnrow.append((name,row[rowname]))
    return returnrow

def getDataFromKey( data, key, row):
    ret = []
    for i in key:
        ret.append((i,data[i][row]))
    return ret

def calcAverage( data, key, row):
    total = 0
    for i in key:
        total += float(data[i][row])
    return total/len(key)

def dict2tuplelist( dictdata ):
    d2tuplelist = [(name, data) for name, data in dictdata.items()]
    return d2tuplelist

def sortData( data , reverse = False):
    data.sort(key=lambda x:float(x[1]), reverse=reverse)
    return data

def tupleval( data ):
    return [x for _,x in data]

def countMin( data ):
    data = [x for _,x in data]
    return data.count(min(data))

def countMax( data ):
    data = [x for _,x in data]
    return data.count(max(data))

def filterByData ( data, where):
    output = {}
    for name, projectdata in data.items():
        ok = True
        for fkey, fval in where.items():
            if projectdata[fkey] != fval:
                ok = False
                break
        if ok:
            output[name]=projectdata
    return output

def filterByData_for_js ( data, where):
    output = {}
    for name, projectdata in data.items():
        ok = True
        for fkey, fval in where.items():
            if projectdata[fkey].lower().count(fval) == 0:
                ok = False
                break
        if ok:
            output[name]=projectdata
    return output

def filterByData_for_ext ( data, where):
    output = {}
    for name, projectdata in data.items():
        ok = True
        for fkey, fval in where.items():
            if projectdata[fkey].split('.')[-1].lower() in fval or projectdata[fkey].count('.')==0:
                ok = False
                break
        if ok:
            output[name]=projectdata
    return output

def main():
    data = loadSMCSV()
    platform_list = sortData(dict2tuplelist(fetchRowGroup(data, 'Platform')), True)
    license_list = sortData(dict2tuplelist(fetchRowGroup(data, 'License')), True)
    version_list = sortData(fetchSomeRow(data,'NbOfVersions'), True)
    print('1.',len(platform_list),platform_list[0:2])
    print('2.',len(license_list),license_list[0:3])
    print('3.',version_list[0:2])

    python_list = [x for x,y in fetchSomeRow(data,'Language') if y == 'Python']
    print('4.',calcAverage(data,python_list,'Size'),'MB')

    github_list = filterByData(data,{'Host':'GitHub'})
    git_lang = sortData(dict2tuplelist(fetchRowGroup(github_list, 'Language')))
    print('5.',countMin(git_lang))
    print('6.',git_lang[0:30])

    non_markdown_list = filterByData_for_ext(data,{'ReadmeFilename':['md','markdown']})
    non_markdown = fetchSomeRow( non_markdown_list, 'ReadmeFilename')
    readme_file = tupleval(non_markdown)
    ext = set()
    for filename in readme_file:
        ext.update([filename.split('.')[-1].lower()])
    print('7.',len(ext))

    github_star = sortData(fetchSomeRow( github_list, 'Stars'), True)
    print('8.',github_star[0][0],data[github_star[0][0]])

    js_data = filterByData_for_js(data,{'Name':'js'})
    print('9.',len(js_data))

if __name__ == "__main__":
    main()