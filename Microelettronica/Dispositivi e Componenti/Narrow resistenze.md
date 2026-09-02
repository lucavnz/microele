In microelettronica e nei modelli circuitale di simulazione (SPICE), il parametro **`NARROW`** rappresenta la correzione geometrica dovuta alla **sottoincisione laterale (*side etching*)** che avviene durante i processi di fabbricazione delle piste conduttrici e dei resistori integrati.

---

### 1. Che cos'è $W$ e cosa succede in camera bianca?

Spesso si è portati a pensare a $W$ come allo "spazio vuoto" scavato tra due piste; al contrario, nei resistori:
* **$W$ (Width)** è la **larghezza fisica del corpo conduttore** (la striscia di polisilicio o metallo in cui scorre la corrente utile).
* **$L$ (Length)** è la **lunghezza** della pista nella direzione del flusso di corrente.

#### Il processo di attacco chimico (*Etching*) passo per passo:

1. **Stesura dello strato conduttore:**  
   Si deposita uno strato piano e continuo di polisilicio o metallo su tutto il wafer:
   ```
   ┌─────────────────────────────────────────────────────────────┐
   │             STRATO CONTINUO DI POLISILICIO                  │
   └─────────────────────────────────────────────────────────────┘
   ═══════════════════════════════════════════════════════════════ Substrato/Ossido
   ```

2. **Applicazione della maschera (Fotoresist):**  
   Si applica una striscia protettiva di fotoresist larga esattamente quanto la quota disegnata a CAD ($W$):
   ```
                          Maschera Protettiva
                           (Larghezza = W)
                           ┌─────────────┐
                           │ FOTORESIST  │
   ┌───────────────────────┴─────────────┴───────────────────────┐
   │                    STRATO DI POLISILICIO                    │
   └─────────────────────────────────────────────────────────────┘
   ═══════════════════════════════════════════════════════════════
   ```

3. **Attacco chimico / plasma (*Etching*):**  
   L'agente chimico o il plasma rimuove il materiale non protetto. Poiché l'attacco chimico non è perfettamente anisotropo (non incide solo a $90^\circ$ verticale), **l'acido comincia a "mangiare" anche lateralmente sotto i bordi del fotoresist (*side etching* / *under-etching*)**:
   ```
                          ┌─────────────┐  <-- Maschera intatta (larga W)
           Attacco        │ FOTORESIST  │          Attacco
             ▼            │             │            ▼
    ░░░░░░░░             ◄┤             ├►            ░░░░░░░░
    (Rimosso              │ L'attacco   │             (Rimosso
      via!)               │ si infila   │               via!)
                          │ sotto!      │
                          └─────────────┘
   ═══════════════════════════════════════════════════════════════
   ```

4. **Rimozione del fotoresist (Risultato finale):**  
   Rimosso il fotoresist protettivo, il conduttore rimasto sul silicio è **più stretto** rispetto alla maschera originale disegnata a CAD:
   ```
                               Maschera CAD (W)
                           :                     :
                           :   ┌─────────────┐   :
                           :   │ PISTA REALE │   :
                           :   └─────────────┘   :
                           :◄-►:             :◄-►:
                            Side             Side
                           Etching          Etching
                          
                                W_effettivo
   ```

$$W_{\text{effettivo}} = W_{\text{disegnato}} - \text{NARROW}$$
$$L_{\text{effettivo}} = L_{\text{disegnato}} - \text{NARROW}$$

*(Nelle tecnologie CMOS planari, `NARROW` vale tipicamente attorno a $0.1\ \mu\text{m} = 100\text{ nm}$).*

---

### 2. Modello SPICE (Slide 26)

Nel simulatore SPICE, la resistenza del componente integrato non usa ciecamente le dimensioni nominali del layout ($W, L$), ma applica la correzione geometrica calcolando:

$$R = R_{SH} \cdot \frac{L - \text{NARROW}}{W - \text{NARROW}}$$

* **$R_{SH}$ (*Sheet Resistance* / Resistenza di strato $R_\square$):** espressa in $\Omega/\square$.
* **`NARROW`:** valore estratto e fornito dalla fonderia (es. `NARROW = 1e-7` m).
* Se il conduttore è più stretto ($W_{\text{eff}}$ più piccolo al denominatore), la sezione utile si riduce e la **resistenza reale è più ALTA di quella ideale nominale**.

---

### 3. Errore Sistematico vs Variabilità Intrinseca

È importante distinguere tra due concetti:

1. **`NARROW` è un Errore Deterministico / Sistematico:**  
   Non è una fluttuazione statistica casuale: è un offset fisso e prevedibile. La fonderia sa già a priori che quel tipo di attacco chimico "mangia" sistematicamente $0.1\ \mu\text{m}$ di bordo.
2. **La Variabilità Statistica Intrinseca (Tolleranze di Fabbricazione):**  
   Fluttuazioni da wafer a wafer (piccole variazioni di temperatura del forno, dosi di drogaggio, spessore dell'ossido) vengono invece modellate tramite:
   * **Simulazioni Monte Carlo:** dove parametri come $R_{SH}$ e `NARROW` variano secondo distribuzioni statistiche gaussiane.
   * **Process Corners:** simulazioni nei casi limite *Worst-Case* (*Slow-Slow*, *Fast-Fast*).

---

### 4. Regola di Progettazione: Piste Larghe vs Piste a Larghezza Minima

L'impatto di `NARROW` è tanto più devastante quanto più la pista è stretta:

* **Pista Larga ($W = 10\ \mu\text{m}$):**  
  Con $\text{NARROW} = 0.1\ \mu\text{m}$:
  $$W_{\text{eff}} = 10 - 0.1 = 9.9\ \mu\text{m} \implies \text{Errore dell' } 1\% \text{ (trascurabile)}$$
* **Pista a Larghezza Minima ($W = W_{\text{min}} = 0.5\ \mu\text{m}$):**  
  Con $\text{NARROW} = 0.1\ \mu\text{m}$:
  $$W_{\text{eff}} = 0.5 - 0.1 = 0.4\ \mu\text{m} \implies \text{Errore del } 20\%!$$
  La resistenza reale aumenta di ben il $25\%$ rispetto ai calcoli teorici.

> 💡 **Regola d'oro di Layout:** Nei circuiti analogici o di riferimento dove il valore della resistenza deve essere accurato e prevedibile, **non si usano mai resistori a larghezza minima ($W_{\text{min}}$)**, ma si sceglie un $W$ generoso per rendere trascurabile l'effetto della sottoincisione laterale.

---

*Pagine correlate:*
- [Matching e Variabilita nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [Resistore](./Resistore.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Induttore](./Induttore.md)
- [Condensatori](./Condensatori.md)
- [Wafer produzione](../Tecnologia%20e%20Fabbricazione/Wafer%20produzione.md)
