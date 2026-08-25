La **CVD** (*Chemical Vapor Deposition*, Deposizione Chimica da Fase Vapore) è una tecnica di fabbricazione in cui uno o più gas precursori reagiscono chimicamente sulla superficie riscaldata del wafer, depositando un film solido uniforme ed espellendo i sottoprodotti di reazione in forma gassosa.

A differenza della [PVD](./PVD.md) (che trasferisce materiale solido per via meccanica), la CVD si basa su **reazioni chimiche di superficie**.

---

### 1. Il Vantaggio Chiave: Copertura Conforme al 100%

Poiché il materiale non viene "spruzzato in linea retta" ma trasportato da molecole di gas fluide, i reagenti si diffondono ovunque all'interno della camera a vuoto.
* **Assenza di Effetto Ombra:** il gas si insinua in trincee microscopiche e fori ad altissimo rapporto d'aspetto, depositando uno strato uniforme su tutte le pareti verticali e sul fondo.
* È la tecnologia indispensabile per il riempimento dei [Vias](./Vias.md) e delle trincee isolanti STI ([MOS](./MOS.md)).

---

### 2. Esempi Fondamentali di Reazioni CVD in Microelettronica

* **Tungsteno metallico per i contatti verticali ([Vias](./Vias.md)):**
  $$\text{WF}_6\text{ (gas)} + 3\text{H}_2\text{ (gas)} \longrightarrow \text{W}\text{ (solido)} + 6\text{HF}\text{ (gas)}$$
  Permette di riempire canali stretti senza lasciare cavità d'aria interne (*void-free plug*).
* **Polisilicio per i Gate e Resistori ([MOS](./MOS.md), [Resistore](./Resistore.md)):**
  $$\text{SiH}_4\text{ (Silano)} \overset{\Delta}{\longrightarrow} \text{Si}\text{ (policristallino)} + 2\text{H}_2\text{ (gas)}$$
* **Biossido di Silicio ($\text{SiO}_2$) isolante per riempimento trincee STI o inter-livello:**
  Decomposizione di $\text{TEOS}$ (*Tetraetilortosilicato*) o reazione silano-ossigeno per creare dielettrici conformali.

---

### 3. Varianti Principali della CVD

* **LPCVD (*Low Pressure CVD*):** lavora a bassa pressione e temperature medie ($500^\circ\text{C}-800^\circ\text{C}$). Offre un'uniformità e purezza molecolare eccellente (usata per polisilicio e nitruro).
* **PECVD (*Plasma Enhanced CVD*):** il plasma fornisce l'energia necessaria alla reazione chimica, permettendo di depositare film a temperature molto più basse ($200^\circ\text{C}-400^\circ\text{C}$), ideale quando sono già presenti strati metallici che non tollerano calore elevato.

---

*Pagine correlate:*
- [PVD](./PVD.md)
- [Vias](./Vias.md)
- [Siliciuro](./Siliciuro.md)
- [MOS](./MOS.md)
- [Elettromigrazione e tossicità dei metalli](./Elettromigrazione%20e%20tossicit%C3%A0%20dei%20metalli.md)
- [Resistore](./Resistore.md)
