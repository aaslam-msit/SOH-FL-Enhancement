import shap

def explain_model(model, background, sample):
    explainer = shap.DeepExplainer(model, background)
    shap_values = explainer.shap_values(sample)
    return shap_values