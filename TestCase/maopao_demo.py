def maopao():
    alist=[2,3,1,4,6,5,9,8,7]
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j]>alist[j+1]:
                a=alist[j]
                alist[j]=alist[j+1]
                alist[j+1]=a
            print(alist)




def jiujiu():
    for i in range(1,10):

        for j in range(1,i+1):
            print('%s*%s=%s'%(i,j,i*j),end='   ')

        print('')





def jiiu():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s*%s=%s'%(i,j,i*j),end='    ')
        print('')






if __name__ == '__main__':
    maopao()
    # jiiu()






