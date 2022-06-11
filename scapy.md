<div id="top"></div>

<div align="center">
  <a href="https://github.com/franckferman/network-elements-synthesis">
    <img src="https://raw.githubusercontent.com/franckferman/network-elements-synthesis/main/img/scapy.png" alt="Scapy" width="400" height="200">
  </a>

<h3 align="center">Scapy</h3>

  <p align="center">
    La manipulation de paquets avancée avec Scapy.
    <br/>
    <a href="https://scapy.net/"><strong>Lien vers le site officiel de Scapy »</strong></a>
    <br/>
	<br/>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
	  <li><a href="#1-présentation-de-Scapy">Présentation très générale de Scapy</a></li>
    <li><a href="#2-une-forte-communaute">Une forte communauté, quelques exemples de scripts</a></li>
      <li><a href="#3-Scapy-utilisation">Utilisation de Scapy</a></li>
  </ol>
</details>

<div align="center">
<h2>1. Présentation très générale de Scapy</h2>

<p>Scapy est un outil extrêmement puissant et utile permettant de nombreuses actions telles que la manipulation de paquets, la capture du trafic (comme le fait tcpdump ou wireshark par exemple), il est capable de réaliser du fingerprinting, faire de l'analyse en tous genres, de forger, de recevoir et d'emettre des paquets (et/ou) des trames vers des infrastructures avec une multitude de protocoles réseaux différents (IP, TCP, UDP, ARP, SNMP, ICMP, DNS, DHCP...)<br/>

À lui seul, il est capable de remplacer plus de 80% des outils de sécurité ou d'analyse du réseau tel que nmap, arpspoof, tcpump, tshark, p0f et des commandes/outils telles que ping, traceroute...<br/>

Et dans certains cas, Scapy a un bien plus gros potentiel (que ces derniers outils cités précédemment).<br/>

En dehors du fait que la plupart des outils se limitent à des protocoles très basiques (TCP/UDP/ICMP), je dirais que la contrainte principale de ces outils (cités précédemment), réside dans le fait qu'ils ne vous permettent généralement pas de faire autre chose que ce qui a été pensé par le développeur de l'outil. Ces outils ont été construits dans un but bien précis et ne s'écartent que très peu de celui-ci.<br/>

Un programme permettant de réaliser un empoisonnement du cache ARP (arpspoof par exemple), ne vous permettra le plus souvent pas d'associer cette attaque avec d'autres.<br/>

Alors qu'avec Scapy, vous avez un contrôle total sur ce que vous faites, les paquets que vous forgez, les attaques menées, vous êtes le véritable maitre à bord. La seule limite est votre créativité ainsi que votre expertise du réseau.<br/>

Nous pouvons par exemple très facilement associer une attaque de type empoisonnement de cache ARP avec du VLAN hopping (double tagging en l'occurence):<br/>

<code>>>> send( Ether(dst=XX-XX-XX-XX-XX)/Dot1Q(vlan=1)/Dot1Q(vlan=2) /ARP(op="who-has", psrc=gateway, pdst=client), inter=RandNum(10,40), loop=1 )</code><br/>

Bien entendu, des attaques plus basiques sont possibles, tout aussi simplement:<br/>

Pour effectuer un simple empoisonnement de cache ARP par exemple:<br/>

<code>>>> arpcachepoison(target, victim, interval=60)</code>

<br/>

Comme dit précédemment, Scapy vous permet de sniffer le trafic, à l'instar d'outils comme tshark ou tcpdump.<br/>

<code>>>> x=sniff(filter="icmp")</code>
<code>>>> x.show()</code>

<br/>

Contrairement à de nombreux outils comme Nmap, il décode mais n'interprète pas. Ce qui permet de ne pas se limiter à l'interprétation d'un programme avoir la possibilité de réaliser une analyse poussée (de ce qui s'est réellement passé sur le réseau).<br/>

La commande help() peut être utilisée pour avoir des informations sur des fonctions, help(traceroute) ou help(fuzz) par exemple<br/> 

Scapy permet également de faire du fuzzing.<br/>

>>> y=fuzz(IP())<br/>

Si j'effectue y.show(), nous constatons que l'ensemble l'ensemble des valeurs ont été rendus aléatoires.<br/>

<code>
>>> y.show()
###[ IP ]###
  version= <RandNum>
  ihl= None
  tos= <RandByte>
  len= None
  id= <RandShort>
  flags= DF
  frag= <RandNum>
  ttl= <RandByte>
  proto= <RandByte>
</code><br/>

Pour finir cette introduction, je dirais que la seule contraintre réside dans le fait que Scapy est logiquement plus difficile à prendre en main que les outils cités précédemment (clés en main) mais encore une fois, il permet également d'aller beaucoup plus loin.

<br/><br/>

<div align="center">
<h2>2. Une forte communauté, quelques exemples</h2>

Possédant une très forte communauté, il existe de très nombreuses ressources sur Internet, et de nombreux scripts sur Github que vous pourrez reprendre et personnaliser en fonction de vos besoins.<br/>

Typiquement, le repository Github de David BOMBAL (/davidbombal/scapy) offre une multitude de scripts particulièrement intéressants et montre quelques exemples concrets d'utilisation de Scapy, par exemple:<br/>

-  L'attaque du protocole BGP:<br/>

Quand vous communiquer sur Internet (en allant sur le site de l'ANSSI par exemple), le choix du chemin à emprunter (sur le WAN) jusqu'à ce celui-ci sera, entre autres, géré par le protocole de routage BGP.<br/>

Le protocole BGP est un protocole de type EGP (Exterior gateway protocol), c'est-à-dire un protocole de routage externe (à l'inverse de protocoles de routages tels que RIP ou OSPF, qui eux, sont des protocoles de routage internes, de type IGP) et c'est ce protocole est utilisé pour communiquer entres les différents AS (AS généralement sous le contrôle des fournisseurs d'accès à Internet).<br/>

Les AS sont comparables à des bureaux de poste. Le courrier va de bureau de poste en bureau de poste jusqu'à ce qu'il atteigne la bonne ville, et le bureau de poste de cette ville distribuera alors le courrier dans cette ville.<br/>

N'étant n'est pas le sujet principal, disons simplement qu'Internet repose en grande partie sur BGP.<br/>

David BOMBAL montre comment il est possible, avec Scapy, de réaliser des attaques sur ce protocole.<br/>

- Injection d'une fausse route BGP (https://github.com/davidbombal/scapy/blob/main/bgp-add-fake-routes.py).<br/>

- Effectuer une attaque DOS (https://github.com/davidbombal/scapy/blob/main/bgp-dos-reset-neighbors.py).<br/>

Il s'agit de deux exemples parmi tant d'autres de tout que vous pouvez faire avec Scapy.<br/><br/>

<div align="center">
<h2>3. Utilisation de Scapy</h2>

<p>Pour être plus précis sur ce qu'est réellement Scapy, c'est à la fois un interpréteur de commande (basé sur celui de Python) et une bibliothèque.<br/>

Il existe des fonctions qui permettent de lire et d’écrire des fichiers pcap qui contiennent des captures de trafic réseau, des fonctions d’analyse et de construction des paquets réseaux (à partir de la couche 2), des fonctions d’envoi de ces paquets et de réception des paquets réponses associés, des fonctions d’écoute (sniffing) du trafic réseau et des fonctions de génération de représentations graphiques (courbes d’un ensemble de valeurs calculées, graphe d’échanges entre matériels, graphes de la topologie d’un réseau).<br/>

Pour pouvoir utiliser les fonctions de Scapy dans votre programme Python il vous suffit simplement d'importer la bibliothèque Scapy.<br/>

Mais vous pouvez également utiliser Scapy en mode interactif (interpréteur de commande) ce qui est très utile pouvoir tester rapidement des instructions sans avoir à écrire de programme au préalable.<br/>

Une fois dans ce mode interactif, vous pouvez entrer la commande ls() pour afficher la liste des protocoles que sait gérer Scapy et lsc() pour afficher la liste des commandes.<br/>

La commande ls() peut également être utilisée en renseignant un protocole, par exemple ls(IP), ce qui va nous permettre d'afficher la liste des possibilités (paramètres) offertes par celui-ci.<br/>

- Un exemple concret :<br/>

Déclarons une variable X auquel nous allons attribuer le protocole souhaité (l'opérateur / est utilisé pour lier les couches entre elles).<br/>

>>>x=IP()/TCP()

Nous pouvons vérifier les paramètres attribuables.<br/>

>>> ls(x)
version    : BitField  (4 bits)                  = 4               (4)
ihl        : BitField  (4 bits)                  = None            (None)
tos        : XByteField                          = 0               (0)
len        : ShortField                          = None            (None)
id         : ShortField                          = 1               (1)
flags      : FlagsField  (3 bits)                = <Flag 0 ()>     (<Flag 0 ()>)
frag       : BitField  (13 bits)                 = 0               (0)
ttl        : ByteField                           = 64              (64)
proto      : ByteEnumField                       = 0               (0)
chksum     : XShortField                         = None            (None)
src        : SourceIPField                       = '127.0.0.1'     (None)
dst        : DestIPField                         = '127.0.0.1'     (None)
options    : PacketListField                     = []              ([])

Attribuons les valeurs qui nous intéressent.<br/>

>>> x.src="127.0.0.1"
>>> x.dst="franckferman.fr"
>>> x.ttl=32

Nous pouvons envoyer le paquet.<br/>

>>> send(x)