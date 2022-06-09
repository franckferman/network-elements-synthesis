<div id="top"></div>

<div align="center">
  <a href="https://github.com/franckferman/network-elements-synthesis">
    <img src="https://raw.githubusercontent.com/franckferman/network-elements-synthesis/main/img/tcpdump.png" alt="tcpdump" width="80" height="80">
  </a>

<h3 align="center">tcpdump</h3>

  <p align="center">
    L'analyse de paquets depuis votre terminal.
    <br/>
    <a href="https://www.tcpdump.org/"><strong>Lien vers le site officiel de tcpdump »</strong></a>
    <br/>
	<br/>
  </p>
</div>

<div align="center">
<h2>1. Présentation de tcpdump</h2>

<p>tcpdump est un outil couramment utilisé dont le but est d'effectuer des analyses et des captures du trafic sur un réseau ou entre des machines. <br/>Il permet d'écouter (sniffer) le trafic entrant/sortant sur de nombreux périphériques (Ethernet, Wi-Fi, USB...)<br/><br/>

Dans l'idée, l'outil est semblable à Wireshark mais il se différencie principalement par son utilisation s'effectuant en ligne de commande uniquement.<br/><br/>

Son plus gros défaut, si l'on doit lui en donner un, réside probablement dans la difficulté de compréhension de la syntaxe mais une fois celle-ci suffisamment bien acquise, l'utilisation de cet outil devient rapidement un jeu d'enfant (et devient vite une alternative à Wireshark pour la réalisation de captures ou analyses sur le réseau). Cet outil est particulièrement apprécié pour sa puissance et s'installe très facilement sur les systèmes GNU/Linux.<br/><br/>

De plus, il est bon de noter que des captures peuvent être effectuées avec tcpdump puis analysées par la suite avec Wireshark.<br/><br/>

Comme Wireshark, l'outil permet l'utilisation de nombreux filtres comme par exemple la mise en place d'un filtre pour le port 80, 25 ou 22.<br/><br/>

Une autre différence notable avec Wireshark est que tcpdump peut être utilisé pour l'analyse et la capture du trafic sur une machine distante (SSH).<br/><br/></p>

<div align="center">
<h2>2. Commandes et utilisation basique de tcpdump</h2>

<div align="center">
Voici quelques exemples de commandes basiques pour l'utilisation de tcpdump:<br/><br/>

Afficher la liste des interfaces disponibles:<br/>
<code>tcpdump -D</code>

<br/><br/>

Écouter sur toutes les interfaces disponibles:<br/>
<code>tcpdump -i any</code>

<br/><br/>

Écouter sur une interface spécifique:<br/>
<code>tcpdump -i eth0</code>

<br/><br/>

Mode verbeux (TTL, longueur totale, vérification de la somme de contrôle des en-têtes IP et ICMP...):<br/>
<code>tcpdump -v</code>

<br/><br/>

Mode le moins verbeux (idéal pour un rapide aperçu des échanges):<br/>
<code>tcpdump -q</code>

<br/><br/>

Mise en place d'une limite du nombre de paquets reçue avant arrêt de la capture:<br/>
<code>tcpdump -c 100</code>

<br/><br/>

Enregistrement dans un fichier (idéal pour analyse par la suite avec Wireshark par exemple):<br/>
<code>tcpdump -w capture01.pcap</code>

<br/><br/>

Lire un fichier préalablement enregistré:<br/>
<code>tcpdump -r capture01.pcap</code>

<br/><br/>

Des filtres peuvent être ajoutés pour la lecture:<br/>
<code>tcpdump -r capture01.pcap arp</code>

<br/><br/>

<div align="center">
Voici quelques exemples de basiques d'utilisation des filtres:<br/><br/>

Filtre un hôte/une adresse IP:<br/>
<code>tcpdump -i eth0 -v host 192.168.0.1</code>

<br/><br/>

Traffic destiné à une adresse IP bien précise (en destination), similaire au filtre ip.dst de Wireshark:<br/>
<code>tcpdump -i eth0 -v dst 192.168.0.1</code>

<br/><br/>

Traffic destiné à une adresse IP bien précise (source), similaire au filtre ip.src de Wireshark:<br/>
<code>tcpdump -i eth0 -v src 192.168.0.1</code>

<br/><br/>

Filtrer un protocole (ARP pour l'exemple):<br/>
<code>tcpdump -i eth0 arp</code>

<br/><br/>

Filtrer un port (22 pour l'exemple):<br/>
<code>tcpdump -i eth0 -port 22</code>

<br/><br/>

Filtrer plusieurs conditions:<br/>
<code>tcpdump -i eth0 -v dst 192.168.0.1 && src 127.0.0.1 icmp</code>

<br/><br/>

Sniffer tout un bloc de réseau:<br/>
<code>tcpdump -i eth0 -v net 192.168.0.1/24</code>

<br/><br/>