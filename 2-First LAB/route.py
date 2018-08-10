dist={
    'Seattle':{
        'Atlanta':2641,
        'Boston':3032,
        'Chicago':2043,
        'Los Angeles':1208,
        'New York City':2832,
        'San Francisco':808
    },
    'Atlanta':{
        'Boston':1110,
        'Chicago':718,
        'Los Angeles':2175,
        'New York City':888,
        'San Francisco':2473
    },
    'Boston':{
        'Chicago':992,
        'Los Angeles':2991,
        'New York City':215,
        'San Francisco':3106
    },
    'Chicago':{
        'Los Angeles':2015,
        'New York City':791,
        'San Francisco':2131
    },
    'Los Angeles':{
        'New York City':2709,
        'San Francisco':381
    },
    'New York City':{
        'San Francisco':2901
    }
}

cities={
        'Seattle':False,
        'Atlanta':False,
        'Boston':False,
        'Chicago':False,
        'Los Angeles':False,
        'New York City':False,
        'San Francisco':False
}

def getDist(start,end):
    if(start not in dist):
        (start,end)=(end,start)
    if(end in dist[start]):
        return (dist[start][end])
    else:
        return (dist[end][start])

def bruteforce(unsuccessroute):
    newroute=[]
    for route in unsuccessroute:
        leftcities=[x for x,y in cities.items() if not y and x not in route['route']]
        for newcity in leftcities:
            if len(leftcities)==1:
                newroute.append({'dist':route['dist']+getDist(route['route'][-1],newcity)+getDist(newcity,end),'route':route['route']+[newcity,end]})
            else:
                newroute.append({'dist':route['dist']+getDist(route['route'][-1],newcity),'route':route['route']+[newcity]})
    if len(leftcities)!=1:
        newroute = bruteforce(newroute)
    return newroute
        
 

start='Atlanta'
end='San Francisco'

cities[start]=True
cities[end]=True
route=[{'dist':0,'route':[start]}]
route=bruteforce(route)
route=sorted(route, key=lambda eachroute: eachroute['dist'])

print("Total route calculated:",len(route))
print("Shortest route is ")
print(route[0]['route'])
print("With",route[0]['dist'],"miles")
