Nei circuiti integrati è fondamentale isolare elettricamente i transistor adiacenti realizzati sullo stesso substrato, per evitare che piste conduttive o di metallo sovrastanti agiscano da gate parassiti accendendo canali indesiderati tra sacche vicine.

---

### 1. Il Processo Storico LOCOS e la Nascita del Bird's Beak

Il processo storico di isolamento era il **LOCOS** (*LOCal Oxidation of Silicon*):
* **Principio:** si fanno crescere spesse zone di biossido di silicio (*Field Oxide* / $\text{FOX}$) tra i transistor per alzare drasticamente la tensione di soglia parassita ed evitare accoppiamenti.
* **La maschera di nitruro:** la regione attiva viene protetta da una maschera di nitruro di silicio ($\text{Si}_3\text{N}_4$), impermeabile all'ossigeno. Il wafer viene poi posto in forno ad alta temperatura ($1000^\circ\text{C}$).
* **Il Becco d'Uccello (*Bird's Beak*):** l'ossidazione termica è **isotropa**. L'ossigeno non scava solo verso il basso consumando silicio, ma si infila anche **lateralmente sotto i bordi del nitruro**. L'ossido cresce aumentando di volume e solleva la maschera, formando una svasatura laterale conica affusolata identica a un becco d'uccello.

![Meccanismo LOCOS e Bird's Beak](../../Immagini/locos_birds_beak.png)

---

### 2. Il Dilemma della Profondità e la Strozzatura della Larghezza $W$

Nel LOCOS più vogliamo isolare, più dobbiamo andare in profondità con l'ossido:
* **Profondità ed espansione laterale:** poiché l'ossidazione è isotropa, maggiore è il tempo nel forno per andare a fondo, maggiore sarà l'espansione laterale del becco d'uccello.
* **Perché mangia la $W$ e NON la $L$:**
  * L'ossido circonda l'area attiva come un recinto.
  * La striscia di **Gate (Polisilicio)** scavalca l'area attiva lungo la larghezza $W$, poggiando direttamente sopra i due becchi d'uccello laterali. Sotto i becchi l'ossido è troppo spesso per accendere il canale: il canale utile si forma solo al centro, **strozzando la larghezza effettiva** ($W_{eff} = W_{drawn} - 2\Delta W_{beak}$).
  * Lungo la lunghezza $L$ il canale è protetto al centro dal Gate di polisilicio ed è separato dal LOCOS dalle sacche di Source e Drain: il becco tocca solo il margine esterno estremo delle diffusioni, lasciando intatta $L$.

![Confronto Sezione Lungo L vs Sezione Lungo W](../../Immagini/locos_l_vs_w_cross_sections.png)

---

### 3. Gerarchia dei Processi: Perché Prima l'Ossidazione e Poi il Gate?

Nella fabbricazione si esegue **prima l'ossidazione LOCOS e solo dopo la deposizione del Gate**:
1. Il Gate di polisilicio viene depositato in modo conformale e **segue la forma del becco d'uccello**, arrampicandosi sulla gobba laterale dell'ossido spesso (profilo a sella ai bordi).
2. **Perché non depositare prima il Gate e poi ossidare?**
   * **Il Gate è di polisilicio:** se il Gate fosse già sul wafer durante l'ossidazione a $1000^\circ\text{C}$, l'ossigeno lo divorerebbe ossidandolo interamente in $\text{SiO}_2$ (un blocco di vetro isolante!).
   * **Espansione volumetrica:** l'ossido cresce aumentando di volume del $220\%$ e generando pressioni enormi (GigaPascal) che solleverebbero e spaccherebbero l'ossido sottile di gate.

---

### 4. Il Passaggio a STI (*Shallow Trench Isolation*)

Nel LOCOS, per compensare lo spazio rubato dai becchi bisognava distanziare maggiormente i transistor. Moltiplicando questo spreco di area per miliardi di transistor, il costo del chip diventa insostenibile.

Per questo si è passati alla **STI** (*Shallow Trench Isolation*):
* Si scava una trincea verticale netta nel silicio tramite attacco al plasma anisotropo (**Reactive Ion Etching**).
* Si riempie la trincea con ossido $\text{SiO}_2$ depositato chimicamente ([CVD](./CVD.md)).
* Si spiana la superficie con lucidatura chimico-meccanica (**CMP**).
* **Risultato:** pareti verticali a $90^\circ$, **zero Bird's Beak**, superficie perfettamente piana e transistor impacchettabili a distanze nanometriche.

---

*Pagine correlate:*
- [Isolamento](./Isolamento.md)
- [BJT](./BJT.md)
- [Diodo](./Diodo.md)
- [Siliciuro](./Siliciuro.md)
- [Vias](./Vias.md)
- [Elettromigrazione e tossicità dei metalli](./Elettromigrazione%20e%20tossicit%C3%A0%20dei%20metalli.md)
- [CVD](./CVD.md)
- [PVD](./PVD.md)
- [Wafer produzione](./Wafer%20produzione.md)
- [Difficoltà nel fare un componente ideale](./Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Resistore](./Resistore.md)
- [Condensatori](./Condensatori.md)
- [La soglia da cosa dipende](../Introduzione/La%20soglia%20da%20cosa%20dipende.md)