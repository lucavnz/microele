# Amplificatori Operazionali Rail-to-Rail

Negli amplificatori operazionali a basso consumo e a bassa tensione di alimentazione ($V_{DD} \le 1.8\,\text{V} \div 3\,\text{V}$), uno stadio differenziale classico perde gran parte della sua dinamica. Gli **amplificatori rail-to-rail** nascono per garantire che sia l'intervallo di modo comune in ingresso (**ICMR**, *Input Common-Mode Range*) sia la dinamica di uscita (**output voltage swing**) possano spaziare liberamente dall'alimentazione negativa $V_{SS}$ a quella positiva $V_{DD}$.

---

### 1. Perché una Coppia Differenziale Classica NON è Rail-to-Rail?

In uno stadio differenziale standard a singolo tipo di transistor, il circuito si spegne se la tensione di modo comune d'ingresso $V_{in,CM} = \frac{V_{in1} + V_{in2}}{2}$ si avvicina a una delle due rotaie (*rails*):

```
       COPPIA NMOS                           COPPIA PMOS
          Vdd                                   Vdd
           │                                     │
      [Carichi]                                [Itail] (PMOS tail)
        ┌──┴──┐                               ┌──┴──┐
        │     │                               │     │
  Vin1 ─┤M1 M2├─ Vin2                   Vin1 ─┤M1 M2├─ Vin2
        └──┬──┘                               └──┬──┘
           │                                     │
        [Itail] (NMOS tail)                  [Carichi]
           │                                     │
          Vss                                   Vss
```

#### A) Coppia differenziale NMOS: si spegne vicino a $V_{SS}$
Affinché il generatore di corrente di coda (*tail*) e i transistor d'ingresso $M_1, M_2$ siano accesi e in saturazione, serve:
$$V_{in,CM} \ge V_{SS} + V_{ov,\text{tail}} + V_{GS,NMOS} = V_{SS} + V_{ov,\text{tail}} + V_{th,n} + V_{ov,n}$$
Con valori tipici ($V_{th,n} \approx 0.7\,\text{V}$, $V_{ov} \approx 0.2\,\text{V}$):
$$V_{in,CM,\text{min}} \approx V_{SS} + 1.1\,\text{V}$$
Se $V_{in,CM}$ scende sotto $1.1\,\text{V}$, la coppia NMOS **si spegne completamente**. Funziona solo per segnali alti, spostati verso $V_{DD}$.

#### B) Coppia differenziale PMOS: si spegne vicino a $V_{DD}$
Per la coppia PMOS vale il vincolo duale verso l'alto:
$$V_{in,CM} \le V_{DD} - |V_{ov,\text{tail}}| - |V_{GS,PMOS}| = V_{DD} - |V_{ov,\text{tail}}| - |V_{th,p}| - |V_{ov,p}| \approx V_{DD} - 1.1\,\text{V}$$
Se $V_{in,CM}$ sale sopra $V_{DD} - 1.1\,\text{V}$, la coppia PMOS **si spegne completamente**. Funziona solo per segnali bassi, spostati verso $V_{SS}$.

#### Dove nasce il problema critico?
Se alimentiamo a $V_{DD} = 1.8\,\text{V}$, nessuna delle due coppie da sola copre l'intervallo da $0$ a $1.8\,\text{V}$.  
Questo è fatale nella configurazione a **inseguitore di tensione (buffer a guadagno unitario)**:
$$V_{out} = V_{in} \implies V_{in,CM} = V_{in}$$
Se il segnale analogico da inseguire deve oscillare su tutto il range da $V_{SS}$ a $V_{DD}$, l'ingresso dell'operazionale deve necessariamente essere rail-to-rail.

---

### 2. L'Idea Base: La Doppia Coppia Differenziale Complementare

Si mettono **in parallelo** una coppia NMOS e una coppia PMOS, collegando entrambi gli ingressi differenziali ($V_{in1}, V_{in2}$) ai Gate di entrambe le coppie:

```
                      Vdd
                       │
                     [Ip] (Tail PMOS)
                    ┌──┴──┐
                    │     │
              ┌─────┤PM1a PM1├─────┐
              │     └──┬──┘        │
              │        │           │
   Vin1 ──────┴────────┼───────────┼───────┐
                       │           │       │
              ┌────────┼───────────┼───────┤
              │        │           │       │
              │     ┌──┴──┐        │       │
              └─────┤NM2a NM2├─────┘       │
                    └──┬──┘                │
                       │                   │
   Vin2 ───────────────┴───────────────────┘
                       │
                     [In] (Tail NMOS)
                       │
                      Vss
```

Al variare del modo comune $V_{CM}$ lungo l'asse $V_{SS} \to V_{DD}$:
1. **$V_{CM}$ vicino a $V_{SS}$:** NMOS spenti ($I_n = 0$), **PMOS accesi**.
2. **$V_{CM}$ a centro scala:** **Entrambe le coppie sono accese**.
3. **$V_{CM}$ vicino a $V_{DD}$:** PMOS spenti ($I_p = 0$), **NMOS accesi**.

Almeno una coppia conduce sempre: il circuito non si spegne mai su tutto l'intervallo $V_{SS} \to V_{DD}$.

---

### 3. Il Problema della Transconduttanza ($g_m$) Variabile

L'accoppiamento in parallelo crea un serio effetto collaterale:
* Agli estremi ($V_{CM}$ vicino a $V_{SS}$ o $V_{DD}$), lavora una sola coppia:
  $$g_{m,\text{tot}} \approx g_m$$
* A centro scala, lavorano contemporaneamente entrambe le coppie:
  $$g_{m,\text{tot}} = g_{m,n} + g_{m,p} \approx \mathbf{2 g_m}$$

#### Perché il raddoppio di $g_m$ è un problema grave?
1. **Spostamento della Banda a Guadagno Unitario ($GBW$):**  
   $$GBW = \frac{g_{m,\text{tot}}}{2\pi C_c}$$
   Al centro dell'intervallo la frequenza di taglio a $0\,\text{dB}$ raddoppia.
2. **Crollo del Margine di Fase e Rischio Instabilità:**  
   Il secondo polo ad alta frequenza ($p_2$) è fissato dai nodi interni. Spostare a destra la frequenza di taglio a $0\,\text{dB}$ la avvicina pericolosamente a $p_2$: **il margine di fase crolla e l'amplificatore rischia di oscillare o produrre forte ringing transitorio**.  
   Se invece si sovradimensiona la capacità di compensazione $C_c$ per renderlo stabile a centro scala ($2g_m$), agli estremi (dove $g_m$ si dimezza) l'amplificatore diventa lentissimo.
3. **Distorsione Armonica da Non-Linearità:**  
   Il guadagno d'anello varia punto per punto lungo la dinamica dell'onda sinusoidale, introducendo distorsione non lineare e intermodulazione sul segnale.

---

### 4. La Soluzione: "Monitor Circuit" + "$g_m$ Equalizer"

Per rendere costante la transconduttanza complessiva si inserisce un anello di controllo della polarizzazione:
* **Monitor Circuit:** Rileva quanta corrente sta conducendo la coppia PMOS ($I_p(V_{CM})$). Se il modo comune sale verso $V_{DD}$ e la coppia PMOS inizia a spegnersi, il monitor registra il calo di $I_p$.
* **$g_m$ Equalizer:** Elabora questa informazione e pilota lo specchio di corrente della coppia NMOS, modulando $I_n(V_{CM})$ in senso opposto.

```
          Ip, In, Ip+In
      120 µA ┌─────────────────────────────────────────┐  Ip + In (costante!)
             │═════════════════════════════════════════│
       80 µA │        Ip (scende)                      │
             │ \                                     / │  In (sale)
       40 µA │  \                                   /  │
             │   \                                 /   │
        0 µA └───┴──────────┴──────────┴──────────┴────┘
                0 V        1.0 V      2.0 V      3.0 V    Vcm
```

* **In debole inversione:** Poiché $g_m = \frac{I_D}{n V_T} \propto I_D$, basta mantenere **costante la somma delle correnti**:
  $$I_n + I_p \approx I_{\text{ref}} = \text{costante}$$
* **In forte inversione:** Poiché $g_m = \sqrt{2 \mu C_{ox} (W/L) I_D} \propto \sqrt{I_D}$, il circuito equalizzatore mantiene costante la somma delle radici ($\sqrt{I_n} + \sqrt{I_p} = \text{costante}$), tipicamente quadruplicando la corrente della coppia attiva quando l'altra è spenta.

---

### 5. Topologie Circuitali di Implementazione

#### A) Esempio 1: Amplificatore Miller con uscita Push-Pull
La doppia coppia differenziale d'ingresso pilota due specchi di corrente complementari:
* La coppia NMOS ($NM_0, NM_1$) pilota uno specchio PMOS superiore ($PM_2, PM_3$).
* La coppia PMOS ($PM_0, PM_1$) pilota uno specchio NMOS inferiore ($NM_2, NM_3$).
* I nodi d'uscita dei due specchi pilotano i Gate di uno stadio finale **Push-Pull Inverter ($PM_4 + NM_4$)**.

> 💡 **Perché l'uscita Push-Pull?** Permette di ottenere un'escursione d'uscita fino a pochi millivolt da $V_{DD}$ e da $V_{SS}$ (attraverso la caduta $V_{DS,\text{sat}}$ dei transistor finali), realizzando un amplificatore **Rail-to-Rail sia in ingresso che in uscita**.

#### B) Esempio 2: Folded Cascode (L'ambiente ideale per il Rail-to-Rail)
Il [Folded Cascode e Recycling](./Folded%20Cascode%20e%20Recycling.md) è la topologia ottimale per accogliere la doppia coppia:
1. **Nodi di Folding a bassa impedenza ($1/g_m$):** I Gate dei cascode sono a potenziale fisso; le loro sorgenti presentano una resistenza d'ingresso piccolissima ($R \approx 1/g_m$).
2. **Iniezione diretta delle correnti:**
   * I Drain della coppia NMOS d'ingresso tirano corrente direttamente dai nodi di sorgente del cascode PMOS (in alto).
   * I Drain della coppia PMOS d'ingresso iniettano corrente direttamente nei nodi di sorgente del cascode NMOS (in basso).
3. **Nessun polo lento:** Essendo l'impedenza dei nodi di folding minima, le capacità parassite non introducono poli a bassa frequenza, preservando banda e margine di fase.
4. **Somma algebrica naturale:** Entrambe le correnti di segnale confluiscono direttamente sull'unico nodo di uscita ad altissima impedenza $V_o$.

#### C) Esempio 3: Folded Cascode Completamente Differenziale
La struttura Folded Cascode viene estesa a 4 piani (2 PMOS e 2 NMOS) con uscite differenziali bilanciate ($V_{out+}, V_{out-}$), richiedendo il controllo del modo comune di uscita tramite [Amplificatori Fully-Differential e CMFB](./Amplificatori%20Fully-Differential%20e%20CMFB.md).

---

*Pagine correlate:*
- [Folded Cascode e Recycling](./Folded%20Cascode%20e%20Recycling.md)
- [Coppia Differenziale e Cascode Telescopico](./Coppia%20Differenziale%20e%20Cascode%20Telescopico.md)
- [Amplificatori Fully-Differential e CMFB](./Amplificatori%20Fully-Differential%20e%20CMFB.md)
- [Immunità alle EMI e Slew Rate Asimmetrico](./Immunit%C3%A0%20alle%20EMI%20e%20Slew%20Rate%20Asimmetrico.md)
- [Layout e Tecniche di Progettazione dei MOS](./Layout%20e%20Tecniche%20di%20Progettazione%20dei%20MOS.md)
- [Matching e Variabilita nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [Capacità parassite nel MOSFET](./Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [Overdrive e Regioni di Inversione](./Overdrive%20e%20Regioni%20di%20Inversione.md)
