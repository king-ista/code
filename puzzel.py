
import math,random
class puzzel:
    def __init__(self):
        #self.node=[]
        self.fronts=[]
        self.GoalNode=['1','2','3','4','5','6','7','8','0']
        self.StartNode=['1','2','3','4','5','6','7','8','0']
        self.PreviousNode=[]
        self.prePreviousNode=[]
        self.PreviousCount=1
    
    def Solve(self):
        self.shufler(10)
        print(self.StartNode)
        self.sucessor(self.StartNode)
        nxNode=self.getNextNode()
        print (nxNode)
        count=1
        while nxNode!=self.GoalNode:
            #print(self.fronts)
            print(count)
            count+=1
            self.sucessor(nxNode)
            nxNode=self.getNextNode()
            print (nxNode)
        print('result',nxNode)
        
    
    def shufler(self):
                
            while True:
                node=self.StartNode
                subNode=[]
                direct=random.randint(1,4)
                getZeroLocation=node.index('0')+1
                subNode.extend(node)
                boundry=self.boundries(getZeroLocation)
                        
                if getZeroLocation+3<=9 and direct==1:
                    temp=subNode[node.index('0')]
                    subNode[node.index('0')]=subNode[node.index('0')+3]
                    subNode[node.index('0')+3]=temp
                    self.StartNode=subNode
                    return
                    
                elif getZeroLocation-3>=1 and direct==2:
                    temp=subNode[node.index('0')]
                    subNode[node.index('0')]=subNode[node.index('0')-3]
                    subNode[node.index('0')-3]=temp
                    self.StartNode=subNode
                    return
                
                elif getZeroLocation-1>=boundry[0] and direct==3:
                    temp=subNode[node.index('0')]
                    subNode[node.index('0')]=subNode[node.index('0')-1]
                    subNode[node.index('0')-1]=temp
                    self.StartNode=subNode
                    return
                
                elif getZeroLocation+1<=boundry[1] and direct==4:
                    temp=subNode[node.index('0')]
                    subNode[node.index('0')]=subNode[node.index('0')+1]
                    subNode[node.index('0')+1]=temp
                    self.StartNode=subNode
                    return
                
    def boundries(self,location):
        lst=[[1,2,3],[4,5,6],[7,8,9]]
        low=0
        high=0
        for i in lst:
            if location in i:
                low=i[0]
                high=i[2]
        
        return [low,high]
    
    def getNextNode(self):
        nxNode=[]
        tNode=[]
        while True:
            hrCost=100000
            for i in self.fronts:
                    if(i[-1]<hrCost):
                        hrCost=i[-1]
                        nxNode=i[0:-1]
                        tNode=i
            
            if tNode in self.PreviousNode and tNode in self.fronts:
                self.fronts.remove(tNode)
                self.PreviousNode.append(tNode)
                
            else:
                self.PreviousNode.append(tNode)
                return nxNode

    
    def heruistic(self,node):
        herMisplaced=0
        herDist=0
        
        for i in range(9):
            if node[i]!=self.GoalNode[i]:
                herMisplaced +=1
        for i in node:
            herDist +=math.fabs(node.index(i)-self.GoalNode.index(i))
        
        totalHerst=herDist+herMisplaced
       
        node.append(totalHerst)
        return node
        
        
    
    def sucessor(self,node=[]):
        subNode=[]
        getZeroLocation=node.index('0')+1
        subNode.extend(node)
        boundry=self.boundries(getZeroLocation)
#        for i in self.fronts:
#           if i[0:-1]==node:
#              self.fronts.remove(i)
        self.fronts=[]
                
        if getZeroLocation+3<=9:
            temp=subNode[node.index('0')]
            subNode[node.index('0')]=subNode[node.index('0')+3]
            subNode[node.index('0')+3]=temp
            self.fronts.append(self.heruistic(subNode))
            subNode=[]
            subNode.extend(node)
        if getZeroLocation-3>=1:
            temp=subNode[node.index('0')]
            subNode[node.index('0')]=subNode[node.index('0')-3]
            subNode[node.index('0')-3]=temp
            self.fronts.append(self.heruistic(subNode))
            subNode=[]
            subNode.extend(node)
        if getZeroLocation-1>=boundry[0]:
            temp=subNode[node.index('0')]
            subNode[node.index('0')]=subNode[node.index('0')-1]
            subNode[node.index('0')-1]=temp
            self.fronts.append(self.heruistic(subNode))
            subNode=[]
            subNode.extend(node)
        if getZeroLocation+1<=boundry[1]:
            temp=subNode[node.index('0')]
            subNode[node.index('0')]=subNode[node.index('0')+1]
            subNode[node.index('0')+1]=temp
            self.fronts.append(self.heruistic(subNode))
            subNode=[]
            subNode.extend(node)
        
                        
                
