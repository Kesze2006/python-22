import random

vezeteknev=["Aberdán","Aberer","Aberle","Aberman","Abermann","Abert","Aberth","Abfal","Abidovits","Abis","Abisch","Abkarovics","Abl","Abodi","Abonyi","Abádi","Abár","Abért","Aczél","Adamcsik","Adamich","Adamis","Adonics","Adonyi","Ady","Aggházy","Agárdi","Agócs","Ajtay","Alberth","Almási","Almássi","Almássy","Almásy""Alpár","Ama","Amachel","Amade","Amadei","Amadey","Amadin","Amadinger","Aman","Amancsia","Amand","Amann","Amant","Amar","Amberg","Amberger","Ambich","Ambrus","Ambrusics","Ambrusik","Ambruska","Ambruzs","Ambrózfalvi","Ambrózi","Ambrózy","Amelin","Amena","Ament","Amerand","Amerán","Amirás","Amisits","Amlacher","Amment","Ammer","Amon","Amorth","Amrik","Amring","Amthauzer","Amvein","Amwel","Amzel","Amán","Ancsel","Apáczai","Arany","Aranyi","Aranykövi","Aranykövy","Aranyos","Aranyosi","Aranyoss","Aranyossy","Aranyosy","Arányi","Avar","Aág","Aágh","Aáron","Babits","Bachman","Bajza","Bakos","Bakucz","Balassi","Balduin",]


keresztnevf=["Aba"," Abád"," Abbás"," Abdiás"," Abdon","Abdullah","Ábel"," Abelárd", "Ábner"," Abod","Abony","Abos", "Abosa", "Ábrahám"," Ábrám","Ábrán","Ábris"," Absa", "Absolon"," Acél"," Achilles","Achillesz","Áchim", "Acsád", "Adalbert"," Ádám","Adeboró","Ádel", "Adelmár", "Áden", "Adeodát","Ádér","Ádin", "Adolár", "Adolf", "Ádomás","Adonisz","Adony", "Adorján", "Adrián", "Adriánó","Agád","Agamemnon", "Agapion", "Ágas", "Agaton","Agenor","Aggeus", "Agmánd", "Ágost", "Ágoston","Ahillész","Áhim", "Ahmed", "Airton", "Ajád","Ajándok", "Ájhán","Ajtony"," Akács", "Akhilleusz", "Akitó"," Ákos","Aladár", "Aladdin","Aladin"," Alajos"," Alán"," Alap", "Alárd","Alarik","Albert"," Albin", "Aldán"," Áldás", "Aldó","Áldor","Alek", "Alen", "Alex", "Alekszej","Alexander","Bács", "Bacsó", "Bagamér", "Baján","Bajka","Bajnok", "Bájron", "Bakács", "Baksa","Bakta","Balabán","Baladéva", "Balambér", "Balár","Balaráma","Balassa", "Balázs","Guidó"]


khj = random.choice(keresztnevf)

nev1= vezeteknev[random.randint(0,len(vezeteknev)-1)]
#print(nev1)
nev2= keresztnevf[random.randint(0,len(keresztnevf)-1)]
print(nev1+" "+nev2)
