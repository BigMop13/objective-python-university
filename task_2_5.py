import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

plt.style.use('ggplot')
sns.set_palette("husl")

def analyze_teachers_data():
    df = pd.read_csv('nauczyciele.csv', sep=';')
    df = df.drop(columns=[df.columns[0]])
    df_long = df.melt(id_vars=['Nazwa'], var_name='kategoria', value_name='liczba')
    df_long['liczba'] = df_long['liczba'].astype(str).str.replace(',', '.').str.replace('"', '')
    df_long['liczba'] = pd.to_numeric(df_long['liczba'], errors='coerce')
    df_long['Nazwa'] = df_long['Nazwa'].str.replace('"', '')
    def parse_kategoria(kat):
        parts = kat.replace('"', '').split(';')
        while len(parts) < 5:
            parts.append('')
        return pd.Series({
            'stanowisko': parts[0],
            'plec': parts[1],
            'typ_uczelni': parts[2],
            'rok': parts[3]
        })
    df_long = pd.concat([df_long, df_long['kategoria'].apply(parse_kategoria)], axis=1)
    df_long = df_long[df_long['rok'].isin(['2014', '2015', '2016', '2017', '2018'])]
    nauczyciele_ogolem = df_long[(df_long['stanowisko'] == 'nauczyciele akademiccy') & (df_long['plec'] == 'ogółem') & (df_long['typ_uczelni'] == 'uniwersytety')]
    pivot1 = nauczyciele_ogolem.pivot_table(index='Nazwa', columns='rok', values='liczba', aggfunc='sum')
    pivot1.sum(axis=1).plot(kind='bar', figsize=(12,6))
    plt.title('Nauczyciele akademiccy ogółem na uniwersytetach (2014-2018) wg województwa')
    plt.ylabel('Liczba nauczycieli')
    plt.tight_layout()
    plt.savefig('nauczyciele_wojewodztwa.png')
    plt.close()
    slaskie = df_long[(df_long['Nazwa'].str.upper() == 'ŚLĄSKIE') & (df_long['stanowisko'].isin(['asystenci', 'adiunkci', 'profesorowie'])) & (df_long['plec'] == 'ogółem') & (df_long['typ_uczelni'] == 'uniwersytety')]
    stanowiska_slaskie = slaskie.groupby('stanowisko')['liczba'].sum()
    stanowiska_slaskie.plot(kind='bar', figsize=(8,6))
    plt.title('Stanowiska (asystenci, adiunkci, profesorowie) w woj. śląskim (2014-2018)')
    plt.ylabel('Liczba nauczycieli')
    plt.tight_layout()
    plt.savefig('stanowiska_slaskie.png')
    plt.close()
    slaskie_plec = df_long[(df_long['Nazwa'].str.upper() == 'ŚLĄSKIE') & (df_long['stanowisko'] == 'nauczyciele akademiccy') & (df_long['typ_uczelni'].isin(['uniwersytety', 'wyższe szkoły techniczne'])) & (df_long['plec'].isin(['kobiety', 'ogółem']))]
    plec_pivot = slaskie_plec.pivot_table(index='plec', columns='typ_uczelni', values='liczba', aggfunc='sum')
    plec_pivot.plot(kind='bar', figsize=(8,6))
    plt.title('Nauczyciele akademiccy wg płci w woj. śląskim (uniwersytety i szkoły techniczne)')
    plt.ylabel('Liczba nauczycieli')
    plt.tight_layout()
    plt.savefig('plec_slaskie.png')
    plt.close()
    print("\nDane dla województwa śląskiego:")
    print(df_long[df_long['Nazwa'].str.upper() == 'ŚLĄSKIE'])
    total_by_woj = nauczyciele_ogolem.groupby('Nazwa')['liczba'].sum()
    print("\nNajwięcej nauczycieli akademickich:", total_by_woj.idxmax(), total_by_woj.max())
    print("Najmniej nauczycieli akademickich:", total_by_woj.idxmin(), total_by_woj.min())
    kobiety = df_long[(df_long['stanowisko'] == 'nauczyciele akademiccy') & (df_long['plec'] == 'kobiety') & (df_long['typ_uczelni'] == 'uniwersytety')]
    kobiety_by_woj = kobiety.groupby('Nazwa')['liczba'].sum()
    mean_kobiety = kobiety_by_woj.mean()
    print("\nWojewództwa zatrudniające kobiety ponad średnią:")
    print(kobiety_by_woj[kobiety_by_woj > mean_kobiety])

def analyze_inflation_data():
    df1 = pd.read_excel('inflacja.xlsx', sheet_name='Table 1', header=None)
    df2 = pd.read_excel('inflacja.xlsx', sheet_name='Table 2', header=None)
    df3 = pd.read_excel('inflacja.xlsx', sheet_name='Table 3', header=None)
    lata = ['2017', '2018', '2019']
    miesiace = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    df1.columns = [f'col{i}' for i in range(len(df1.columns))]
    df1 = df1[df1['col2'].astype(str).isin(lata)]
    plt.figure(figsize=(10,6))
    for year in lata:
        row = df1[df1['col2'].astype(str) == year]
        if not row.empty:
            values = row.iloc[0, -12:].astype(float).values
            plt.plot(miesiace, values, label=year)
    plt.title('Inflacja: rok do grudnia poprzedniego roku')
    plt.xlabel('Miesiąc')
    plt.ylabel('Wartość')
    plt.legend()
    plt.tight_layout()
    plt.savefig('inflacja_rok_do_roku.png')
    plt.close()
    df2.columns = [f'col{i}' for i in range(len(df2.columns))]
    df2 = df2[df2['col1'].astype(str).isin(lata)]
    paz_values = []
    for year in lata:
        row = df2[df2['col1'].astype(str) == year]
        if not row.empty:
            paz_values.append(float(row.iloc[0, 10]))
        else:
            paz_values.append(None)
    plt.figure(figsize=(6,6))
    plt.bar(lata, paz_values)
    plt.title('Inflacja w październiku względem poprzedniego miesiąca')
    plt.ylabel('Wartość')
    plt.tight_layout()
    plt.savefig('inflacja_pazdziernik.png')
    plt.close()
    df3.columns = [f'col{i}' for i in range(len(df3.columns))]
    df3 = df3[df3['col1'].astype(str).isin(lata)]
    plt.figure(figsize=(10,6))
    for year in lata:
        row = df3[df3['col1'].astype(str) == year]
        if not row.empty:
            values = row.iloc[0, 2:14].astype(float).values
            plt.plot(miesiace, values, label=year)
    plt.title('Inflacja: rok do analogicznego miesiąca poprzedniego roku')
    plt.xlabel('Miesiąc')
    plt.ylabel('Wartość')
    plt.legend()
    plt.tight_layout()
    plt.savefig('inflacja_miesiac_do_miesiaca.png')
    plt.close()
    print("\nAnaliza danych inflacji:")
    for name, df, col in zip(['Table 1', 'Table 2', 'Table 3'], [df1, df2, df3], [df1.columns[-12:], df2.columns[2:14], df3.columns[2:14]]):
        print(f"\n{name} (2017-2019):")
        for idx, row in df.iterrows():
            year = row['col1'] if name != 'Table 1' else row['col2']
            values = pd.to_numeric(row[col], errors='coerce')
            print(f"Rok {year}:")
            print(f"  Max: {values.max():.2f}")
            print(f"  Min: {values.min():.2f}")
            print(f"  Średnia: {values.mean():.2f}")

if __name__ == "__main__":
    print("Analiza danych nauczycieli akademickich:")
    analyze_teachers_data()
    print("\nAnaliza danych inflacji:")
    analyze_inflation_data()
