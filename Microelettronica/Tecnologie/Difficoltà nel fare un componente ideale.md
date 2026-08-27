Nell'elettronica di base usiamo il **modello a parametri concentrati** (leggi di Kirchhoff), assumendo componenti ideali e propagazione istantanea del segnale. 
Nel silicio reale non è così per due grandi motivi:

---

### 1. Parassiti Distribuiti (Perché i componenti non sono ideali)

Ogni porzione di conduttore o semiconduttore integrata sul silicio interagisce fisicamente con tutto ciò che ha intorno:

* **Il Resistore in polisilicio a serpentina:**
  Per creare una resistenza si deposita una striscia di polisilicio ripiegata a zigzag (serpentina) per occupare meno spazio.
  👉 Approfondimento: [Resistore](./Resistore.md) per layout, siliciuro e non-linearità.
  Il problema è che i tratti affiancati formano **capacità parassite tra le piste**, oltre alla capacità parassita verso il substrato di silicio sottostante. Ad alte frequenze la corrente scavalca la resistenza "saltando" attraverso queste capacità.
* **L'Induttore a spirale:**
  Stessa dinamica: le spire adiacenti creano capacità parassite tra di loro e con il substrato. Oltre una certa frequenza critica, l'induttore smette di fare l'induttore e si comporta come un condensatore!
  👉 Approfondimento: [Induttore](./Induttore.md) per parassiti, frequenza di autorisonanza, schermatura PGS e [Condensatori](./Condensatori.md).

> **In sintesi:** sul silicio non esiste il "componente puro": ogni geometria crea capacità, resistenze e induttanze parassite distribuite con il substrato e con i conduttori vicini.

---

### 2. Dalle Leggi di Kirchhoff alle Linee di Trasmissione (Effetti di Propagazione)

Il principio è esattamente lo stesso dell'antenna:
* **In ricezione:** un circuito capta onde esterne quando la sua lunghezza $d$ è paragonabile a $\lambda$.
  👉 Vedi: [Integrati protetti da interferenze](../Introduzione/Integrati%20protetti%20da%20interferenze.md)
* **In trasmissione (segnale interno):** se il circuito genera internamente un segnale con frequenza così alta che la sua lunghezza d'onda $\lambda$ diventa **paragonabile alle dimensioni fisiche $d$ del collegamento** ($d \approx \lambda$ o $d \gtrsim \lambda/10$), non possiamo più trattare il filo come un conduttore ideale a potenziale uniforme.

Dobbiamo passare alla **teoria delle linee di trasmissione e delle radiofrequenze (RF)**, considerando:
* Effetti di propagazione e sfasamento dell'onda lungo la pista.
* **Riflessioni del segnale** alle estremità se non c'è corretto **adattamento di impedenza** ($Z_{load} = Z_0$).
* Irraggiamento di disturbi (*crosstalk*) verso i circuiti adiacenti.

---

*Pagine correlate:*
- [Diodo](./Diodo.md)
- [Transitori del diodo e capacità](./Transitori%20del%20diodo%20e%20capacita.md)
- [Breakdown e Diodo Zener](./Breakdown%20e%20Diodo%20Zener.md)
- [BJT](./BJT.md)
- [MOS](./MOS.md)
- [Resistore](./Resistore.md)
- [Condensatori](./Condensatori.md)
- [Induttore](./Induttore.md)
- [Integrati protetti da interferenze](../Introduzione/Integrati%20protetti%20da%20interferenze.md)
- [Analogico non si scende di dimensioni](../Introduzione/Analogico%20non%20si%20scende%20di%20dimensioni.md)
