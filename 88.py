df = pd.read_csv('example')
df

df.to_csv('example',index=False)

pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')

df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')
