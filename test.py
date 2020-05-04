from sklearn.ensemble import RandomForestClassifier
import numpy as np

domainlist = []
class Domain:
	def __init__(self,_name,_label):
		self.name = _name
		self.label = _label
    
        def returnData(self):
		return analyse(self.name)

	def returnLabel(self):
		if self.label == "notdga":
			return 0
		else:
			return 1

def analyse(name):
	num=0;
	for i in name:
		if i.isdigit():
			num=num+1;
	return [len(name),num];


def initData(filename):
	with open(filename) as f:
		for line in f:
			line = line.strip()
			if line.startswith("#") or line =="":
				continue
			tokens = line.split(",")
			name = tokens[0]
			label = tokens[1]
			domainlist.append(Domain(name,label))

def main():
	initData("train.txt")
	featureMatrix = []
	labelList = []
	for item in domainlist:
		featureMatrix.append(item.returnData())
		labelList.append(item.returnLabel())
	clf = RandomForestClassifier(random_state=0)
	clf.fit(featureMatrix,labelList)
	f=open("test.txt",mode='r');
	output=open("result.txt",mode='w');
	for line in f:
		line = line.strip()
		if line.startswith("#") or line =="":
			continue
		tokens = line.split(",")
		name = tokens[0]
		result=clf.predict([analyse(name)]);
		if(result ==0):
			output.write(name+","+"notdga\n")
		else:
			output.write(name+","+"dga\n")
	f.close();
	output.close();


if __name__ == '__main__':
	main()
