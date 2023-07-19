#Need to install requests package for python
#easy_install requests
import requests
import json

#Set up for JSON data
def getJDict(filename):
    with open(filename) as j:
        jDict = json.loads(j.read())
    return jDict

def getRecords(jDict):
    return jDict['records']

myDict = getJDict(r'x_380321_cmdpost_element.json')
rawRecords = getRecords(myDict)
jLevel2 = getRecords(getJDict(r'C:\Users\randy\Documents\Programming_resources\Scripts\Python_Scripts\Kraken\levels\level_2\x_380321_cmdpost_element_level2.json'))
# print(myDict['records'][0])
# exit()

#Element Class
class Element(object):
    def __init__(self, data_dict) -> None:
        self.category = ''
        self.children = []
        self.configuration_item = ''
        self.configuration_item_display_value = ''
        self.hierarchy = ''
        self.hierarchy_display_value = ''
        self.is_head = False
        self.metric_pairs = {}
        self.name = ''
        self.number = ''
        self.short_description = ''
        self.sys_id = ''
        self.u_circuitid = ''
        self.u_domain = ''
        self.u_element_entity = ''
        self.u_grandparent = ''
        self.u_grouping = ''
        self.u_image = ''
        self.u_include_diagram = ''
        self.u_level = ''
        self.u_parent = ''
        self.u_personnel_name = ''
        self.u_root_element = ''
        self.u_root_element_display_value = ''
        self.fromDict(data_dict)
        self.__metric_group_ids = [] 

    def fromDict(self, d):
        self.category = d['category'] if 'category' in d else self.category
        self.children = d['children'] if 'children' in d else self.children
        self.configuration_item = d['configuration_item'] if 'configuration_item' in d else self.configuration_item
        self.hierarchy = d['hierarchy'] if 'hierarchy' in d else self.hierarchy
        # if 'metric_pairs' in d:
        #     val = d['metric_pairs']
        #     if type(val) == dict:
        #         self.metric_pairs = val
        #         self.metric_groups = val.keys()
        self.name = d['name'] if 'name' in d else self.name
        self.number = d['number'] if 'number' in d else self.number
        self.short_description = d['short_description'] if 'short_description' in d else self.short_description
        self.sys_id = d['sys_id'] if 'sys_id' in d else self.sys_id
        self.u_circuitid = d['u_circuitid'] if 'u_circuitid' in d else self.u_circuitid
        self.u_domain = d['u_domain'] if 'u_domain' in d else self.u_domain
        self.u_element_entity = d['u_element_entity'] if 'u_element_entity' in d else self.u_element_entity
        self.u_grandparent = d['u_grandparent'] if 'u_grandparent' in d else self.u_grandparent
        self.u_grouping = d['u_grouping'] if 'u_grouping' in d else self.u_grouping
        self.u_image = d['u_image'] if 'u_image' in d else self.u_image
        self.u_include_diagram = d['u_include_diagram'] if 'u_include_diagram' in d else self.u_include_diagram
        self.u_level = d['u_level'] if 'u_level' in d else self.u_level
        self.u_parent = d['u_parent'] if 'u_parent' in d else self.u_parent
        self.u_personnel_name = d['u_personnel_name'] if 'u_personnel_name' in d else self.u_personnel_name
        self.u_root_element = d['u_root_element'] if 'u_root_element' in d else self.u_root_element
    
    def getProperties(self, *properties):
        return {p:self.__dict__[p] for p in properties}
    
    @property
    def eDict(self):
        return self.__dict__
    
#Utility Functions
def editElem(elem):
    hierIDs = {'Transport': '32eb15882f803110c1dcae6df699b690', 'Connections': '7ff1acc847d91110d396c789826d433c'}
    fields = ['short_description', 'u_domain', 'u_group', 'u_circuitid', 'u_entity', 'u_cmdb_group', 'u_attributes', 'u_simple_name_values_2', 'u_nist_control', 'u_personnel_name', 'configuration_item', 'name', 'category', 'u_attribute_group','u_parent','element_source']
    e = {}
    for f in fields:
        e[f] = elem[f]
    u_level = int(elem['u_level'])
    e['u_level'] = u_level + 1
    e['hierarchy'] = hierIDs['Connections']
    e['u_parent'] = '585ee9e22f40b110c1dcae6df699b69b'
    e['u_hide_fom'] = 'true'
    return e
 
def makeNewElems(oldDict):
    records = oldDict['records']
    return [editElem(r) for r in records]

def sortRecords(records, key):
    newDict = {}
    for r in records:
        value = r[key]
        newDict.setdefault(value, [])
        newDict[value].append(r)
    return newDict

def sort1(records, key):
    return {r[key]: r for r in records}

def mapThing(rec1, rec2, k1, k2): #k1 is the common key, k2 is where they differ
    q1, q2 = sort1(rec1, k1), sort1(rec2, k1) #query for sorting recs by k1
    print(type(q1))
    newDict = {}
    for k,v in q1.items(): #k key would be instance of k1
        # print(k)
        # print(v)
        v1 = v[k2] #v is the dict of q1
        v2 = q2[k][k2] #v
        newDict[k] = {v1:v2}
    return newDict

def flatMap(mapper):
    return {k:v for i in mapper.values() for k,v in i.items()}

def getChildren(elem, records=rawRecords):
    childrenid = set(elem['children'].split(','))
    children = list(filter(lambda x: x['sys_id'] in childrenid, records))
    return children


# print('\n')
# print(makeNewDict(myDict)['records'][0])

#REQUESTS SET UP
# Set the request parameters
url = 'https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'arendil.plummer'
pwd = 'Only4ankp!'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

#create the new JSON
records = makeNewElems(myDict)
# unBoxRec = records['records']

#---------Test Begin----------------------------------

jLevel3 = getRecords(getJDict(r'C:\Users\randy\Documents\Programming_resources\Scripts\Python_Scripts\Kraken\levels\level_3\x_380321_cmdpost_element_level3.json'))

rawTree = sortRecords(rawRecords, 'u_level')
tree = sortRecords(records, 'u_level')
# testChildren = getChildren(tree[3])
# print([t['element_source'] for t in records])

def groupMap(rec1, rec2, k1, k2): #k1 is the common key, k2 is where they differ
    q1, q2 = sort1(rec1, k1), sort1(rec2, k1) #query for sorting recs by k1
    print(type(q1))
    newDict = {}
    for k,v in q1.items(): #k key would be instance of k1
        # print(k)
        # print(v)
        v1 = v[k2] #v is the dict of q1
        v2 = q2[k][k2] #v
        newDict[k] = {v1:v2}
    return newDict

def getParents(parents, newParents, children):
    mapper = flatMap(mapThing(parents, newParents, 'name', 'sys_id'))
    print(mapper)
    for c in children:
        oldP = c['u_parent']
        # print(oldP)
        c['u_parent'] = mapper[oldP]

# print(tree[3][0]['u_parent'])
# mapper = flatMap(mapThing(rawTree['1'], jLevel2, 'name', 'sys_id'))
# getParents(rawTree['1'], jLevel2, tree[3])
# print(tree[4][0]['u_parent'])
# getParents(rawTree['2'], jLevel3, tree[4])
# print(tree[4][0]['u_parent'])
pid = 'TC12M0710G'
# print(len([t for t in tree[3] if t['u_parent'] == pid]))
# testE = Element(rawRecords[0])
# print(testE.__dict__)

# print(len(testChildren))
# names_id = mapThing(rawTree['1'], jLevel2, 'name', 'sys_id')
# print(flatMap(names_id))
# levelID = {1: {'Transport': '585ee9e22f40b110c1dcae6df699b69b'}, 2: {'[A16] Georgia Hydro Data Center': }}
# print('\n%s' %(total))
# payload = [r for r in records if r['u_level'] == 2]

# exit()
#----------Test End-------------------------------------


#making one HTTP request
def makeRequest(url, user, pwd, headers, payload):
    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers, json=payload)

    # Check for HTTP codes other than 200
    # if response.status_code != 200: 
        # print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        # exit()
    return response

def manyRequests(paylist, url=url, user=user, pwd=pwd, headers=headers):
    for p in paylist:
        r = makeRequest(url, user, pwd, headers, p)
        if r.status_code != 201:
            print(r.json())
            break    
# Decode the JSON response into a dictionary and use the data
# data = response.json()
# print(data)

#going through the list
manyRequests(records)