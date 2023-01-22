import pickle
import json
import pandas as pd
import numpy as np
import config


class HeartDisease():
    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trestbps = trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal



    def load_file(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)


    def get_predicted_disease(self):
        self.load_file()  # calling load_file method to get

        array = np.zeros(len(self.json_data['columns']))

        array[0] = self.age
        array[1] = self.json_data['sex_dict'][self.sex]
        array[2] = self.json_data['cp_dict'][self.cp]
        array[3] = self.trestbps
        array[4] = self.chol
        array[5] = self.json_data['fbs_dict'][self.fbs]
        array[6] = self.json_data['restecg_dict'][self.restecg]
        array[7] = self.thalach
        array[8] = self.json_data['exang_dict'][self.exang]
        array[9] = self.oldpeak
        array[10] = self.json_data['slope_dict'][self.slope]
        array[11] = self.ca
        array[12] = self.json_data['thal_dict'][self.thal]

        print("Test Array -->\n",array)
        predicted_disease = self.model.predict([array])[0]
        return predicted_disease





if __name__ == "__main__":

    age = 63
    sex = 'male'
    cp = 'typical angina'
    trestbps= 145
    chol = 233
    fbs = 'lower'
    restecg = 'abnormal'
    thalach = 150
    exang = 'no'
    oldpeak = 2.3
    slope = 'up'
    ca = 1
    thal = 'normal'

    hd = HeartDisease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    disease = hd.get_predicted_disease()
    print()
    print(f"patient predicted heart disease {disease}")
    