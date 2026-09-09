# Logica Sequenziale e Temporizzazione

Nei circuiti digitali la logica si divide in due grandi famiglie:
* **Logica Combinatoria pura:** l'uscita al tempo $t$ dipende **esclusivamente dagli ingressi applicati al tempo $t$** ($Out = f(In)$). Non c'è memoria né concetto di passato (vedi [Circuiti Combinatori CMOS](../Circuiti%20Combinatori%20CMOS/Tecniche%20di%20Ottimizzazione%20per%20Porte%20Complesse%20Veloci.md)).
* **Logica Sequenziale:** l'uscita dipende dagli **ingressi attuali** e dalla **storia passata degli ingressi**, riassunta nello **Stato Corrente** (*Current State*).

```
                            MODELLO CANONICO DI CIRCUITO SEQUENZIALE
                            
                     Inputs ────────►┌──────────────┐────────► Outputs
                                     │    LOGICA    │
                                ┌───►│ COMBINATORIA │───┐
                                │    └──────────────┘   │
                  Current State │                       │ Next State
                                │      ┌─────────┐      │
                                └──────┤REGISTRI ├──────┘
                                       │ (D   Q) │
                                       └───▲─────┘
                                           │ CLK
```

$$\text{Next State} = g(\text{Inputs}, \text{Current State})$$
$$\text{Outputs} = f(\text{Inputs}, \text{Current State})$$

> [!NOTE]
> **I 2 meccanismi fisici di memoria:**
> 1. **Statica (Positive Feedback):** anelli di retroazione positiva bistabili (inverter incrociati che mantengono il dato indefinitamente finché c'è alimentazione).
> 2. **Dinamica (Charge-based):** carica immagazzinata temporaneamente sulla capacità parassita di un nodo (es. latch dinamici $C^2\text{MOS}$ o TSPC); richiede rinfresco o clock continuo per non perdere la carica per leakage.

---

### 1. Il Pipelining è Logica Sequenziale?

**Sì, assolutamente.**

Nel pipelining si spezza una lunga catena combinatoria interponendo registri di campionamento sincronizzati dal clock tra uno stadio e il successivo:

```
    In ──►[ REG ]──►[ Stadio 1 ]──►[ REG ]──►[ Stadio 2 ]──►[ REG ]──► Out
            ▲                         ▲                         ▲
           CLK                       CLK                       CLK
```

Anche se non c'è un anello di retroazione evidente (è una struttura puramente *feed-forward*):
1. Ci sono elementi di memoria regolati dal clock.
2. Il circuito possiede uno **stato interno distribuito**: in ogni ciclo di clock contiene contemporaneamente dati diversi a stadi di elaborazione diversi ($a_1, a_2, a_3 \dots$).
3. L'uscita al ciclo $k$ dipende dall'ingresso iniettato **$N$ cicli prima** ($N$ = profondità della pipeline o latenza).

---

### 2. Nomenclatura: Latch vs Register (Flip-Flop)

Nella letteratura tecnica (e in particolare nell'approccio di Jan Rabaey) si adotta una distinzione rigorosa per evitare confusioni:

* **Latch (Sensibile al livello - *Level Sensitive*):**
  * È **trasparente** per tutta la durata in cui il clock si trova a un determinato livello logico (alto o basso): il dato in ingresso attraversa il componente e l'uscita segue l'ingresso.
  * Diventa **opaco** (memorizza) nell'altra metà del periodo di clock.
* **Register / Flip-Flop (Sensibile al fronte - *Edge-Triggered*):**
  * Campiona il dato e aggiorna l'uscita **solo ed esclusivamente nell'istante del fronte di salita (o discesa)** del clock.
  * Per tutto il resto del tempo l'uscita resta rigidamente isolata dall'ingresso.

---

### 3. Latch-Based Design (Evitare le Corse Critiche)

Se si usasse un solo latch trasparente in un loop con logica combinatoria, durante la fase di trasparenza il segnale attraverserebbe la logica e **rientrerebbe nello stesso latch durante lo stesso colpo di clock** (*race-through* o corsa critica incontrollata).

Per impedirlo, si alternano due latch di tipo opposto pilotati dallo stesso clock $\phi$:
* **N-Latch (Negative Latch):** trasparente quando $\phi = 0$, opaco quando $\phi = 1$.
* **P-Latch (Positive Latch):** trasparente quando $\phi = 1$, opaco quando $\phi = 0$.

```
         ┌────────┐      ┌─────────┐      ┌────────┐      ┌─────────┐
 ───────►│ N-Latch│─────►│  Logic  │─────►│ P-Latch│─────►│  Logic  │───────► (feedback)
         └───┬────┘      └─────────┘      └───┬────┘      └─────────┘
             │                                │
    ϕ=0: Trasparente (scrive)        ϕ=0: Opaco (blocca e fa da barriera)
    ϕ=1: Opaco (congela)             ϕ=1: Trasparente (scrive)
```

* **Fase $\phi = 0$:** l'N-Latch è aperto e acquisisce il dato. Il P-Latch a valle è **chiuso (opaco)**, fungendo da barriera insormontabile. Il dato non può scappare oltre.
* **Fase $\phi = 1$:** l'N-Latch si **chiude** (congela il dato). Contemporaneamente il P-Latch si **apre**, lasciando scorrere il dato congelato verso il secondo blocco combinatorio.

Non esiste mai un percorso continuo aperto contemporaneamente: è il principio delle chiuse idrauliche e l'architettura base del **Master-Slave Register**.

---

### 4. Parametri di Temporizzazione (Timing Definitions)

In un registro edge-triggered (attivo su fronte di salita) ci sono 3 parametri temporali sacri:

```
            CLK  ─────────────┐
                              └───────────────────────────────
                               ◄──tsu──►◄──thold──►
              D  ═════════════╤═══════════════════╤═══════════
                              │    DATA STABLE    │
                 ─────────────┴───────────────────┴───────────
                              ◄───tc2q───►
              Q  ─────────────────────────════════════════════
                                          │    DATA STABLE    │
```

1. **$t_{su}$ (Setup Time):**  
   Tempo minimo in cui il dato di ingresso $D$ deve essere **già stabile PRIMA dell'arrivo del fronte di clock**.  
   *Se violato:* i nodi interni non completano la commutazione e il circuito cade in [Metastabilità](./Bistabilit%C3%A0,%20Metastabilit%C3%A0%20e%20Latch%20Statici.md).
2. **$t_{hold}$ (Hold Time):**  
   Tempo minimo in cui il dato $D$ deve **rimanere stabile DOPO il fronte di clock**.  
   *Se violato:* gli interruttori interni impiegano un tempo finito a isolare il nodo; il nuovo dato sovrascrive quello appena campionato.
3. **$t_{c2q}$ (o $t_{clk-Q}$, Clock-to-Q Delay):**  
   Ritardo di propagazione dal fronte di clock all'istante in cui l'uscita $Q$ diventa valida e stabile.

#### Differenza nei Latch: $t_{C2Q}$ vs $t_{D2Q}$
* **Nel Register:** l'uscita cambia solo su ordine del clock $\implies$ esiste solo **$t_{C2Q}$**.
* **Nel Latch:**
  * Se $D$ arriva prima che il latch si apra $\implies$ il ritardo parte dal clock (**$t_{C2Q}$**).
  * Se il latch è **già aperto/trasparente** e $D$ cambia adesso $\implies$ il dato attraversa il latch come una normale porta combinatoria: il ritardo si misura direttamente da $D$ a $Q$ (**$t_{D2Q}$**).

---

### 5. Massima Frequenza di Clock ($f_{\text{max}}$)

Consideriamo un anello sincrono formato da registro $\to$ rete combinatoria ($t_{p,comb}$) $\to$ registro:

```
                     ┌──────────────────┐
                     │ LOGICA COMBIN.   │
                     │    (tp,comb)     │
                     └────────▲─────────┘
                              │
                    ┌─────────┴─────────┐
                    │     REGISTRO      │
                    │ (tclk-Q , tsetup) │
                    └─────────▲─────────┘
                              │ CLK (periodo T)
```

Seguendo il percorso del dato tra due fronti di clock consecutivi:
1. Al primo fronte di clock, il dato esce dal registro impiegando **$t_{clk-Q}$**.
2. Il segnale si propaga lungo il cammino critico combinatorio peggiore impiegando **$t_{p,comb}$**.
3. Il nuovo dato deve arrivare all'ingresso del registro successivo con un anticipo di almeno **$t_{setup}$** rispetto al fronte successivo.

Il periodo di clock minimo $T_{\text{min}}$ è la somma dei tre tempi:
$$T \ge t_{clk-Q} + t_{p,comb} + t_{setup}$$

E la massima frequenza di clock teorica vale:
$$f_{\text{max}} = \frac{1}{T_{\text{min}}} = \frac{1}{t_{clk-Q} + t_{p,comb} + t_{setup}}$$

> [!TIP]
> **Come spingere la frequenza verso l'alto:**
> * Ridurre $t_{p,comb}$ spezzando la logica tramite **pipelining**.
> * Progettare celle di registro ultra-veloci con $t_{clk-Q}$ e $t_{setup}$ ridotti al minimo.

---

*Pagine correlate:*
- [Bistabilità, Metastabilità e Latch Statici](./Bistabilit%C3%A0,%20Metastabilit%C3%A0%20e%20Latch%20Statici.md)
- [Retroazione nell'Inverter e Ring Oscillator](../Famiglie%20Logiche/Retroazione%20nell%27Inverter%20e%20Ring%20Oscillator.md)
- [Pass-Transistor Logic e Level Restorer](../Circuiti%20Combinatori%20CMOS/Pass-Transistor%20Logic%20e%20Level%20Restorer.md)
- [Tecniche di Ottimizzazione per Porte Complesse Veloci](../Circuiti%20Combinatori%20CMOS/Tecniche%20di%20Ottimizzazione%20per%20Porte%20Complesse%20Veloci.md)
- [Effetto di Fan-In e Fan-Out sul Ritardo (Elmore)](../Circuiti%20Combinatori%20CMOS/Effetto%20di%20Fan-In%20e%20Fan-Out%20sul%20Ritardo%20(Elmore).md)
- [Soglia Logica e Margine di Rumore](../Famiglie%20Logiche/Soglia%20Logica%20e%20Margine%20di%20Rumore.md)
