import pandas as pd, numpy as np, statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, r2_score
df = pd.read_csv("Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2024_Regresion_Lineal_Python/adjuntos/Advertising.csv")
print(df.describe().round(2)); print(df[["tv","radio","periodico","ventas"]].corr().round(3))
for x in ["tv","radio","periodico"]:
    m = smf.ols(f"ventas ~ {x}", df).fit()
    b = m.params[x]; print(f"{x}: b={b:.4f} a={m.params['Intercept']:.3f} R2={m.rsquared:.3f} p={m.pvalues[x]:.2e} unid/1000={b*1000:.1f} margen_min={1000/(b*1000):.2f} IC={m.conf_int().loc[x].round(4).tolist()}")
    for mg in [5,8,30]: print(f"   margen {mg}: {b*1000*mg-1000:+.0f} USD por cada mil")
full = smf.ols("ventas ~ tv + radio + periodico", df).fit(); print(full.summary().tables[1]); print("R2 full", round(full.rsquared,4), "adj", round(full.rsquared_adj,4))
two = smf.ols("ventas ~ tv + radio", df).fit(); print("TV+radio", two.params.round(4).to_dict(), "R2", round(two.rsquared,4))
inter = smf.ols("ventas ~ tv * radio", df).fit(); print("interaccion", inter.params.round(5).to_dict(), "R2", round(inter.rsquared,4))
# baseline holdout
X_tr, X_te, y_tr, y_te = train_test_split(df[["tv","radio","periodico"]], df.ventas, test_size=0.25, random_state=42)
base = DummyRegressor().fit(X_tr, y_tr); print("base pred", round(base.predict(X_te[:1])[0],3), "MAE base", round(mean_absolute_error(y_te, base.predict(X_te)),3))
for cols in [["tv"],["radio"],["periodico"],["tv","radio"],["tv","radio","periodico"]]:
    lr = LinearRegression().fit(X_tr[cols], y_tr); p = lr.predict(X_te[cols])
    print(cols, "MAE", round(mean_absolute_error(y_te,p),3), "R2 test", round(r2_score(y_te,p),3), "MAPE", round(np.mean(np.abs((y_te-p)/y_te))*100,2))
# nuevo mercado
new = pd.DataFrame({"tv":[150],"radio":[25],"periodico":[30]})
pr = two.get_prediction(new).summary_frame(alpha=0.10); print(pr.round(3))
print("rangos", df.tv.min(), df.tv.max(), df.radio.min(), df.radio.max())
print("corr radio-periodico", round(df.radio.corr(df.periodico),3))
