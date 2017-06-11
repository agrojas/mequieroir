import graphlab as gl
import os

class NeighborsTool:

	def __init__(self,datasetPath):
		self.model = None
		if os.path.exists(datasetPath):
			self.sf = gl.SFrame.read_csv(datasetPath)
			#for c in self.sf.column_names():
			#	if(c!='proposalId'):
	   		#		self.sf[c] = (self.sf[c] - self.sf[c].mean()) / self.sf[c].std()
			self.model = gl.nearest_neighbors.create(self.sf, 'proposalId')
			#self.sf.print_rows(5)
		else:
		    print "model could not be initialized correctly. Dataset inexistent"
		
	#self.sf.head(5)
	#self.sf.export_csv('C:\\Users\\Marina\\gl-env\\Scripts\\aplicaciones\\salida1.csv',',')

	def modelSumary(self):
		if self.model is None:
		    print "cannot call sumary the model. Model inexistent"
		    return
		self.model.summary()

	def query(self,id,neighborsQuantity):
		if self.model is None:
		    print "cannot call query to the model. Model inexistent"
		    return
		knn = self.model.query(self.sf[:id], 'proposalId', k=neighborsQuantity)
		#knn.export_csv("C:\\Users\\Marina\\gl-env\\Scripts\\aplicaciones\\resultado1.csv",',')
		knn.print_rows(neighborsQuantity)	
		knnResults = knn[:neighborsQuantity] 
		result = {}
		result["proposal_id"] = list(knnResults["reference_label"]) 
		result["rank"] = list(knnResults["rank"])
		result["distance"] = list(knnResults["distance"]) 		
		return result
	