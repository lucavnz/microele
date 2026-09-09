# Bistabilità, Metastabilità e Latch Statici

La memoria statica nei circuiti digitali si basa sulla **retroazione positiva**: due inverter collegati in anello chiuso ($V_{o1} = V_{i2}$ e $V_{o2} = V_{i1}$).

```
                  ┌─────────[ Inv 1 ]────────┐
                  │                          ▼
             Nodo 1 (V1)                Nodo 2 (V2)
                  ▲                          │
                  └─────────[ Inv 2 ]────────┘
```

Se il nodo 1 si trova a $1$ ($V_{DD}$), l'inverter 1 forza il nodo 2 a $0$ ($GND$). L'inverter 2 riceve $0$ e rafforza il nodo 1 a $1$.  
Il loop si auto-alimenta e congela il bit indefinitamente finché il chip riceve alimentazione:
$$\mathbf{1} \xrightarrow{\text{Inv 1}} \mathbf{0} \xrightarrow{\text{Inv 2}} \mathbf{1} \quad \text{oppure} \quad \mathbf{0} \xrightarrow{\text{Inv 1}} \mathbf{1} \xrightarrow{\text{Inv 2}} \mathbf{0}$$

---

### 1. Le Curve VTC Incrociate e i 3 Punti di Lavoro

Sovrapponendo le caratteristiche statiche di trasferimento (VTC) dei due invertitori si ottengono **tre punti di equilibrio matematico**:

```
        Vo1, Vi2 ^
                 │  Punto A (Stato '1')
             VDD ┼───●═════════
                 │   │         \
                 │   │          \       Punto C (METASTABILE)
           VDD/2 ┼───┼───────────●
                 │   │            \
                 │   │             \    Punto B (Stato '0')
             GND ┼───┴──────────────●═════════
                 └───────────────────────────────► Vi1, Vo2
                    GND        VDD/2   VDD
```

1. **Punto A ($V_1 = V_{DD}$, $V_2 = 0\text{ V}$):** punto di equilibrio **stabile** (memorizza '1').
2. **Punto B ($V_1 = 0\text{ V}$, $V_2 = V_{DD}$):** punto di equilibrio **stabile** (memorizza '0').
3. **Punto C ($V_1 \approx V_2 \approx V_{DD}/2$):** punto di equilibrio **instabile (Metastabile)**.

---

### 2. Il Fenomeno della Metastabilità

Il punto $C$ corrisponde alla regione di transizione ad alto guadagno ($|A_v| > 1$).  
Fisicamente equivale a una pallina posizionata in perfetto equilibrio sulla punta di una collina (o un'altalena perfettamente orizzontale):

```
       Stato Stabile A                        Stato Stabile B
          ('1' o '0')                           ('0' o '1')
             \                                     /
              \       Punto C (METASTABILE)       /
               \               o                 /
                \             / \               /
                 \___________/   \_____________/
```

#### Perché il guadagno deve essere $> 1$ nella regione di transizione?
Affinché il circuito sia **rigenerativo**, la retroazione positiva deve amplificare qualsiasi minima variazione $d$:
$$\Delta V_{\text{next}} = |A_v| \cdot d > d$$
La divergenza rispetto al punto di equilibrio segue una legge esponenziale nel tempo:
$$\Delta V(t) = \Delta V_0 \cdot e^{+\frac{t}{\tau}}$$
dove $\Delta V_0$ è lo scostamento iniziale dal punto di simmetria e $\tau$ è la costante di tempo dell'inverter.

#### Cosa succede se il dato finisce nella regione metastabile?
Se il segnale di ingresso al flip-flop varia troppo a ridosso del fronte di clock (violando il tempo di setup $t_{su}$ o di hold $t_{hold}$ visti in [Logica Sequenziale e Temporizzazione](./Logica%20Sequenziale%20e%20Temporizzazione.md)), il circuito campiona una tensione intermedia che cade proprio nel punto $C$. Le conseguenze sono gravissime:

1. **Perdita e corruzione del dato (indeterminazione logica):**  
   Non essendoci alcun margine di rumore a favore di $0$ o $1$, sarà un disturbo termico microscopico casuale a far collassare il circuito verso $A$ o verso $B$. L'esito finale è puramente stocastico (testa o croce).
2. **Tempo di risoluzione indefinito:**  
   Se $\Delta V_0 \approx 0$, il tempo necessario al circuito per decidere ed evadere verso $A$ o $B$ può diventare arbitrariamente lungo, superando di gran lunga il periodo di clock nominale.
3. **Corrente di cortocircuito (*Crowbar Current*):**  
   Con la tensione interna ferma a circa $V_{DD}/2$, sia i transistor nMOS che pMOS delle porte a valle restano simultaneamente accesi, provocando una violenta corrente parassita continua da $V_{DD}$ a massa (vedi [Inverter CMOS e Regioni di Funzionamento](../Famiglie%20Logiche/Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)).
4. **Glitch e asincronia a cascata:**  
   Porte logiche a valle possono interpretare la tensione intermedia in modo discordante (una legge `0`, l'altra `1`), mandando in crash l'intero sistema.

---

### 3. Come Scrivere in un Latch Statico

Dato che i due inverter difendono lo stato memorizzato con la retroazione positiva, non si può forzare brutalmente un nuovo dato senza provocare un cortocircuito logico. Esistono due filosofie circuitali:

```
    METODO 1: Tagliare l'anello (MUX)         METODO 2: Forzare per sovrapotenza
    
           ┌───[ Switch ]───┐                           ┌───[ Inverter 2 ]───┐
           │   (aperto in   │                           │                    │
    D ──[Switch]──►[Inv 1]──┴──► Q               D ──[Pass]──►[ Inverter 1 ]─┴──► Q
       (chiuso in                                    (W/L grande:
        scrittura)                                    vince su Inv 2)
```

1. **Tagliare l'anello con interruttori (Mux-Based Latch):**  
   Durante la fase di scrittura si apre l'anello di retroazione e si lascia entrare il dato $D$. Durante la memorizzazione si chiude l'anello e si scollega l'ingresso.
2. **Forzare lo stato (*Overpowering*):**  
   L'anello rimane sempre chiuso. Il nuovo dato viene applicato tramite un transistor passante con una corrente sufficientemente forte da sconfiggere il transistor di pull-up/pull-down dell'inverter di retroazione (principio cardine della **cella SRAM a 6 transistor**).

---

### 4. Mux-Based Latch: L'Astrazione e le Equazioni

Il latch con anello interrotto è descritto dall'equazione di un **Multiplexer 2-a-1**:
* **Negative Latch (trasparente con $\text{CLK} = 0$, memorizza con $\text{CLK} = 1$):**
  $$Q = \overline{\text{CLK}} \cdot D + \text{CLK} \cdot Q$$
* **Positive Latch (trasparente con $\text{CLK} = 1$, memorizza con $\text{CLK} = 0$):**
  $$Q = \text{CLK} \cdot D + \overline{\text{CLK}} \cdot Q$$

---

### 5. Il Transmission Gate (TG): La Chiave del Full CMOS Static

Per implementare gli interruttori del multiplexer a livello di silicio si impiega il **Transmission Gate (TG)**: un nMOS e un pMOS posti in parallelo.

```
                  ┌────┤ pMOS ├───┐   (Gate pilotato da CLK_bar)
       In o───────┤               ├───────o Out
                  └────┤ nMOS ├───┘   (Gate pilotato da CLK)
```

#### Come funziona fisicamente: Non si alternano nel tempo, ma sulla tensione!
I gate sono polarizzati per condurre **insieme** quando l'interruttore è abilitato ($V_{G,n} = V_{DD}$, $V_{G,p} = 0\text{ V}$).  
La "staffetta" avviene lungo l'escursione di tensione del segnale che deve passare (vedi anche [Pass-Transistor Logic e Level Restorer](../Circuiti%20Combinatori%20CMOS/Pass-Transistor%20Logic%20e%20Level%20Restorer.md)):

* **L'nMOS è uno "Strong 0" ma "Weak 1":**  
  Passa benissimo la massa ($0\text{ V}$), ma verso l'alto si spegne da solo appena la tensione sale a $V_{DD} - V_{Tn}$.
* **Il pMOS è uno "Strong 1" ma "Weak 0":**  
  Passa benissimo la tensione piena ($V_{DD}$), ma verso il basso si spegne da solo appena la tensione scende sotto $|V_{Tp}|$.

```
    Resistenza ^
               │      / \          <-- Rn (sale alle alte tensioni)
               │     /   \
               │    /     \        <-- Rp (sale alle basse tensioni)
               │   ═════════       <-- Req = Rn // Rp (QUASI COSTANTE!)
               └───────────────────► Tensione V_out
                  0V     VDD/2   VDD
```

* **In parallelo si completano:** sulle tensioni basse lavora l'nMOS, sulle tensioni alte lavora il pMOS, a metà tensione conducono entrambi a piena corrente.
* La resistenza equivalente $R_{eq} = R_n \parallel R_p$ è **bassa e uniforme** lungo l'intero intervallo $[0, V_{DD}]$.
* Il segnale trasmesso è **pienamente rail-to-rail** senza cadute di soglia, garantendo massimi margini di rumore e zero consumo statico.

---

### 6. Variante Compatta a Soli nMOS (Pseudo-Static)

Per risparmiare silicio (dimezzando i transistor degli interruttori) si possono usare singoli pass-transistor nMOS:

```
            CLK                      /CLK
             │                        │
      D ───┤nMOS├───┬───[Inv 1]───┬───┤nMOS├───┐
                    │             │            │
                    │             └───[Inv 2]──┘
                    │                   (Feedback)
                    └──────────► Q
```

Questa struttura impone due compromessi critici:
1. **Perdita di soglia ("Pseudo-Static"):** il dato $1$ trasferito all'ingresso dell'inverter vale al massimo $V_{DD} - V_{Tn}$, riducendo il margine di rumore.
2. **Clock rigorosamente non sovrapposti (*Non-overlapping clocks*):**  
   Tra la disattivazione di $\text{CLK}$ e l'attivazione di $\overline{\text{CLK}}$ deve esistere una **zona morta** in cui entrambi i clock valgono $0$. Se entrambi gli nMOS conducessero simultaneamente anche solo per una frazione di picosecondo, il dato d'ingresso e quello di retroazione entrerebbero in collisione distruggendo il valore memorizzato.

---

*Pagine correlate:*
- [Logica Sequenziale e Temporizzazione](./Logica%20Sequenziale%20e%20Temporizzazione.md)
- [Pass-Transistor Logic e Level Restorer](../Circuiti%20Combinatori%20CMOS/Pass-Transistor%20Logic%20e%20Level%20Restorer.md)
- [Inverter CMOS e Regioni di Funzionamento](../Famiglie%20Logiche/Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)
- [Caratteristica di Trasferimento e Rigenerazione](../Famiglie%20Logiche/Caratteristica%20di%20Trasferimento%20e%20Rigenerazione.md)
- [Retroazione nell'Inverter e Ring Oscillator](../Famiglie%20Logiche/Retroazione%20nell%27Inverter%20e%20Ring%20Oscillator.md)
- [Soglia Logica e Margine di Rumore](../Famiglie%20Logiche/Soglia%20Logica%20e%20Margine%20di%20Rumore.md)
