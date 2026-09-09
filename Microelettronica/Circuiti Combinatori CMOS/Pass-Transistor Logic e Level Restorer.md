# Pass-Transistor Logic (PTL) e Level Restorer

Nelle famiglie logiche convenzionali (CMOS complementare e Ratioed Logic), i segnali di ingresso vengono applicati **esclusivamente sui terminali di Gate** dei transistor, mentre i terminali di conduzione (Source e Drain) sono vincolati alle linee di alimentazione ($V_{DD}$ e GND).

La **Pass-Transistor Logic (PTL)** introduce un radicale **cambio di paradigma architetturale**:
* **Gli ingressi vengono applicati direttamente ai terminali di Source e Drain!**
* Il transistor agisce come un semplice **interruttore passante bidirezionale** (*pass switch*): quando il Gate è alto ($1$), l'interruttore si chiude e trasferisce la tensione dal Source al Drain; quando il Gate è basso ($0$), il transistor si apre e isola i nodi.

```
       CMOS CLASSICO: Ingressi su GATE               PTL: Ingressi su SOURCE/DRAIN
       
                 VDD                                              Controllo (Gate)
                  │                                                      │
         ┌────────┴────────┐                                     ┌───────┴───────┐
  In ───►│  GATE TRANSISTOR│                      Ingresso ─────►│  SOURCE/DRAIN │─────► Uscita
         └────────┬────────┘                      (Segnale)      └───────────────┘       (Dati)
                 GND
```

---

### 1. Il Grande Vantaggio: Compattezza Estrema (La Porta AND a 2 Transistor)

Poiché il canale stesso trasporta i segnali logici, la logica PTL permette di sintetizzare funzioni complesse con un numero di transistor drasticamente inferiore rispetto al CMOS statico ($N$ transistor contro i consueti $2N$).

L'esempio più emblematico è la **porta AND ($F = A \cdot B$) realizzata con soli 2 transistor nMOS** (contro i 6 transistor richiesti dal CMOS standard: 4 per la NAND2 + 2 per l'inverter):

```
                               PORTA AND A 2 TRANSISTOR nMOS
                               
                                    B (Controllo Gate)
                                   ┌───┴───┐
                      A ───────────┤  Mn1  ├───────────┐
                   (Segnale)       └───┬───┘           │
                                                       o─────── F = A · B
                                  /B (Controllo Gate)  │
                                   ┌───┴───┐           │
                    GND (0V) ──────┤  Mn2  ├───────────┘
                                   └───┬───┘
```

#### Tabella di Funzionamento:
* **Se $B = 1$ (quindi $\overline{B} = 0$):**
  * $Mn_1$ è ACCESO, $Mn_2$ è SPENTO.
  * Il segnale $A$ viene trasferito direttamente all'uscita: **$F = A$**.  
    Se $A = 1 \implies F = 1$; se $A = 0 \implies F = 0$.
* **Se $B = 0$ (quindi $\overline{B} = 1$):**
  * $Mn_1$ è SPENTO, $Mn_2$ è ACCESO.
  * L'uscita viene collegata direttamente a massa: **$F = 0\text{ V}$**.
* **Risultato:** L'uscita è alta solo se $A=1$ AND $B=1$. Funzione perfetta con soli due componenti!

---

### 2. Il Difetto Fisico Mortale: Il "Weak 1" e la Caduta di Soglia

Nonostante la straordinaria densità di integrazione, i pass-switch a soli nMOS soffrono di una gravissima limitazione fisica:  
**l'nMOS è un eccellente conduttore dello zero logico ("Strong 0"), ma un pessimo conduttore dell'uno logico ("Weak 1")**.

```
                   IL MECCANISMO DELLO SPEGNIMENTO AUTONOMO
                   
                   VG = VDD = 2.5V
                          │
                      ┌───┴───┐
     VDD = 2.5V ──────┤  nMOS ├──────o───────── Nodo X (Capacità CL)
      (Drain)         └───┬───┘      │ (Source)
                          │         === CL
                         GND         │
                                    GND
                                     │
                                     └── IL NODO X NON RAGGIUNGE MAI 2.5V!
                                         SI FERMA A: VDD - VTn ≈ 1.8V
```

#### Perché il nodo non raggiunge mai $V_{DD}$?
Affinché il canale dell'nMOS rimanga invertito e possa condurre corrente per caricare il condensatore di carico $C_L$, la tensione Gate-Source deve soddisfare la condizione di accensione:
$$V_{GS} \ge V_{Tn} \implies V_G - V_S \ge V_{Tn}$$

1. Il terminale di Gate è mantenuto alla tensione di controllo $V_G = V_{DD} = 2.5\text{ V}$.
2. Inizialmente il nodo di Source è a $0\text{ V}$, quindi $V_{GS} = 2.5\text{ V} > V_{Tn}$: il transistor conduce forte corrente e carica rapidamente $C_L$.
3. Man mano che il condensatore si carica, la tensione di Source $V_x$ sale progressivamente.
4. La tensione $V_{GS} = V_{DD} - V_x$ si riduce continuamente, finché, nel momento esatto in cui:
   $$\mathbf{V_x = V_{DD} - V_{Tn}}$$
   si ottiene:
   $$V_{GS} = V_{DD} - (V_{DD} - V_{Tn}) = V_{Tn}$$
5. Sotto questa soglia ($V_{GS} < V_{Tn}$), il canale si strozza e **il transistor si spegne da solo**! Non può più erogare alcuna corrente per completare la carica del nodo.
6. **Conclusione:** Il livello alto in uscita rimane bloccato al valore degradato $V_{\text{max}} = V_{DD} - V_{Tn} \approx 2.5\text{ V} - 0.7\text{ V} = 1.8\text{ V}$. Si ha una **perdita secca pari a un'intera tensione di soglia ($\Delta V = V_{Tn}$)**.

---

### 3. L'Aggravamento per Effetto Body ($V_{SB} > 0$)

Il fenomeno del Weak 1 è reso ancora più severo dall'**effetto Body** (vedi [La soglia da cosa dipende](../Dispositivi%20e%20Componenti/La%20soglia%20da%20cosa%20dipende.md)):
* Il substrato (bulk) dei transistor nMOS su silicio è permanentemente vincolato al potenziale più basso del chip ($V_B = \text{GND} = 0\text{ V}$).
* Quando il nodo di Source sale a $V_x \approx 1.8\text{ V}$, si instaura una forte d.d.p. inversa tra Source e Body:
  $$V_{SB} = V_x - V_B = 1.8\text{ V} > 0\text{ V}$$
* L'allargamento della regione di carica spaziale nel canale incrementa la tensione di soglia effettiva:
  $$V_{Tn} = V_{Tn0} + \gamma \left( \sqrt{2\phi_F + V_{SB}} - \sqrt{2\phi_F} \right)$$
* La soglia $V_{Tn}$ schizza da $0.4\text{ V}$ fino a **$0.8 \div 1.0\text{ V}$**, "mangiandosi" quasi la metà della tensione di alimentazione e lasciando il nodo $X$ degradato a soli $\approx 1.5\text{ V}$!

---

### 4. La Catastrofe della Potenza Statica nell'Inverter a Valle

Perché nei manuali di elettronica la promessa *"No static power consumption"* della PTL è sempre accompagnata da un punto interrogativo critico?

Sebbene la rete pass-transistor in sé non consumi corrente continua a regime, **il livello degradato distrugge le porte CMOS collegate a valle**:

```
                       CATASTROFE STATICA NELL'INVERTER A VALLE
                       
           Pass-Switch                       Inverter CMOS Standard
                                                     VDD = 2.5V
                                                      │
                                                  ┌───┴───┐
                                                  │  pMOS │ VGS,p = 1.8V - 2.5V = -0.7V
                                      ┌───────────┤  (M2) │ (NON SI SPEGNE! RIMANE ACCESO!)
                                      │           └───┬───┘
                                      │               │
     Vin = 2.5V ───[Mn]───o─── X ─────┤               o─────── OUT = 0V
                          │           │               │
                        CL ===        │           ┌───┴───┐
                          │           └───────────┤  nMOS │ VGS,n = 1.8V > VTn
                         GND                      │  (M1) │ (ACCESO!)
                                                  └───┬───┘
                                                      │
                                                  ───┴─── GND
                                                      ▲
                                                      │ CORRENTE DI CORTO CIRCUITO
                                                      └── DIRETTA DA VDD A MASSA!
```

#### Meccanismo del Cortocircuito Statico:
1. Il pass-transistor porta il nodo intermedio $X$ a $V_x \approx 1.8\text{ V}$ anziché a $2.5\text{ V}$.
2. Per l'nMOS $M_1$ dell'inverter a valle: $V_{GS,n} = 1.8\text{ V} > V_{Tn} \implies M_1$ è acceso e conduce verso massa.
3. **Ma per il pMOS $M_2$ dell'inverter:** il Source è collegato stabilmente a $V_{DD} = 2.5\text{ V}$. La sua tensione Gate-Source vale:
   $$V_{GS,p} = V_G - V_S = 1.8\text{ V} - 2.5\text{ V} = \mathbf{-0.7\text{ V}}$$
4. Poiché $|V_{GS,p}| = 0.7\text{ V} \ge |V_{Tp}|$, **il pMOS $M_2$ NON SI SPEGNE AFFATTO!** Rimane parzialmente acceso in zona attiva.
5. **Risultato disastroso:** Sia il pMOS superiore che l'nMOS inferiore sono contemporaneamente conduttivi. Si instaura una **pesantissima corrente di cortocircuito continuo ($I_{DD,\text{stat}}$)** che drena potenza costante dalla batteria per tutto il tempo in cui il nodo rimane alto!

---

### 5. La Soluzione: Il Level Restorer Transistor ($M_r$)

Per conservare la densità della logica a pass-transistor eliminando la caduta di soglia e la potenza statica, si introduce un piccolo transistor pMOS ausiliario di retroazione, denominato **Level Restorer ($M_r$)**:

```
                               CIRCUITO CON LEVEL RESTORER
                               
                                          VDD                         VDD
                                           │                           │
                                      ┌────┴────┐                 ┌────┴────┐
                                      │ pMOS Mr │                 │   M2    │
                               ┌──────┤ (Level  │                 │  (pMOS) │
                               │      │ Restorer│                 └────┬────┘
                               │      └────┬────┘                      │
                               │           │                           o────── OUT
                               │           o───────── Nodo X ──────────┤
                               │           │                           │
     Segnale A ───────[Mn]─────┼───────────┤                       ┌────┴────┐
                   (Gate B)    │          === CL                   │   M1    │
                               │           │                       │  (nMOS) │
                               │          GND                      └────┬────┘
                               │                                       │
                               └───────────────────────────────────────┘
                                (Il Gate di Mr è pilotato dall'uscita OUT!)
```

#### Come Funziona il Ripristino del Livello ($0 \to 1$):
1. **Fase di carica iniziale:** L'ingresso commuta ad alto. L'nMOS $M_n$ eroga corrente e fa salire velocemente il nodo $X$ da $0\text{ V}$ fino a $V_{DD} - V_{Tn}$ ($1.8\text{ V}$).
2. **Commutazione dell'inverter:** La tensione di $1.8\text{ V}$ è ampiamente superiore alla soglia logica di commutazione dell'inverter $V_M \approx 1.25\text{ V}$. Di conseguenza, **l'uscita $OUT$ crolla verso $0\text{ V}$**.
3. **Attivazione del Restorer:**
   * Poiché $OUT \to 0\text{ V}$, il gate del pMOS $M_r$ viene forzato a massa ($V_{GS,r} = -V_{DD}$).
   * **$M_r$ si accende violentemente** in piena conduzione!
   * $M_r$ collega direttamente il nodo $X$ alla linea $V_{DD}$, **portando $X$ dal valore degradato ($1.8\text{ V}$) fino al livello ideale completo ($2.5\text{ V}$)** (*Full-Swing Restoration*).
4. **Azzeramento della potenza statica:** Non appena $X$ raggiunge $V_{DD} = 2.5\text{ V}$, la d.d.p. Gate-Source del pMOS $M_2$ diventa $V_{GS,p} = 2.5\text{ V} - 2.5\text{ V} = 0\text{ V} \implies \mathbf{M_2 \text{ si spegne al 100\%}}$. La corrente statica svanisce all'istante.

---

### 6. I Trade-off e il "Ratio Problem" nel Level Restorer

L'introduzione del Level Restorer non è gratuita e impone vincoli dimensionali critici:

1. **Capacità Parassita Aggiuntiva:**
   Il drain di $M_r$ è fisicamente connesso al nodo $X$, aggiungendo la propria capacità parassita di giunzione $C_{db,r}$ a $C_L$, rallentando lievemente la salita iniziale.

2. **Il Problema del Rapporto (*Ratio Problem*) durante la discesa ($1 \to 0$):**
   Cosa accade quando il segnale in ingresso ordina al nodo $X$ di scaricarsi a massa ($0\text{ V}$)?
   * All'inizio della transizione, il nodo $X$ è a $V_{DD}$ e l'uscita $OUT$ è a $0\text{ V}$.
   * Di conseguenza, **$M_r$ è ancora completamente acceso e pompa corrente da $V_{DD}$ tentando disperatamente di mantenere $X$ alto!**
   * L'nMOS di commutazione $M_n$ deve non solo scaricare il condensatore $C_L$, ma **deve essere in grado di vincere la corrente erogata da $M_r$** per riuscire ad abbassare il potenziale di $X$ sotto la soglia logica $V_M$ dell'inverter.
   * Se $M_r$ fosse progettato troppo "forte" ($W_r$ grande), l'nMOS non riuscirebbe mai a tirare giù il nodo: il circuito rimarrebbe bloccato permanentemente a livello logico 1 (*latchup di stato*)!

```
                               IL RATIO PROBLEM IN DISCESA (1 -> 0)
                               
                                          VDD
                                           │
                                       [Mr] pMOS (Acceso! Pompa corrente verso X)
                                           │   |
                                           │   ▼ ID,r
                                           o───────── Nodo X (Deve scendere sotto VM!)
                                           │   ▲
                                           │   │ ID,n
                                       [Mn] nMOS (Acceso! Deve "vincere" contro Mr)
                                           │
                                      Vin = 0V (GND)
```

> [!IMPORTANT]
> **Regola di Dimensionamento per il Restorer:**  
> Il transistor $M_r$ deve essere dimensionato **volutamente piccolo e debole** (*Weak PMOS*):
> $$\left(\frac{W}{L}\right)_r \ll \left(\frac{W}{L}\right)_n$$
> In questo modo, quando $M_n$ si accende per scaricare il nodo, vince facilmente la contesa; non appena $X$ scende e $OUT$ sale a $V_{DD}$, $M_r$ si spegne lasciando che l'uscita completi la transizione a $0\text{ V}$ indisturbata.

---

### Confronto di Sintesi

| Configurazione | Conteggio Transistor | Escursione Logica Alto | Corrente Statica Inverter | Margine di Rumore | Ratio Sizing Richiesto? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PTL nMOS Semplice** | Minimo ($N$) | Degradata ($V_{DD} - V_{Tn}$) | **Altissima (Cortocircuito)** | Pessimo | No |
| **PTL + Level Restorer** | Basso ($N + 1$ per porta) | **Piena ($V_{DD}$ Rail-to-Rail)** | **Zero (A regime stazionario)** | **Ottimo** | **Sì ($M_r$ debole)** |
| **Transmission Gate (TG)** | Medio ($2N$: nMOS + pMOS) | **Piena ($V_{DD}$ Rail-to-Rail)** | **Zero** | **Ottimo** | No (Interruttore simmetrico) |

---

*Pagine correlate:*
- [Ratioed Logic e DCVSL](./Ratioed%20Logic%20e%20DCVSL.md)
- [Dimensionamento Transistor e Ritardo di Pattern (Sizing)](./Dimensionamento%20Transistor%20e%20Ritardo%20di%20Pattern%20(Sizing).md)
- [Effetto di Fan-In e Fan-Out sul Ritardo (Elmore)](./Effetto%20di%20Fan-In%20e%20Fan-Out%20sul%20Ritardo%20(Elmore).md)
- [Tecniche di Ottimizzazione per Porte Complesse Veloci](./Tecniche%20di%20Ottimizzazione%20per%20Porte%20Complesse%20Veloci.md)
- [Inverter CMOS e Regioni di Funzionamento](../Famiglie%20Logiche/Inverter%20CMOS%20e%20Regioni%20di%20Funzionamento.md)
- [La soglia da cosa dipende](../Dispositivi%20e%20Componenti/La%20soglia%20da%20cosa%20dipende.md)
- [Soglia Logica e Margine di Rumore](../Famiglie%20Logiche/Soglia%20Logica%20e%20Margine%20di%20Rumore.md)
