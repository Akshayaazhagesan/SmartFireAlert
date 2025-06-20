# FireAlarmAI

FireAlarmAI is a machine learning project designed to predict potential fire hazards based on environmental sensor inputs. It uses logistic regression to classify the risk and simulate a basic smart fire alarm system.

## Technologies Used
- Python
- scikit-learn
- Pandas
- NumPy
- Matplotlib (for optional visualization)

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the training script:
   ```bash
   python train_fire_model.py
   ```

3. Use the model to make predictions:
   ```bash
   python predict_fire_risk.py
   ```

## Files Included
- `train_fire_model.py` – trains and saves the model
- `predict_fire_risk.py` – loads model and predicts fire risk
- `fire_model.pkl` – trained model file
- `requirements.txt` – dependencies list
