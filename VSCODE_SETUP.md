# VSCode + Claude Code Setup Instructions

## 📥 Download & Setup

### Step 1: Download Files
1. Download all 4 files from Claude.ai:
   - `conjugate_priors_cybersecurity_detection.ipynb`
   - `conjugate_priors_article_tds.md`  
   - `PROJECT_CONTEXT.md`
   - `README.md`

### Step 2: Create Local Workspace
```bash
# Create project directory
mkdir conjugate-priors-cybersecurity
cd conjugate-priors-cybersecurity

# Create structure
mkdir -p {notebooks,article,plots,data}

# Move downloaded files
mv conjugate_priors_cybersecurity_detection.ipynb notebooks/
mv conjugate_priors_article_tds.md article/
mv PROJECT_CONTEXT.md .
mv README.md .
```

### Step 3: Initialize Git Repository
```bash
git init
echo "data/" > .gitignore
echo "plots/*.png" >> .gitignore
echo ".DS_Store" >> .gitignore
git add .
git commit -m "Initial commit: Conjugate priors cybersecurity project"
```

## 🔧 Claude Code Configuration

### Step 4: Open in VSCode
```bash
code .
```

### Step 5: Install Claude Code Extension
1. Install Claude Code extension from VSCode marketplace
2. Authenticate with your Anthropic account

### Step 6: Create .claude-code Config
Create `.claude-code/config.json`:
```json
{
  "project_context": "PROJECT_CONTEXT.md",
  "include_patterns": [
    "*.py",
    "*.ipynb", 
    "*.md",
    "*.json"
  ],
  "exclude_patterns": [
    "data/*",
    "plots/*",
    ".git/*"
  ]
}
```

## 💬 First Claude Code Prompt Template

When you start Claude Code, use this initial prompt:

```
I'm continuing work on a conjugate priors cybersecurity project. Please read PROJECT_CONTEXT.md for full background.

CURRENT STATUS: 
- ✅ Mathematical framework designed (Dirichlet-Categorical conjugate priors)
- ✅ Complete implementation in Jupyter notebook  
- ✅ Article draft with plot placeholders
- 🎯 NEXT: Need to refine and generate publication-ready materials

IMMEDIATE GOALS:
1. Review notebook for Colab optimization
2. Test different α (alpha) prior values experimentally  
3. Generate high-quality plots for article
4. Refine mathematical explanations
5. Prepare for GitHub publication

Please examine the current files and suggest specific improvements or experiments to run.

KEY CONTEXT: This is educational content for Towards Data Science showing how 250-year-old math (conjugate priors) elegantly solves modern ML problems.
```

## 🔄 Workflow Tips

### Maintain Context Between Sessions
- Always reference `PROJECT_CONTEXT.md` in new conversations
- Keep mathematical notation consistent (θ, α, etc.)
- Preserve the educational focus - clarity over optimization

### Git Best Practices
```bash
# Commit frequently with descriptive messages
git add -A
git commit -m "Refactor notebook for better Colab experience"

# Create branches for experiments
git checkout -b experiment-alpha-values
git checkout -b improve-visualizations
```

### File Organization
```
conjugate-priors-cybersecurity/
├── .claude-code/
│   └── config.json
├── article/
│   └── conjugate_priors_article_tds.md
├── notebooks/
│   └── conjugate_priors_cybersecurity_detection.ipynb
├── plots/
│   └── (generated outputs)
├── data/
│   └── (LANL dataset - not tracked in git)
├── PROJECT_CONTEXT.md
├── README.md
└── .gitignore
```

## 🎯 Common Claude Code Requests

Here are effective prompt patterns for this project:

### Notebook Improvements
```
Please review the notebook and suggest improvements for:
1. Colab compatibility and runtime optimization
2. Mathematical explanation clarity  
3. Code documentation and comments
4. Error handling and edge cases
```

### Experimentation
```
Let's experiment with different α values (0.1, 1.0, 10.0) and compare:
1. Anomaly score distributions
2. Performance metrics  
3. Mathematical interpretation
Add this as a new notebook section.
```

### Visualization
```
Create publication-quality plots for the article:
1. ROC curve with confidence intervals
2. Score distributions with statistical annotations
3. Authentication pattern heatmaps
4. Computer specialization analysis
```

### Article Refinement  
```
Review the article for:
1. Mathematical accuracy and notation consistency
2. Educational flow and clarity
3. Missing technical details
4. Plot integration points
```

## 🚀 Quick Commands

### Start Jupyter Server
```bash
jupyter notebook notebooks/
```

### Generate Plots
```bash
python -c "
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
# Execute notebook and save outputs
"
```

### Article Preview
```bash
# If you have pandoc installed
pandoc article/conjugate_priors_article_tds.md -o article_preview.pdf
```

This setup preserves all our mathematical work and implementation decisions while giving you full development flexibility in VSCode!
