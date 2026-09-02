Il **siliciuro metallico** è un composto chimico intermetallico formato dalla reazione tra atomi di silicio e un metallo di transizione (i più utilizzati sono $\text{NiSi}$, $\text{CoSi}_2$ o $\text{TiSi}_2$).

Non è silicio puro e non è un metallo isolato: viene formato direttamente sulla superficie del Gate in polisilicio e sulle sacche drogate di Source e Drain per ottimizzare il trasporto di carica.

---

### 1. Il Processo Salicide (*Self-Aligned Silicide*)

Il siliciuro viene realizzato mediante un processo auto-allineato che **non richiede maschere fotolitografiche aggiuntive**:
1. Si deposita un velo sottile di metallo puro (es. Nichel o Cobalto) su tutta la superficie del wafer.
2. Si esegue un trattamento termico rapido a temperatura controllata ($400^\circ\text{C}-700^\circ\text{C}$):
   * Dove il metallo tocca il **silicio nudo** (Gate, Source e Drain), reagisce chimicamente consumando qualche nanometro di silicio e formando il siliciuro metallico.
   * Dove il metallo tocca l'**ossido isolante** (distanziatori *spacers* e isolamenti STI), **non avviene alcuna reazione**.
3. Un lavaggio chimico selettivo con acido rimuove il metallo non reagito sopra l'ossido, lasciando intatto il siliciuro solo sopra Gate e diffusioni.

---

### 2. Perché si Usa il Siliciuro: I Due Vantaggi Fondamentali

#### A. Crollo della Resistenza di Strato ($R_\square$)
Il silicio drogato di Source/Drain e il polisilicio hanno una resistenza di strato di $R_\square \approx 50 - 200\,\Omega/\square$.
Con la formazione del siliciuro, la resistenza di strato **crolla a $R_\square \approx 2 - 5\,\Omega/\square$** (ridotta di $20-50$ volte). La corrente che entra nelle sacche sceglie il percorso a minima resistenza, scorrendo lungo la superficie siliciurata ad altissima conducibilità invece di attraversare l'intera profondità della sacca.
👉 Approfondimento: [Resistore](../Dispositivi%20e%20Componenti/Resistore.md) per l'uso della maschera di blocco del siliciuro (SAB).

#### B. Contatto Ohmico Ideale: Abbassamento e Restringimento della Barriera
Il passaggio di corrente tra semiconduttore e metallo incontra una barriera di potenziale (giunzione Schottky) caratterizzata da due parametri:
* **Larghezza della barriera ($W_{dep}$):** viene resa sottilissima (pochi nanometri) grazie al **forte drogaggio superficiale ($N^+$)**, che stringe la zona di svuotamento ($W_{dep} \propto \frac{1}{\sqrt{N_D}}$).
* **Altezza della barriera ($\Phi_B$):** viene **abbassata chimicamente dal siliciuro**.

La probabilità che gli elettroni attraversino la barriera per **effetto tunnel** quantistico (*Field Emission*) dipende esponenzialmente da entrambi i fattori:
$$R_c \propto \exp\left( \frac{2\sqrt{\varepsilon_{si} m^*}}{\hbar} \cdot \frac{\Phi_B}{\sqrt{N_D}} \right)$$

Il forte drogaggio stringe la barriera e il siliciuro ne riduce l'altezza: la loro combinazione trasforma il contatto in un **contatto ohmico perfetto** con resistenza specifica trascurabile ($R_c < 10^{-8}\,\Omega\cdot\text{cm}^2$).
👉 Approfondimento: [Contatti Ohmici e Giunzioni High-Low](../Dispositivi%20e%20Componenti/Contatti%20Ohmici%20e%20Giunzioni%20High-Low.md).

---

*Pagine correlate:*
- [Contatti Ohmici e Giunzioni High-Low](../Dispositivi%20e%20Componenti/Contatti%20Ohmici%20e%20Giunzioni%20High-Low.md)
- [Diodo PIN e Modulazione di Conducibilita](../Dispositivi%20e%20Componenti/Diodo%20PIN%20e%20Modulazione%20di%20Conducibilita.md)
- [Vias](./Vias.md)
- [Elettromigrazione e tossicità dei metalli](./Elettromigrazione%20e%20tossicit%C3%A0%20dei%20metalli.md)
- [Resistore](../Dispositivi%20e%20Componenti/Resistore.md)
- [MOS](../Dispositivi%20e%20Componenti/MOS.md)
- [CVD](./CVD.md)
- [PVD](./PVD.md)
