<div id="top"></div>

<div align="center">
  <a href="https://github.com/franckferman/network-elements-synthesis">
    <img src="https://raw.githubusercontent.com/franckferman/network-elements-synthesis/main/img/skull.png" alt="Skull" width="128" height="128">
  </a>

<h3 align="center">ARP cache poisoning</h3>

  <p align="center">
    L'attaque de l'homme du milieu.
    <br/>
	<br/>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
	<li><a href="#1-introduction">Introduction</a></li>
    <li><a href="#2-cas_pratique">Cas pratique</a></li>
  </ol>
</details>

<div align="center">
<h2>1. Introduction</h2>

<p>De manière générale, quand les gens parlent de sécurité informatique (et de hacking), ils pensent très souvent aux failles applicatives, aux erreurs humaines (social engineering), au cracking (cryptographie), mais les problèmes concernant la sécurité des réseaux ne sont pas à prendre à la légère. Le réseau comporte tous autant de potentielle vulnérabilité que les autres catégories citées précédemment.<br/>

Je suppose que cela s'explique par le fait que la grande majorité des personnes se dirigeant vers le domaine de l'informatique ne font pas du réseau leur domaine de prédilection.<br/>

L'ARP cache poisoning (ou empoisonnement de cache ARP en français) est probablement le cas le plus fréquent d'attaque de type MiTM (Man-in-The-Middle ou l'attaque de l'homme du milieu).<br/>

Le principe d'une attaque dite de l'homme du milieu est, comme son nom l'indique, de se placer "au milieu" d'un échange entre des correspondants, pour pouvoir intercepter (et même manipuler) les communications entre ceux-ci et ce, sans que ni l'un ni l'autre puisse se douter que le canal de communication entre eux a été compromis (qu'un homme se trouve au milieu, en quelque sorte).<br/> 

Pour en revenir à notre attaque, l'ARP cache poisoning est une attaque qui consiste à exploiter la faiblesse du protocole ARP pour permettre à l'attaquant de détourner des flux de communications transitant entre une machine cible et une passerelle (routeur, box...), puis comme dit précédemment, l'attaquant peut ensuite écouter, modifier ou encore bloquer les paquets réseaux.<br/>

<div align="center">
Comment fonctionne ARP et où se situe sa faiblesse ?<br/>

Le protocole ARP sert à établir une liaison entre une adresse IP et une adresse MAC.<br/>

Quand une machine A souhaite communiquer avec une machine B sur un réseau, la machine A vérifie dans un premier dans sa table ARP, pour voir si une correspondance existe. ARP gère une table de correspondance (cache) pour mémoriser les relations, celle-ci est essentielle pour pouvoir adresse la trame au bon périphérique sur le réseau.<br/>

Si la correspondance n'est pas trouvée, une diffusion (broadcast) est émise, permettant de demander l'information aux machines sur le réseau, l'échange ressemble à cela.

<code>Request who-has 172.18.24.142 tell 172.18.24.143</code><br/>
<code>Reply 172.18.24.142 is-at 00:15:5d:ea:57:71</code><br/>

L'ordinateur va demander clairement, « quelle est l’adresse MAC correspondant à l’adresse IP adresseIP ? Répondez à monAdresseIP » (who-has). Puisqu’il s’agit d’un broadcast, tous les ordinateurs du segment vont recevoir la requête et en observant son contenu, ils pourront déterminer quelle est l’adresse IP sur laquelle porte la recherche.<br/>

La machine qui possède cette adresse IP sera la seule à répondre en envoyant à la machine émettrice une réponse ARP du type « je suis adresseIP, mon adresse MAC est adresseMAC » (Reply 172.18.24.142 is-at 00:15:5d:ea:57:71). Pour émettre cette réponse au bon ordinateur, il crée une entrée dans son cache ARP à partir des données contenues dans la requête ARP qu’il vient de recevoir.<br/>

La machine à l’origine de la requête ARP reçoit la réponse (Reply), met à jour son cache ARP et peut donc envoyer à l’ordinateur concerné le message qu’elle avait mis en attente.<br/>

Le problème, réside dans la façon avec laquelle ce protocole a été pensé et conçu. Celui-ci n'a, en effet pas été conçu pour prendre en compte les aspects de sécurité.<br/>

Il n'est pas nécessaire d'attendre qu'une machine vous demande votre adresse mac. Vous pouvez très bien la lui communiquer à n'importe quel moment en lui envoyant un simple packet ARP reply. Cela mettra à jour son cache ARP. Maintenant, imaginez que quelqu'un modélise et envoie un packet ARP Reply à une machine avec de fausses informations... C'est à ce moment que l'arp cache poisoning intervient.<br/>

On pourrait donc logiquement imaginer qu'un hacker se fasse passer pour une machine qu'il n'est pas (usurpation) et de ce fait intercepte le dialogue entre deux hôtes.<br/>

Mettons un exemple concret. Si nous corrompons le cache ARP de la victime en y inscrivant la correspondance entre l'adresse mac de l'attaquant et l'adresse ip du routeur, tous les packets qui transitent de la machine cible au routeur seraient alors interceptés par l'attaquant. Cela permettrait notamment d'intercepter les requêtes émises sur internet par la machine cible. Mais il reste tout de même un problème à résoudre pour l'attaquant. Les packets émis vont en effet passer par la machine du hacker mais ils ne seront pas reroutés vers la bonne machine. Ainsi, la machine cible ne pourra plus envoyer de paket au delà de son réseau local.<br/> 

Pour pouvoir les intercepter de manière transparente, l'attaquant doit simplement activer le mode routage ip sur sa machine. Cela va permettre de rerouter l'intégralité des packets dont l'adresse ip de destination est différente de la sienne. Que ce soit sous Windows ou Linux, cela s'effectue très facilement.<br/>

Il est bon de noter que de nombreux outils existent pour réaliser ce type d'attaque (Ettercap, Bettercap, arpspoof...)<br/>

<div align="center">
<h2>2. Cas pratique</h2>

<p>Attention, je tiens à préciser que cette vidéo (https://youtu.be/q3BvbugyMuQ) est une pure démonstration, en rien une quelconque un tutoriel.</p><br/>


<div align="center">
  <a href="https://youtu.be/q3BvbugyMuQ">
    <img src="https://raw.githubusercontent.com/franckferman/network-elements-synthesis/main/img/thumbnail-mitm_arp.png" alt="Skull" width="800" height="400">
  </a>
