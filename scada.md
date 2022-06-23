<p>Tout d'abord, avant de vous présenter Scada, j'aimerais commencer par mettre au point un élément qui me paraît particulièrement important car une erreur est très souvent effectuée quand on pense à celui-ci.<br>

ICS (Industrial Control System) et Scada (Supervisory Control and Data Acquisition) sont très souvent confondus, il s'agit pourtant bien de deux éléments bien distincts.<br>

Scada est en fait, en quelque sorte une des composantes de l'ICS.<br>

- Pour commencer, qu'est-ce qu'un ICS ?<br>

L'ICS désigne les systèmes industriels de manière générale.<br>

Pour être plus précis, un système industriel désigne, en l'occurrence, un système informatique s’interfaçant avec des systèmes physiques tels que des capteurs, des moteurs, des vannes...<br>

Ce type de système est de manière générale objectivement très peu étudié dans les écoles d'informatiques, ce qui est regrettable puisque l'on retrouve ces systèmes notamment dans les centrales nucléaires, les circuits de distribution d’eau, les systèmes d’alarme, de vidéosurveillance...<br>

L'ICS et l'IACS (Industrial Automation and Control Systems) représentent la même chose. En revanche, ces derniers sont encore une fois très souvent confondus avec les systèmes Scada, et plus rarement avec les DCS (Distribued Control System).<br>

En réalité, Scada concerne essentiellement la partie de supervision des différents systèmes ou des différents composants de notre système d'information industriel.<br>

La partie SCADA d’un ICS est composée (principalement) de trois éléments :<br>

- Les automates industriels programmables : il s'agit d'un micro-ordinateur/IoT programmable qui va permettre d'interagir (transformation des entrées électriques en sorties électriques, avec un système de condition, par exemple, ajuster une vitesse de rotation en fonction d'une température) avec des actionneurs (une pompe, un système mécanique...)<br>

Ces équipements sont typiquement équipés de processeurs ARM et peuvent éventuellement contenir un OS.<br>

- Une station de programmation, qui sert à concevoir et télécharger un programme utilisateur sur l'automate.<br>

- D'un poste de supervision : le plus souvent, on parlera d'IHM (Interface Homme Machine), son but principal est de superviser l’état du système physique et de déclencher des actions (fermer une vanne X, changer la vitesse des moteurs Y et Z...)<br>

Il est commun de trouver des IHM sur des PC avec des interfaces graphiques dessinées et assemblées, permettant à quiconque de visualiser et de communiquer avec les automates (typiquement pour réaliser les actions vues précédemment).<br><br></p>
