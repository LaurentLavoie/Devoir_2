# coding: utf-8

import json
import csv
import requests

fichier = "banq.csv"



entete = {
	"User-Agent": "Laurent Lavoie",
	"From":"laurent.lavoie96@gmail.com"
}
for code in range(1000,2001):
# url = "http://collections.banq.qc.ca/api/service-notice?handle=52327/"
	urls = "http://collections.banq.qc.ca/api/service-notice?handle=52327/{0}".format(code)
	# print(code)
	# print(urls)

	req = requests.get(urls, headers=entete)

	print(req)
	if req.status_code != 200:
		print("marche pas")
	else:
		fichiers = req.json()

		if fichiers["type"] == "audio":
				au = []
				au.append(fichiers["titre"].split("/")[0])
				au.append(fichiers["createurs"][0])
				au.append(fichiers["dateCreation"])
				au.append(fichiers["descriptionMat"])
				au.append(fichiers["url"])
				# print("titre")
				# print("createurs")
				# print("dateCreation")
				# print("descriptionMat")
				print(au)
				print("#"*80)

		f2 = open(fichier,"a")
		final = csv.writer(f2)
		final.writerow(au)

