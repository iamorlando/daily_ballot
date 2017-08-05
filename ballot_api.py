#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:59:48 2017

@author: iamorlando
"""

import requests
from json import loads as to_dict
from json import dumps as to_json

base_url = 'https://www.googleapis.com/civicinfo/v2/'
api_key = 'AIzaSyDRalwUxSfckOC3_9FcgdmI0YdKkxFMdu8'


def http_get(endpoint, params):
    params['key'] = api_key
    response = requests.request("GET", base_url+endpoint, params=params)
    print(response.url)
    print(response.text)
    return response.text



def call_civic_api_representatives(address, levels, *,
                        roles=["deputyHeadOfGovernment",
                                  "executiveCouncil",
                                  "governmentOfficer",
                                  "headOfGovernment",
                                  "headOfState",
                                  "highestCourtJudge",
                                  "judge",
                                  "legislatorLowerBody",
                                  "legislatorUpperBody",
                                  "schoolBoard",
                                  "specialPurposeOfficer"],
                        fields=['divisions',
                                'kind',
                                'normalizedInput',
                                'offices',
                                'officials']
                        ):
    """
    lists all representatives, their offices, for a given address
    """
    params = {'address': address}
    params['roles'] = roles
    params['includeOffices']='true'
    params['levels'] = levels
    params['fields'] = ','.join(fields)
    return http_get('representatives', params)


def make_representatives(offices_officials_dict):
    dict_ = offices_officials_dict
    #print(dict_)
    rep_list = []
    for i in dict_['offices']:
        for j in i['officialIndices']:
            rep_list.append({'representative': dict_['officials'][int(j)],
                             'office': i})
    return rep_list


def get_representatives(address, levels, *,
                        roles=["deputyHeadOfGovernment",
                                  "executiveCouncil",
                                  "governmentOfficer",
                                  "headOfGovernment",
                                  "headOfState",
                                  "highestCourtJudge",
                                  "judge",
                                  "legislatorLowerBody",
                                  "legislatorUpperBody",
                                  "schoolBoard",
                                  "specialPurposeOfficer"]
                        ):
    fields_ = ["officials","offices"]
    res = call_civic_api_representatives(address,
                                                   levels, roles=roles,
                                                   fields=fields_)
    #print (res)

    dict_ = to_dict(res)


    #print(dict_)
    dict_list = make_representatives(dict_)
    reps = {'representatives':dict_list}
    return to_json(reps)


