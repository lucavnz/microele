Il comportamento dinamico del **diodo a giunzione $PN$** nei circuiti integrati non è istantaneo: durante le commutazioni veloci entrano in gioco le cariche accumulate all'interno del dispositivo, dando origine a fenomeni capacitivi fortemente non lineari.

---

### 1. Le Due Capacità Fisiche: Giunzione ($C_j$) vs Diffusione ($C_d$)

Il diodo non ha armature fisiche come un condensatore classico, ma immagazzina carica tramite due meccanismi microscopici distinti:

* **Capacità di Giunzione / Svuotamento ($C_j$):**
  * **Origine fisica:** è la carica spaziale fissa scoperta nella regione di svuotamento (SCR), formata dagli ioni droganti ionizzati ($N_A^-$ e $N_D^+$). Al variare della tensione applicata, lo spessore $W(V)$ si allarga o si restringe:
    $$C_j(V) = \frac{\epsilon_s A}{W(V)} = \frac{C_{j0}}{\left(1 - \frac{V}{\Phi_B}\right)^m}$$
    dove $\Phi_B$ è il potenziale di built-in e $m$ vale $1/2$ per giunzioni brusche e $1/3$ per giunzioni a drogaggio graduale.
  * **Dove domina:** a diodo **spento/interdetto ($V < 0$)** e a bassissima tensione diretta.

* **Capacità di Diffusione ($C_d$):**
  * **Origine fisica:** quando il diodo è in conduzione diretta ($V > 0$), inietta un'enorme quantità di portatori minoritari nelle regioni neutre adiacenti alla giunzione. Questa carica in transito $Q_d$ vale:
    $$Q_d(t) \approx \tau_T \cdot I_D(t)$$
    dove $\tau_T$ è il **tempo di transito** dei portatori minoritari prima della ricombinazione.
  * **Formula differenziale:**
    $$C_d = \frac{dQ_d}{dV} = \tau_T \frac{dI_D}{dV} = \frac{\tau_T I_D}{V_T} = \frac{\tau_T}{\Phi_T} I_S e^{\frac{V}{\Phi_T}}$$
  * **Dove domina:** a diodo **acceso a regime ($V \approx V_{ON}$)**, dove la corrente $I_D$ è elevata e fa esplodere $C_d$ esponenzialmente, superando $C_j$ di diversi ordini di grandezza.
  👉 Approfondimento: [Condensatori](./Condensatori.md) per il confronto con le capacità integrate lineari (MIM, PIP).

---

### 2. Regime Quasi-Stazionario vs Regime Dinamico Veloce

Per modellare analiticamente $C_j$ e $C_d$ si fa spesso l'ipotesi di **regime quasi-stazionario**:
* **Cosa significa:** le grandezze esterne (tensione e corrente) variano abbastanza lentamente rispetto ai tempi fisici interni del silicio (tempo di transito $\tau_T$ e tempo di rilassamento dielettrico).
* In queste condizioni, i profili di concentrazione dei minoritari $p_n(x,t)$ hanno il tempo di adattarsi istante per istante alla corrente presente ($p_n(x,t) \approx p_n(x, I(t))$), rendendo valida la relazione statica $Q_d = \tau_T I_D$.
* **Cosa succede nei transitori veloci (Regime dinamico):**
  Se applichiamo una commutazione brusca (es. un gradino di tensione ideale):
  * I profili di carica si deformano e non corrispondono più a quelli statici.
  * La carica $Q_d$ non può seguire istantaneamente la corrente, ma è regolata dall'**equazione di continuità e controllo della carica**:
    $$\frac{dQ_d(t)}{dt} + \frac{Q_d(t)}{\tau_T} = I(t)$$
  * ⚠️ **Regola pratica per le simulazioni:** *MAI applicare gradini ideali di tensione o corrente nelle simulazioni circuitali (SPICE)*, perché violano l'ipotesi quasi-stazionaria e creano discontinuità matematiche non fisiche nei modelli numerici.

---

### 3. Modello Circuitale Dinamico a Componenti Anomali

Nel silicio integrato reale, il diodo in regime dinamico a grandi segnali viene modellato da quattro elementi concentrati:

```text
               rs (anomalo serie: bulk e contatti)
   Anodo o──────/\/\/\/\──────┬─────────────────────┬────────────o Catodo
                              │                     │
                         ┌────┴────┐           ┌────┴────┐
                         │  Diodo  │           │   Cp    │ (anomalo parallelo:
                         │ Ideale  │           │ Cj + Cd │  giunzione + diffusione)
                         │Shockley │           └────┬────┘
                         └────┬────┘                │
                              │                     │
                         ┌────┴────┐                │
                         │   rp    │ (anomalo       │
                         │ parallelo: ricomb/gen,   │
                         │ breakdown)               │
                         └────┬────┘                │
                              └─────────────────────┘
```

Perché sono detti **componenti anomali**?
* Non sono componenti passivi ideali a valore costante: i loro parametri dipendono fortemente dallo **stato di polarizzazione istantaneo** del diodo ($V$ e $I$).
* **Resistore anomalo serie ($r_s$):** modella la resistività delle zone neutre e dei contatti; diminuisce ad alte correnti per la modulazione di conducibilità (inondazione di cariche libere).
  👉 Vedi: [Diodo](./Diodo.md) (Sezione Resistenza Serie) e [Difficoltà nel fare un componente ideale](./Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md).
* **Resistore anomalo parallelo ($r_p$):** tiene conto della generazione/ricombinazione termica nella SCR e crolla a valori minimi in zona di breakdown.
  👉 Vedi: [Breakdown e Diodo Zener](./Breakdown%20e%20Diodo%20Zener.md).
* **Condensatore anomalo parallelo ($C_p = C_j + C_d$):** somma delle due capacità non lineari dipendenti da $V$ e $I$.

---

### 4. Transitorio di Spegnimento (Turn-Off da $+V_1$ a $-V_2$)

Consideriamo un diodo polarizzato in diretta con un generatore $V_g = +V_1$ attraverso una resistenza $R$. A regime conduce una corrente $I \approx \frac{V_1 - V_{ON}}{R} \approx \frac{V_1}{R}$, con tensione $V(0) = V_{ON} \approx 0.7\text{ V}$ e una carica di diffusione accumulata $Q_d(0) \approx \tau_T \frac{V_1}{R}$.

All'istante $t = 0$ il generatore commuta bruscamente a $V_g = -V_2$ (tensione inversa). Il transitorio si articola in **due fasi distinte**:

```text
       Vg ^
      +V1 |--------\
          |        |
      -V2 |________|____________________________> t
                   0

        I ^
  +V1/R   |--------\
          |        |
          |________|____________________________> t
                   | tS: storage time
  -V2/R   |        |-------------------\
          |                             \_______ -Is ≈ 0

        V ^
     +VON |--------\  (V ≈ VON quasi costante!)
          |         \
        0 |__________|__________________________> t
          |          tS \
      -V2 |              \______________________ -V2 (scarica RC con Ceq)
```

#### Fase 1: Tempo di Immagazzinamento ($0 \le t \le t_S$, Storage Time)
* **Cosa fa la fisica:** il diodo è pieno di portatori minoritari nelle zone neutre. Finché la concentrazione di minoritari ai bordi della giunzione non si azzera, la giunzione interna **resta polarizzata in diretta**. La tensione ai capi del diodo **rimane inchiodata a $V(t) \approx V_{ON}$**!
* **La corrente inversa:** con $V_g = -V_2$ e $V_D \approx V_{ON}$, la corrente salta istantaneamente a un valore **negativo costante**, imposto dalla maglia esterna:
  $$I(t) \approx \frac{-V_2 - V_{ON}}{R} \approx -\frac{V_2}{R} = \text{costante}$$
* **Svuotamento della carica:** questa corrente estrae le cariche minoritarie. L'equazione di carica:
  $$\frac{dQ_d(t)}{dt} + \frac{Q_d(t)}{\tau_T} = -\frac{V_2}{R}$$
  porta a un **decadimento esponenziale** (e non logaritmico!) della carica:
  $$Q_d(t) = Q_d(\infty) + \left[Q_d(0) - Q_d(\infty)\right] e^{-\frac{t}{\tau_T}} = \tau_T \left[ -\frac{V_2}{R} + \frac{V_1 + V_2}{R} e^{-\frac{t}{\tau_T}} \right]$$
* **Perché la tensione scende poco prima di crollare?**
  La tensione è legata alla carica da una relazione logaritmica: $V(t) = V_T \ln\left(1 + \frac{Q_d(t)}{\tau_T I_S}\right)$. Finché $Q_d > 0$, il logaritmo varia pochissimo; crolla verso zero solo quando $Q_d$ è quasi del tutto azzerata.
* **Calcolo del tempo di storage $t_S$:** imponendo $Q_d(t_S) = 0 \implies V(t_S) = 0$:
  $$t_S = \tau_T \ln\left(1 + \frac{V_1}{V_2}\right) \quad \text{oppure} \quad t_S = \tau_T \ln\left(\frac{V_1 + V_2}{V_{ON} + V_2}\right)$$
* In questa fase la capacità di giunzione $C_j$ è del tutto trascurabile: **comanda solo l'estrazione di $Q_d$**.

#### Fase 2: Da $0\text{ V}$ verso $-V_2$ ($t > t_S$)
* **Cosa fa la fisica:** i minoritari sono stati spazzati via ($Q_d \approx 0 \implies C_d \approx 0$).
* Ora la regione di svuotamento deve allargarsi per sostenere la tensione inversa fino a $-V_2$.
* **Linearizzazione con $C_{eq}$:** poiché $C_j(V)$ è non lineare, si calcola una capacità equivalente media costante tra $V_a = -V_2$ e $V_b = 0\text{ V}$:
  $$C_{eq} = K_{eq} C_{j0} = \frac{\Delta Q_j}{\Delta V} = \frac{Q_j(0) - Q_j(-V_2)}{V_2}$$
  con $K_{eq} = \frac{\Phi_B}{(1-m) V_2} \left[ \left(1 + \frac{V_2}{\Phi_B}\right)^{1-m} - 1 \right]$.
* Il circuito diventa una **scarica RC pura** con costante di tempo $\tau = R \cdot C_{eq}$:
  $$V(t) = -V_2 \left(1 - e^{-\frac{t - t_S}{R C_{eq}}}\right)$$
  e la corrente inversa decade esponenzialmente da $-V_2/R$ fino alla corrente di saturazione inversa $-I_S \approx 0$.

---

### 5. Transitorio di Accensione (Turn-On da $-V_2$ a $+V_1$)

Supponiamo ora il caso opposto: il diodo parte da spento con $V_g = -V_2$, quindi $V(0) = -V_2$ e $I \approx 0$. All'istante $t = 0$ il generatore commuta a $V_g = +V_1$.

Anche qui l'analisi si divide in due fasi:

#### Fase 1: Da $-V_2$ a $0\text{ V}$ ($0 \le t \le t_0$)
* **Cosa fa la fisica:** finché la tensione è negativa ($V \le 0$), il diodo è interdetto e non inietta minoritari: **$Q_d = 0$ e $C_d = 0$**.
* Il generatore deve solo caricare la capacità di giunzione attraverso $R$ per stringere la regione di svuotamento.
* È una **carica RC pura** governata dalla sola capacità equivalente di giunzione $C_{eq}$:
  $$V(t) = V_1 - (V_1 + V_2) e^{-\frac{t}{R C_{eq}}}$$
* Il tempo $t_0$ necessario per azzerare la tensione ($V(t_0) = 0$) vale:
  $$t_0 = R C_{eq} \ln\left(1 + \frac{V_2}{V_1}\right)$$
  Questo intervallo è **estremamente breve**, tipicamente nell'ordine di poche centinaia di picosecondi ($400\text{--}700\text{ ps}$). Nella pratica, questo modello RC puro si estende bene fino a circa l'$80\%$ di $V_{ON}$.

#### Fase 2: Da $0\text{ V}$ verso $+V_{ON}$ ($t > t_0$)
* **La sorpresa delle simulazioni: Prevale ancora $C_j$!**
  * Verrebbe spontaneo pensare che, appena $V > 0$, la capacità di diffusione $C_d$ prenda subito il sopravvento. **Non è così!**
  * A basse tensioni dirette ($0 < V < 0.5\text{ V}$), la corrente che scorre è ancora molto piccola. Essendo $C_d = \frac{\tau_T I_D}{V_T}$ direttamente proporzionale a $I_D$, la capacità di diffusione parte da valori minimi.
  * Al contrario, la capacità di giunzione $C_j$ aumenta man mano che $V$ sale verso $\Phi_B$.
  * **Conclusione:** per gran parte della salita verso $V_{ON}$, **è ancora la capacità di giunzione $C_j$ a "rompere le scatole" e a rallentare la carica!**
* Solo a ridosso del valore finale di regime (quando la corrente si stabilizza a $I \approx V_1/R$), $C_d$ esplode e diventa dominante.

---

### 6. Sintesi Comparativa dei Transitori

| Fase del Transitorio | Intervallo Tensione | Capacità Dominante | Modello Circuitale | Durata Tipica |
| :--- | :--- | :--- | :--- | :--- |
| **Spegnimento: Fase 1 (Storage)** | $V(t) \approx V_{ON}$ | **Diffusione ($Q_d$)** ($C_j$ trascurabile) | Estrazione carica a corrente costante: $I \approx -\frac{V_2}{R}$ | $t_S \sim \tau_T \ln(1 + V_1/V_2)$ (ns) |
| **Spegnimento: Fase 2 (Svuotamento)** | Da $0\text{ V}$ a $-V_2$ | **Giunzione ($C_{eq}$)** ($C_d \approx 0$) | Scarica esponenziale RC pura: $\tau = R C_{eq}$ | Pochi $\tau = R C_{eq}$ (sub-ns) |
| **Accensione: Fase 1 (Interdizione)** | Da $-V_2$ a $\sim 0\text{ V}$ | **Giunzione ($C_{eq}$)** ($C_d \approx 0$) | Carica esponenziale RC pura: $\tau = R C_{eq}$ | $t_0 \sim R C_{eq} \ln(1 + V_2/V_1)$ (ps) |
| **Accensione: Fase 2 (Conduzione)** | Da $0\text{ V}$ a $+V_{ON}$ | **Prevale ancora $C_j$!** (poi $C_d$ a regime) | Non lineare: iniezione minoritari rallentata fortemente da $C_j$ | Dipende da $\tau_T$ e $R C_j$ |

---

*Pagine correlate:*
- [Diodo](./Diodo.md)
- [Breakdown e Diodo Zener](./Breakdown%20e%20Diodo%20Zener.md)
- [Condensatori](./Condensatori.md)
- [Resistore](./Resistore.md)
- [Difficoltà nel fare un componente ideale](./Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
