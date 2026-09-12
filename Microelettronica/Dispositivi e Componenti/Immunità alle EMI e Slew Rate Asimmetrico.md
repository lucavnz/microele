# Immunità alle EMI e Slew Rate Asimmetrico negli Op-Amp

Nei moderni circuiti integrati per automotive, avionica e comunicazioni mobili, gli amplificatori operazionali operano immersi in campi elettromagnetici ad altissima frequenza (**EMI**, *Electromagnetic Interference*, da centinaia di $\text{MHz}$ a decine di $\text{GHz}$).  
Sebbene tali frequenze siano enormemente superiori alla banda passante dell'amplificatore (es. $GBW \approx 10\,\text{MHz}$), i dispositivi analogici non lineari convertono questi disturbi ad alta frequenza in un deleterio **offset continuo (DC)** che altera permanentemente le misure e i punti di lavoro.

---

### 1. La Fisica del Fenomeno: Raddrizzamento del Segnale RF nel MOS

I transistor MOS non sono amplificatori lineari ideali: la loro caratteristica corrente-tensione in saturazione è quadratica:
$$I_D = \frac{1}{2} k' \frac{W}{L} (V_{GS} - V_{th})^2$$

Se un disturbo a radiofrequenza $V_{emi}(t) = V_m \sin(\omega t)$ si sovrappone alla tensione di polarizzazione continua $V_{GS0}$:
$$I_D(t) = \frac{1}{2} k' \frac{W}{L} \left[ (V_{GS0} - V_{th}) + V_m \sin(\omega t) \right]^2$$
Sviluppando il quadrato e calcolando il valor medio temporale $\langle I_D \rangle$:
* Il termine lineare a frequenza fondamentale ha media nulla: $\langle \sin(\omega t) \rangle = 0$.
* Il termine quadratico ha media positiva:
  $$\langle \sin^2(\omega t) \rangle = \left\langle \frac{1 - \cos(2\omega t)}{2} \right\rangle = \frac{1}{2}$$

La corrente media complessiva erogata dal MOS diventa:
$$\langle I_D \rangle = I_{D0} + \mathbf{\frac{1}{4} k' \frac{W}{L} V_m^2}$$

```
                Disturbo RF ad alta frequenza (fuori banda)
                                    │
                                    ▼
                Non-linearità quadratica del transistore
                                    │
                                    ▼
           Generazione di una corrente continua parassita (ΔI_DC ∝ Vm²)
                                    │
                                    ▼
             Spostamento permanente della tensione DC (Offset)
```

> 📌 **L'esperimento del Source Follower:**  
> In un inseguitore di sorgente polarizzato a $V_{out} = 0.77\,\text{V}$, applicando un disturbo EMI ad alta frequenza e filtrando l'uscita con un condensatore da $500\,\text{pF}$, la tensione continua **non torna a $0.77\,\text{V}$**, ma si stabilizza a circa **$0.90\,\text{V}$**. Si genera un offset continuo permanente di oltre **$+130\,\text{mV}$**.

---

### 2. Confronto tra Topologie: Perché il Folded Cascode Vince?

Dal confronto sistematico tra le principali architetture a parità di specifiche:
1. **Amplificatore a due stadi di Miller** classico.
2. **Cascode**.
3. **Folded Cascode**.

I risultati sperimentali mostrano che **il Folded Cascode è di gran lunga la topologia meno suscettibile alle EMI**.  
La causa radice risiede nella **simmetria dello Slew Rate ($SR^+ \approx SR^-$)**: il Folded Cascode garantisce percorsi fisici identici per la carica e la scarica dei nodi interni.

---

### 3. Perché lo Slew Rate è Asimmetrico negli Amplificatori Tradizionali?

Nella teoria elementare si assume $SR^+ = SR^- = I_{\text{tail}}/C$. Nella realtà di un amplificatore classico (come il Miller *single-ended*), intervengono tre asimmetrie fisiche:

```
                       Vdd
                      ┌─┴─┐
                      │   │
                  M3 ┌┴┐ ┌┴┐ M4
        (a diodo) └──┤   ├───┘ (specchio)
           Cp2 ───►  │   │
                     ├───┼───────► Vout (con capacità CL)
                     │   │
                  M1 └┬┘ └┬┘ M2
      Vin1 (in+) ────┤   ├─── Vin2 (in-)
                     └─┬─┘
                       │ ◄── Cp1 (nodo di coda)
                      [Ib]
                       │
                      GND
```

#### A) Percorso Diretto (Discesa) vs Percorso Lento attraverso lo Specchio (Salita)
* **In discesa ($SR^-$):** Il transistor d'ingresso di destra $M_2$ è collegato direttamente all'uscita. Quando $V_{in2}$ sale, $M_2$ scarica **immediatamente** la capacità di carico $C_L$ verso massa.
* **In salita ($SR^+$):** Il transistor d'ingresso di sinistra $M_1$ scarica la corrente nel transistor a diodo $M_3$. Per accendere lo specchio $M_4$ e iniziare a caricare $C_L$, la corrente deve prima scaricare la capacità parassita del nodo di Gate $C_{p2}$. Si introduce un ritardo:
  $$\tau_{\text{mirror}} \approx \frac{C_{p2}}{g_{m3}}$$
  Durante questo transitorio $M_4$ eroga meno corrente: **in salita l'amplificatore parte in ritardo e sale più lentamente ($SR^+ < SR^-$)**.

#### B) Asimmetria del Secondo Stadio di Potenza
Nel classico secondo stadio a source comune:
* **In salita ($SR^+$):** La corrente massima che carica l'uscita è rigidamente limitata dal generatore di corrente di carico PMOS ($I_{\text{max,salita}} = I_{\text{bias}}$).
* **In discesa ($SR^-$):** Il transistor NMOS di pilotaggio può essere sovrapilotato dal primo stadio fino a $V_{GS} \approx V_{DD}$, conducendo correnti impulsive transitorie enormi ($I_{\text{max,discesa}} \gg I_{\text{bias}}$).

#### C) Capacità Parassite Dipendenti dalla Tensione
Le capacità di svuotamento di giunzione $C_j(V) = \frac{C_{j0}}{\sqrt{1 + V_R/\phi_0}}$ e l'effetto Miller dinamico $C_{\text{eq}} = C_{gd}(1 + A_v(t))$ variano continuamente durante la traiettoria: il valore equivalente di capacità visto dal circuito durante la salita verso $V_{DD}$ è strutturalmente diverso da quello durante la discesa verso massa.

---

### 4. Il Paradosso dell'Accumulo di Carica: Perché l'Offset non va all'Infinito?

Se ad ogni ciclo di un disturbo a $1\,\text{GHz}$ l'amplificatore guadagna una minuscola quota di carica netta ($\Delta Q = (SR^+ - SR^-) \cdot \Delta t$), dopo miliardi di cicli al secondo **perché la tensione non sale fino a sbattere contro l'alimentazione positiva?**

L'accumulo si arresta per effetto di un **equilibrio dinamico** generato da tre fattori:
1. **La Retroazione Negativa dell'Anello Chiuso:**  
   L'Op-Amp opera tipicamente in configurazione retroazionata (es. a buffer unitario, con $V_{out}$ collegata all'ingresso invertente $V_{in-}$).  
   Non appena la tensione continua $V_{out}$ inizia a salire, la tensione differenziale d'ingresso diventa negativa:
   $$V_{id} = V_{in+} - V_{in-} < 0$$
   Questo errore DC negativo forza l'amplificatore a spingere con più forza in discesa, contrastando la carica parassita.
2. **La Corrente di Fuga Resistiva:**  
   All'uscita è presente una resistenza finita $R_{\text{out}}$. Man mano che la tensione $V_{out}$ sale, la corrente continua di scarica $I_{\text{fuga}} = V_{out}/R_{\text{out}}$ aumenta, finché non eguaglia esattamente la corrente media generata dall'asimmetria EMI ($\Delta I_{EMI}$):
   $$V_{\text{offset}} = \Delta I_{EMI} \cdot R_{\text{out}}$$
3. **L'Auto-limitazione dei Transistor:**  
   All'aumentare di $V_{out}$, le tensioni $V_{DS}$ dei transistor che caricano diminuiscono, riducendone la capacità di pompaggio.

> ⚖️ **Conclusione:** L'offset DC misurato sperimentalmente (es. $600\,\text{mV}$ nel $\mu\text{A741}$) è il **punto di equilibrio** tra la spinta di carica delle EMI e la reazione dell'anello chiuso.

---

### 5. La Soluzione Circuitale: Folded Cascode Fully-Differential

Per azzerare l'offset all'equilibrio occorre annullare la causa primaria: rendere $\Delta I_{EMI} \approx 0 \implies SR^+ = SR^-$.

Il circuito progettato (Prof.ssa Richelli, Slide 14-15) impiega:
1. **Primo Stadio:** Folded Cascode Fully-Differential a 4 piani, simmetrico al $100\%$.
2. **Secondo Stadio:** Buffer bilanciato in classe AB.
3. **Prestazioni misurate su silicio (AMS $0.8\,\mu\text{m}$):**
   * Guadagno: $93\,\text{dB}$
   * Banda $GBW$: $10\,\text{MHz}$
   * **Simmetria di Slew Rate:**
     $$SR(+) = 21.3\,\text{V}/\mu\text{s}, \qquad SR(-) = 21.6\,\text{V}/\mu\text{s} \quad (\text{scarto } \le 1.4\%)$$

---

### 6. Le Tecniche di Layout per Preservare la Simmetria

Affinché la simmetria teorica non venga distrutta dalle asimmetrie fisiche del silicio, il layout richiede tre regole ferree:

```
    A1  B1      D Da G1 S G1 Db D Db G2 S G2 Da G2 S G2 Db D
    B2  A2      ▲                                          ▲
  (Common       └───────────── Transistor DUMMY ───────────┘
  Centroid)
```

1. **Resistori a Centroide Comune Interlacciati (Slide 16):**  
   Le strisce di resistenza del partitore di polarizzazione ($R_1, R_2, R_3$) vengono alternate a pettine ($R_2 - R_1 - R_3 - R_1 - R_2 \dots$). Qualunque gradiente termico o di drogaggio lungo il chip viene mediato, mantenendo coincidenti i baricentri geometrici.
2. **Coppia Differenziale a Centroide Comune 2D (Slide 17):**  
   I transistor d'ingresso vengono divisi in semicelle disposte a scacchiera incrociata ($A_1-B_1 / B_2-A_2$), circondati da un **Guard Ring** metallico che drena a massa i disturbi viaggianti nel substrato.
3. **Transistor Interdigitati e Strutture DUMMY (Slide 18):**  
   I transistor larghi vengono divisi in dita parallele (*fingers*). Ai bordi estremi si inseriscono transistor fittizi (**Dummy**) non collegati: assorbono l'errore dell'attacco chimico (*over-etching*) sui bordi, garantendo che le dita attive interne abbiano bordi perfetti e identici.

---

### 7. Risultati Sperimentali: Confronto $\mu\text{A741}$ vs Op-Amp Immune (Slide 20)

Sottoponendo i circuiti a disturbi EMI da $100\,\text{kHz}$ a $10\,\text{GHz}$:
* **Disturbo sull'ingresso (@EMI-input):**  
  Il $\mu\text{A741}$ tradizionale subisce un'escursione di offset DC che supera i **$+600\,\text{mV}$**.  
  L'Op-Amp Folded Cascode simmetrico mantiene un offset **rigidamente piatto a $0\,\text{mV}$** su tutta la banda.
* **Disturbo sulle alimentazioni (@EMI-Vdd e @EMI-Gnd):**  
  Il $\mu\text{A741}$ manifesta picchi di offset tra $-500\,\text{mV}$ e $+400\,\text{mV}$.  
  L'Op-Amp simmetrico resta inchiodato a **$0\,\text{mV}$**.

---

*Pagine correlate:*
- [Amplificatori Fully-Differential e CMFB](./Amplificatori%20Fully-Differential%20e%20CMFB.md)
- [Amplificatori Rail-to-Rail](./Amplificatori%20Rail-to-Rail.md)
- [Folded Cascode e Recycling](./Folded%20Cascode%20e%20Recycling.md)
- [Layout e Tecniche di Progettazione dei MOS](./Layout%20e%20Tecniche%20di%20Progettazione%20dei%20MOS.md)
- [Matching e Variabilita nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [Capacità parassite nel MOSFET](./Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [Effetto Miller](./Effetto%20Miller.md)
- [Integrati protetti da interferenze](../Scaling%20e%20Limiti%20Fisici/Integrati%20protetti%20da%20interferenze.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
