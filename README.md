# Conjugate Priors for Cybersecurity Anomaly Detection

*Demonstrating the mathematical elegance of Dirichlet-Categorical conjugate priors through real-world enterprise authentication data*

## 🎯 Overview

This project showcases how **conjugate priors** - a 250-year-old mathematical concept - can solve modern cybersecurity challenges with remarkable elegance. Using the LANL cybersecurity dataset (1.6 billion authentication events), we demonstrate that sometimes the most sophisticated solution is also the most mathematically principled one.

## 📚 Educational Article

**[Understanding Conjugate Priors Through Real-World Data](article/conjugate_priors_article_tds.md)**

Published on Towards Data Science, this article covers:
- Bayesian inference fundamentals  
- Mathematical framework of conjugate priors
- Dirichlet-Categorical conjugate pairs
- Real-world anomaly detection application
- Performance analysis and insights

## 🚀 Interactive Notebook

**[Complete Implementation](notebooks/conjugate_priors_cybersecurity_detection.ipynb)**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-USERNAME/YOUR-REPO/blob/main/notebooks/conjugate_priors_cybersecurity_detection.ipynb)

A fully runnable Jupyter notebook that implements:
- Dirichlet-Categorical conjugate prior models
- Enterprise-scale authentication anomaly detection
- Temporal evaluation with realistic train/test splits  
- Comprehensive performance analysis
- Mathematical theory explanations

## ⚡ Key Results

- **AUC-ROC: 0.724** on extremely imbalanced data (1:2M attack ratio)
- **29.4 million events** processed with linear time complexity
- **Zero hyperparameter tuning** required
- **Real-time scoring** capability for production deployment
- **Interpretable results** with clear probabilistic meaning

## 🧮 Mathematical Foundation

**Core Innovation**: Using Dirichlet-Categorical conjugate priors for online Bayesian learning:

```
Prior: θ ~ Dir(α)
Likelihood: x | θ ~ Categorical(θ)  
Posterior: θ | data ~ Dir(α + counts)
```

**Beautiful Update Rule**: Just add observed counts to prior parameters - no optimization needed!

## 📊 Dataset

**Los Alamos National Laboratory Comprehensive Multi-Source Cyber-Security Events**
- 1.648 billion authentication events over 58 days
- 749 red team attack events  
- 12,425 users across 17,684 computers
- Available at: https://csr.lanl.gov/data/cyber1/

## 🛠️ Quick Start

1. **Open the notebook** in Google Colab (click badge above)
2. **Mount Google Drive** and upload the LANL dataset
3. **Update file paths** in the notebook  
4. **Run all cells** - complete pipeline takes ~15-20 minutes

No local setup required - everything runs in Colab!

## 📁 Repository Structure

```
├── article/
│   └── conjugate_priors_article_tds.md     # Educational article
├── notebooks/  
│   └── conjugate_priors_cybersecurity_detection.ipynb  # Complete implementation
├── plots/
│   └── (Generated visualization outputs)
├── PROJECT_CONTEXT.md                      # Development context
└── README.md                               # This file
```

## 🎓 Learning Outcomes

After working through this project, you'll understand:

- **When and why** to choose conjugate priors
- **How Bayesian updating** works in practice  
- **Online learning** for streaming data
- **Cybersecurity anomaly detection** challenges
- **Evaluation strategies** for extreme class imbalance
- **Mathematical elegance** vs. algorithmic complexity

## 🤝 Contributing

This is an educational project. Contributions welcome for:
- Additional visualizations
- Extended mathematical analysis  
- Alternative datasets
- Performance optimizations
- Documentation improvements

## 📖 Citations

```bibtex
@article{conjugate_priors_cybersecurity_2024,
  title={Understanding Conjugate Priors Through Real-World Cybersecurity Data},
  author={[Your Name]},
  journal={Towards Data Science},
  year={2024},
  url={[Article URL]}
}
```

## 📄 License

MIT License - feel free to use for educational and research purposes.

---

**"Sometimes the most sophisticated approach is also the most mathematically principled one."**
