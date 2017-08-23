class Big_words(object):
        def open_file(self,name):
            h=open(name)
            r=h.read()
            r=r.lower()
            return r
        def dic(self,r):
            dic_words={}
            lis_words=[]
            lis_words=r.split(' ')
            #print (words)  
            for i in lis_words:
                if i in dic_words:
                    dic_words[i]+=1
                else:
                    dic_words[i]=1
            return dic_words
        def product(self,lis,dict1):
            u=0
            for i in lis:
                s=dict1.get(i,0)**2
                u=u+s
            return u
        def duplicates(self,lis):
                lis4=[]
                for i in lis3:
                    if i not in lis4:
                        lis4.append(i)
                return lis4
        def dot_product(self,lis,dict1,dict2):
                p=0
                for i in lis4:
                    u1=a.get(i,0)*b.get(i,0)
                    p=p+u1
                return p                
new=Big_words()

s1=input('enter the file name:')
a=new.dic(new.open_file(s1))

s2=input('enter another file name:')
b=new.dic(new.open_file(s2))

lis1=list(a.keys())
lis2=list(b.keys())
lis3=lis1+lis2

lis4=new.duplicates(lis3)

new_p=new.dot_product(lis4,a,b)

new_u=new.product(lis4,a)

new_u1=new.product(lis4,b)

final=(new_p/(new_u*new_u1)**0.5)
print(final*100)



        

