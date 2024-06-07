import joblib as joblib
import pandas as pd

def get_model():
    model = joblib.load("src/data/knn_model.sav")
    return model

def predict(model, features):
    return model.predict(features)

def transform(features):

    features["island"].replace({"Torgersen": 2, "Biscoe": 0, "Dream": 1}, inplace=True)
    features["sex"].replace({"MALE": 1, "FEMALE": 0}, inplace=True)
    
    return features

def get_class(prediction):

    case = {
        0: "Adelie",
        1: "Chinstrap",
        2: "Gentoo"
    }
    
    return case[prediction]

def get_num_features():
    
    try:
        print("Please enter the following features (numbers only):")

        culmen_length = float(input("culmen_length: "))
        culmen_depth = float(input("culmen_depth: "))
        flipper_length = int(input("flipper_length: "))
        body_mass = int(input("body_mass: "))    

        num_features = pd.DataFrame([[culmen_length, culmen_depth, flipper_length, body_mass]], columns=['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g'])
    
        return num_features

    except ValueError as err:
        print(err)

        return None

def get_cat_features():

    try:
        print("Please enter the following features (text only):")

        island = input("island: ")
        sex = input("sex: ")

        cat_features = pd.DataFrame([[island, sex]], columns=['island', 'sex'])

        return transform(cat_features)

    except ValueError as err:
        print(err)

        return None

def get_features():

    num_features = get_num_features()
    cat_features = get_cat_features()
    
    try:
        features = pd.concat([cat_features, num_features], axis=1)
    except:
        return None
    
    return features

def main():
    features = get_features()

    if features is not None:
        model = get_model()
        prediction = predict(model, features)
        print(f"The predicted species is {get_class(prediction[0])}")

if __name__ == "__main__":
    main()