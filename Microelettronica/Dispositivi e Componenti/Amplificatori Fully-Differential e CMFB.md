# Amplificatori Fully-Differential e CMFB (Common-Mode Feedback)

Un amplificatore **Fully-Differential** (completamente differenziale) elabora un segnale differenziale sia all'ingresso che all'uscita: possiede **2 ingressi** ($V_{in+}, V_{in-}$) e **2 uscite** ($V_{out+}, V_{out-}$).

---

### 1. Definizione e Vantaggi del Fully-Differential

In presenza di un segnale differenziale puro in ingresso, le due uscite presentano **stesso guadagno in modulo ma sfasamento di $180^\circ$**:
$$v_{out+} = + \frac{A_d}{2} v_{in,\text{diff}}, \qquad v_{out-} = - \frac{A_d}{2} v_{in,\text{diff}}$$

Il segnale differenziale utile prelevato è la differenza tra i due nodi:
$$V_{out,\text{diff}} = V_{out+} - V_{out-}$$
mentre il loro livello medio rappresenta la **tensione di modo comune di uscita**:
$$V_{out,CM} = \frac{V_{out+} + V_{out-}}{2}$$

```
                  ┌───────────────────┐
         Vin+ ───►│                   ├───► Vout+
                  │ Fully-Differential│
         Vin- ───►│      Op-Amp       ├───► Vout-
                  └─────────┬─────────┘
                            │
                       [Anello CMFB]
```

#### I tre vantaggi chiave:
1. **Raddoppio della dinamica di uscita (Output Swing):**  
   Se ciascuna uscita può oscillare entro un intervallo limitato dall'alimentazione ($V_{DD} - V_{SS}$), la tensione differenziale $V_{out+} - V_{out-}$ raggiunge un'escursione picco-picco **doppia** ($2 \times (V_{DD} - V_{SS})$ ideale). Questo è essenziale nei circuiti integrati *low-power* alimentati a basse tensioni ($1.2\,\text{V} \div 1.8\,\text{V}$).
2. **Reiezione intrinseca dei disturbi di modo comune:**  
   Il rumore presente sulle linee di alimentazione ($V_{DD}$), sul substrato e le interferenze esterne (EMI) colpiscono entrambi i rami simmetrici nello stesso modo: sottraendo le due uscite, il disturbo si elide matematicamente.
3. **Cancellazione delle distorsioni armoniche pari:**  
   Le non linearità quadratiche del secondo ordine dei MOS generano armoniche con la stessa polarità su entrambe le uscite, che si cancellano nella differenza differenziale.

---

### 2. Il "Dilemma del Modo Comune": Perché il CMFB è Obbligatorio?

In un amplificatore classico *single-ended*, uno dei rami interni ha un carico collegato a diodo ($V_{GS} = V_{DS}$): questo crea un nodo a bassa impedenza ($1/g_m$) che ancora rigidamente la tensione DC di polarizzazione.

In un amplificatore completamente differenziale:
* **Entrambe le uscite sono nodi ad altissima impedenza ($r_o$ o $g_m r_o^2$):** ciascuna uscita è sospesa tra il Drain di un generatore di corrente PMOS in alto ($I_{\text{top}}$) e il Drain di un generatore di corrente NMOS in basso ($I_{\text{bottom}}$).
* **Assenza di autocorrezione:** Nella realtà dei chip, per via delle micro-tolleranze di processo (*mismatch*) e gradienti termici, le due correnti non sono mai identiche:
  $$\Delta I = I_{\text{top}} - I_{\text{bottom}} \neq 0$$
* **Deriva e saturazione dei nodi di uscita:**  
  Non avendo una via di fuga a bassa impedenza, la minima discrepanza $\Delta I$ carica o scarica le capacità parassite dei nodi di uscita:
  $$\frac{dV_{out,CM}}{dt} = \frac{\Delta I}{C_{\text{nodo}}}$$
  Le tensioni $V_{out+}$ e $V_{out-}$ scivolano rapidamente fino a **sbattere contro $V_{DD}$ o contro massa**.
* **Morte dell'amplificatore:** Una volta che l'uscita tocca le rotaie, i transistor escono dalla regione di saturazione ed entrano in **zona lineare/triodo** (o si interdicono), annullando la resistenza differenziale $r_o$ e azzerando il guadagno.

> ⚠️ **Punto fondamentale:** La normale retroazione differenziale esterna applicata all'amplificatore (es. resistori tra $V_{out}$ e $V_{in}$) controlla solo la tensione differenziale $V_{out+} - V_{out-}$, ma **non ha alcun controllo sul livello medio $V_{out,CM}$**.  
> Un circuito **CMFB (Common-Mode Feedback)** dedicato è **strettamente obbligatorio** per rilevare $V_{out,CM}$, confrontarlo con un riferimento fisso (tipicamente $V_{DD}/2$) e modulare le correnti di polarizzazione per bloccarlo al centro della dinamica.

---

### 3. Implementazioni del Circuito CMFB

Il circuito CMFB esegue tre operazioni:
1. **Misura** del modo comune di uscita $V_{out,CM} = (V_{out1} + V_{out2})/2$ senza caricare o attenuare il segnale differenziale.
2. **Confronto** con una tensione di riferimento $V_{\text{ref},CM}$ (es. $V_{DD}/2$).
3. **Attuazione:** Modulazione della corrente dei generatori superiori (PMOS) o inferiori (NMOS).

---

#### A) Esempio 1: CMFB Passivo con Transistor in Zona Lineare (Triodo)

Nei rami inferiori dell'amplificatore (sotto i cascode), si inseriscono due transistor $M_{12}$ e $M_{13}$ polarizzati intenzionalmente in **zona lineare/triodo**, con i Gate collegati direttamente a $OUT_1$ e $OUT_2$:

```
        OUT1 ──── Gate M12 ┐
                           ├─── Nodo P (Sorgenti dei generatori NMOS)
        OUT2 ──── Gate M13 ┘
              (in triodo)
```

1. Ciascun transistor in zona triodo agisce come una resistenza controllata in tensione:
   $$R \approx \frac{1}{k' \frac{W}{L} (V_{GS} - V_{th})}$$
2. Essendo in parallelo, la conduttanza equivalente totale è la somma delle conduttanze:
   $$G_{\text{eq}} = G_{12} + G_{13} \propto (V_{OUT1} - V_{th}) + (V_{OUT2} - V_{th}) = 2(V_{OUT,CM} - V_{th})$$
   **La componente differenziale si elide!** La resistenza equivalente $R_{\text{eq}}$ dipende solo ed esclusivamente dal modo comune di uscita $V_{OUT,CM}$.
3. **Anello di retroazione negativa:**
   * Se $V_{OUT,CM}$ sale per un disturbo $\implies V_{GS12,13}$ aumenta $\implies R_{\text{eq}}$ diminuisce.
   * Il potenziale del nodo $P$ scende verso massa $\implies$ aumenta la caduta $V_{GS}$ dei transistor NMOS soprastanti.
   * I rami NMOS scaricano una **corrente maggiore verso massa**, sottraendo carica ai nodi di uscita.
   * Il livello $V_{OUT,CM}$ **scende**, contrastando l'aumento iniziale e chiudendo l'anello di retroazione.

---

#### B) Esempio 2: CMFB Attivo con Amplificatore d'Errore

I nodi d'uscita $OUT_1$ e $OUT_2$ vengono collegati ai Gate di una coppia differenziale di misura ausiliaria (*sensing pair*):

```
       OUT1 ──── Gate M_sense1 ┐
                               ├─── [Generatore di corrente IB]
       OUT2 ──── Gate M_sense2 ┘
```

1. **Rilevamento:** Se $V_{CM}$ delle uscite aumenta, la coppia di sensing conduce più corrente complessiva ($\uparrow I_B$).
2. **Attuazione sullo specchio:** Questa corrente viene specchiata verso i Gate dei generatori di corrente PMOS superiori della colonna cascode.
3. Facendo salire la tensione di Gate dei PMOS, **la corrente erogata dall'alto verso le uscite si riduce**.
4. Essendoci meno corrente che carica i nodi di uscita, $V_{OUT,CM}$ scende fino al valore desiderato.

---

### 4. L'Uso del Fully-Differential come "Single-Ended" per la Massima Simmetria

Un utilizzo architetturale cruciale evidenziato nella progettazione di precisione è il seguente:
> *È possibile utilizzare un amplificatore Fully-Differential prelevando una sola uscita e lasciando l'altra bilanciata (connessa a un carico/condensatore parassita equivalente).*

Sebbene comporti un maggiore consumo di area e corrente rispetto a un singolo stadio Miller, offre un vantaggio fondamentale: **la perfetta simmetria fisica interna dei rami**.  
Negli amplificatori tradizionali a singola uscita, l'asimmetria interna sbilancia lo Slew Rate ($SR^+ \neq SR^-$), rendendo il circuito vulnerabile alle interferenze RF ad alta frequenza. La simmetria speculare del Fully-Differential elimina alla radice questa suscettibilità.

👉 Approfondimento: [Immunità alle EMI e Slew Rate Asimmetrico](./Immunit%C3%A0%20alle%20EMI%20e%20Slew%20Rate%20Asimmetrico.md)

---

*Pagine correlate:*
- [Amplificatori Rail-to-Rail](./Amplificatori%20Rail-to-Rail.md)
- [Folded Cascode e Recycling](./Folded%20Cascode%20e%20Recycling.md)
- [Coppia Differenziale e Cascode Telescopico](./Coppia%20Differenziale%20e%20Cascode%20Telescopico.md)
- [Immunità alle EMI e Slew Rate Asimmetrico](./Immunit%C3%A0%20alle%20EMI%20e%20Slew%20Rate%20Asimmetrico.md)
- [Matching e Variabilita nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [Layout e Tecniche di Progettazione dei MOS](./Layout%20e%20Tecniche%20di%20Progettazione%20dei%20MOS.md)
- [Overdrive e Regioni di Inversione](./Overdrive%20e%20Regioni%20di%20Inversione.md)
