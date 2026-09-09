# Confronto tra Tecnologie Integrate: CMOS Standard, Twin-Tub, Triple-Well, SOI e BiCMOS

Nello sviluppo dei circuiti integrati moderni la scelta della tecnologia di fabbricazione rappresenta il compromesso (*trade-off*) primario tra costi, consumi, velocità, densità e precisione analogica.

Le principali tecnologie a confronto sono:
1. **CMOS Standard ($n\text{-well}$ su substrato $p$):** La tecnologia bulk classica ed economica.
2. **CMOS Twin-Tub (Doppio Pozzo):** Pozzi $n\text{-well}$ e $p\text{-well}$ separati cresciuti su uno strato epitassiale leggermente drogato.
3. **CMOS Triple-Well (con Deep N-Well, DNW):** Aggiunge uno strato profondo di isolamento $n$ per racchiudere e isolare completamente singoli transistor NMOS.
4. **SOI (*Silicon On Insulator*):** Transistor ricavati su un film sottilissimo di silicio separato dal substrato da un ossido sepolto (**BOX**).
5. **BiCMOS:** Integrazione monolitica di transistor bipolari [BJT](../Dispositivi%20e%20Componenti/BJT.md) e [MOS](../Dispositivi%20e%20Componenti/MOS.md) sullo stesso chip.

---

### 1. Come si Confrontano le Tecnologie? (Le Metriche di Scelta)

La valutazione ingegneristica si basa su 5 parametri chiave:
* **Costo e complessità di processo:** Numero di maschere litografiche, passi termici/epitassiali e costo del wafer grezzo di partenza.
* **Capacità parassite e velocità ($f_T$, ritardi $t_p$):** L'entità delle capacità verso il substrato ($C_{db}, C_{sb}$) determina la velocità di commutazione delle porte logiche e la banda degli stadi analogici.
* **Correnti di dispersione (*leakage*):** Perdite di giunzione inversa verso il substrato e correnti di sottosoglia da spento ($I_{OFF}$).
* **Isolamento dal rumore e flessibilità del Body:** Possibilità di azzerare l'effetto body ($V_{SB} = 0$) connettendo localmente il bulk al source, e capacità di bloccare i disturbi di commutazione digitale iniettati nel silicio (*substrate noise coupling*).
* **Immunità al [Latch-Up](../Famiglie%20Logiche/Latchup%20nei%20circuiti%20CMOS.md):** Resistenza all'innesco distruttivo dei tiristori parassiti $pnpn$.

---

### 2. Quale Layout Risulta Più Compatto?

**La tecnologia più compatta in assoluto è la [SOI](../Dispositivi%20e%20Componenti/SOI.md).**

* **Perché:** I transistor sono isolati dielettricamente sia sul fondo (dal BOX di $\text{SiO}_2$) sia sui lati (dalle trincee [STI](./Isolamento.md) che poggiano direttamente sul BOX).
* **Niente sprechi di spazio:** Non essendoci giunzioni $pn$ di contenimento nel silicio, **non servono ampie distanze di sicurezza tra pozzi (*well-to-well spacing*)**, non servono anelli di guardia (*guard rings*) continui per il latch-up, né contatti continui di pozzetto. I transistor NMOS e PMOS possono essere accostati con distanze minime, garantendo la massima densità di integrazione logica.
* *Nel silicio massivo (Bulk):* La più compatta è il **CMOS standard a singolo pozzo ($n\text{-well}$)**, poiché il Twin-Tub e il Triple-Well introducono pozzetti aggiuntivi e distanze di rispetto maggiori.

---

### 3. Quale Layout Risulta Meno Compatto?

**La meno compatta in assoluto è la tecnologia BiCMOS; tra le varianti puramente CMOS è il CMOS Triple-Well.**

* **BiCMOS:** I transistori bipolari BJT integrati occupano aree notevolmente superiori rispetto ai MOSFET a causa della loro struttura tridimensionale (strati sepolti, pozzi profondi di collettore a imbuto/*sinker*, terminali multipli $E, B, C, S$) e richiedono ampi anelli di guardia per drenare le correnti nel substrato.
* **CMOS Triple-Well:** Per isolare un singolo NMOS (o un piccolo gruppo di NMOS analogici) dal substrato comune $p$, la struttura richiede una serie di anelli concentrici di guardia che "rubano" un'area enorme:
  1. L'area interna per il $p\text{-well}$ dedicato;
  2. L'anello di contatto del $p\text{-well}$;
  3. L'ampia trincea/regione di isolamento del *Deep N-Well* (DNW);
  4. L'anello esterno di contatti per l'$n\text{-well}$ di chiusura laterale;
  5. L'anello esterno di contatti per il substrato $p$ circostante.

👉 Approfondimento sulla struttura delle sacche: [Isolamento](./Isolamento.md).

---

### 4. Dal Punto di Vista del Matching Sono Uguali?

**No, non sono affatto uguali!**

* **SOI ha il matching più critico (peggiore):**
  * *Floating Body Effect (nel PD-SOI):* La sacca neutra di silicio non contattata accumula cariche fluttuanti generate per impatto, facendo variare dinamicamente la soglia $V_{th}$ in base alla frequenza e alla storia delle commutazioni precedenti (*History Effect*).
  * *Auto-riscaldamento (Self-Heating):* L'ossido sepolto $\text{SiO}_2$ ha una conducibilità termica pessima (circa 100 volte inferiore al silicio monocristallino). Il calore dissipato dal canale non riesce a fluire verso il substrato e crea gradienti termici locali marcati tra transistor vicini, sbilanciando correnti e tensioni di soglia.
* **Triple-Well e Twin-Tub migliorano il matching nei circuiti analogici:**
  * Nel CMOS standard a singolo pozzo, tutti gli NMOS condividono lo stesso potenziale di substrato (tipicamente massa). Nei transistor impilati (es. rami cascode o coppie differenziali con source fluttuante), la tensione $V_{SB} \ne 0$ altera la soglia per effetto body, introducendo un mismatch non lineare.
  * Con il **Triple-Well** si può connettere il bulk al source ($V_{SB}=0$) per ogni singolo dispositivo, eliminando alla radice il disadattamento da effetto body e schermando la coppia differenziale dal rumore di fondo.
* **BiCMOS:** Nei punti critici ad altissima precisione (es. riferimenti di tensione Bandgap, stadi d'ingresso di amplificatori a basso rumore), i **BJT** garantiscono un matching della tensione di giunzione $V_{BE}$ straordinario: la dispersione tipica è di appena $1 \div 2\text{ mV}$, contro i $5 \div 20\text{ mV}$ di disallineamento della $\Delta V_{th}$ tipica dei MOSFET.

👉 Approfondimento: [Matching e Variabilita nei Componenti Integrati](../Dispositivi%20e%20Componenti/Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md).

---

### 5. Quale Tecnologia è Più Costosa?

**BiCMOS** e **SOI** sono le più costose, mentre il **CMOS standard** è la più economica:

* **BiCMOS:** È la più costosa dal punto di vista della **fabbricazione (processo)**. Fondere passi di processo MOS e Bipolari richiede epitassia controllata, impianti ad alta energia per gli strati sepolti ($n^+$ e $p^+$ buried layers), diffusioni profonde per i sinker e drogaggi dedicati di base ed emettitore. Comporta l'aggiunta di $4 \div 8$ maschere litografiche in più rispetto a un CMOS puro, facendo lievitare i costi e riducendo la resa (*yield*).
* **SOI:** Il costo elevato deriva principalmente dal **costo del wafer di partenza**. I dischi di silicio speciali con ossido sepolto integrato (prodotti con metodologie SmartCut o SIMOX) costano da 3 a 5 volte di più rispetto a un wafer convenzionale di silicio bulk Czochralski.
* **CMOS Standard:** È la soluzione con il minor costo per millimetro quadro, grazie al minor numero di maschere litografiche e all'uso di wafer di silicio massivo standard.

---

### 6. Quale Tecnologia è Migliore per Applicazioni Low Power?

**La tecnologia SOI (in particolare FD-SOI, *Fully Depleted SOI*).**

I motivi fisici sono tre:
1. **Crollo delle capacità parassite ($C_{db}, C_{sb}$):** I terminali di source e drain poggiano direttamente sull'ossido sepolto. Poiché la potenza dinamica di commutazione digitale è:
   $$P_{\text{dyn}} = C_{\text{tot}} \cdot V_{DD}^2 \cdot f$$
   ridurre del $50\% \div 70\%$ le capacità parassite abbatte direttamente il consumo energetico a parità di frequenza operativa.
2. **Minime perdite verso il substrato (*leakage*):** Nel silicio bulk esiste un'ampia area di giunzione polarizzata inversamente che perde corrente verso il substrato (*"Large area for leakage"*). Nel SOI quest'area verso il basso è sbarrata dal BOX (*"Small area for leakage"*).
3. **Pendenza di sottosoglia ideale e scaling aggressivo di $V_{DD}$:** L'accoppiamento elettrostatico ideale del canale sottile ($t_{\text{Si}} \approx 6\text{ nm}$) permette un subthreshold swing ripido ($S \approx 62 - 65\text{ mV/dec}$ contro gli $80 - 95\text{ mV/dec}$ del bulk). Ciò consente di abbassare drasticamente la tensione di alimentazione $V_{DD}$ (anche a $0.4 \div 0.5\text{ V}$) mantenendo correnti di perdita da spento ($I_{\text{OFF}}$) microscopiche. Inoltre, la modulazione della soglia via Back-Gate (*Back Biasing*) permette di passare istantaneamente dalla modalità ad alte prestazioni a quella di riposo a consumo zero.

👉 Approfondimento completo: [SOI](../Dispositivi%20e%20Componenti/SOI.md).

---

### 7. Se nei CMOS Servono i BJT: BJT Integrati in BiCMOS

Quando in un circuito CMOS servono transistori bipolari (ad esempio per stadi di uscita ad alta corrente, stadi RF a basso rumore o riferimenti di tensione Bandgap precisi), la tecnologia BiCMOS li realizza integrando due strutture fondamentali:

```
A) BJT NPN VERTICALE (Flusso di corrente verticale E -> B -> C):
       S          C          B          E          B          C
       │          │          │          │          │          │
   ┌───┴───┐  ┌───┴───┐  ┌───┴───┐  ┌───┴───┐  ┌───┴───┐  ┌───┴───┐
   │  p+   │  │  n+   │  │   p   │  │  n+   │  │   p   │  │  n+   │
   └───────┘  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘
                  │          │          │          │          │
                  │          └──────────┼──────────┘          │
                  │               Base p superficiale          │
                  │                     │                     │
                  └──────────────► Pozzo n- (Collettore) ◄─────┘
                  ┌───────────────────────────────────────────┐
                  │          n+ Buried Layer (Autostrada)     │
                  └───────────────────────────────────────────┘
                               Substrato p (S)

B) BJT PNP LATERALE (Flusso di corrente laterale E -> C):
       S          B          C          E          C          B
       │          │          │          │          │          │
   ┌───┴───┐  ┌───┴───┐  ┌───┴───┐  ┌───┴───┐  ┌───┴───┐  ┌───┴───┐
   │  p+   │  │  n+   │  │   p   │  │   p   │  │   p   │  │  n+   │
   └───────┘  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘
                  │       Collettore   Emettitore Collettore   │
                  │            │            │          │       │
                  │            └──────◄ ◄ ──┴── ► ► ───┘       │
                  │               Corrente laterale            │
                  └──────────────►  Pozzo n- (Base)  ◄─────────┘
                  ┌───────────────────────────────────────────┐
                  │          n+ Buried Layer (Schermo)        │
                  └───────────────────────────────────────────┘
                               Substrato p (S)
```

#### 1. BJT NPN Verticale (*Vertical NPN*)
* **Funzionamento:** La corrente di elettroni scorre verticalmente dall'Emettitore superficiale ($n^+$) attraverso la sottile Base ($p$) fino al Collettore profondo ($n^-$).
* **Ruolo dello strato sepolto ($n^+$ Buried Layer):** La corrente scesa in profondità incontra la lamina fortemente drogata $n^+$, che funge da autostrada a bassissima resistività convogliando il flusso orizzontalmente verso i contatti superficiali di Collettore ($C$), abbattendo drasticamente la resistenza parassita di collettore ($R_C$).
* **Substrato ($S$):** Il substrato $p$ è contattato tramite diffusioni $p^+$ e tenuto alla tensione più negativa del circuito per garantire l'isolamento a giunzione.

#### 2. BJT PNP Laterale (*Lateral PNP*)
* **Funzionamento:** Emettitore ($p$) e Collettore ($p$) sono realizzati contemporaneamente in superficie all'interno dello stesso pozzo $n^-$ (che funge da Base). La conduzione delle lacune avviene in senso **orizzontale/laterale** tra l'emettitore centrale e il collettore circostante (che nel layout avvolge ad anello l'emettitore).
* **Ruolo dello strato sepolto ($n^+$ Buried Layer):** Oltre a ridurre la resistenza di base, funge da **barriera di potenziale elettrostatica**: impedisce alle lacune iniettate dall'emettitore di scendere in profondità nel substrato $p$, evitando l'innesco di un PNP parassita verticale verso massa.

👉 Per tutti i dettagli fisici sul BJT integrato e la differenza tra Fake e Real BiCMOS: [BJT](../Dispositivi%20e%20Componenti/BJT.md).

---

### Tabella Comparativa di Sintesi

| Parametro | CMOS Standard (n-well) | CMOS Triple-Well | SOI (FD-SOI) | BiCMOS |
| :--- | :---: | :---: | :---: | :---: |
| **Compattezza layout** | Buona | Bassa (larghi anelli DNW) | **Massima** | Minima |
| **Costo complessivo** | **Più basso** | Medio | Alto (costo wafer) | **Più alto** (n° maschere) |
| **Matching analogico** | Discreto | Buono (bulk dedicati) | Critico (floating/termico) | **Eccellente** (sui BJT) |
| **Isolamento da rumore** | Scarso | Molto elevato | Eccellente (dielettrico) | Medio/Basso |
| **Consumi (Low Power)** | Standard | Buono | **Migliore in assoluto** | Elevati (correnti di base) |

---

*Pagine correlate:*
- [SOI](../Dispositivi%20e%20Componenti/SOI.md)
- [BJT](../Dispositivi%20e%20Componenti/BJT.md)
- [Isolamento](./Isolamento.md)
- [Capacità parassite nel MOSFET](../Dispositivi%20e%20Componenti/Capacit%C3%A0%20parassite%20nel%20MOSFET.md)
- [Matching e Variabilita nei Componenti Integrati](../Dispositivi%20e%20Componenti/Matching%20e%20Variabilita%20nei%20Componenti%20Integrati.md)
- [Latchup nei circuiti CMOS](../Famiglie%20Logiche/Latchup%20nei%20circuiti%20CMOS.md)
- [MOS](../Dispositivi%20e%20Componenti/MOS.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
- [Integrati protetti da interferenze](../Scaling%20e%20Limiti%20Fisici/Integrati%20protetti%20da%20interferenze.md)
