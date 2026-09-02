Il **diodo PIN** è una variante fondamentale della giunzione $PN$ in cui viene interposto uno strato spesso di **silicio intrinseco (o leggermente drogato)** tra due regioni pesantemente drogate $P^+$ e $N^+$.

A prima vista verrebbe da chiedersi: *a cosa serve mettere la regione $N^+$ alla fine se l'intrinseco basta già ad allargare lo svuotamento per alzare il breakdown?* 
In realtà, la regione $N^+$ è indispensabile sia per la conduzione in diretta che per la tenuta in inversa.

---

### 1. Perché la Struttura $P-I-N$ e Non Solo $P-I$? (Doppia Iniezione e Neutralità)

Se provassimo a realizzare un dispositivo con solo $P-I$ e un contatto metallico all'altro capo, la fisica del trasporto fallirebbe per ragioni elettrostatiche:

#### A. Il limite della Carica Spaziale (SCLC / Legge di Mott-Gurney)
* Se inietti **solo lacune** da $P^+$ dentro la regione $I$, non ci sono ioni negativi fissi né elettroni a compensarle.
* Appena entra un piccolo gruppo di lacune, la regione $I$ si carica positivamente ($\rho = +q \cdot p > 0$).
* Per l'equazione di Poisson ($\nabla \cdot \mathcal{E} = \frac{q p}{\varepsilon_s}$), questo accumulo crea un **campo elettrico repulsivo interno** che respinge le nuove cariche in arrivo (*Space-Charge-Limited Current*).
* **Risultato:** per far passare anche pochi milliampere servirebbero centinaia di Volt e la regione $I$ resterebbe ad altissima resistenza.

#### B. La Quasi-Neutralità di Carica nel Diodo PIN ($\rho \approx 0$)
Nel diodo $P-I-N$, durante la polarizzazione diretta accade la **doppia iniezione**:
* Dalla regione $P^+$ vengono iniettate **lacune** ($+q$).
* Dalla regione $N^+$ vengono iniettati **elettroni** ($-q$).
* Per ogni lacuna che entra da un lato, un elettrone entra dal lato opposto:
  $$\rho = q(p - n) \approx 0$$
* **La regione $I$ rimane elettricamente neutra.** Non formandosi una barriera di carica spaziale repulsiva, è possibile stipare nell'intrinseco una densità enorme di portatori liberi ($n \approx p \gg n_i$, tipicamente $10^{16} \div 10^{17}\text{ cm}^{-3}$).

#### C. La Modulazione di Conducibilità (*Conductivity Modulation*)
La conducibilità vale:
$$\sigma = q(\mu_p p + \mu_n n)$$
Con $p$ e $n$ aumentati di molti ordini di grandezza, la resistenza della regione intrinseca $I$ **crolla da megaohm a frazioni di ohm**. Quello che a riposo era un isolante si trasforma in un eccellente conduttore.
👉 Vedi anche: [Diodo](./Diodo.md) (Sezione 1.D su alte iniezioni e resistenza serie).

---

### 2. Perché la Regione $N^+$ Inietta Elettroni nell'Intrinseco?

L'iniezione dei portatori dalla regione $N^+$ verso la regione $I$ avviene grazie a due fattori:

1. **Il Serbatoio di Cariche (Gradiente di Concentrazione):**  
   La regione $N^+$ è drogata pesantemente ($N_D \sim 10^{19}\text{ cm}^{-3}$), mentre la regione $I$ è quasi priva di portatori a riposo ($n_i \approx 10^{10}\text{ cm}^{-3}$). C'è un dislivello di concentrazione di circa un miliardo di volte.
2. **Abbattimento della Barriera in Polarizzazione Diretta ($V > 0$):**  
   A riposo gli elettroni sono trattenuti all'interno di $N^+$ dalla barriera di potenziale intrinseca ($V_{bi}$). Applicando una tensione diretta all'anodo ($V_A > V_K$), le barriere alle due giunzioni si abbassano: gli elettroni scavalcano la barriera per energia termica e **diffondono spontaneamente a fiumi** nella regione $I$. Lo stesso fanno le lacune da $P^+$.

---

### 3. Tensione di Breakdown: Profilo Rettangolare (PIN) vs Triangolare (PN)

La tensione applicata $V$ in polarizzazione inversa corrisponde all'**area sottesa dal campo elettrico**:
$$V = \int_0^W \mathcal{E}(x) \, dx$$
Il breakdown a valanga si innesca quando il campo elettrico di picco raggiunge il valore critico del silicio ($\mathcal{E}_{max} = \mathcal{E}_{crit} \approx 3 \times 10^5\text{ V/cm}$).

```text
    GIUNZIONE PN (Triangolare)                 DIODO PIN (Rettangolare)
    
     E(x)                                       E(x)
      ^                                          ^
E_crit|      /\                           E_crit|  +---------------+
      |     /  \                                |  |               |
      |    /    \                               |  |               |  <-- Tutta l'area
      |   / Area \                              |  |     Area      |      è sfruttata!
      |  /Triangolo\                            |  | Rettangolare  |
      +---------------+--> x                    +--+---------------+--> x
      0               W                         0                  W
         V_BR = 1/2 * E_crit * W                   V_BR = E_crit * W
```

* **Nella Giunzione $PN$ (Profilo Triangolare):**  
  La presenza di ioni droganti scoperti nella SCR impone una pendenza al campo per l'equazione di Poisson ($\frac{d\mathcal{E}}{dx} = \frac{q N_D}{\varepsilon_s} \neq 0$). Il campo ha una forma triangolare con area dimezzata:
  $$V_{BR, PN} = \frac{1}{2} \cdot \mathcal{E}_{crit} \cdot W$$
  👉 Approfondimento: [Breakdown e Diodo Zener](./Breakdown%20e%20Diodo%20Zener.md).

* **Nel Diodo PIN (Profilo Rettangolare):**  
  Nella regione intrinseca non ci sono cariche fisse di droganti ($\rho = 0$). Di conseguenza:
  $$\frac{d\mathcal{E}}{dx} = 0 \implies \mathcal{E}(x) = \text{costante}$$
  Il campo elettrico è piatto e costante lungo tutto lo spessore $W$. L'area è quella di un rettangolo:
  $$V_{BR, PIN} = \mathcal{E}_{crit} \cdot W$$

> 💡 **Vantaggio Progettuale:** A parità di spessore della zona svuotata $W$, **il diodo PIN regge il DOPPIO della tensione di breakdown ($2 \times V_{BR}$)** rispetto a una giunzione $PN$ standard. A parità di $V_{BR}$ richiesta, permette di dimezzare $W$, riducendo tempi di transito e perdite.

---

### 4. Il Ruolo di $N^+$ come *Field Stopper* (Arresto di Campo)

Senza lo strato $N^+$, il campo elettrico costante raggiungerebbe il contatto metallico esterno con un'intensità vicina a $\mathcal{E}_{crit}$. Le asperità microscopiche e i difetti di interfaccia del metallo innescherebbero scariche per **emissione di campo**, portando alla rottura distruttiva del dispositivo a tensioni molto inferiori al breakdown teorico.

Lo strato $N^+$ iper-drogato ($10^{19}\text{ cm}^{-3}$) possiede una densità di carica altissima: appena il campo tocca $N^+$, la pendenza $\frac{d\mathcal{E}}{dx}$ diventa ripidissima e **il campo crolla a zero in una frazione di nanometro**, confinando l'alta tensione all'interno del silicio.

Inoltre, il contatto metallico su $N^+$ forma un **contatto ohmico ideale** a bassissima resistenza grazie all'effetto tunnel quantistico.  
👉 Approfondimento: [Contatti Ohmici e Giunzioni High-Low](./Contatti%20Ohmici%20e%20Giunzioni%20High-Low.md).

---

### 5. Applicazioni Principali del Diodo PIN

1. **Interruttori e Attenuatori RF/Microonde:**
   * In inversa ($V_R < 0$), la grande larghezza $W$ rende la capacità parassita di giunzione piccolissima ($C_j = \frac{\varepsilon A}{W} \to 0$), offrendo un isolamento eccellente ad alte frequenze.
   * In diretta ($V_F > 0$), la modulazione di conducibilità azzera la resistenza serie ($R_{ON} \approx 0$), comportandosi come un quasi-corto circuito RF.
2. **Fotorivelatori (Fotodiodo PIN):**
   * L'ampia regione intrinseca $I$ massimizza il volume di cattura ottica per assorbire fotoni e generare coppie $e^-/h^+$. Il campo elettrico costante separa rapidamente le cariche, garantendo elevata velocità di risposta e larghezza di banda.
3. **Dispositivi di Potenza ad Alta Tensione:**
   * Consente di reggere migliaia di Volt in interdizione senza dover gestire le resistenze serie dissipative che avrebbe un semiconduttore convenzionale poco drogato.

---

*Pagine correlate:*
- [Diodo](./Diodo.md)
- [Breakdown e Diodo Zener](./Breakdown%20e%20Diodo%20Zener.md)
- [Contatti Ohmici e Giunzioni High-Low](./Contatti%20Ohmici%20e%20Giunzioni%20High-Low.md)
- [Transitori del diodo e capacita](./Transitori%20del%20diodo%20e%20capacita.md)
- [Condensatori](./Condensatori.md)
- [Siliciuro](../Tecnologia%20e%20Fabbricazione/Siliciuro.md)
- [Difficoltà nel fare un componente ideale](../Scaling%20e%20Limiti%20Fisici/Difficolt%C3%A0%20nel%20fare%20un%20componente%20ideale.md)
