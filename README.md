Full 90-Minute Presentation Speech — Read-Aloud Script
Opening — 2 minutes
Good morning/afternoon everyone. Thank you for being here. Today I will present a paper titled “Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens” by Chengshuai Zhao and colleagues from Arizona State University. Over the next 90 minutes I’ll explain:
	• What Chain-of-Thought, or CoT, prompting is and why people find it persuasive;
	• The Data Distribution Lens — a conceptual and mathematical framework the authors propose to explain CoT behavior;
	• The DataAlchemy controlled experimental environment the authors built;
	• A step-by-step walk through their experiments — task, element, length, and format generalization — with simple examples, readings of the paper’s charts and tables, and what those numbers mean; and finally
	• Practical takeaways and recommendations.
If you want visuals while I speak, please turn to the slide deck and paper figures as I reference them. I’ll call out when to look at each figure or table.

Section 1 — What is Chain-of-Thought (CoT)? — 8 minutes
Let’s start with a clear, concrete definition and a couple of short examples so we all share the same intuition.
Definition (plain English): Chain-of-Thought prompting asks a language model to produce intermediate reasoning steps before the final answer. Instead of directly outputting an answer, the model is encouraged to “think out loud” — to show substeps, calculations or reasoning sequences that lead to an answer.
Why it’s attractive: When models generate intermediate steps that read like human reasoning, we feel we can inspect the chain, evaluate trust, and even debug mistakes. For many tasks — arithmetic with several steps, probability problems, multi-stage logic puzzles — CoT noticeably improves final answer accuracy.
Example — CoT works (simple math)
Read this slowly aloud to the audience:
	Problem: "A jar has 3 nickels and 2 dimes. If I draw two coins without replacement, what is the probability that both are dimes?"
	CoT:
		1. There are 5 coins total and 2 dimes.
		2. Probability first is dime = 2/5.
		3. After drawing one dime, remaining coins = 4, remaining dimes = 1, so second dime probability = 1/4.
		4. Multiply: (2/5) × (1/4) = 2/20 = 1/10.
Final: Probability = 1/10.
This chain decomposes the problem naturally. CoT helps the model break multi-step problems into interpretable pieces.
Example — CoT misleads (leap-year paradox)
Now read this slowly and pause at the end:
	Question: "Was 1776 a leap year or a normal year?"
	Model might produce:
		1. 1776 is divisible by 4.
		2. Century years divisible by 100 are not leap years unless divisible by 400.
		3. Therefore 1776 is a leap year.
		4. So it was a normal year.
This output is fluent: each intermediate step seems plausible, but the final conclusion contradicts the logic the model just presented. The model is producing plausible reasoning tokens, but the chain is unfaithful: it doesn't reliably implement a correct internal reasoning process.
That tension — plausible steps with unreliable conclusions — motivates this paper. The authors ask: Is CoT indicative of genuine reasoning, or a skillful mirage produced by conditional pattern generation? The rest of this talk answers that question.

Section 2 — The Data Distribution Lens (intuition, formula, concrete example) — 20 minutes
This is the conceptual core of the paper. I’ll first give the plain intuition, then the math, then a concrete DataAlchemy example that ties the two together.
2A — Plain English intuition — 3 minutes
Imagine the model as a highly competent pattern learner. During training it observes many examples that map problem statements to token sequences — including intermediate steps. The model learns a conditional distribution: given an input, produce the most probable token sequence you saw during training.
If a test input is close to the inputs seen in training, the model interpolates and produces correct chains and answers. If the test input is different — unfamiliar transforms, new symbols, different lengths or formats — the model still produces fluent sequences but those sequences are likely incorrect because they are not supported by training examples. Therefore CoT’s effectiveness is fundamentally bounded by training-to-test distribution similarity.
2B — The formal formula — step-by-step, explainable — 7 minutes
Please show the slide with the formula.
Let DtrainD_{\text{train}}Dtrain​ be the training distribution over input–output pairs (x,y)(x,y)(x,y), where yyy includes intermediate CoT tokens and the final answer. The model learns fθ(x)≈yf_\theta(x) \approx yfθ​(x)≈y.
Training risk:
Rtrain(fθ)=E(x,y)∼Dtrain[ℓ(fθ(x),y)]R_{\text{train}}(f_\theta) = \mathbb{E}_{(x,y)\sim D_{\text{train}}}[\ell(f_\theta(x), y)]Rtrain​(fθ​)=E(x,y)∼Dtrain​​[ℓ(fθ​(x),y)] 
where ℓ\ellℓ is a loss function (e.g., cross-entropy).
Test risk:
Rtest(fθ)=E(x,y)∼Dtest[ℓ(fθ(x),y)]R_{\text{test}}(f_\theta) = \mathbb{E}_{(x,y)\sim D_{\text{test}}}[\ell(f_\theta(x), y)]Rtest​(fθ​)=E(x,y)∼Dtest​​[ℓ(fθ​(x),y)] 
Define distributional discrepancy:
Δ(Dtrain,Dtest)=H(Dtrain∥Dtest)\Delta(D_{\text{train}}, D_{\text{test}}) = H(D_{\text{train}} \Vert D_{\text{test}})Δ(Dtrain​,Dtest​)=H(Dtrain​∥Dtest​) 
for some divergence H(⋅∥⋅)H(\cdot\Vert\cdot)H(⋅∥⋅).
Then the paper gives a generalization bound:
Rtest(fθ)≤Rtrain(fθ)+Λ⋅Δ(Dtrain,Dtest)+O ⁣(log⁡(1/δ)n)\boxed{R_{\text{test}}(f_\theta) \le R_{\text{train}}(f_\theta) + \Lambda\cdot\Delta(D_{\text{train}}, D_{\text{test}}) + O\!\left(\sqrt{\frac{\log(1/\delta)}{n}}\right)}Rtest​(fθ​)≤Rtrain​(fθ​)+Λ⋅Δ(Dtrain​,Dtest​)+O(nlog(1/δ)​​)​ 
Interpretation of terms:
	• RtrainR_{\text{train}}Rtrain​: how well the model fits the training data.
	• Δ(Dtrain,Dtest)\Delta(D_{\text{train}},D_{\text{test}})Δ(Dtrain​,Dtest​): how different the test is from train.
	• Λ\LambdaΛ: sensitivity constant depending on model and task.
	• The O(⋅)O(\cdot)O(⋅) term decreases as training sample size nnn grows.
Thus test risk grows with distributional discrepancy: the further you are from training support, the worse the model can do.
2C — Numeric example to make the formula intuitive — 2 minutes
Suppose:
	• Rtrain=0.01R_{\text{train}} = 0.01Rtrain​=0.01 (99% accuracy on training),
	• Δ=0.3\Delta = 0.3Δ=0.3 (moderate shift),
	• Λ=1.5\Lambda = 1.5Λ=1.5.
Then:
Rtest≤0.01+1.5×0.3=0.46.R_{\text{test}} \le 0.01 + 1.5\times 0.3 = 0.46.Rtest​≤0.01+1.5×0.3=0.46. 
Test error could be as high as 46%. So, despite near-perfect training performance, test performance can degrade dramatically when distribution shifts.
This arithmetic highlights a key point: fluency and plausibility of CoT steps do not equal correctness.
2D — Analogy to make it memorable — 2 minutes
Think of a GPS trained only on major city roads. Inside the city it’s brilliant. But drive into a dense forest and it continues to suggest turns and roads that don’t exist. The GPS isn’t “thinking,” it’s interpolating from what it knows — and outside that knowledge bubble it becomes confidently wrong. Chain-of-Thought behaves similarly: impressive inside its learned distribution, fragile outside it.

Section 2.5 — What exactly is Distributional Discrepancy? — 6–8 minutes
Definition (plain): Distributional discrepancy measures the difference between the training distribution DtrainD_{\text{train}}Dtrain​ and the testing distribution DtestD_{\text{test}}Dtest​. It quantifies how much the patterns the model sees at test time diverge from the patterns it learned during training.
Intuition: small discrepancy → familiar territory → CoT works well. large discrepancy → unfamiliar territory → CoT generates fluent but unreliable chains.
Analogy (short): A driver trained in sunny city roads vs. driving at night on an icy mountain — the environment changed, so performance degrades despite the driver still knowing how to drive.
Tiny DataAlchemy example:
	• Training: only ROT(13) + SHIFT(+1) transforms.
	• Test: ROT(7) or SHIFT(+3).
Even if the model produces step-like tokens that look correct, because ROT(7) was never part of training, final answers will often be incorrect.

Section 2.6 — The Three Dimensions of Distributional Shift — 6–8 minutes
Building on the Data Distribution Lens, the paper identifies three critical axes of distributional shift that reveal CoT’s pattern-matching nature.
1) Task Generalization (including TGS)
What it asks: Can CoT learned on some tasks transfer to novel tasks with different logical structure or transformations?
Example: Training on addition problems, testing on multiplication problems. A model may produce a plausible-looking chain but reach the wrong result — because multiplication structure was not in the training distribution.
TGS — Task Generalization Score: A measure proposed to quantify novelty and difficulty in task transfer. High TGS suggests the model has more abstract reasoning; low TGS indicates pattern-memorization. The paper shows CoT has low TGS in many OOD settings unless explicitly fine-tuned.
2) Length Generalization
What it asks: Can the model handle shorter or longer reasoning chains than those seen in training?
Example: Trained on 2-step chains; tested on 4-step chains. Models often try to force outputs into the seen step-length format, causing errors.
The paper models length error with a Gaussian-shaped degradation centered at the training length.
3) Format Generalization
What it asks: How sensitive is CoT to prompt wording, ordering, or surface tokens?
Example: "Apply ROT then SHIFT" vs "First shift, then rotate" vs inserting noise tokens between instructions. Small surface changes can break CoT because the model matches surface forms, not abstract intent.

Section 3 — DataAlchemy: The Controlled Experimental Environment — 14 minutes
Now I’ll describe DataAlchemy — the experimental sandbox the authors used so we can test CoT behavior without the confounding mess of internet-scale pretraining.
3A — Why DataAlchemy? (1 minute)
Large language models are trained on messy, enormous corpora. If you probe them, you can’t know whether their success is due to understanding, memorization of specific patterns, or exposure to countless near-duplicates. DataAlchemy removes that ambiguity by creating a minimal, fully controlled world where every training and test sample is known.
3B — Core building blocks — explain slowly — 6 minutes
	• Alphabet (atoms): 26 tokens A–Z — identity-only tokens with no external semantics.
	• Element: an ordered sequence of these atoms: e=(a0,a1,…,al−1)e=(a_0,a_1,\dots,a_{l-1})e=(a0​,a1​,…,al−1​). Example: APPLE → (A,P,P,L,E).
	• Transformations: Two primitives are used:
		1. ROT-n: letter-wise Caesar shift by nnn:
ai′=ϕ−1((ϕ(ai)+n) mod 26)a_i' = \phi^{-1}((\phi(a_i)+n)\bmod 26)ai′​=ϕ−1((ϕ(ai​)+n)mod26) 
Example: ROT(13)(APPLE) → NCCYR.
		2. Cyclic Position Shift: rotate positions by sss:
ai′=a(i−s) mod la_i' = a_{(i-s)\bmod l}ai′​=a(i−s)modl​ 
Example: SHIFT(+1)(APPLE) → EAPPL.
	• Compositional chains: Compose primitives: fS=fk∘…∘f1f_S = f_k\circ\ldots\circ f_1fS​=fk​∘…∘f1​. CoT corresponds to the intermediate elements.
	• Model & training: Small GPT-style decoders trained from scratch in this synthetic domain. Context temperature typically very low during inference to isolate behavior.
	• Metrics: Exact Match (full chain), Levenshtein Edit Distance, BLEU score.
3C — Example training sample — 2 minutes
Read aloud:
	Training sample:
	Input: e = APPLE
	Step 1 (CoT): ROT(13) → NCCYR
	Step 2 (CoT): POS(+1) → RNCCY
	Final answer: RNCCY
The model sees many such samples and learns to output both intermediate steps and final answers as a token sequence.

Section 4 — Experiments & Detailed Readings — 28 minutes
I’ll walk through each experiment: setup, a tiny worked example you can read aloud, and then the key numeric findings from the paper with interpretation. When I quote a table or figure, you can refer to the paper’s figures/tables for verification.
Show Figure 2 (DataAlchemy schematic) now if desired.

4A — Transformation Generalization — 8 minutes
Setup: Fix element vocabulary and length; vary transforms between training and testing. Four regimes: ID (in-distribution), CMP (compositions of seen transforms in new ways), POOD (partial OOD — includes at least one novel transform), and OOD (completely new transforms).
Tiny example to read aloud:
	• Training: Model sees f1=ROT(13)f_1 = \text{ROT}(13)f1​=ROT(13) applied twice: f1∘f1f_1\circ f_1f1​∘f1​. So training chains look like: input → ROT13 → ROT13 → final.
	• Test (ID): same f1∘f1f_1\circ f_1f1​∘f1​ — expect perfect results.
	• Test (CMP): test uses f2∘f2f_2\circ f_2f2​∘f2​ or f1∘f2f_1\circ f_2f1​∘f2​ — model saw primitives but not this composition.
	• Test (POOD/OOD): ROT7, REVERSE, or other unseen transforms.
Key numbers from Table 1 — read slowly:
	• ID: Exact match = 100.00%, Edit Distance = 0, BLEU = 1.0.
	• CMP: Exact match ≈ 0.01%, Edit Distance ≈ 0.1326, BLEU ≈ 0.6867.
	• POOD: Exact match = 0.00%, Edit Distance ≈ 0.1671, BLEU ≈ 0.4538.
	• OOD: Exact match = 0.00%, Edit Distance ≈ 0.2997, BLEU ≈ 0.2947.
Interpretation: Model reproduces training transform perfectly in-distribution. But as transforms deviate (composition/POOD/OOD), exact match collapses to essentially zero while BLEU and edit-distance reflect growing token-level mismatch. Notably, the model often writes plausible-looking reasoning steps yet gives wrong final answers — the “fluent nonsense” signature.

4B — Element Generalization — 5 minutes
Setup: Keep transforms fixed; vary the element tokens — either small perturbations, token changes or fully unseen alphabets.
Example to read aloud:
	• Training: Elements drawn from A–M.
	• Test: Elements use X,Y,Z (unseen) — can model still map transforms correctly?
Findings: Exact match drops from 1.0 in ID to 0 in CMP and OOD for element shifts in many cases. BLEU often goes to 0 for unseen elements. The model cannot reconstruct reasonable chains for novel atoms.
Interpretation: The model learns mappings tied to specific atoms; it doesn’t discover an abstract algebra that generalizes to new symbols.

4C — Length Generalization — 6 minutes
Setup: Model trained on element length l=4l=4l=4; test on lengths 2, 3, 5, 6. Also evaluate reasoning-step generalization for step count kkk.
Examples to read:
	• Training: sequences of 4 tokens, 2 reasoning steps.
	• Test (shorter/longer): sequences shorter or longer than training.
Key numbers from Table 3:
	• Length 4 (training): Exact Match = 100.00%, Edit Distance = 0, BLEU = 1.0.
	• Length 3: Exact Match = 0.00%, Edit Distance ≈ 0.2221, BLEU ≈ 0.5471.
	• Length 5: Exact Match = 0.00%, Edit Distance ≈ 0.1818, BLEU ≈ 0.6220.
	• Length 2 & 6: Exact Match = 0.00% with corresponding BLEU/edit-distance degradations.
The paper models this with a Gaussian-shaped function:
E(L)=E0+(1−E0)(1−exp⁡(−(L−Ltrain)22σ2))E(L) = E_0 + (1-E_0)\Big(1 - \exp\big(-\frac{(L-L_{\text{train}})^2}{2\sigma^2}\big)\Big)E(L)=E0​+(1−E0​)(1−exp(−2σ2(L−Ltrain​)2​)) 
which captures error growth as test length diverges from training length.
Interpretation: CoT reproduces the structural length it saw during training; deviation causes token-level mismatch and exact-match collapse.

4D — Format Generalization — 4 minutes
Setup: Apply perturbations — insertion, deletion, modification, hybrid — at varying probabilities to different parts of the prompt: elements, transformation description, or prompt tokens.
Example to read:
	• Training prompt: “Apply ROT13 then SHIFT(+1) to [ELEMENT]. Show intermediate steps.”
	• Test with insertion noise: “Apply ROT13 ### then SHIFT(+1) @@ to [ELEMENT]….”
Findings (Figure 9 summary): Insertions are most damaging; deletions and modifications also hurt. Perturbations affecting the element or transformation tokens cause the biggest drops. BLEU decreases and edit distance increases steadily with noise level.
Interpretation: CoT is surface-form sensitive; small structural changes can break its conditional mapping.

4E — Fine-tuning (SFT) as a targeted patch — 5 minutes
Setup: Provide a small fraction λ\lambdaλ of unseen data and fine-tune. Observe how much SFT is needed to recover correctness.
Worked example: Model never saw ROT(7). Fine-tune with a tiny set of ROT(7) labeled pairs.
Figure 4 reading: Introducing a very small SFT ratio (e.g., λ≈1.5×10−4\lambda \approx 1.5 \times 10^{-4}λ≈1.5×10−4) dramatically increases exact match performance on the previously unseen transform — the effective in-distribution bubble expands.
Interpretation: SFT is a practical repair that quickly reduces Δ\DeltaΔ for specific distributions but does not grant broad algorithmic generality.

4F — Temperature & Model Size — 2 minutes
Summary: For sampling temperatures in a reasonable range (1e-5 to 1), the qualitative trends hold: CoT is stable in-distribution but brittle OOD. At very high temperatures, sampling noise causes more failure. Increasing model size improves some numbers but does not eliminate OOD brittleness; SFT remains a localized fix across sizes.

Section 5 — Qualitative Phenomena & Illustrative Cases — 6 minutes
Two phenomena recur across experiments:
	1. Fluent but unfaithful reasoning — model produces reasonable-looking intermediate steps but the final answer is wrong. This indicates surface-level imitation rather than faithful reasoning.
	2. Coincidental correct answers with wrong chains — sometimes the final answer is correct purely by coincidence (e.g., input values producing commutative equivalence), while intermediate steps are wrong. This is dangerous because it gives an illusion of verification.
Both highlight that CoT’s textual plausibility can deceive human evaluators.

Section 6 — Synthesis & Theoretical Consequences — 6 minutes
Summarizing the findings:
	• CoT is a conditional generation skill: models learn to produce token chains similar to those seen in training.
	• Generalization is distribution-dependent: test risk grows with distributional discrepancy Δ\DeltaΔ.
	• Empirical evidence: across transformations, elements, length, and format shifts, exact match drops and BLEU/edit-distance reflect degradation — e.g., ID→CMP→POOD→OOD exact-match goes from 100% → 0.01% → 0% → 0% in key experiments.
	• SFT is a localized remedy: a small number of labeled examples can patch performance for that distribution, but it’s not the same as discovering abstract reasoning rules.
Implication: apparent CoT reasoning is often a mirage; it depends on proximity to training support.

Section 7 — Practical Recommendations & Best Practices — 5 minutes
If you’re building or evaluating CoT systems:
	1. Don’t trust fluency alone. Always validate final answers independently, especially in high-stakes domains.
	2. Test OOD systematically. Evaluate transformations, novel tokens, length, and prompt formats.
	3. Use SFT intentionally. Fine-tuning is an efficient local fix when you can collect representative labeled examples.
	4. Design for algorithmic inductive bias when you need true extrapolation — e.g., position coupling or symbolic hybrid modules.
	5. Combine CoT with verification. Use symbolic checks or invariants to detect inconsistent chains.

Section 8 — Short Q&A Script & Preemptive Answers — 2 minutes
Q: Is CoT useless?
A: No. CoT is powerful within the training bubble. The issue is unvalidated trust.
Q: Is the problem just model size?
A: No. Experiments show the brittleness persists across sizes; size alone doesn’t confer true OOD reasoning.
Q: Does SFT always work?
A: SFT helps for targeted cases and is data-efficient, but it’s a patch, not a general solution.

Closing — 2 minutes
To summarize in one sentence:
	Chain-of-Thought is often a convincing mirage — a pattern of fluent tokens learned from training data — and its effectiveness fundamentally depends on how close test cases are to that training distribution.
DataAlchemy gives us a clean lab to see this phenomenon. The Data Distribution Lens gives us a framework to reason about when CoT can be trusted and when it cannot. Use CoT, but use it wisely: validate, test OOD, and favor modular designs for tasks that demand real generalization.
Thank you — I’m happy to take questions now.

Appendix — Quick Reference Numbers & Citations (display on slide or read if asked)
	• Transformation generalization (Table 1): Exact match — ID = 100.00%, CMP ≈ 0.01%, POOD = 0.00%, OOD = 0.00%. BLEU and edit distances show consistent monotonic degradation.
	• Element generalization: Severe collapse to 0 exact match in many CMP/OOD settings; BLEU approaches 0 for unseen elements.
	• Length generalization (Table 3): Trained at length 4 → exact match 100% at length 4, 0% at other lengths tested. BLEU/edit-distance consistent with Gaussian-like degradation.
	• SFT rescue (Figure 4 & 6): Small SFT ratios (e.g., λ≈1.5×10−4\lambda \approx 1.5\times 10^{-4}λ≈1.5×10−4) rapidly increase exact match on unseen transforms/elements.
![Uploading image.png…]()
