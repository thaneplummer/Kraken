"""

CmdPostLib.py

Project: E2ESA

--tkp

Version: 1.2

"""


import click
from ipaddress import ip_address
from urllib import response
from SvcNowApi import SvcNowApi


# INSTANCE = 'dev108862'
# USER = 'thane.plummer'
# PWD = 'kdRs9ZuftR3kyt'
INSTANCE = 'dev57368'
USER = 'admin'
PWD = 'awiZ4uZSJ2*-'


class CmdPostLib(object):
    def __init__(self, element_table='x_380321_cmdpost_element', 
                        rule_nominee_table='x_380321_cmdpost_rule_nominee', 
                        fom_table='x_380321_cmdpost_metric', 
                        default_metric_group='a66e227a47199510d396c789826d433d', # Ops Status - IT
                        verbose=0) -> None:
        self.api = SvcNowApi(INSTANCE, USER, PWD)
        self.verbose = verbose
        self.element_table = element_table
        self.rule_nominee_table = rule_nominee_table
        self.fom_table = fom_table
        self.default_metric_group = default_metric_group
        self.foms = []
    

    def elementFromCmdbIP(self, ip_addr: str):
        element = None  # The return object
        # Validate IP address format.
        ip = ip_address(ip_addr)

        # Get CI sys_id by doing a JOIN on cmdb_ci AND element_table
        response = self.api.get('cmdb_ci', ['sys_id'], f'ip_address={ip.compressed}', 1)
        if response is not None:
            sys_id = response[0]['sys_id']
            print(f'cmdb_ci sys_id: {sys_id}')
            response = self.api.get(self.element_table, None, f'configuration_item={sys_id}', 1)
            if response is not None:
                element = Element(response[0])
                if self.verbose > 0:
                    print(element)
        return element
    

    def insertRuleNominee(self, rule_nominee):
        self.api.post(self.rule_nominee_table, rule_nominee)

    # @classmethod
    # def class_method(cls, passed_params):
    #     #code to execute

    # @staticmethod
    # def fomsFromGroupId(api: SvcNowApi, metric_group_id: str, fom_table='x_380321_cmdpost_metric'):
        # pass
    def fomsFromGroupId(self, metric_group_id: str):
        foms = []
        qry = f'metric_group={metric_group_id}'
        response = self.api.get(self.fom_table, None, qry, 20)
        if response is not None and len(response) > 0:
            for d in response:
                fom = FigureOfMerit(d)
                foms.append(fom)
        return foms
    

    def defaultFoms(self):
        return self.fomsFromGroupId(self.default_metric_group)
    

    @property
    def defaultFom(self):
        fom = None
        qry = f'metric_group={self.default_metric_group}^u_default=true'
        response = self.api.get(self.fom_table, None, qry, 1)
        # print('defaultFom...')
        # print(response)
        if response is not None and len(response) == 1:
            fom = FigureOfMerit(response[0])
        return fom



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
    

    # Getter method
    @property
    def metric_groups(self):
        return self.__metric_group_ids
     
    # Setter method
    @metric_groups.setter
    def metric_groups(self, val):
        self.__metric_group_ids = val
    
    # Deleter method
    @metric_groups.deleter
    def metric_groups(self):
       del self.__metric_group_ids

    # @property
    # def metric_group_ids(self):
    #     if self.metric_pairs == {}:
    #         return []
    #     return self.metric_pairs.keys()
    

    def __repr__(self) -> str:
        return f'Element(category={self.category}, \
metric_pairs={self.metric_pairs}, \
metric_group_ids={self.metric_groups}, \
name={self.name}, \
number={self.number}, \
short_description={self.short_description}, \
sys_id={self.sys_id}, \
u_domain={self.u_domain}, \
u_element_entity={self.u_element_entity}, \
u_grandparent={self.u_grandparent}, \
u_grouping={self.u_grouping}, \
u_level={self.u_level}, \
u_parent={self.u_parent}, \
u_personnel_name={self.u_personnel_name}, \
u_root_element={self.u_root_element})'


class FigureOfMerit(object):
    def __init__(self, data_dict) -> None:
        self.color = 'White'
        self.css_class = None
        self.integer_value = 0
        self.name = 'new_fom' 
        self.order = 0
        self.short_description = ''
        self.string_value = ''
        self.sys_id = None
        self.u_default = False
        self.fromDict(data_dict)
        self.dict = self.toDict()


    def fromDict(self, d):
        self.color = d['color'] if 'color' in d else self.color
        self.css_class = d['css_class'] if 'css_class' in d else self.css_class
        self.integer_value = d['integer_value'] if 'integer_value' in d else self.integer_value
        self.name = d['name'] if 'name' in d else self.name
        self.order = d['order'] if 'order' in d else self.order
        self.short_description = d['short_description'] if 'short_description' in d else self.short_description
        self.string_value = d['string_value'] if 'string_value' in d else self.string_value
        self.sys_id = d['sys_id'] if 'sys_id' in d else self.sys_id
        if 'u_default' in d:
            if d['u_default'].lower() == 'true':
                self.u_default = True
    

    def toDict(self):
        d = {}
        d['color'] = self.color
        d['css_class'] = self.css_class
        d['integer_value'] = self.integer_value
        d['name'] = self.name
        d['order'] = self.order
        d['short_description'] = self.short_description
        d['string_value'] = self.string_value
        d['sys_id'] = self.sys_id
        d['u_default'] = self.u_default
        return d


    def __repr__(self) -> str:
        return f'FigureOfMerit(color={self.color}, \
css_class={self.css_class}, \
integer_value={self.integer_value}, \
name={self.name}, \
order={self.order}, \
short_description={self.short_description}, \
string_value={self.string_value}, \
sys_id={self.sys_id}, \
u_default={self.u_default})'



class RuleNominee(object):
    def __init__(self, element_ref, prior_status, new_status, u_action, rule, new_metric):
        self.element_ref = element_ref 
        self.prior_status = prior_status 
        self.new_status = new_status 
        self.u_action = u_action 
        self.rule = rule 
        self.new_metric = new_metric 


    def toDict(self):
        return { "element_ref": self.element_ref,
            "prior_status": self.prior_status,
            "new_status": self.new_status,
            "u_action": self.u_action,
            "rule": self.rule,
            "new_metric": self.new_metric }
    

    def __repr__(self) -> str:
        return f'RuleNominee(element_ref={self.element_ref}, \
prior_status={self.prior_status}, \
new_status={self.new_status}, \
u_action={self.u_action}, \
rule={self.rule}, \
new_metric={self.new_metric})'


# -------------------------  T E S T S   B E G I N   -------------------------

def testGetFoMs():
    snlib = CmdPostLib()
    metric_group_id = 'e1ea2d4f47d9d510d396c789826d43c3'
    foms = snlib.fomsFromGroupId(metric_group_id)
    return foms


def testRuleNominee():
    element_ref = '34cc975c47891510d396c789826d4382'
    prior_status = 'FMC'
    new_status = 'NMC'
    u_action = 'approve'
    rule = 'd9a4327247599510d396c789826d4313'
    new_metric = '79c5bdad1be301100a015467624bcb85' 
    # Create a RuleNominee object
    rule_nominee = RuleNominee(element_ref, prior_status, new_status, u_action, rule, new_metric)
    # Get dictionary of object
    data = rule_nominee.toDict()
    # Write to SvcNow database
    table = 'x_380321_cmdpost_rule_nominee'
    api = SvcNowApi(INSTANCE, USER, PWD)
    result = api.post(table, data)
    return result


def run_tests():
    print('Running tests...')
    r = testGetFoMs()
    r = testRuleNominee()
    return r


# -------------------------  T E S T S   E N D   -------------------------


def main():
    print('cmdPostApi main function')
    # Given an IP address, get the element, FoMs, and create a RuleNominee to send to SvcNow.
    ip_addr = '10.0.53.5'
    print(f'\nGiven the IP address: {ip_addr}, find the associated Element.')
    snlib = CmdPostLib()
    element = snlib.elementFromCmdbIP(ip_addr)
    if (element.metric_pairs == {}):
        element.metric_pairs = {snlib.default_metric_group: snlib.defaultFom}
        element.metric_groups = list(element.metric_pairs.keys())
    print('\nELEMENT')
    print(element)
    print(f'From the associated Element, find the allowable FoMs.')
    metric_group_id = element.metric_groups[0] # 'e1ea2d4f47d9d510d396c789826d43c3'
    foms = snlib.fomsFromGroupId(metric_group_id)
    print('\nFOMs')
    print('==========================')
    for fom in foms:
        print(fom)
    # Now make an new RuleNominee
    print('\nFrom the Element and FoM list, create a new RuleNominee and insert it to ServiceNow.')
    element_fom = element.metric_pairs[metric_group_id]
    new_fom = foms[-1]
    prior_status = element_fom.string_value
    new_status = new_fom.string_value
    u_action = 'approve'
    # Hard-coded Rule sys_id. This will be part of the expert system.
    rule = '574aae3b1bd281100a015467624bcb68'
    new_metric = new_fom.sys_id
    # Create a RuleNominee object
    rule_nominee = RuleNominee(element.sys_id, prior_status, new_status, u_action, rule, new_metric)
    print('\nNew RuleNominee')
    print(rule_nominee)
    # Get dictionary of object
    data = rule_nominee.toDict()
    # Write to SvcNow database
    print('\nSaving new RuleNominee to ServiceNow')
    response = snlib.api.post(snlib.rule_nominee_table, data)
    print(f'POST RuleNominee response: {response.status_code}')
    return element


@click.command()
@click.option("--ip_address", default="8.1.252.2", help="IP address of server.")
@click.option("--description", default="Login failure", help="Description of the cyber anomaly.")
@click.option("--verbosity", default=2, help="Verbosity level (0-3).")
def postRuleNominee(ip_address, description, verbosity):
    snlib = CmdPostLib()
    element = snlib.elementFromCmdbIP(ip_address)
    if element is not None:
        if (element.metric_pairs == {}):
            element.metric_pairs = {snlib.default_metric_group: snlib.defaultFom}
            element.metric_groups = list(element.metric_pairs.keys())
        if verbosity > 0:
            print(f'\nELEMENT FOUND -> IP Address {ip_address}\n')
            if verbosity > 1:
                print(element)
        metric_group_id = element.metric_groups[0] # 'e1ea2d4f47d9d510d396c789826d43c3'
        foms = snlib.fomsFromGroupId(metric_group_id)
        if verbosity > 0:
            print('\nELEMENT FoMs FOUND')
            if verbosity > 2:
                print('==========================')
                for fom in foms:
                    print(fom)
        # Now make an new RuleNominee
        if verbosity > 2:
            print('\nFrom the Element and FoM list, create a new RuleNominee and insert it to ServiceNow.')
        element_fom = element.metric_pairs[metric_group_id]
        new_fom = foms[-1]
        prior_status = element_fom.string_value
        new_status = new_fom.string_value
        u_action = 'approve'
        # Hard-coded Rule sys_id. This will be part of the expert system.
        rule = '574aae3b1bd281100a015467624bcb68'   # Multiple failed logon attempts
        new_metric = new_fom.sys_id
        # Create a RuleNominee object
        rule_nominee = RuleNominee(element.sys_id, prior_status, new_status, u_action, rule, new_metric)
        if verbosity > 0:
            print('\nNEW RuleNominee CREATED IN SERVICENOW\n')
            if verbosity > 1:
                print(rule_nominee)
        # Get dictionary of object
        data = rule_nominee.toDict()
        # Write to SvcNow database
        if verbosity > 0:
            print('\nSaving new RuleNominee to ServiceNow')
        response = snlib.api.post(snlib.rule_nominee_table, data)
        if verbosity > 0:
            print(f'POST RuleNominee response: {response.status_code}')
    return element


if __name__ == "__main__":
    el = postRuleNominee()
    