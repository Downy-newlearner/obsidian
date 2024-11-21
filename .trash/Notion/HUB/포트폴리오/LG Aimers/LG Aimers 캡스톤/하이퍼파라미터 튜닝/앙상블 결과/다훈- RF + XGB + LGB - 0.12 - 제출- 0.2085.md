```JavaScript
# 모델 생성
rf_model = RandomForestClassifier(n_estimators = 118, max_depth = 6, min_samples_split = 4, min_samples_leaf = 4, class_weight={0: 1, 1: 20}, random_state=42)
xgb_model = XGBClassifier(n_estimators = 286, max_depth = 10, learning_rate = 0.21366513084005267, subsample = 0.6122668648564789, colsample_bytree = 0.7768644502170545, gamma = 0.2855489821421704, min_child_weight = 1, random_state=42)
lgbm_model = LGBMClassifier(random_state=42)
# 소프트 보팅 앙상블 모델 생성
voting_model = VotingClassifier(estimators=[
    ('rf', rf_model),
    ('xgb', xgb_model),
    ('lgbm', lgbm_model)
], voting='soft')
# 모델 학습
voting_model.fit(X_train_smote, y_train_smote)
# 검증 데이터에 대한 예측
y_val_pred = voting_model.predict(X_val)
# 분류 리포트 출력
print(classification_report(y_val, y_val_pred))
```
  
precision recall f1-score support  
  
0 0.16 0.10 0.12 441  
1 0.95 0.97 0.96 7642  
  
accuracy 0.92 8083  
macro avg 0.55 0.53 0.54 8083  
weighted avg 0.91 0.92 0.91 8083  
  
['AbNormal' 'Normal'] [ 1703 15658]