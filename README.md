# Conjugate Priors for Cybersecurity Anomaly Detection

Companion code for the Towards Data Science article  
**"Understanding Conjugate Priors Through Real-World Cybersecurity Data"**

Demonstrates **Dirichlet-Categorical conjugate priors** applied to enterprise authentication anomaly detection on the LANL dataset (1.6 billion events, 749 red team attacks).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gauravchawla/conjugate-priors-cybersecurity/blob/main/notebooks/conjugate_priors_cybersecurity_detection.ipynb)

---

## What This Demonstrates

| Concept | Implementation |
|---------|---------------|
| Dirichlet-Categorical conjugate pair | `DirichletCategorical` class |
| Online Bayesian learning | Single-pass streaming updates |
| Posterior predictive anomaly scoring | −log P(category \| history) |
| Temporal train/test split | Train strictly on pre-attack data |
| Per-computer behavioral fingerprinting | Independent Dirichlet model per host |

**Key results:** AUC-ROC 0.8269, Cohen's d = 1.343 on 29.4M training events.

---

## Repository Structure

```
conjugate-priors-cybersecurity/
├── notebooks/
│   └── conjugate_priors_cybersecurity_detection.ipynb   # Main notebook (Colab-ready)
├── article/
│   └── conjugate_priors_article_tds.md                  # Full article text
├── plots/                                                # Publication figures
│   ├── auth_distribution.png
│   ├── score_distributions.png
│   ├── roc_curve.png
│   ├── pr_curve.png
│   ├── precision_at_k.png
│   ├── alpha_sensitivity.png
│   └── computer_specialization.png
├── data/                                                 # Place LANL files here
├── requirements.txt
└── README.md
```

---

## Dataset

**LANL Comprehensive Multi-Source Cyber-Security Events**  
Download from: https://csr.lanl.gov/data/cyber1/

You need two files:
- `auth.txt.gz` — 1.648 billion authentication events (~25 GB compressed)
- `redteam.txt.gz` — 749 red team attack events

Place both files in `data/`, or update the paths in notebook cell 2.

---

## Running on Google Colab (Recommended)

1. Upload `auth.txt.gz` and `redteam.txt.gz` to Google Drive at `MyDrive/Lanl_login_data/`
2. Click the Colab badge above
3. Run all cells — Drive mounts automatically
4. Expected runtime: **15–20 minutes** on a standard instance (High-RAM recommended)

## Running Locally

```bash
git clone https://github.com/gauravchawla/conjugate-priors-cybersecurity
cd conjugate-priors-cybersecurity
pip install -r requirements.txt
jupyter notebook notebooks/conjugate_priors_cybersecurity_detection.ipynb
```

Update the file paths in notebook cell 2 before running.

---

## The Core Math

```
Prior:   θ ~ Dir(α, α, ..., α)         # uniform — no initial bias
Update:  Dir(α) + counts → Dir(α + n)  # just addition
Score:   −log( (α + n_k) / (α₀ + N) ) # surprisal
```

No gradient descent. No convergence monitoring. Just counting.

---

## Results

| Metric | Value |
|--------|-------|
| AUC-ROC | 0.8269 |
| Average Precision | 0.07 |
| Cohen's d (score separation) | 1.343 |
| Attack mean score | 4.24 |
| Normal mean score | 2.12 |
| Computers modelled | 10,413 |
| Training events | 29.4M |
| Precision@10 | ~40% |

---

## Requirements

Python 3.8+. See `requirements.txt`.  
Minimum 4 GB RAM; 16 GB recommended for the full dataset.

---

## License

MIT — see LICENSE.

---

## Citation

```bibtex
@article{chawla2026conjugate,
  title   = {Understanding Conjugate Priors Through Real-World Cybersecurity Data},
  author  = {Chawla, Gaurav},
  journal = {Towards Data Science},
  year    = {2026},
  url     = {https://github.com/gauravchawla/conjugate-priors-cybersecurity}
}
```
