import graphlab as gl
import os

class NeighborsTool:

	def __init__(self,datasetPath):
		if os.path.exists(datasetPath):
			sf = gl.SFrame.read_csv(datasetPath)
			for c in sf.column_names():
				if(c!='proposalId'):
	   				sf[c] = (sf[c] - sf[c].mean()) / sf[c].std()
			self.model = gl.nearest_neighbors.create(sf, 'proposalId')
			#sf.print_rows(5)
		else:
		    print "SFrame could not be initialized correctly. Dataset inexistent"
		
	#sf.head(5)
	#sf.export_csv('C:\\Users\\Marina\\gl-env\\Scripts\\aplicaciones\\salida1.csv',',')

	def modelSumary(self):
		self.model.summary()

	def query(self,proposal,neighborsQuantity):
		knn = self.model.query(proposal, 'proposalId', k=neighborsQuantity)
		#knn.export_csv("C:\\Users\\Marina\\gl-env\\Scripts\\aplicaciones\\resultado1.csv",',')
		knn.print_rows(5)	
	