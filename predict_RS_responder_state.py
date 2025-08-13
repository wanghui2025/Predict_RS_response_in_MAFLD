import numpy as np
import pandas as pd
import xgboost as xgb
import pickle
import argparse

def main(input_file,output_file):
    demo=pd.read_csv(input_file,header=None)
    with open('model/all_xgb_models.pkl', 'rb') as f:
        all_models = pickle.load(f)
    print("[INFO] Model loaded succuessfully")
    y_df=[]
    for i in range(100):
    	loaded_model = xgb.Booster()
    	model_tem=all_models["_".join(["RS_model",str(i)])]
    	X_demo=np.array(demo)
    	y_demo= model_tem.predict(xgb.DMatrix(X_demo))
    	#print(y_demo)
    	y_df.append(y_demo.tolist())

    print("[INFO] Prediction finished")

    y_demo=(pd.DataFrame(y_df).mean(axis=0)>0.5).map({True:"HR",False:"LR"})
    y_demo.to_csv(output_file)
    print(f"[INFO] Please found your responder state in {output_file}!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict responder state using RS models.")
    parser.add_argument("--input", "-i", required=True, help="Path to input CSV file (X_demo.csv)")
    parser.add_argument("--output", "-o", required=True, help="Path to output CSV file")

    args = parser.parse_args()

    main(args.input, args.output)