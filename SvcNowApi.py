"""

SvcNowApi.py

Project: E2ESA

--tkp

"""


import requests


INSTANCE = 'dev108862'
USER = 'thane.plummer'
PWD = 'kdRs9ZuftR3kyt'


class SvcNowApi(object):
    def __init__(self, instance, user, pwd) -> None:
        self.instance = instance
        self.credentials = (user, pwd)
        self.headers = {"Content-Type":"application/json","Accept":"application/json"}
        self.url = f'https://{instance}.service-now.com/api/now/table/'


    def get(self, table, fieldlist=None, query=None, limit=10, verbose=0):
        params = []
        url = self.url + f'{table}?'
        if fieldlist is not None:
            params.append(f"sysparm_fields={','.join(fieldlist)}")
        if query is not None:
            params.append(f'sysparm_query={query}')
        params.append(f'sysparm_limit={limit}')
        url += '&'.join(params)
        response = requests.get(url, auth=self.credentials, headers=self.headers)
        # Check for HTTP codes other than 200
        if response.status_code != 200: 
            print('ERROR')
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
            return None

        # Decode the JSON response into a dictionary and return the data
        data = response.json()  # Converts to a dict.
        results = data['result']
        if verbose > 0:
            print(f'GET yielded {len(results)} rows')
        return results


    def post(self, table, datadict, verbose=0):
        # Set the request parameters
        keys = ','.join(datadict.keys())
        url = self.url + f'{table}?sysparm_fields={keys}'
        datastr = str(datadict) #, encoding = "utf-8", errors ="ignore")
        datastr = datastr.replace('None', '""')     # <<=== The MAGIC line that makes it work!
        datastr = datastr.encode('utf-8')
        if verbose > 0:
            print(f'Sending POST request. url: {url}, data: {datastr}')
        response = requests.post(url, auth=self.credentials, headers=self.headers ,data=datastr)
        if verbose > 0:
            print('Response from POST: ', response)
        return response


# -------------------------  T E S T S   B E G I N   -------------------------


def get_test():
    table = 'x_380321_cmdpost_rule_nominee'
    fields = 'element_ref,u_action,rule,new_status,prior_status,approve,new_metric'.split(',')
    api = SvcNowApi(INSTANCE, USER, PWD)
    results = api.get(table, fields) #, None, limit)
    return results


def get_test_query(ip_address):
    limit = 1
    table = 'cmdb_ci'
    fields = None
    query = f'ip_address={ip_address}'
    api = SvcNowApi(INSTANCE, USER, PWD)
    results = api.get(table, fields, query, limit)
    return results


def post_test():
    table = 'x_380321_cmdpost_rule_nominee'
    data = {"element_ref":"34cc975c47891510d396c789826d4382",
        "prior_status":"FMC",
        "new_status":"NMC",
        "u_action":"approve",
        "rule":"d9a4327247599510d396c789826d4313",
        "new_metric":"79c5bdad1be301100a015467624bcb85"}
    api = SvcNowApi(INSTANCE, USER, PWD)
    result = api.post(table, data)
    return result


def run_tests():
    print('Running tests...')
    ip_addr = '10.0.53.5'
    results = get_test_query(ip_addr)
    if results is not None:
        for result in results:
            print(result)
    r = post_test()
    return r


# -------------------------  T E S T S   E N D   -------------------------


def main():
    print('SvcNowApi main function')
    r = run_tests()
    return r


if __name__ == "__main__":
    response = main()
    