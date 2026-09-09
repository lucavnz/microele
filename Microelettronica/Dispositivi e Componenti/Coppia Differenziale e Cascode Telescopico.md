# Coppia Differenziale e Cascode Telescopico MOS

La **coppia differenziale** è il blocco fondamentale dell'amplificazione analogica integrata. Abbinata alla tecnica del **cascode telescopico**, consente di massimizzare il guadagno in continua mantenendo una topologia a singolo stadio.

---

### 1. Coppia Differenziale MOS e Dipendenza Termica del Guadagno

Consideriamo una coppia differenziale classica polarizzata da un generatore di coda a corrente costante $I_{SS}$ (*tail current*):

```
          VDD               VDD
           │                 │
          [RD]              [RD]      (oppure carichi attivi a MOS)
           │                 │
           ├─── Vo1   Vo2 ───┤
           │                 │
         [M1]               [M2]      (Coppia di ingresso)
      VI1 ─┤                 ├─ VI2
           └───┬─────────┬───┘
               │  nodo S │
              [M_tail] (ISS)
                 ┴ GND
```

In condizione di riposo e simmetria, la corrente si divide equamente tra i due rami:
$$I_{D1} = I_{D2} = \frac{I_{SS}}{2}$$

Il guadagno di tensione differenziale vale:
$$|A_{vd}| = g_{m1,2} \cdot R_{out}$$

#### Perché all'aumentare della temperatura il guadagno SCENDE?
1. **La corrente $I_D$ è vincolata:** Essendo imposta dal generatore di coda $I_{SS}$, la corrente di bias di ciascun ramo non varia con la temperatura ($I_D = \text{cost}$).
2. **Crollo della mobilità ($\mu$):** All'aumentare di $T$, l'aumento delle vibrazioni reticolari (*lattice scattering*) riduce la mobilità dei portatori:
   $$\mu(T) \propto T^{-m} \quad (m \approx 1.5 \div 2.0)$$
3. **Calo della transconduttanza $g_m$:**
   $$g_m = \sqrt{2 \mu(T) C_{ox} \frac{W}{L} I_D} \propto \sqrt{\mu(T)} \propto T^{-0.75}$$
   Poiché $\mu$ crolla, **$g_m$ scende**.
4. **Effetto su $R_{out}$ e sul guadagno:**
   * **Con carico passivo ($R_D$):** $|A_{vd}| = g_m R_D \propto T^{-0.75} \implies$ **il guadagno scende**.
   * **Con carico attivo MOS ($R_{out} \approx r_{on} \parallel r_{op}$):** Poiché [la resistenza di uscita](../Effetti%20di%20Canale%20Corto/Crollo%20di%20ro.md) vale $r_o \approx \frac{1}{\lambda I_D}$ e la corrente $I_D$ è fissa, $r_o$ varia poco. Di conseguenza:
     $$|A_{vd}| \approx g_m (r_{on} \parallel r_{op}) \propto g_m(T) \implies \mathbf{|A_{vd}| \text{ SCENDE con la temperatura}}$$

*(Nota per il BJT: $g_m = \frac{I_C}{V_T} = \frac{q I_C}{k T} \propto \frac{1}{T}$. Poiché la tensione termica $V_T$ cresce con $T$, il guadagno crolla ancora più rapidamente in modo inversamente proporzionale alla temperatura).*

---

### 2. Coppia Cascode Telescopica MOS: Guadagno in Continua

Nelle tecnologie moderne a canale corto il guadagno intrinseco di un singolo MOS è molto basso ($g_m r_o \approx 10 \div 30$, vedi [Crollo di ro](../Effetti%20di%20Canale%20Corto/Crollo%20di%20ro.md)). Per ottenere un guadagno elevato senza aggiungere un secondo stadio (che richiederebbe una complessa compensazione in frequenza), si impiega la configurazione **Cascode Telescopico**.

```
                 VDD
               ┌──┴──┐
              [M7   M8]    Carico PMOS (specchio / sorgente)
               │     │
              [M5   M6]    Cascode PMOS (gate a V_bias,p)
               │     │
               ├───┬─┴──>  V_out (nodo ad altissima impedenza)
               │   │
              [M3   M4]    Cascode NMOS (gate a V_bias,n)
               │     │
              [M1   M2]    Coppia differenziale di ingresso
           VI1 ┤     ├ VI2
               └──┬──┘
                 [M_tail]  Generatore di coda (ISS)
                  ┴ GND
```

Tutti i dispositivi sono impilati in verticale tra $V_{DD}$ e massa (da cui il nome *telescopico*).

#### A) Calcolo analitico del guadagno in continua ($A_{v0}$)
Il guadagno di tensione differenziale a vuoto è dato da:
$$A_{v0} = - G_m \cdot R_{out}$$

1. **Transconduttanza complessiva ($G_m$):**
   I transistor cascode $M_3, M_4$ lavorano a gate comune e si limitano a trasferire la corrente di drain all'uscita con guadagno di corrente unitario:
   $$G_m \approx g_{m1,2}$$
2. **Resistenza di uscita ($R_{out}$):**
   Ciascun transistor cascode moltiplica la resistenza vista verso il proprio source per il proprio guadagno intrinseco:
   * Verso il basso (NMOS): $R_{down} \approx g_{m3} r_{o3} \cdot r_{o1}$
   * Verso l'alto (PMOS): $R_{up} \approx g_{m5} r_{o5} \cdot r_{o7}$
   * Al nodo di uscita le due resistenze sono in parallelo:
     $$R_{out} = R_{down} \parallel R_{up} \approx (g_{mn} r_{on}^2) \parallel (g_{mp} r_{op}^2)$$
3. **Formula del guadagno in continua:**
   Assumendo parametri tipici confrontabili ($g_{mi} \approx g_m$, $r_{oi} \approx r_o$):
   $$A_{v0} \approx - g_m \cdot \left[ \frac{1}{2} (g_m r_o) r_o \right] = \mathbf{-\frac{1}{2} (g_m r_o)^2}$$

#### B) Ordine di grandezza numerico
* **Canale corto / nanometrico ($g_m r_o \approx 20 \div 50$):**
  $$|A_{v0}| \approx \frac{1}{2} (20 \div 50)^2 \approx 200 \div 1250 \implies \mathbf{45 \div 65\text{ dB}}$$
* **Canale lungo ($g_m r_o \approx 50 \div 100$):**
  $$|A_{v0}| \approx 2500 \div 5000 \implies \mathbf{70 \div 75\text{ dB}}$$

Il cascode telescopico fornisce il guadagno tipico di una cascata a due stadi ($\propto (g_m r_o)^2$) pur rimanendo un **singolo stadio**.

---

### 3. Perché si usa il Telescopico e quali sono i suoi limiti?

#### Vantaggi (Perché si fa):
1. **Velocità e banda massima:** Non essendoci un secondo stadio, non compaiono poli intermedi interni a bassa frequenza. L'unico polo dominante è direttamente sul nodo di uscita ad alta impedenza. Non serve la compensazione a condensatore di [Effetto Miller](./Effetto%20Miller.md).
2. **Consumo ridotto al minimo:** La stessa corrente di coda $I_{SS}$ attraversa contemporaneamente l'ingresso differenziale e il carico cascode. Non ci sono rami ausiliari con corrente a vuoto (a differenza del *folded cascode*).
3. **Basso rumore termico:** Meno transistor attivi con percorsi di corrente indipendenti rispetto a stadi complessi multistadio.

#### Limite fondamentale (Il collo di bottiglia):
* **Crollo della dinamica di uscita (*Output Swing*):**
  Tra $V_{DD}$ e massa ci sono ben 5 transistor impilati in serie:
  $$M_{\text{tail}} + M_1 + M_3 + M_5 + M_7$$
  Ciascun transistor per rimanere in saturazione richiede una caduta minima pari alla propria [tensione di overdrive](./Overdrive%20e%20Regioni%20di%20Inversione.md) $V_{ov} = V_{GS} - V_{TH}$.  
  Lo swing utile della tensione d'uscita è quindi compresso:
  $$V_{out,\text{max}} - V_{out,\text{min}} \approx V_{DD} - 5 V_{ov}$$
  Con alimentazioni moderne basse ($V_{DD} \le 1.2\text{ V}$), se ogni transistor ha $V_{ov} \approx 150 \div 200\text{ mV}$, lo swing residuo diventa quasi nullo ($< 200\text{ mV}$). In tali contesti si preferisce il *Folded Cascode* (che disaccoppia l'alimentazione consumando più corrente) o amplificatori a 2 stadi.

#### Dipendenza termica nel Cascode Telescopico:
Poiché $A_{v0} \approx \frac{1}{2}(g_m r_o)^2$, e ciascun fattore intrinseco $g_m r_o$ si riduce con la temperatura a causa del calo di mobilità $\mu(T)$, anche nel cascode telescopico **il guadagno in continua scende sensibilmente con l'aumento della temperatura**.

---

*Pagine correlate:*
- [Effetto Miller](./Effetto%20Miller.md)
- [MOS](./MOS.md)
- [Crollo della Resistenza di Uscita (ro) e Guadagno Intrinseco](../Effetti%20di%20Canale%20Corto/Crollo%20di%20ro.md)
- [Matching e Variabilita nei Componenti Integrati](./Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [Overdrive e Regioni di Inversione](./Overdrive%20e%20Regioni%20di%20Inversione.md)
- [Capacità parassite nel MOSFET](./Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [Resistenza termica](../Scaling%20e%20Limiti%20Fisici/Resistenza%20termica.md)
- [Inverter CMOS e Regioni di Funzionamento](../Famiglie%20Logiche/Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)
- [Analogico non si scende di dimensioni](../Scaling%20e%20Limiti%20Fisici/Analogico%20non%20si%20scende%20di%20dimensioni.md)
