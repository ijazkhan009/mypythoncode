#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import json
import os
import pycurl
import sys
import cStringIO

if __name__ == "__main__":

    name_server_standart = "Server created by script %d"
    json_file_standart = "{ \"server\" : {  \"name\" : \"%s\", \"imageRef\" : \"%s\", \"flavorRef\" : \"%s\" } }"

    curl_auth_token = pycurl.Curl()

    gettoken = cStringIO.StringIO()

    curl_auth_token.setopt(pycurl.URL, "http://192.168.100.241:8774/v1.1")
    curl_auth_token.setopt(pycurl.POST, 1)
    curl_auth_token.setopt(pycurl.HTTPHEADER, ["X-Auth-User: cpca",
                          "X-Auth-Key: 438ac2d9-689f-4c50-9d00-c2883cfd38d0"])

    curl_auth_token.setopt(pycurl.HEADERFUNCTION, gettoken.write)
    curl_auth_token.perform()
    chg = gettoken.getvalue()

    auth_token = chg[chg.find("X-Auth-Token: ")+len("X-Auth-Token: ") : chg.find("X-Server-Management-Url:")-1]

    token = "X-Auth-Token: {0}".format(auth_token)
    curl_auth_token.close()

    #----------------------------

    getter = cStringIO.StringIO()
    curl_hab_image = pycurl.Curl()
    curl_hab_image.setopt(pycurl.URL, "http://192.168.100.241:8774/v1.1/nuvemcpca/images/7")
    curl_hab_image.setopt(pycurl.HTTPGET, 1) #tirei essa linha e funcionou, nao sei porque
    curl_hab_image.setopt(pycurl.HTTPHEADER, [token])

    curl_hab_image.setopt(pycurl.WRITEFUNCTION, getter.write)
    #curl_list.setopt(pycurl.VERBOSE, 1)
    curl_hab_image.perform()
    curl_hab_image.close()

    getter = cStringIO.StringIO()

    curl_list = pycurl.Curl()
    curl_list.setopt(pycurl.URL, "http://192.168.100.241:8774/v1.1/nuvemcpca/servers/detail")
    curl_list.setopt(pycurl.HTTPGET, 1) #tirei essa linha e funcionou, nao sei porque
    curl_list.setopt(pycurl.HTTPHEADER, [token])

    curl_list.setopt(pycurl.WRITEFUNCTION, getter.write)
    #curl_list.setopt(pycurl.VERBOSE, 1)
    curl_list.perform()
    curl_list.close()

    #----------------------------

    resp = getter.getvalue()

    con = int(resp.count("status"))

    s = json.loads(resp)

    lst = []

    for i in range(con):
        lst.append(s['servers'][i]['status'])

    for j in range(len(lst)):
        actual = lst.pop()
        print actual

        if actual != "ACTIVE" and actual != "BUILD" and actual != "REBOOT" and actual != "RESIZE":

            print "Entra no If"

            f = file('counter', 'r+w')

            num = 0
            for line in f:
                num = line

            content = int(num)+1

            ins = str(content)

            f.seek(0)
            f.write(ins)
            f.truncate()
            f.close()

            print "Contador"

            json_file = file('json_file_create_server.json','r+w')

            name_server_final = name_server_standart % content
            path_to_image = "http://localhost:9999/v1.1/nuvemcpca/images/7"
            path_to_flavor = "http://localhost:8774/v1.1/nuvemcpca/flavors/1"

            new_json_file_content = json_file_standart % (name_server_final, path_to_image, path_to_flavor)

            json_file.seek(0)
            json_file.write(new_json_file_content)
            json_file.truncate()
            json_file.close()

            print("json fie created")

            fil = file("json_file_create_server.json")
            siz = os.path.getsize("json_file_create_server.json")

            cont_size = "Content-Length: %d" % siz
            cont_type = "Content-Type: application/json"
            accept = "Accept: application/json"

            c_create_servers = pycurl.Curl()

            logger = cStringIO.StringIO()

            c_create_servers.setopt(pycurl.URL, "http://192.168.100.241:8774/v1.1/nuvemcpca/servers")

            c_create_servers.setopt(pycurl.HTTPHEADER, [token, cont_type, accept, cont_size])

            c_create_servers.setopt(pycurl.POST, 1)

            c_create_servers.setopt(pycurl.INFILE, fil)

            c_create_servers.setopt(pycurl.INFILESIZE, siz)

            c_create_servers.setopt(pycurl.WRITEFUNCTION, logger.write)

            print "Teste perform!"

            c_create_servers.perform()

            print logger.getvalue()

            c_create_servers.close()

            print("done")