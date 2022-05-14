import json

js = {"csrftoken":"rLweKo6K1ivmXhMh9ZY5GbgUA0Dk0F8x","SPC_F":"g6kvQHITRM38zB0XeYT9rrOw2SzVJh4T","REC_T_ID":"4e3fba94-9757-11ec-836d-6e1f9bdb8336","SPC_SI":"mall.NLjm7g1QhnHt31dG9mJ5O0PTSObQlSdt","_QPWSDCXHZQA":"94b14e7e-dae3-4030-b27b-506a131a7275","G_ENABLED_IDPS":"google","G_AUTHUSER_H":"0","SPC_EC":"\"SnZ1dDJxTEFBVnNMUzNZcBzLuVNFaFO/HO3cxj6Q1w8HCbW9Gj0aVysW89hPRb8azWAnIu5z63+ToQ+uhhsuZjuiqyuE8wVYGzfRpoFm54TXM+v6D/lTx7DUf5rGdAZ1JwkK5Uazi9pBC15rNqO4dDKnK/Tx7wxpJdkKu5k5Zds=\"","SPC_U":"157524507","SPC_CLIENTID":"ZzZrdlFISVRSTTM4yrwzwypcqcbhrpym","SPC_ST":".YndZY3JrSEFVUU1jS0pvaeKlvDXdURkURB9HZrkJ0Qd+hYLdwx29ViUNPzvDNfkGDu6yCWOrzSzcgJoT/gu8/V2Se3JiRcsr/U79tmmVnfJ9qnSRHH+hNn3wzHUM5aiqeiqg8Htgcv3FORs74IxVIGwRSDXdW0SV2RfUsyFpiaBuhefcXpi9/7nimMTCynY2elyeC4m11ZlDxCF1LuV4qQ==","SPC_IA":"1","SPC_T_IV":"FwZ43tjvGK8GnjlmAP83iQ==","SPC_T_ID":"pCGMsIBA7SPdYG+cv1i/2G9t/9aj7tQyjHjSFXcrjPxkiHoIhvEfX+GETUruoLT7M7OBfpmFcfHzMXxX0bEElKCL3PZO/ERIdZJN9LXx8AY=","SPC_R_T_ID":"pCGMsIBA7SPdYG+cv1i/2G9t/9aj7tQyjHjSFXcrjPxkiHoIhvEfX+GETUruoLT7M7OBfpmFcfHzMXxX0bEElKCL3PZO/ERIdZJN9LXx8AY=","SPC_R_T_IV":"FwZ43tjvGK8GnjlmAP83iQ==","shopee_webUnique_ccd":"ApHCAk0Vb0VerJfQapnXxg%3D%3D%7CQPDyA9IXFTIhNS2odz1E65%2B2y9DptdtdGBjapfFDe5qjYQfLROuAzuHoJxJUnOyVEhRaviXNu9MGa0FsjF2iSqw%3D%7ClbIAnFtZKQOxdjOK%7C04%7C3"}

nama_file = 'akunabi.json'

f = open(nama_file, 'w')
dt_dict = []
for i in js:
    format_js = {"name": "%s"%i, "value": "%s"%js[i]}
    dt_dict.append(format_js)
json.dump(dt_dict, f, indent=2)