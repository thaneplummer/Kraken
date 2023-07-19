
import requests

jsondata = """{
  "result": [
    {
      "short_description": "Estimate the maximum bandwidth of those channels. ",
      "is_head": "false",
      "u_domain": "",
      "u_group": "",
      "sys_updated_on": "2023-06-14 21:13:36",
      "u_circuitid": "",
      "u_level": "3",
      "sys_class_name": "x_380321_cmdpost_element",
      "number": "",
      "sys_id": "0016060a2fa12150c1dcae6df699b638",
      "sys_updated_by": "thane.plummer",
      "children": "",
      "sys_created_on": "2023-03-14 16:33:09",
      "element_source": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element_source/9d88f47f2fdba110c1dcae6df699b678",
        "value": "9d88f47f2fdba110c1dcae6df699b678"
      },
      "u_entity": "",
      "u_cmdb_group": "",
      "u_attributes": "",
      "u_simple_name_values_2": "",
      "sys_created_by": "thane.plummer",
      "u_nist_control": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_auditplus_nist_800_53/1ba8e6202f782190c1dcae6df699b609",
        "value": "1ba8e6202f782190c1dcae6df699b609"
      },
      "hierarchy": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_hierarchy/647835482f046510c1dcae6df699b614",
        "value": "647835482f046510c1dcae6df699b614"
      },
      "u_root_element": "",
      "sys_mod_count": "6",
      "sys_tags": "",
      "u_personnel_name": "",
      "u_hide_fom": "false",
      "u_parent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/11458a862fa12150c1dcae6df699b6c4",
        "value": "11458a862fa12150c1dcae6df699b6c4"
      },
      "configuration_item": "",
      "name": "SC-31 b",
      "category": "nist control",
      "u_grandparent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/cf25c6862fa12150c1dcae6df699b63c",
        "value": "cf25c6862fa12150c1dcae6df699b63c"
      },
      "metric_pairs": "",
      "u_attribute_group": ""
    },
    {
      "short_description": "",
      "is_head": "false",
      "u_domain": "",
      "u_group": "",
      "sys_updated_on": "2023-06-14 21:13:36",
      "u_circuitid": "",
      "u_level": "2",
      "sys_class_name": "x_380321_cmdpost_element",
      "number": "",
      "sys_id": "00454a862fa12150c1dcae6df699b6eb",
      "sys_updated_by": "thane.plummer",
      "children": "5806420a2fa12150c1dcae6df699b638,d006420a2fa12150c1dcae6df699b639,9c06420a2fa12150c1dcae6df699b639",
      "sys_created_on": "2023-03-14 16:29:35",
      "element_source": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element_source/1d88f47f2fdba110c1dcae6df699b679",
        "value": "1d88f47f2fdba110c1dcae6df699b679"
      },
      "u_entity": "",
      "u_cmdb_group": "",
      "u_attributes": "",
      "u_simple_name_values_2": "",
      "sys_created_by": "thane.plummer",
      "u_nist_control": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_auditplus_nist_800_53/6bac3f89473f1110d396c789826d43fa",
        "value": "6bac3f89473f1110d396c789826d43fa"
      },
      "hierarchy": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_hierarchy/647835482f046510c1dcae6df699b614",
        "value": "647835482f046510c1dcae6df699b614"
      },
      "u_root_element": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/0325c6862fa12150c1dcae6df699b63c",
        "value": "0325c6862fa12150c1dcae6df699b63c"
      },
      "sys_mod_count": "9",
      "sys_tags": "",
      "u_personnel_name": "",
      "u_hide_fom": "false",
      "u_parent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/0325c6862fa12150c1dcae6df699b63c",
        "value": "0325c6862fa12150c1dcae6df699b63c"
      },
      "configuration_item": "",
      "name": "PM-11",
      "category": "nist control",
      "u_grandparent": "",
      "metric_pairs": "",
      "u_attribute_group": ""
    },
    {
      "short_description": "",
      "is_head": "false",
      "u_domain": "",
      "u_group": "",
      "sys_updated_on": "2023-06-14 21:13:36",
      "u_circuitid": "",
      "u_level": "2",
      "sys_class_name": "x_380321_cmdpost_element",
      "number": "",
      "sys_id": "00454a862fa12150c1dcae6df699b6f6",
      "sys_updated_by": "thane.plummer",
      "children": "2006420a2fa12150c1dcae6df699b683,a806420a2fa12150c1dcae6df699b683,6406420a2fa12150c1dcae6df699b684",
      "sys_created_on": "2023-03-14 16:29:36",
      "element_source": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element_source/5988f47f2fdba110c1dcae6df699b67a",
        "value": "5988f47f2fdba110c1dcae6df699b67a"
      },
      "u_entity": "",
      "u_cmdb_group": "",
      "u_attributes": "",
      "u_simple_name_values_2": "",
      "sys_created_by": "thane.plummer",
      "u_nist_control": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_auditplus_nist_800_53/efac3f89473f1110d396c789826d43fe",
        "value": "efac3f89473f1110d396c789826d43fe"
      },
      "hierarchy": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_hierarchy/647835482f046510c1dcae6df699b614",
        "value": "647835482f046510c1dcae6df699b614"
      },
      "u_root_element": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/0325c6862fa12150c1dcae6df699b63c",
        "value": "0325c6862fa12150c1dcae6df699b63c"
      },
      "sys_mod_count": "9",
      "sys_tags": "",
      "u_personnel_name": "",
      "u_hide_fom": "false",
      "u_parent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/0325c6862fa12150c1dcae6df699b63c",
        "value": "0325c6862fa12150c1dcae6df699b63c"
      },
      "configuration_item": "",
      "name": "PM-21",
      "category": "nist control",
      "u_grandparent": "",
      "metric_pairs": "",
      "u_attribute_group": ""
    },
    {
      "short_description": "",
      "is_head": "false",
      "u_domain": "space",
      "u_group": "",
      "sys_updated_on": "2023-06-14 21:13:36",
      "u_circuitid": "",
      "u_level": "4",
      "sys_class_name": "x_380321_cmdpost_element",
      "number": "",
      "sys_id": "009af3a247e51110d396c789826d439c",
      "sys_updated_by": "thane.plummer",
      "children": "",
      "sys_created_on": "2022-08-29 18:07:56",
      "element_source": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element_source/5588f47f2fdba110c1dcae6df699b67b",
        "value": "5588f47f2fdba110c1dcae6df699b67b"
      },
      "u_entity": "",
      "u_cmdb_group": "",
      "u_attributes": "",
      "u_simple_name_values_2": "",
      "sys_created_by": "elliott.claus",
      "u_nist_control": "",
      "hierarchy": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_hierarchy/a77cb67247999510d396c789826d43da",
        "value": "a77cb67247999510d396c789826d43da"
      },
      "u_root_element": "",
      "sys_mod_count": "8",
      "sys_tags": "",
      "u_personnel_name": "",
      "u_hide_fom": "false",
      "u_parent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/4588a71747d11110d396c789826d43c2",
        "value": "4588a71747d11110d396c789826d43c2"
      },
      "configuration_item": {
        "link": "https://dev57368.service-now.com/api/now/table/cmdb_ci/c2533e351be341100a015467624bcb11",
        "value": "c2533e351be341100a015467624bcb11"
      },
      "name": "Solar Array 1",
      "category": "cmdb item",
      "u_grandparent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/0de0224b47511910d396c789826d4326",
        "value": "0de0224b47511910d396c789826d4326"
      },
      "metric_pairs": "",
      "u_attribute_group": ""
    },
    {
      "short_description": "Require, if no NIAP-approved Protection Profile exists for a specific technology type but a commercially provided information technology product relies on cryptographic functionality to enforce its security policy, that the cryptographic module is FI",
      "is_head": "false",
      "u_domain": "",
      "u_group": "",
      "sys_updated_on": "2023-06-14 21:13:36",
      "u_circuitid": "",
      "u_level": "4",
      "sys_class_name": "x_380321_cmdpost_element",
      "number": "",
      "sys_id": "00b6864a2fa12150c1dcae6df699b639",
      "sys_updated_by": "thane.plummer",
      "children": "",
      "sys_created_on": "2023-03-14 16:35:52",
      "element_source": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element_source/5d8830372f1fa110c1dcae6df699b6d0",
        "value": "5d8830372f1fa110c1dcae6df699b6d0"
      },
      "u_entity": "",
      "u_cmdb_group": "",
      "u_attributes": "",
      "u_simple_name_values_2": "",
      "sys_created_by": "thane.plummer",
      "u_nist_control": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_auditplus_nist_800_53/fd012e672fac6950c1dcae6df699b62c",
        "value": "fd012e672fac6950c1dcae6df699b62c"
      },
      "hierarchy": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_hierarchy/647835482f046510c1dcae6df699b614",
        "value": "647835482f046510c1dcae6df699b614"
      },
      "u_root_element": "",
      "sys_mod_count": "6",
      "sys_tags": "",
      "u_personnel_name": "",
      "u_hide_fom": "false",
      "u_parent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/be06c20a2fa12150c1dcae6df699b63d",
        "value": "be06c20a2fa12150c1dcae6df699b63d"
      },
      "configuration_item": "",
      "name": "SA-4(7) (b)",
      "category": "nist control",
      "u_grandparent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/34458a862fa12150c1dcae6df699b65c",
        "value": "34458a862fa12150c1dcae6df699b65c"
      },
      "metric_pairs": "",
      "u_attribute_group": ""
    },
    {
      "short_description": "Identify a secondary authoritative time source that is in a different geographic region than the primary authoritative time source; and ",
      "is_head": "false",
      "u_domain": "",
      "u_group": "",
      "sys_updated_on": "2023-06-14 21:13:36",
      "u_circuitid": "",
      "u_level": "4",
      "sys_class_name": "x_380321_cmdpost_element",
      "number": "",
      "sys_id": "00b6864a2fa12150c1dcae6df699b682",
      "sys_updated_by": "thane.plummer",
      "children": "",
      "sys_created_on": "2023-03-14 16:35:53",
      "element_source": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element_source/1d8830372f1fa110c1dcae6df699b6d1",
        "value": "1d8830372f1fa110c1dcae6df699b6d1"
      },
      "u_entity": "",
      "u_cmdb_group": "",
      "u_attributes": "",
      "u_simple_name_values_2": "",
      "sys_created_by": "thane.plummer",
      "u_nist_control": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_auditplus_nist_800_53/a9ff6eac2f782190c1dcae6df699b684",
        "value": "a9ff6eac2f782190c1dcae6df699b684"
      },
      "hierarchy": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_hierarchy/647835482f046510c1dcae6df699b614",
        "value": "647835482f046510c1dcae6df699b614"
      },
      "u_root_element": "",
      "sys_mod_count": "6",
      "sys_tags": "",
      "u_personnel_name": "",
      "u_hide_fom": "false",
      "u_parent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/9416060a2fa12150c1dcae6df699b668",
        "value": "9416060a2fa12150c1dcae6df699b668"
      },
      "configuration_item": "",
      "name": "SC-45(2) (a)",
      "category": "nist control",
      "u_grandparent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/6d45ca862fa12150c1dcae6df699b60e",
        "value": "6d45ca862fa12150c1dcae6df699b60e"
      },
      "metric_pairs": "",
      "u_attribute_group": ""
    },
    {
      "short_description": "Determine and document the types of changes to the system that are configuration controlled;",
      "is_head": "false",
      "u_domain": "",
      "u_group": "",
      "sys_updated_on": "2023-06-14 21:13:36",
      "u_circuitid": "",
      "u_level": "3",
      "sys_class_name": "x_380321_cmdpost_element",
      "number": "",
      "sys_id": "00f58ec62fa12150c1dcae6df699b611",
      "sys_updated_by": "thane.plummer",
      "children": "",
      "sys_created_on": "2023-03-14 16:32:36",
      "element_source": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element_source/998830372f1fa110c1dcae6df699b6d2",
        "value": "998830372f1fa110c1dcae6df699b6d2"
      },
      "u_entity": "",
      "u_cmdb_group": "",
      "u_attributes": "",
      "u_simple_name_values_2": "",
      "sys_created_by": "thane.plummer",
      "u_nist_control": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_auditplus_nist_800_53/c9b8af732fc8a110c1dcae6df699b6f7",
        "value": "c9b8af732fc8a110c1dcae6df699b6f7"
      },
      "hierarchy": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_hierarchy/647835482f046510c1dcae6df699b614",
        "value": "647835482f046510c1dcae6df699b614"
      },
      "u_root_element": "",
      "sys_mod_count": "6",
      "sys_tags": "",
      "u_personnel_name": "",
      "u_hide_fom": "false",
      "u_parent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/8b354a862fa12150c1dcae6df699b62b",
        "value": "8b354a862fa12150c1dcae6df699b62b"
      },
      "configuration_item": "",
      "name": "CM-3 a",
      "category": "nist control",
      "u_grandparent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/0b25c6862fa12150c1dcae6df699b63a",
        "value": "0b25c6862fa12150c1dcae6df699b63a"
      },
      "metric_pairs": "",
      "u_attribute_group": ""
    },
    {
      "short_description": "",
      "is_head": "false",
      "u_domain": "it",
      "u_group": "",
      "sys_updated_on": "2023-06-14 21:13:36",
      "u_circuitid": "",
      "u_level": "3",
      "sys_class_name": "x_380321_cmdpost_element",
      "number": "",
      "sys_id": "010469a047151110d396c789826d4334",
      "sys_updated_by": "thane.plummer",
      "children": "",
      "sys_created_on": "2022-08-10 15:46:48",
      "element_source": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element_source/198830372f1fa110c1dcae6df699b6d3",
        "value": "198830372f1fa110c1dcae6df699b6d3"
      },
      "u_entity": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_entity/82376c531bce81100a015467624bcb99",
        "value": "82376c531bce81100a015467624bcb99"
      },
      "u_cmdb_group": "",
      "u_attributes": "",
      "u_simple_name_values_2": "",
      "sys_created_by": "elizabeth.campbell",
      "u_nist_control": "",
      "hierarchy": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_hierarchy/f0e4f1291be301100a015467624bcb13",
        "value": "f0e4f1291be301100a015467624bcb13"
      },
      "u_root_element": "",
      "sys_mod_count": "13",
      "sys_tags": "",
      "u_personnel_name": "",
      "u_hide_fom": "false",
      "u_parent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/4db221ec47d11110d396c789826d4340",
        "value": "4db221ec47d11110d396c789826d4340"
      },
      "configuration_item": {
        "link": "https://dev57368.service-now.com/api/now/table/cmdb_ci/93a20f451b4241100a015467624bcb5c",
        "value": "93a20f451b4241100a015467624bcb5c"
      },
      "name": "T19RTW001",
      "category": "cmdb item",
      "u_grandparent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/beb704b31bf341100a015467624bcb70",
        "value": "beb704b31bf341100a015467624bcb70"
      },
      "metric_pairs": "",
      "u_attribute_group": ""
    },
    {
      "short_description": "Attach data tags containing [Assignment: organization-defined authorized processing] to [Assignment: organization-defined elements of personally identifiable information]. ",
      "is_head": "false",
      "u_domain": "",
      "u_group": "",
      "sys_updated_on": "2023-06-14 21:13:36",
      "u_circuitid": "",
      "u_level": "3",
      "sys_class_name": "x_380321_cmdpost_element",
      "number": "",
      "sys_id": "0106420a2fa12150c1dcae6df699b6dc",
      "sys_updated_by": "thane.plummer",
      "children": "",
      "sys_created_on": "2023-03-14 16:32:56",
      "element_source": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element_source/d58830372f1fa110c1dcae6df699b6d4",
        "value": "d58830372f1fa110c1dcae6df699b6d4"
      },
      "u_entity": "",
      "u_cmdb_group": "",
      "u_attributes": "",
      "u_simple_name_values_2": "",
      "sys_created_by": "thane.plummer",
      "u_nist_control": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_auditplus_nist_800_53/d2289d172f2ce550c1dcae6df699b66d",
        "value": "d2289d172f2ce550c1dcae6df699b66d"
      },
      "hierarchy": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_hierarchy/647835482f046510c1dcae6df699b614",
        "value": "647835482f046510c1dcae6df699b614"
      },
      "u_root_element": "",
      "sys_mod_count": "6",
      "sys_tags": "",
      "u_personnel_name": "",
      "u_hide_fom": "false",
      "u_parent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/6c458a862fa12150c1dcae6df699b63b",
        "value": "6c458a862fa12150c1dcae6df699b63b"
      },
      "configuration_item": "",
      "name": "PT-2(1)",
      "category": "nist control",
      "u_grandparent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/8725c6862fa12150c1dcae6df699b63c",
        "value": "8725c6862fa12150c1dcae6df699b63c"
      },
      "metric_pairs": "",
      "u_attribute_group": ""
    },
    {
      "short_description": "Present [Assignment: organization-defined consent mechanisms] to individuals at [Assignment: organization-defined frequency] and in conjunction with [Assignment: organization-defined personally identifiable information processing]. ",
      "is_head": "false",
      "u_domain": "",
      "u_group": "",
      "sys_updated_on": "2023-06-14 21:13:36",
      "u_circuitid": "",
      "u_level": "3",
      "sys_class_name": "x_380321_cmdpost_element",
      "number": "",
      "sys_id": "0106420a2fa12150c1dcae6df699b6e3",
      "sys_updated_by": "thane.plummer",
      "children": "",
      "sys_created_on": "2023-03-14 16:32:56",
      "element_source": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element_source/558830372f1fa110c1dcae6df699b6d5",
        "value": "558830372f1fa110c1dcae6df699b6d5"
      },
      "u_entity": "",
      "u_cmdb_group": "",
      "u_attributes": "",
      "u_simple_name_values_2": "",
      "sys_created_by": "thane.plummer",
      "u_nist_control": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_auditplus_nist_800_53/ee4ad51b2f2ce550c1dcae6df699b6fb",
        "value": "ee4ad51b2f2ce550c1dcae6df699b6fb"
      },
      "hierarchy": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_hierarchy/647835482f046510c1dcae6df699b614",
        "value": "647835482f046510c1dcae6df699b614"
      },
      "u_root_element": "",
      "sys_mod_count": "6",
      "sys_tags": "",
      "u_personnel_name": "",
      "u_hide_fom": "false",
      "u_parent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/a0458a862fa12150c1dcae6df699b63d",
        "value": "a0458a862fa12150c1dcae6df699b63d"
      },
      "configuration_item": "",
      "name": "PT-4(2)",
      "category": "nist control",
      "u_grandparent": {
        "link": "https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element/8725c6862fa12150c1dcae6df699b63c",
        "value": "8725c6862fa12150c1dcae6df699b63c"
      },
      "metric_pairs": "",
      "u_attribute_group": ""
    }
  ]
}"""

def createElement(element, parent_sys_id):
    data = {}
    data['is_head'] = element['is_head']
    print('Creating ' + element['name'])
    # response = requests.post(header, data=data)  # not comple


# Loop to get all the elements and childre

# Set the request parameters
parent = '59ff19cc2f803110c1dcae6df699b64e'
url = 'https://dev57368.service-now.com/api/now/table/x_380321_cmdpost_element?sysparm_limit=100&parent=' + parent

# Eg. User name="admin", Password="admin" for this code sample.
user = 'arendil.plummer'
pwd = 'Only4ankp!'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Decode the JSON response into a dictionary and use the data
r = response.json()
elements = r['result']
for element in elements:
    print(element['name'])
    new_sys_id = 'asdf'  # get from dict
    createElement(element, new_sys_id)