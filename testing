import graphlab as gl
import os

if os.path.exists('houses.csv'):
	sf = gl.SFrame.read_csv('houses.csv')
else:
    data_url = 'https://static.turi.com/datasets/regression/houses.csv'
    sf = gl.SFrame.read_csv(data_url)
    sf.save('houses.csv')
sf = gl.SFrame.read_csv('houses.csv')
sf.print_rows(5)
#sf.head(5)
#sf.export_csv('C:\\Users\\Marina\\gl-env\\Scripts\\aplicaciones\\salida1.csv',',')

for c in sf.column_names():
	if(c!='label'):
   		sf[c] = (sf[c] - sf[c].mean()) / sf[c].std()
model = gl.nearest_neighbors.create(sf, 'label',features=['bedroom', 'bath', 'size'])
model.summary()

knn = model.query(sf[:5], 'label', k=5)
#knn.export_csv("C:\\Users\\Marina\\gl-env\\Scripts\\aplicaciones\\resultado1.csv",',')
knn.print_rows(5)
#knn.head()