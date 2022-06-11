<div id="top"></div>

<div align="center">
  <a href="https://github.com/franckferman/network-elements-synthesis">
    <img src="https://raw.githubusercontent.com/franckferman/network-elements-synthesis/main/img/scapy.png" alt="Scapy" width="200" height="200">
  </a>

<h3 align="center">Scapy</h3>

  <p align="center">
    La manipulation de paquets avec Scapy.
    <br/>
    <a href="https://scapy.net/"><strong>Lien vers le site officiel de Scapy »</strong></a>
    <br/>
	<br/>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
	  <li><a href="#1-scapy-overview">Présentation de Scapy</a></li>
    <li><a href="#2-strong-community">Une communauté grandissante d'experts</a></li>
      <li><a href="#3-scapy-usage">Utilisation de Scapy</a></li>
  </ol>
</details>

<div align="center">
<h2>1. Présentation de Scapy</h2>

<p>Scapy est un outil extrêmement puissant permettant de nombreuses actions telles que la manipulation de paquets, la capture (sniffing) du trafic (comme le fait tcpdump ou wireshark par exemple), il est capable de réaliser du fingerprinting (comme peut le faire p0f), faire de l'analyse en tous genres, forger, recevoir et emettre des paquets et des trames avec une multitude de protocoles réseaux différents (IP, TCP, UDP, ARP, SNMP, ICMP, DNS, DHCP...)<br/>

À lui seul, il est capable de remplacer de nombreux outils et utilitaires de sécurité et d'analyses tels que nmap, arpspoof, arping, tcpump, tshark, p0f, hping, ping, traceroute...<br/>

À la différence près que Scapy possède un bien meilleur potentiel que ces derniers. Bien évidemment, un meilleur potentiel ne signifie pas nécessairement que celui-ci devrait remplacer tous ces outils. À vrai dire, tout dépend véritablement des besoins de l'utilisateur. L'utilisation des outils précédemment cités peut dans de nombreux cas être utilisées sans Scapy et répond amplement aux besoins de l'utilisateur.<br/>

En revanche, Scapy, en plus de permettre une centralisation de ces outils, permet d'aller bien plus loin techniquement parlant. La plupart des outils se limitent à des protocoles très basiques (TCP/UDP/ICMP), ce qui n'est pas le cas de Scapy. De plus, la contrainte principale de ces outils est qu'ils sont particulièrement restreints. Ils ne permettent généralement pas de faire autre chose que ce qui a été pensé par le développeur.<br/>

À titre de comparaison, typiquement, Scapy peut associer différentes attaques. Par exemple, il peut associer une attaque de type ARP cache poisoning avec du VLAN hopping.<br/>

<code>>>> send( Ether(dst=XX-XX-XX-XX-XX)/Dot1Q(vlan=1)/Dot1Q(vlan=2) /ARP(op="who-has", psrc=gateway, pdst=client), inter=RandNum(10,40), loop=1 )</code><br/>

Bien entendu, des attaques plus basiques sont possibles vous pouvez par exemple un simple empoisonnement de cache ARP de cette manière.<br/>

<code>>>> arpcachepoison(target, victim, interval=60)</code><br/>

Comme dit précédemment, des fonctions basiques sont également disponibles, Scapy vous permet de sniffer le trafic simplement (à l'instar d'outils comme tshark ou tcpdump).<br/>

<code>>>> x=sniff(filter="icmp")</code><br>
<code>>>> x.show()</code><br/>

Pour en revenir à ce qui fait sa particularité, vous avez par exemple la possibilité de forger vos propres paquets (à partir de la couche 2), envoyer des trames invalides, casser complètement les règles du modèle TCP/IP (cf. David Bombal)...<br/>

Pour résumé simplement, avec Scapy, vous êtes le véritable maitre à bord et la seule limite est votre créativité ainsi que votre expertise du réseau.<br/>

Contrairement à une certaine partie des nombreux outils cités précédemment, Scapy décode mais n'interprète pas. Ce qui, à première vue peut paraître être un inconvénient, est en réalité dans certains cas un réel atout puisque cela permet de ne pas se limiter à l'interprétation d'un programme et avoir la possibilité de réaliser une analyse poussée de ce qui se passe réellement. Analyse qui sera plus fastidieuse et demandera assurément plus de compétences techniques mais qui, si elle est correctement réalisée, sera bien plus précise.<br/>

Je peux utiliser la commande lsc() pour afficher les fonctions offertes par Scapy, et la commande help() pour la compréhension des paramètres attendus par celle-ci.<br/>

Par exemple, la commande help(arpcachepoison) me permet de voir la liste des paramètres attendus et m'affiche la description de la fonction.<br/>

<code>Poison target's cache with (your MAC,victim's IP) couple.</code>
<code>arpcachepoison(target, victim, interval=60)</code><br/>

La commande help(traceroute).<br/>

<code>Instant TCP traceroute.</code>
<code>traceroute(target, dport=80, minttl=1, maxttl=30, sport=<RandShort>, l4=None, filter=None, timeout=2</code><br/>

Pour résumé, la seule contrainte réside dans la nécessité pour l'utilisateur de posséder une certaine expertise pour pouvoir manipuler cet outil au mieux. Scapy me paraît plus difficile à prendre en main que les outils clés en main citée précédemment mais celui-ci permet malgré tout d'aller amplement plus loin en matière de manipulation.</p><br/>

<div align="center">
<h2>2. Une communauté grandissante d'experts</h2>

<p>Scapy est un outil particulièrement reconnu et populaire, il possède plus de 7000 étoiles et plus de 300 contributeurs sur Github, et est utilisé et reconnu par de nombreux experts (dont des experts de l'ANSSI, l'un des contributeurs les plus importants, Monsieur Guillaume Valadon, est par ailleurs un doctorant et ancien de l'ANSSI...)<br/>

Scapy s'est fait un nom dans le milieu et est reconnu par l'ensemble des experts du domaine de la sécurité et des réseaux. À ce titre, au vu de sa popularité, le fait qu'il soit libre, soutenu et maintenu par des experts, à créer un certain engouement et par conséquent une communauté.<br/>

Grâce à sa popularité, il existe de très nombreuses ressources sur Internet, de forums sur lesquels vous pourrez demander de l'aide en cas de besoin, de nombreuses documentations, de nombreux tutoriels, de nombreux scripts sur Github, que vous pourrez reprendre et personnaliser en fonction de vos besoins...<br/>

Pour vous donner un exemple concret, David Bombal a mis à disposition de nombreux scripts particulièrement intéressants. Il offre une multitude de scripts et montre des exemples concrets d'utilisation de Scapy, par exemple:<br/>

- L'attaque du protocole BGP.<br/>

Quand vous communiquez sur Internet, par exemple, quand vous vous connectez au site Web de l'ANSSI, vous traversez Internet, et pour cela, vous empruntez des chemins. Et bien, le choix du chemin à emprunter jusqu'à celui-ci sera, entre autres, géré par le protocole de routage BGP.<br/>

Le protocole BGP est un protocole de type EGP (Exterior gateway protocol), c'est-à-dire un protocole de routage externe (à l'inverse des protocoles de routages internes de type IGP tels que RIP ou OSPF par exemple), c'est ce protocole qui est utilisé pour communiquer entre les différents AS (AS, généralement sous le contrôle des fournisseurs d'accès à Internet).<br/>

Les AS (pour Autonomous system) sont comparables à des bureaux de poste. Le courrier va de bureau de poste en bureau de poste jusqu'à ce qu'il atteigne la bonne ville, et le bureau de poste de cette ville distribuera alors le courrier dans cette ville.<br/>

N'étant pas le sujet principal de mon présent document, pour résumé, disons simplement qu'Internet repose et dépend en grande partie de BGP.<br/>

David Bombal, dans l'une de ses vidéos, montre comment il est possible, avec Scapy, de réaliser des attaques sur ce protocole. Il a également publié le code source de ses scripts sur Github:<br/>

- Injection d'une fausse route — https://github.com/davidbombal/scapy/blob/main/bgp-add-fake-routes.py.<br/>
- Réalisation d'une attaque par déni de service — https://github.com/davidbombal/scapy/blob/main/bgp-dos-reset-neighbors.py.<br/>

Ces deux exemples montrent la puissance de Scapy, si celle-ci est utilisée avec suffisamment de maitrise.</p><br/>

<div align="center">
<h2>3. Utilisation de Scapy</h2>

<p>Scapy est à la fois un interpréteur de commande (basé sur celui de Python) et une bibliothèque.<br/>

Je 

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