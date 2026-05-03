# Conjugate Priors Cybersecurity Project - Context for Claude Code

## Project Overview
Educational article + runnable notebook demonstrating **Dirichlet-Categorical conjugate priors** for cybersecurity anomaly detection using the LANL authentication dataset (1.6B events).

## Goal
Submit to **Towards Data Science** (Medium) - educational article showing mathematical elegance of conjugate priors through real-world application.

## Current Status ✅
- [x] Complete mathematical theory developed
- [x] Full implementation created and tested
- [x] Jupyter notebook ready for Colab
- [x] Article drafted with plot placeholders
- [ ] **CURRENT TASK**: Refine files, run experiments, generate plots

## Mathematical Framework
**Core Model**: Two Dirichlet-Categorical conjugate pairs per computer:
1. Authentication type patterns: θ_auth^(c) ~ Dir(α,α,α,α)
2. User access patterns: θ_user^(c) ~ Dir(α,α,...,α)

**Update Rule**: Dir(α) + observed_counts → Dir(α + counts)  
**Anomaly Score**: -log(posterior_predictive_probability)  
**Prior Choice**: α = 1 (uniform prior) - no domain bias, minimal influence

## Dataset Details
- **LANL Comprehensive Multi-Source Cyber-Security Events**
- 1.648B authentication events over 58 days
- 749 red team attacks, 12,425 users, 17,684 computers
- Features used: auth_type, source_user, dest_computer, timestamp

## Key Implementation Decisions Made
1. **Temporal split**: Train only on pre-attack data (realistic deployment)
2. **Computer-window labeling**: Any access to compromised computers during attack period = suspicious
3. **Global + local models**: Per-computer models with global fallback
4. **Score combination**: Arithmetic mean of auth_score and user_score

## File Structure
```
notebooks/
  └── conjugate_priors_cybersecurity_detection.ipynb  # Complete runnable implementation
article/
  └── conjugate_priors_article_tds.md                 # Article with plot placeholders
data/
  └── (LANL dataset - user provides)
plots/
  └── (Generated from notebook runs)
```

## Performance Achieved
- **AUC-ROC**: ~0.724 (significantly above random 0.5)
- **Training**: 29.4M events, 10,413 computer models
- **Clear score separation**: Attack (8.23) vs Normal (5.41) mean scores
- **Cohen's d**: 1.342 (large effect size)

## Key Classes Implemented
1. **DirichletCategorical**: Core conjugate prior math
2. **EnterpriseAuthDetector**: Multi-signal anomaly detection
3. **Complete pipeline**: Data loading → Training → Evaluation → Plotting

## Next Steps
- Refine notebook for better Colab experience
- Generate high-quality plots for article
- Test different α values experimentally
- Add more detailed analysis sections
- Prepare for GitHub publication

## Important Notes for Claude Code
- Focus on **educational clarity** over performance optimization
- Mathematical rigor important - this demonstrates Bayesian theory
- Code should be **self-contained** and **reproducible**
- Article should emphasize **mathematical elegance** of conjugate priors
- Target audience: ML practitioners wanting to understand Bayesian methods

## Article Plot Placeholders to Fill
1. Authentication patterns distribution
2. ROC curve  
3. Precision-Recall curve
4. Score distribution histograms
5. Precision@K operational metrics
6. Computer specialization examples

## Mathematical Notation Established
- θ: probability parameters (Dirichlet distributed)
- α: prior pseudo-counts (chosen = 1.0)
- n: observed category counts
- P(x=k|data) = (α_k + n_k)/(α_0 + N): posterior predictive
- Score = -log(probability): anomaly measure
