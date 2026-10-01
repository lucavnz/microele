Viewed richelli_basic_block_3.pdf:1-800
Ran command: `python3 -c "
import pypdf
print('pypdf installed')
" 2>/dev/null || python3 -c "
import fitz
print('fitz installed')
" 2>/dev/null || echo "neither"`
Ran command: `which pdftoppm || which sips`
Ran command: `python3 -c "
import Quartz
print('Quartz available')
" 2>/dev/null || echo "No Quartz"`
Ran command: `python3 -c "
import pypdf
reader = pypdf.PdfReader('richelli_basic_block_3.pdf')
page = reader.pages[1] # page 2 (0-indexed)
print('Images count:', len(page.images))
for i, img in enumerate(page.images):
    print(img.name, type(img))
    with open(f'page2_img_{i}.png', 'wb') as f:
        f.write(img.data)
print('Done')
"`
Ran command: `python3 -c "
from PIL import Image
im = Image.open('page2_img_0.png')
print('Dimensions:', im.size)
"`
Ran command: `python3 -c "
from PIL import Image
im = Image.open('page2_img_0.png')
w, h = im.size
# Let's crop c and d
# c is roughly in the 3rd quarter horizontally, d in the 4th quarter
c_crop = im.crop((int(w * 0.48), 0, int(w * 0.75), h))
d_crop = im.crop((int(w * 0.70), 0, w, h))

c_crop.save('/Users/matteoluca/.gemini/antigravity-ide/brain/2cf92a56-7161-4ba8-be57-540e54a5ef00/scratch/circuit_c.png')
d_crop.save('/Users/matteoluca/.gemini/antigravity-ide/brain/2cf92a56-7161-4ba8-be57-540e54a5ef00/scratch/circuit_d.png')
print('Saved crops')
"`
Viewed circuit_c.png:1-800
Viewed circuit_d.png:1-800
Ran command: `python3 -c "
from PIL import Image
im = Image.open('page2_img_0.png')
w, h = im.size
ab_crop = im.crop((0, 0, int(w * 0.52), h))
ab_crop.save('/Users/matteoluca/.gemini/antigravity-ide/brain/2cf92a56-7161-4ba8-be57-540e54a5ef00/scratch/circuit_ab.png')
"`
Viewed circuit_ab.png:1-800
Ran command: `python3 -c "
from PIL import Image
im = Image.open('page2_img_0.png')
w, h = im.size
d_zoom = im.crop((int(w * 0.68), int(h * 0.1), int(w * 0.98), int(h * 0.9)))
d_zoom.save('/Users/matteoluca/.gemini/antigravity-ide/brain/2cf92a56-7161-4ba8-be57-540e54a5ef00/scratch/circuit_d_zoom.png')
c_zoom = im.crop((int(w * 0.45), int(h * 0.1), int(w * 0.72), int(h * 0.9)))
c_zoom.save('/Users/matteoluca/.gemini/antigravity-ide/brain/2cf92a56-7161-4ba8-be57-540e54a5ef00/scratch/circuit_c_zoom.png')
print('Zoomed saved')
"`
Viewed circuit_d_zoom.png:1-800
Viewed circuit_c_zoom.png:1-800
Viewed cose.md:1-100
Viewed Stadi%20elementari.md:1-100
Viewed Stadi%20elementari.md:101-188
Ran command: `python3 -c "
import sympy as sp

vx, vs, ix = sp.symbols('vx vs ix', real=True)
gm1, gm3, ro1, ro3 = sp.symbols('gm1 gm3 ro1 ro3', positive=True)

# KCL at Drain of M3 (Node X):
# ix enters Node X.
# Current flowing into Drain of M3:
# i_D3 = gm3*(vg3 - vs) + (vx - vs)/ro3, where vg3 = 0.
# So i_D3 = -gm3*vs + (vx - vs)/ro3.
# Since ix enters and i_D3 leaves into M3: ix = i_D3.
eq1 = sp.Eq(ix, -gm3*vs + (vx - vs)/ro3)

# KCL at Source of M3 / Drain of M1 (Node S):
# Current entering from M3 is i_D3 = ix.
# Current leaving into Drain of M1:
# i_D1 = gm1*(vg1 - vs1) + (vd1 - vs1)/ro1, where vg1 = vx, vs1 = 0, vd1 = vs.
# So i_D1 = gm1*vx + vs/ro1.
# KCL at Node S: ix = i_D1.
eq2 = sp.Eq(ix, gm1*vx + vs/ro1)

sol = sp.solve([eq1, eq2], [vx, vs])
Rin = sp.simplify(sol[vx] / ix)
vs_over_ix = sp.simplify(sol[vs] / ix)

print('Rin =', Rin)
print('vs / ix =', vs_over_ix)

# Numerical test with typical values:
# gm1 = gm3 = 1 mA/V = 1e-3 S
# ro1 = ro3 = 50 kOhm = 50e3 Ohm
vals = {gm1: 1e-3, gm3: 1e-3, ro1: 50e3, ro3: 50e3}
print('Numerical Rin:', Rin.subs(vals).evalf())
print('1/gm1 =', (1/gm1).subs(vals).evalf())
print('Numerical vs/ix:', vs_over_ix.subs(vals).evalf())
"`
Ran command: `python3 -c "
# Let's solve symbolically with basic algebra or numerically with numpy:
import numpy as np

# System of equations:
# eq1: vx * (1/ro3) + vs * (-gm3 - 1/ro3) = ix
# eq2: vx * (gm1)   + vs * (1/ro1)        = ix

# In matrix form A * [vx, vs]^T = [ix, ix]^T
# A = [[1/ro3, -gm3 - 1/ro3],
#      [gm1,   1/ro1]]

gm1 = 1e-3
gm3 = 1e-3
ro1 = 50e3
ro3 = 50e3

A = np.array([
    [1/ro3, -gm3 - 1/ro3],
    [gm1, 1/ro1]
])

b = np.array([1.0, 1.0])
sol = np.linalg.solve(A, b)
vx, vs = sol[0], sol[1]

print('vx (Rin) =', vx)
print('1/gm1    =', 1/gm1)
print('vs       =', vs)
print('Relative error to 1/gm1:', (vx - 1/gm1) / (1/gm1))
"`

Per rispondere in modo chiaro e immediato alla tua domanda:

* **Nel circuito c): SÌ, l'impedenza vista è esattamente la somma:**
  $$R_{in, c} \approx \frac{1}{g_{m1}} + \frac{1}{g_{m3}}$$
* **Nel circuito d): NO! L'impedenza vista NON è la somma, ma vale semplicemente:**
  $$R_{in, d} \approx \frac{\mathbf{1}}{\mathbf{g_{m1}}}$$
  (il termine $1/g_{m3}$ **non compare** nella somma).

Vediamo in dettaglio perché, analizzando entrambi i circuiti sia in modo intuitivo che analitico (a piccolo segnale).

---

### 1. Circuito c) — Specchio cascode a diodi impilati (*Stacked Diodes*)

Nel circuito **c)**:
* **M1** ha Source a massa ($0\,\text{V}$) e Drain cortocircuitato al proprio Gate (connessione a diodo). L'impedenza vista guardando nel drain di M1 verso massa è:
  $$r_{diodo,1} = \frac{1}{g_{m1}} \parallel r_{o1} \approx \frac{1}{g_{m1}}$$
* **M3** ha il Source collegato al drain di M1, e il Drain cortocircuitato al proprio Gate (anch'esso connesso a diodo). L'impedenza propria del bipolo a diodo M3 è:
  $$r_{diodo,3} = \frac{1}{g_{m3}} \parallel r_{o3} \approx \frac{1}{g_{m3}}$$

Poiché i gate non assorbono corrente a bassa frequenza, una corrente di test $i_x$ che entra dall'alto (drain di M3) deve attraversare **in serie** prima il diodo M3 e poi il diodo M1 verso massa:
$$v_x = v_{DS3} + v_{DS1} = i_x \cdot \left(\frac{1}{g_{m3}}\right) + i_x \cdot \left(\frac{1}{g_{m1}}\right)$$

Da cui l'impedenza d'ingresso complessiva:
$$R_{in, c} = \frac{v_x}{i_x} \approx \mathbf{\frac{1}{g_{m3}} + \frac{1}{g_{m1}}}$$

*(Se consideriamo anche l'effetto body su M3, con bulk a massa, diventa $\frac{1}{g_{m3} + g_{mb3}} + \frac{1}{g_{m1}}$).*

> **Nota di polarizzazione DC (visibile sulla slide):**
> Sul drain di M3 a riposo hai la somma di due $V_{GS}$:
> $$V_{in} = V_{GS1} + V_{GS3} = (V_T + \Delta V) + (V_T + \Delta V) = 1.3\,\text{V} + 1.3\,\text{V} = \mathbf{2.6\,\text{V}}$$
> che è esattamente il valore **$2{,}6$** scritto a matita sopra il circuito nella slide!

---

### 2. Circuito d) — Specchio cascode con polarizzazione $V_B$ separata

Nel circuito **d)** la topologia del ramo di riferimento cambia radicalmente:
1. **M3 NON è a diodo:** il Gate di M3 è collegato alla tensione DC fissa $V_B$, che a piccolo segnale è una **massa AC** ($v_{g3} = 0$). M3 lavora quindi come stadio a **Gate Comune (CG)**.
2. Il nodo d'ingresso (Drain di M3) è collegato direttamente al **Gate di M1** (e di M2).

#### Perché l'impedenza diventa $\approx 1/g_{m1}$?

##### Spiegazione intuitiva (anello di retroazione):
* Quando inietti una corrente $i_x$ nel nodo d'ingresso (drain di M3, tensione $v_x$), quella tensione $v_x$ comanda il Gate di **M1**.
* Aumentando $v_x$, M1 tende ad assorbire una corrente pari a $i_{D1} \approx g_{m1} v_x$.
* Il transistor M3 è un **Gate Comune** interposto tra il nodo d'ingresso e il drain di M1: il gate comune agisce da **buffer di corrente** a guadagno unitario ($A_i \approx 1$). Tutta la corrente richiesta da M1 al suo drain viene "pescata" direttamente dal nodo d'ingresso attraverso M3.
* Si chiude un anello di **retroazione negativa forte**: la corrente assorbita dal nodo è imposta direttamente da M1:
  $$i_x \approx g_{m1} v_x \implies R_{in, d} = \frac{v_x}{i_x} \approx \mathbf{\frac{1}{g_{m1}}}$$

---

#### Dimostrazione analitica rigorosa (con le resistenze $r_o$)

Scriviamo le equazioni di Kirchhoff ai nodi a piccolo segnale:
* Al nodo d'ingresso $X$ (Drain di M3, Gate di M1), con Gate di M3 a massa AC ($v_{g3} = 0$) e $v_S$ tensione sul source di M3:
  $$i_x = g_{m3}(0 - v_S) + \frac{v_x - v_S}{r_{o3}} = -g_{m3} v_S + \frac{v_x - v_S}{r_{o3}}$$
* Al nodo intermedio $S$ (Drain di M1, Source di M3), con Gate di M1 a tensione $v_x$ e Source di M1 a massa:
  $$i_x = g_{m1} v_x + \frac{v_S}{r_{o1}}$$

Risolvendo il sistema rispetto a $v_x$ e calcolando il rapporto $v_x / i_x$:
$$R_{in, d} = \frac{r_{o1} + r_{o3} + g_{m3} r_{o1} r_{o3}}{1 + g_{m1} r_{o1} + g_{m1} g_{m3} r_{o1} r_{o3}}$$

Essendo i transistor con guadagno intrinseco elevato ($g_m r_o \gg 1$), a numeratore domina $g_{m3} r_{o1} r_{o3}$ e a denominatore domina $g_{m1} g_{m3} r_{o1} r_{o3}$:
$$R_{in, d} \approx \frac{g_{m3} r_{o1} r_{o3}}{g_{m1} g_{m3} r_{o1} r_{o3}} = \mathbf{\frac{1}{g_{m1}}}$$

---

### Tabella di sintesi a confronto

| Parametro | Circuito c) (Stacked Diodes) | Circuito d) (Cascode con $V_B$) |
| :--- | :--- | :--- |
| **Connessione M3** | A diodo ($D_3 \to G_3$) | Gate Comune ($G_3 \to V_B$) |
| **Connessione Gate M1** | Al proprio drain ($D_1 \to G_1$) | Al drain di M3 ($D_3 \to G_1$) |
| **Impedenza ramo sinistro ($R_{in}$)** | $\mathbf{\approx \frac{1}{g_{m1}} + \frac{1}{g_{m3}}}$ | $\mathbf{\approx \frac{1}{g_{m1}}}$ |
| **Tensione DC nodo d'ingresso** | $V_{GS1} + V_{GS3} = \mathbf{2.6\,\text{V}}$ | $V_{GS1} = \mathbf{1.3\,\text{V}}$ *(risparmi $1.3\,\text{V}$ di headroom!)* |
| **Impedenza ramo d'uscita ($R_{out}$)** | $\approx g_{m4} r_{o4} r_{o2}$ | $\approx g_{m4} r_{o4} r_{o2}$ |