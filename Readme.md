# README



This repository provides a Python script to predict **Responder State** (High Responder: `HR`, Low Responder: `LR`) using a set of pre-trained **XGBoost** models.

---

## 📦 Requirements

Make sure you have Python >3.0 installed and the following dependencies:

```bash
pip install numpy pandas xgboost
```

## Project Structure 

```
.
├── predict_RS_responder_state.py   # Main prediction script
├── model/
│   └── all_xgb_models.pkl          # Pre-trained XGBoost models
├── data/
│   └── X_demo.csv                  # Example input data
└── output/
    └── y_predict_label.csv         # Prediction results

```



## 🚀 Usage

First, unzip the model file(all_xgb_models.pkl.zip) in model dir

Then, prepare your own file and Run the script with command-line arguments:

```
python predict_RS_responder_state.py \
    --input data/X_demo.csv \
    --output output/y_predict_label.csv

```

| Argument   | Short | Description                  |
| ---------- | ----- | ---------------------------- |
| `--input`  | `-i`  | Path to input CSV file       |
| `--output` | `-o`  | Path to save output CSV file |

## 📄 Input Format

- **Input CSV** (`X_demo.csv`)

  - No header (`header=None`)

  - Each row = one sample

  - Each column = one feature, feature order is as below

    ```
    'k__Bacteria|p__Firmicutes|c__Clostridia|o__Clostridiales|f__Lachnospiraceae|g__Anaerostipes',
           'k__Bacteria|p__Bacteroidetes|c__Bacteroidia|o__Bacteroidales|f__Prevotellaceae|g__Prevotella',
           'k__Bacteria|p__Bacteroidetes|c__Bacteroidia|o__Bacteroidales|f__Bacteroidaceae|g__Bacteroides|s__Bacteroides_thetaiotaomicron',
           'k__Bacteria|p__Firmicutes|c__Clostridia|o__Clostridiales|f__Lachnospiraceae|g__Roseburia|s__Roseburia_faecis',
           'k__Bacteria|p__Firmicutes|c__Clostridia|o__Clostridiales|f__Lachnospiraceae|g__Lacrimispora',
           'k__Bacteria|p__Bacteroidetes|c__Bacteroidia|o__Bacteroidales|f__Prevotellaceae|g__Paraprevotella',
           'PWY-6527: stachyose degradation',
           'HSERMETANA-PWY: L-methionine biosynthesis III',
           'LACTOSECAT-PWY: lactose and galactose degradation I',
           'P185-PWY: formaldehyde assimilation III (dihydroxyacetone cycle)',
           'PWY-6353: purine nucleotides degradation II (aerobic)', 'B.p exist state', 'Waist',
           'LDLC', 'BMI', 'DBP', 'TBA', 'TBIL', 'SBP', 'UA', 'Hip'
    ```

    

  - Example:

    ```
    0.12,0.85,0.33,0.56,...
    0.44,0.63,0.90,0.12,...
    ```



## 📤 Output

The output is a CSV file containing the predicted **Responder State** for each sample:

```
HR
LR
HR
...
```



## 📝 Notes

- Ensure feature order in the input CSV matches the training dataset.
- Default decision threshold is `0.5` — modify the script to change this.