import pandas as pd

data_frame = pd.read_csv(r"D:\User\VScode\Portf-lio\Projetos\Automation\Python PowerUp\products.csv")
data_frame2 = pd.read_csv(r"D:\User\VScode\Portf-lio\Projetos\Automation\Python PowerUp\prateste.csv")
print(data_frame)
print()

for i in data_frame.index:
    print(f"Linha {i}:")
    for j in data_frame.columns:
        print(data_frame.loc[i,j])
    print()

print(data_frame == data_frame2)
