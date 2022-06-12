<div id="top"></div>

<div align="center">
  <a href="https://github.com/franckferman/network-elements-synthesis">
    <img src="https://raw.githubusercontent.com/franckferman/network-elements-synthesis/main/img/tcpdump.png" alt="tcpdump" width="400" height="200">
  </a>

<h3 align="center">tcpdump</h3>

  <p align="center">
    L'analyse de trafic en ligne de commande.
    <br/>
    <a href="https://www.tcpdump.org/"><strong>Lien vers le site officiel de tcpdump »</strong></a>
    <br/>
	  <br/>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
	  <li><a href="#1-présentation-de-tcpdump">Présentation de tcpdump</a></li>
      <li><a href="#2-commandes-et-utilisation-basique-de-tcpdump">Commandes et utilisation basique de tcpdump</a></li>
	  <li><a href="#3-demo">Démonstration - récupération d'un mot de passe en clair</a></li>
  </ol>
</details>

<div align="center">
<h2>1. Présentation de tcpdump</h2>

<p>tcpdump est un outil couramment utilisé et particulièrement apprécié par sa puissance, dont le but est d'effectuer des captures et une analyse du trafic sur une interface réseau.<br/>

Il permet d'écouter (sniffer) le trafic entrant/sortant sur de nombreux périphériques (Ethernet, Wi-Fi, USB...)<br/>

Dans l'idée, l'outil est semblable à Wireshark mais se différencie principalement de par son utilisation en ligne de commande uniquement à l'instar de tshark (mais à l'inverse de Wireshark, qui lui, dispose d'une interface graphique).<br/>

Comme Wireshark, tcpdump permet l'utilisation de filtres. Ce système de filtrage peut être très utile pour limiter l'obtention d'un trop grand nombre d'informations dans vos captures. En effet, un trop grand nombre d'informations pourrait drastiquement compliquer la recherche de l'information que vous désirez. Ces filtres peuvent aider à cibler les informations souhaitées. De plus, ces filtres peuvent vous aider à limiter la taille des données capturées afin d'empêcher la génération d'un fichier trop volumineux.<br/>

Il faut tout de même faire la distinction entre filtres de capture et filtre d'affichage (post-capture).<br/>

Dans l'exemple ci-dessous, je capture le trafic sans filtre et j'en applique un (d'affichage) au moment de la lecture du fichier.<br/>

<code>tcpdump -i any host 172.18.24.142 -w out.cap</code><br/>
<code>tcpdump -r file.cap icmp and host 172.18.24.142</code><br/>

Ci-dessous, je capture le trafic et j'y applique un filtre (de capture) directement.<br/>

<code>tcpdump -i eth0 -w file.cap icmp and host 172.18.24.142</code><br/>

Les filtres d'affichages (post-capture) sont utilisés pour rechercher des informations à l'intérieur de données déjà capturées (ou en train d'être capturés comme Wireshark le permet, typiquement, ils peuvent même être modifiés en pleine capture).<br/>

Le filtre de capture, quant à lui, est utilisé comme premier large filtre, le plus souvent pour limiter la taille du fichier contenant les données capturées.<br/>

Avec tcpdump, de nombreux filtres peuvent être mis en place, filtrer un port (25, 22, 80...) ou un protocole précis (arp, icmp, tcp...), un hôte (dst, src, entre tel et tel hôte), un paquet d'une taille spécifique (plus grand que, plus petit que...), et bien d'autres.<br/>

tcpdump peut être utilisé sur une machine à distance via SSH.<br/>

<code>ssh root@basicmailserver.com tcpdump -i any</code><br/>

Nous pouvons sans aucun souci effectuer une capture avec tcpdump, et si besoin analyser celle-ci par la suite avec Wireshark (ou avec tshark par exemple).<br/>

<code>tcpdump -i eth0 -w file.pcap</code><br/><br/>

<div align="center">
<h2>2. Commandes et utilisation basique de tcpdump</h2>

Cela me paraît pertinent de noter qu'il existe de nombreux "cheatsheet" en ligne (il s'agit en quelque sorte de "document de rappels", contenant le plus souvent une liste de commandes, les plus utiles) ou d'informations importantes, en l'occurrence (s'il s'agit d'un cheatsheet pour tcpdump), pour l'utilisation de tcpdump.<br/>

Ce type de document (appelé "cheatsheet") peut être extrêmement utile, aussi bien pour les débutants que pour les plus aguerrit. Nul n'est à l'abri d'un oubli et plus généralement, je n'ai jamais rencontré une seule personne prétendre tout connaitre par coeur, y compris des doctorants. Ces documents permettent de former un aperçu rapide des informations et commandes les plus utiles, le plus souvent pour un programme donné ou une liste de protocoles par exemple.<br/>

Pour vous donner quelques exemples concrets, PacketLife propose de nombreux cheatsheets intéressants.<br/>

- Un cheatsheet sur Scapy (https://packetlife.net/media/library/36/scapy.pdf).<br/>
- Un cheatsheet pour le STP (https://packetlife.net/media/library/11/Spanning_Tree.pdf).<br/>
- Un cheatsheet sur les VLANs (https://packetlife.net/media/library/20/VLANs.pdf).<br/>
- Un cheatsheet sur les ports les plus communs (https://packetlife.net/media/library/23/common_ports.pdf).<br/>

Et enfin, pour en revenir au sujet initial, ils proposent également un cheatsheet sur tcpdump (https://packetlife.net/media/library/12/tcpdump.pdf).

Effectuant un tantinet de pratique après avoir vu la théorie.<br/>

<div align="center">
Voici ci-dessous, quelques exemples de commandes basiques pour l'utilisation de tcpdump.<br/>

La commande la plus importante (de loin).<br/>
<code>man tcpdump</code><br/>

Afficher la liste des interfaces disponibles.<br/>
<code>tcpdump -D</code><br/>

Écouter sur toutes les interfaces disponibles.<br/>
<code>tcpdump -i any</code><br/>

Écouter sur une interface spécifique.<br/>
<code>tcpdump -i eth0</code><br/>

Mode verbeux.<br/>
<code>tcpdump -v</code><br/>

Il existe plus précisément trois modes, -v, -vv, -vvv (du moins au plus verbeux).

Le mode permettant d'obtenir le résultat le moins verbeux.<br/>
<code>tcpdump -q</code><br/>

Limiter le nombre de paquets reçus à N paquets.<br/>
<code>tcpdump -c 100</code><br/>

Enregistrement du trafic dans un fichier.<br/>
<code>tcpdump -w file.pcap</code><br/>

Lire un fichier préalablement enregistré.<br/>
<code>tcpdump -r file.pcap</code><br/>

Des filtres peuvent être ajoutés pour la lecture d'un fichier préalablement enregistré.<br/>
<code>tcpdump -r file.pcap arp</code><br/>

<div align="center">
Nous allons voir quelques exemples de basiques d'utilisation des filtres, même si en théorie, le cheatsheet nous permet d'avoir un aperçu relativement complet des filtres pouvant être affectés.<br/><br/>

Filtrer un hôte.<br/>
<code>tcpdump -i eth0 host 192.168.0.1</code><br/>

Filtrer un échange entre deux hôtes.<br/>
<code>tcpdump -i eth0 host 10.0.0.1 and host 10.0.0.2</code><br/>

Filtrer un protocole.<br/>
<code>tcpdump -i eth0 arp</code><br/>

Filtrer un port.<br/>
<code>tcpdump -i eth0 port 22</code><br/>

Exemple d'un filtre comprenant plusieurs conditions.<br/>
<code>tcpdump -i eth0 -vvv dst 192.168.0.1 and src 192.168.0.2 icmp</code><br/>

Écoute d'un bloc réseau.<br/>
<code>tcpdump -i eth0 net 192.168.0.0/24</code><br/><br/>
	
<div align="center">
<h2>3. Démonstration - Récupération d'un mot de passe en clair (authentification FTP)</h2>

[![asciicast](https://asciinema.org/a/gzkltiQC0ubgH4NZVebf5hv61.svg)](https://asciinema.org/a/gzkltiQC0ubgH4NZVebf5hv61)
