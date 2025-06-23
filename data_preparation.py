from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

def prepare_data():
    # Загрузка данных
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    
    # Разделение данных
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop('target', axis=1), 
        df['target'], 
        test_size=0.2, 
        random_state=42
    )
    
    # Сохранение данных
    joblib.dump(X_train, 'X_train.joblib')
    joblib.dump(X_test, 'X_test.joblib')
    joblib.dump(y_train, 'y_train.joblib')
    joblib.dump(y_test, 'y_test.joblib')
    
    print("Данные успешно подготовлены!")

if __name__ == "__main__":
    prepare_data()