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
	  <li><a href="#1-présentation-de-scapy">Présentation de Scapy</a></li>
    <li><a href="#2-une-communauté-grandissante-dexperts">Une communauté grandissante d'experts</a></li>
      <li><a href="#3-utilisation-de-scapy">Utilisation de Scapy</a></li>
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

Voici quelques exemples d'incroyables outils réalisés par des membres de la communauté avec Scapy:<br/>

- ISF, Industrial Control System Exploitation Framework (https://github.com/dark-lbp/isf): an exploitation framework based on Python (similar to metasploit framework). 
- wifiphisher (https://github.com/wifiphisher/wifiphisher): create rogue access point (un outil que j'utilise et j'apprécie particulièrement).<br/>
- ufonet (https://github.com/epsylon/ufonet): create your own botnet to send untraceable DDoS attacks<br/>
- trackerjacker (https://github.com/calebmadrigal/trackerjacker): Maps and tracks Wi-Fi networks and devices through raw 802.11 monitoring. Like nmap for mapping wifi networks you're not connected to, plus device tracking.<br/>
- fenrir (https://github.com/Orange-Cyberdefense/fenrir-ocd): bypass wired 802.1x protection.<br/>
- net-creds (https://github.com/DanMcInerney/net-creds): sniff and catch all sensitive data on an interface.<br/>
- Responder (https://github.com/SpiderLabs/Responder): LLMNR, NBT-NS and MDNS poisoner.<br/>
- sshame (https://github.com/HynekPetrak/sshame): tool to brute force SSH public-key authentication.<br/>
- TorPylle (https://github.com/cea-sec/TorPylle): a Python / Scapy implementation of the OR (TOR) protocol.<br/>

Ces exemples montrent la puissance de Scapy, si celui-ci est utilisé avec une suffisamment bonne maitrise de l'outil et du réseau.</p><br/>

<div align="center">
<h2>3. Utilisation de Scapy</h2>

<p>Scapy est à la fois un interpréteur de commandes (basé sur celui de Python) et une bibliothèque.<br/>

Le mode interpréteur de commandes (appelé également interactif) est particulièrement utile pour effectuer des tests sans avoir à écrire un programme au préalable ou pour la réalisation de taches basiques ne nécessitant pas nécessairement le développement d'un programme.<br/>

Une fois dans ce mode interactif, vous pouvez entrer la commande ls() pour afficher la liste des protocoles que sait gérer Scapy et lsc() pour afficher la liste des commandes.<br/>

La commande ls() peut être utilisée en renseignant un protocole, par exemple ls(IP), ce qui va nous permettre d'afficher la liste des paramètres attribuables.<br/>

- Effectuons un exemple concret:<br/>

Nous pouvons jouer avec la couche 2 et préparer une trame Ethernet.<br/>

<code>>>> Layer2=Ether()</code><br/>

Affichons la liste des paramètres.<br/>

<code>>>> ls(Layer2)<br/>
<code>dst        : DestMACField                        = 'ff:ff:ff:ff:ff:ff' (None)</code><br/>
<code>src        : SourceMACField                      = '00:15:5d:ea:57:71' (None)</code><br/>
<code>type       : XShortEnumField                     = 36864           (36864)</code><br/>

Vous pouvez constater que des valeurs par défaut sont automatiquement remplies par Scapy. Bien entendu, celles-ci peuvent être modifiées à notre guise.<br/>

Pour l'exemple, je peux spoofer mon adresse MAC source.<br/>

<code>>>> Layer2.src="aa:bb:cc:dd:ee:ff"</code><br/>

Cela n'a aucun sens mais si j'en ai l'envie, je peux envoyer dès maintenant cette trame sur le réseau.<br/>

<code>>>> sendp(Layer2)</code><br/>

En l'occurrence, la raison pour laquelle je réalise cette action est pour faire comprendre que l'on a bel et bien un contrôle total sur la génération de paquets/trames (même malformés). En effet, si vous sniffez votre trafic avec Wireshark par exemple, vous verrez que la trame est considérée comme étant malformé, mais ce qui compte, c'est que celle-ci passe tout de même à travers le réseau et est tout de même générée.<br/>

Pour information, la commande sendp est différente de la commande send.<br/>

La fonction send() envoie les paquets au niveau de la couche 3 alors que la commande sendp() fonctionnera au niveau de la couche 2.<br/>

Je vais dès maintenant déclarer la variable pour mon paquet.<br/>

<code>>>> Layer3=IP()</code><br/>

<code>>>> ls(IP)</code><br/>

<code>version    : BitField  (4 bits)                  = (4)</code><br/>
<code>ihl        : BitField  (4 bits)                  = (None)</code><br/>
<code>tos        : XByteField                          = (0)</code><br/>
<code>len        : ShortField                          = (None)</code><br/>
<code>id         : ShortField                          = (1)</code><br/>
<code>flags      : FlagsField  (3 bits)                = (<Flag 0 ()>)</Flag></code><br/>
<code>frag       : BitField  (13 bits)                 = (0)</code><br/>
<code>ttl        : ByteField                           = (64)</code><br/>
<code>proto      : ByteEnumField                       = (0)</code><br/>
<code>chksum     : XShortField                         = (None)</code><br/>
<code>src        : SourceIPField                       = (None)</code><br/>
<code>dst        : DestIPField                         = (None)</code><br/>
<code>options    : PacketListField                     = ([])</code><br/>

Je vais remettre mon adresse mac par défaut à la couche 2.<br/>

<code>>>> Layer2.src="00:15:5d:ea:57:71"</code><br/>

Maintenant, attribuons une adresse de destination.<br/>

<code>>>> Layer3.dst="172.18.24.143"</code><br/>

Je vais en quelque sorte encapsuler mes couches avec l'opérateur '/'.<br/>

Pour vous montrer d'autres types de commandes utiles, je vais utiliser srploop() plutôt que send() ou sendp() déjà vu précédemment.<br/>

srploop() est une boucle qui va envoyer le paquet (à partir de la couche 2 et imprimer la réponse.<br/>

<code>>>> srploop(Layer2/Layer3/ICMP())</code><br/>

<code>RECV 1: Ether / IP / ICMP 172.18.24.143 > 172.18.24.142 echo-reply 0</code><br/>
<code>RECV 1: Ether / IP / ICMP 172.18.24.143 > 172.18.24.142 echo-reply 0</code><br/>
<code>RECV 1: Ether / IP / ICMP 172.18.24.143 > 172.18.24.142 echo-reply 0</code><br/>
<code>RECV 1: Ether / IP / ICMP 172.18.24.143 > 172.18.24.142 echo-reply 0</code><br/>

Comme dit précédemment, je peux, si je le souhaite casser complètement les codes.<br/>

<code>>>> srploop(Layer2/Layer3/Layer3/Layer3/ICMP())</code><br/>

Pour continuer notre démonstration initiale, ajoutons une couche 4.<br/>

<code>>>> Layer4=TCP()</code><br/>

<code>>>> ls(Layer4)</code><br/>

<code>sport      : ShortEnumField                      = 20              (20)</code><br/>
<code>dport      : ShortEnumField                      = 80              (80)</code><br/>
<code>seq        : IntField                            = 0               (0)</code><br/>
<code>ack        : IntField                            = 0               (0)</code><br/>
<code>dataofs    : BitField  (4 bits)                  = None            (None)</code><br/>
<code>reserved   : BitField  (3 bits)                  = 0               (0)</code><br/>
<code>flags      : FlagsField  (9 bits)                = <Flag 2 (S)>    (<Flag 2 (S)>)</code><br/>
<code>window     : ShortField                          = 8192            (8192)</code><br/>
<code>chksum     : XShortField                         = None            (None)</code><br/>
<code>urgptr     : ShortField                          = 0               (0)</code><br/>
<code>options    : TCPOptionsField                     = []              (b'')</code><br/>

Ayant décrit suffisamment d'actions et ayant fourni de nombreuses explications, je ne pense pas qu'il soit nécessaire d'aller plus loin à ce niveau.<br/>

Comme dit précédemment, nous pouvons sniffer le trafic très simplement avec Scapy.<br/>

<code>x=sniff(filter='icmp', count=2, iface='eth0')</code><br/>

<code>x.summary()</code><br/>
<code>Ether / IP / ICMP 172.18.24.142 > 172.18.24.143 echo-request 0</code><br/>
<code>Ether / IP / ICMP 172.18.24.143 > 172.18.24.142 echo-reply 0</code><br/>

tcpdump ou tshark par exemple peuvent également être utilisés.<br/>

Il existe bien d'autres fonctionalitées intéressantes tels que traceroute, arpcachepoison, arping, getmacbyip, etherleak, fuzz, is_promisc (pour vérifier si la cible est en mode promiscuous/promiscuité), rdpcap (pour lire des fichiers pcaps), report_ports...<br/>

Pour aller plus loin avec Scapy, j'ai réalisé un exemple de programme permettant le scan de ports. Il existe plusieurs manières de réaliser un scan de ports, un des cas les plus simples et classiques est la réalisation d'un scan TCP.

Le but est de forger un paquet TCP comportant le drapeau SYN, l'envoyer à l'hôte sur le port que l'on souhaite tester, et si l'on reçoit une réponse comportant les drapeaux SYN et ACK, déclarer le port ouvert. Si le serveur répond avec un RST, c'est que le port est fermé.

Voici l'aperçu final du programme, celui-ci est bien entendu disponible sur mon dépôt Github (https://github.com/franckferman/network-elements-synthesis/blob/main/scapy/tcp_scan.py).

[![asciicast](https://asciinema.org/a/KOZ73YzWUa6Hc9RG5ldZ28DqR.svg)](https://asciinema.org/a/KOZ73YzWUa6Hc9RG5ldZ28DqR)

Pour conclure, nous avons pu voir que le potentiel de Scapy est considérable et il repose majoritairement sur les compétences de l'utilisateur qui l'utilise.</p>
