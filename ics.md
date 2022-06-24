<p>L'ICS désigne les systèmes industriels de manière générale.</br>

Pour être plus précis, un système industriel désigne, en l'occurrence, un système informatique s’interfaçant avec des systèmes physiques tels que des capteurs, des moteurs, des vannes...</br>

Ce type de système est de manière générale objectivement très peu étudié dans les écoles d'informatiques, ce qui est regrettable puisque l'on retrouve ces systèmes notamment dans les centrales nucléaires, les circuits de distribution d’eau, les systèmes d’alarme, de vidéosurveillance...</br>

L'ICS et l'IACS (Industrial Automation and Control Systems) représentent la même chose.</br>

Les  systèmes informatiques industriels sont globalement relativement proches des systèmes informatiques de gestion (utilisation de réseaux Ethernet/TCP/IP, utilisation de PC et serveurs pour la supervision, utilisation de bases de données SQL…) mais, comme dit précédemment, ce n'est pas nécessairement le domaine qui est le plus étudié dans le domaine des réseaux informatiques.</br>

Je prendrais même le risque de dire qu'il s'agit d'une niche. À titre d'exemple, sur des sites de recherches d'emplois tels qu'indeed ou Linkedin, je passe de 10 résultats pour des postes en gestion de réseaux industrielle à 5000 postes d'administrateur systèmes et réseaux "classiques" (chiffres non représentatifs donnés à titre d'exemple).</br>

De plus, ces réseaux ont des spécificités qui les rendent particulièrement vulnérables. Par exemple :</br>

- La plupart des systèmes informatiques industriels doivent être  disponibles sans interruption au vu de l'importance de ceux-ci pour certaines structures (centrales nucléaires, usines de construction, aéroports), rendant difficiles les  mises à jour, les tests de vulnérabilité, etc...</br>

- Certains systèmes informatiques industriels mettent en  jeu la vie des personnes (centrales nucléaires, machines médicales, usines de production de médicaments…) et pour cela reçoivent des habilitations/qualifications qui ne sont plus valables en cas de mise à jour d’un équipement.</br>

- Les équipements de contrôle-commande ont une durée de vie très longue (on trouve encore en fonctionnement dans les usines de très fiables automates Siemens S5 des années 80) et forment un parc souvent hétérogène (chaque machine peut avoir un modèle d’automate ou pire, une marque d’automate différentes). Cela rend le suivi des vulnérabilités et des mises à jour plus fastidieux. Ces automates sont souvent inconnus des informaticiens/ingénieurs en charge de la cybersécurité.</br>

- Les productions alimentaires et pharmaceutiques notamment doivent garantir la traçabilité de leur production. Cela rend nécessaire les connexions entre les machines de terrain (automates, superviseurs) et les machines de l’administration  suivi de la qualité...)</br>

- Les réseaux de terrain standards sur liaison RS485 (Modbus, Profibus, BACnet MSTP), sur bus CAN (CANopen, DeviceNet) ou spécifiques (LON, DALI, KNX…) ne sont pas sécurisés et pas sécurisables de manière simple (un standard sécurisé de KNX apparaît actuellement).</br>

De plus Le passage de ces bus dans des zones publiques où faciles d’accès fait courir le risque d’une intrusion sur le réseau ou tout simplement l'exploitation des automates.</br>

Les réseaux de terrain modernes sur Ethernet (ProfiNet, EtherNet/IP, Ethercat) sont plus récents et leurs standards plus complexes tendent à prendre mieux en compte le risque cyber (authentification de la machine se connectant par exemple). Le protocole OPC-UA, sur Ethernet TCP/IP, utilisé pour la communication entre le superviseur et l’automate, ou entre automates, est même chiffré, ce qui lui donne une popularité certaine actuellement.</br>

Le système informatique industriel basique comprend typiquement un ou plusieurs automates supervisés par un PC de supervision via un réseau Ethernet, pas forcément connecté à Internet. Un serveur de base de données pour l’archivage peut aussi être présent localement. L’automate contrôle wdivers équipements via des bus de terrain standard ou basés sur Ethernet.</br>

Qu'ils soient connectés à Internet ou non, ces réseaux industriels sont susceptibles d'être la cible d'attaques.</br>

Par ailleurs, nous pouvons trouver des systèmes industriels connectés à Internet sur Shodan : https://www.shodan.io/explore/category/industrial-control-systems</br>

Pour illustrer mes propos, voici trois exemples d'attaques populaires sur ce type de réseaux.</br>

- Ver Zotob, arrêt de 13 usines d’assemblage de véhicules.</br>

En s'attaquant aux réseaux industriels, en 2005 le ver Zotob a paralysé 13 usines d’assemblage de véhicules.</br>

Le ver s'est propagé dans tout le réseau dit "classique" (bureautique, administratif...), puis dans le réseau industriel, et une fois dans ce réseau, la propagation s'est effectuée d'usine en usine.</br>

D'après M. RENARD Christophe (agent de l'ANSSI), il n'est pas rare que les entreprises considèrent le fait de se prendre des virus comme étant endémiques et fassent preuve d'un défaitisme, devrais-je dire d'un véritable relâchement hors du commun. Ils décident de faire avec, tout simplement.</br>

- Un industriel allemand victime d’une attaque de type Stuxnet.</br>

Un sidérurgiste allemand a subi une attaque très sophistiquée ayant compromis son système informatique empêchant l'arrêt d'un haut fourneau.</br>

Un rapport (2014) du ministère allemand de la sécurité informatique (BSI, équivalent de l'ANSSI en France) qui vient de sortir met à jour une attaque ayant compromis un système de contrôle de haut fourneau.</br>

Dans son rapport, le ministère précise que l’attaque a commencé par une infiltration du réseau dit "classique" (bureautique, administratif...) de l’entreprise visée, par spear-phishing et ingénierie sociale.</br>

Comme avec Zotob, par la suite, les hackers auraient réussi à compromettre le réseau de contrôle des installations industrielles.</br>

Source du rapport : https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/Lageberichte/Lagebericht2014.pdf?__blob=publicationFile</br>

L'intérêt pour un malveillant est bien évidemment de demander une rançon en échange de l'arrêt / de l'annulation du sabotage en cours.</br>

Nous pouvons faire le lien entre les attaques de type ransomware qui chiffrent les données (des entreprises et des utilisateurs) avec ce type d'attaque à la différence près que la rançon sert dans cette situation à aretter le sabotage des machines industrielles.</br>

Sauf qu'en l'occurrence, comme dit précédemment, le problème étant que ces attaques sont potentiellement bien plus dangereuses / peuvent être bien plus ravageuses / risquent de causer de bien plus grandes pertes que des ransomwares "classiques" puisque ces réseaux industriels sont très souvent utilisés dans des structures très sensibles (centrales nucléaires, aéroports, circuits de distribution d’eau...)</br>

Nous pouvons également parler des potentiels risques d'attaques étatiques (en cas de guerres ou conflit par exemple).</br>

Rappelons la potentielle attaque sur les centrales électriques en Ukraine qui aurait touché plus de 80 000 foyers simultanément (coupure de courant).</br>

Il est possible de "limiter" les risques de nombreuses manières.</br>

Voici quelques éléments proposés par l'ANSSI, que je vous invite à consulter :</br>

- Les bonnes pratiques de l'ANSSI concernant les systèmes industriels : https://www.ssi.gouv.fr/entreprise/bonnes-pratiques/systemes-industriels/</br>

La méthode de sécurisation des systèmes industriels suit 7 étapes :</br>

1. Sensibilisation des personnels.</br>
2. Cartographie des installations et analyse de risque.</br>
3. Prévention : concept de la défense en profondeur.</br>
4. Surveillance des installations et détection des incidents.</br>
5. Traitement des incidents, chaîne d’alerte.</br>
6. Veille sur les menaces et les vulnérabilités.</br>
7. Plans de reprise et de continuité d’activité.</br>
