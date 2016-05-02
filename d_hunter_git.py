#-cmpt120 diamond hunter
#-manipulating arrays
##########################
import random as r
def wel_msg():
    print 'Welcome to the "Diamond Treasure Hunter" game'
    print "=============================================="
    return
def matrix(a,b):
    Col_string="          "
    for i in range(b):
        Col_string+="Col"+str(i)+"   "
    print Col_string
    for i in range(b):
        j=0
        Row_string=""
        start="Row"+str(i)+"  "
        for j in range(b):
            if len(str(a[i][j]))>1:
                Row_string+="     "+str(a[i][j])
            else:
                Row_string+="      "+str(a[i][j])
        print start+Row_string
    return

def flag_(x):
    if x<0:
       res=False
    return res

def valid(x,y):
    flag=flag_(-1)
    while flag==False:
        path=raw_input('\n'+x+'(0 to '+str(y-1)+'):')
        if path.isdigit()!=True:
             print "The value should only have digits, please re-enter"
        elif (int(path)<0 or int(path)>=y):
            print "That is not a valid input, please re-enter"
        else:
             flag=True
    return path

def obtain_list_0s_1s(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i][j]%2==0:
               x[i][j]=0
            else:
                x[i][j]=1
    return x

#TOP LEVEL
wel_msg()
decision=raw_input("\n\nWould you like to play(y/n): ")
while decision!="y" and decision!="n":
    print "That is not a valid input,please re-enter"
    decision=raw_input("\n\nWould you like to play(y/n): ")
all_points=0
total_points=[]
hunter_=[]
trap_status=[]
lucky_number=[]
while decision=="y":
    print  "\n\nOne more game..."
    print "\n==============="
    name=raw_input("Name of treasure hunter: ")
    size=input("\nSize of board(between 3 and 6 inclusive): ")
    creation=raw_input("\nCreation of board?(r-random,u-user): ")
    if creation=="u":
         print "\nProvide a list of lists,same number of rows and columns"
         print " \nwith integer number between 0 and 10 inclusive"
         lis=input("\nand maybe one -1==> ")
         decision2="y"
         trap="n"
         while decision2=="y" and trap=="n":
             print "\n\nThe board is: \n------------"
             matrix(lis,size)   
             print "\n\n\nHow whould you want that "+name+" travels?:"
             print"\nr-row \n\nc-col \n\nm-main diagonal \n\ns-secondaru diagonal"
             travel=raw_input("\nx-random                :")
             if travel=="r":
                r_="Num row"
                row_chosen=valid(r_,size)
                print "\n\npositions visited:...\n"
                for i in range(size):
                    print "["+row_chosen+"]"+"["+str(i)+"]"
                    if lis[int(row_chosen)][i]==-1:
                        print "a -1!"
                        break
                acc=0
                for i in range(size):
                    if (lis[int(row_chosen)][i])%2==0:
                        acc+=lis[int(row_chosen)][i]/2
                        lis[int(row_chosen)][i]=lis[int(row_chosen)][i]/2
                    elif lis[int(row_chosen)][i]==-1:
                        points_gotten=acc
                        trap="y"
                        break
                    else:
                        acc+=(lis[int(row_chosen)][i])
                        lis[int(row_chosen)][i]=0
                points_gotten=acc
                print "\npoints obtained in this trip:... "+str(points_gotten)
                print "\nBoard after trip"
                matrix(lis,size)
             elif travel=="c":
                  c_="Num colume"
                  col_chosen=valid(c_,size)
                  print "\n\npositions visited:...\n"
                  for i in range(size):
                      print "["+str(i)+"]"+"["+col_chosen+"]"
                      if lis[i][int(col_chosen)]==-1:
                          print "oooooooooh!!!! a -1!"
                          break
                  acc=0
                  for i in range(size):
                      if (lis[i][int(col_chosen)])%2==0:
                         acc+=lis[i][int(col_chosen)]/2
                         lis[i][int(col_chosen)]=lis[i][int(col_chosen)]/2
                      elif lis[i][int(col_chosen)]==-1:
                           points_gotten=acc
                           trap=="y"
                           break
                      else:
                          acc+=(lis[i][int(col_chosen)])
                          lis[i][int(col_chosen)]=0
                  points_gotten=acc
                  print "\npoints obtained in this trip:... "+str(points_gotten)
                  print "\nBoard after trip"
                  matrix(lis,size)
             elif travel=="m":
                  print "\n\npositions visited:...\n"
                  for i in range(size):
                      print "["+str(i)+"]"+"["+str(i)+"]"
                      if lis[i][i]==-1:
                        print "oooooooh!!!! a -1!"
                        break
                  acc=0
                  for i in range(size):
                      if (lis[i][i])%2==0:
                          acc+=lis[i][i]/2
                          lis[i][i]=lis[i][i]/2
                      elif lis[i][i]==-1:
                           points_gotten=acc
                           trap="y"
                           break
                      else:
                           acc+=(lis[i][i])
                           lis[i][i]=0
                  points_gotten=acc
                  print "\npoints obtained in this trip:... "+str(points_gotten)
                  print "\nBoard after trip"
                  matrix(lis,size)
             elif travel=="s":
                  print "\n\npositions visited:...\n"
                  for i in range(size):
                      print "["+str(i)+"]"+"["+str(size-i-1)+"]"
                      if lis[i][size-i-1]==-1:
                         print "ooooooooh!!!! a -1!"
                         break
                  acc=0
                  for i in range(size):
                      if (lis[i][size-i-1])%2==0:
                          acc+=lis[i][size-i-1]/2
                          lis[i][size-i-1]=lis[i][size-i-1]/2
                      elif lis[i][size-i-1]==-1:
                          trap="y"
                          break
                      else:
                           acc+=(lis[i][size-i-1])
                           lis[i][size-i-1]=0
                  points_gotten=acc
                  print "\npoints obtained in this trip:... "+str(points_gotten)
                  print "\nBoard after trip"
                  matrix(lis,size)
             elif travel=="x":
                  acc=0
                  n=input("\n\nHow many random cells shall the hunter visit?:")
                  for i in range(n):
                      a=r.randint(0,(size-1))
                      b=r.randint(0,(size-1))
                      print "["+str(a)+"]"+"["+str(b)+"]"
                      if lis[a][b]%2==0:
                          acc+=lis[a][b]/2
                          lis[a][b]=lis[a][b]/2
                      elif lis[a][b]==-1:
                          print "oooooooooh!!!a -1!"
                          trap="y"
                          break
                      else:
                          acc+=lis[a][b]
                          lis[a][b]=0
                  points_gotten=acc
                  print "\npoints obtained in this trip:... "+str(points_gotten)
                  print "\nBoard after trip"
                  matrix(lis,size)
             all_points=all_points+points_gotten
             if trap!="y":
                 decision2=raw_input('\nWould you like '+name+' to do another trip?(y/n):')
                 while decision2!="y" and decision2!="n" and decision2!="trap":
                       print "That is not a valid input,please re-enter"
                       decision2=raw_input('\nWould you like '+name+' to do another trip?(y/n):')
         if trap=="y":
             print "\nOh no! "+name+" got trapped!"
             print name+" cannot travel again :("
         print "\n\nThe treasure hunter "+name+" obtained "+str(all_points)+" points in its game"
         obtain_list_0s_1s(lis)
         num1=0
         num2=0
         string=""
         for i in range(len(lis)):
             num1=0
             for j in range(len(lis)):
                   num1+=lis[i][j]*(2**(len(lis)-j-1))
                   num2+=lis[i][j]*(2**(len(lis)-j-1))
             string+=str(num1)+","
         print "\n\nThe values of each row in the board(as binary number)are:"
         print string+" and therefor the board lucky number is:"+str(num2)
    elif creation=="r":
         diamonds=input("\nMaximum number diamonds in a cell(from 1 to 10): ")
         lis=[]
         for i in range(size):
             lis.append([])
         for i in range(size):
             j=0
             for j in range(size):
                 a=r.randint(0,diamonds)
                 lis[i].append(a)
         x=r.randint(1,5)
         if i!=1:
            n=r.randint(0,(size-1))
            m=r.randint(0,(size-1))
            lis[n][m]=-1
         decision2="y"
         trap="n"
         while decision2=="y" and trap=="n":
             print "\n\nThe board is: \n------------"
             matrix(lis,size)   
             print "\n\n\nHow whould you want that "+name+" travels?:"
             print"\nr-row \n\nc-col \n\nm-main diagonal \n\ns-secondaru diagonal"
             travel=raw_input("\nx-random                :")
             if travel=="r":
                r_="Num row"
                row_chosen=valid(r_,size)
                print "\n\npositions visited:...\n"
                for i in range(size):
                    print "["+row_chosen+"]"+"["+str(i)+"]"
                    if lis[int(row_chosen)][i]==-1:
                        print "a -1!"
                        break
                acc=0
                for i in range(size):
                    if (lis[int(row_chosen)][i])%2==0:
                        acc+=lis[int(row_chosen)][i]/2
                        lis[int(row_chosen)][i]=lis[int(row_chosen)][i]/2
                    elif lis[int(row_chosen)][i]==-1:
                        points_gotten=acc
                        trap="y"
                        break
                    else:
                        acc+=(lis[int(row_chosen)][i])
                        lis[int(row_chosen)][i]=0
                points_gotten=acc
                print "\npoints obtained in this trip:... "+str(points_gotten)
                print "\nBoard after trip"
                matrix(lis,size)
             elif travel=="c":
                  c_="Num colume"
                  col_chosen=valid(c_,size)
                  print "\n\npositions visited:...\n"
                  for i in range(size):
                      print "["+str(i)+"]"+"["+col_chosen+"]"
                      if lis[i][int(col_chosen)]==-1:
                          print "oooooooooh!!!! a -1!"
                          break
                  acc=0
                  for i in range(size):
                      if (lis[i][int(col_chosen)])%2==0:
                         acc+=lis[i][int(col_chosen)]/2
                         lis[i][int(col_chosen)]=lis[i][int(col_chosen)]/2
                      elif lis[i][int(col_chosen)]==-1:
                           points_gotten=acc
                           trap=="y"
                           break
                      else:
                          acc+=(lis[i][int(col_chosen)])
                          lis[i][int(col_chosen)]=0
                  points_gotten=acc
                  print "\npoints obtained in this trip:... "+str(points_gotten)
                  print "\nBoard after trip"
                  matrix(lis,size)
             elif travel=="m":
                  print "\n\npositions visited:...\n"
                  for i in range(size):
                      print "["+str(i)+"]"+"["+str(i)+"]"
                      if lis[i][i]==-1:
                        print "oooooooh!!!! a -1!"
                        break
                  acc=0
                  for i in range(size):
                      if (lis[i][i])%2==0:
                          acc+=lis[i][i]/2
                          lis[i][i]=lis[i][i]/2
                      elif lis[i][i]==-1:
                           points_gotten=acc
                           trap="y"
                           break
                      else:
                           acc+=(lis[i][i])
                           lis[i][i]=0
                  points_gotten=acc
                  print "\npoints obtained in this trip:... "+str(points_gotten)
                  print "\nBoard after trip"
                  matrix(lis,size)
             elif travel=="s":
                  print "\n\npositions visited:...\n"
                  for i in range(size):
                      print "["+str(i)+"]"+"["+str(size-i-1)+"]"
                      if lis[i][size-i-1]==-1:
                         print "ooooooooh!!!! a -1!"
                         break
                  acc=0
                  for i in range(size):
                      if (lis[i][size-i-1])%2==0:
                          acc+=lis[i][size-i-1]/2
                          lis[i][size-i-1]=lis[i][size-i-1]/2
                      elif lis[i][size-i-1]==-1:
                          trap="y"
                          break
                      else:
                           acc+=(lis[i][size-i-1])
                           lis[i][size-i-1]=0
                  points_gotten=acc
                  print "\npoints obtained in this trip:... "+str(points_gotten)
                  print "\nBoard after trip"
                  matrix(lis,size)
             elif travel=="x":
                  acc=0
                  n=input("\n\nHow many random cells shall the hunter visit?:")
                  for i in range(n):
                      a=r.randint(0,(size-1))
                      b=r.randint(0,(size-1))
                      print "["+str(a)+"]"+"["+str(b)+"]"
                      if lis[a][b]%2==0:
                          acc+=lis[a][b]/2
                          lis[a][b]=lis[a][b]/2
                      elif lis[a][b]==-1:
                          print "oooooooooh!!!a -1!"
                          trap="y"
                          break
                      else:
                          acc+=lis[a][b]
                          lis[a][b]=0
                  points_gotten=acc
                  print "\npoints obtained in this trip:... "+str(points_gotten)
                  print "\nBoard after trip"
                  matrix(lis,size)
             all_points=all_points+points_gotten
             if trap!="y":
                 decision2=raw_input('\nWould you like '+name+' to do another trip?(y/n):')
                 while decision2!="y" and decision2!="n" and decision2!="trap":
                       print "That is not a valid input,please re-enter"
                       decision2=raw_input('\nWould you like '+name+' to do another trip?(y/n):')
         if trap=="y":
             print "\nOh no! "+name+" got trapped!"
             print name+" cannot travel again :("
         print "\n\nThe treasure hunter "+name+" obtained "+str(all_points)+" points in its game"
         obtain_list_0s_1s(lis)
         num1=0
         num2=0
         string=""
         for i in range(len(lis)):
             num1=0
             for j in range(len(lis)):
                   num1+=lis[i][j]*(2**(len(lis)-j-1))
                   num2+=lis[i][j]*(2**(len(lis)-j-1))
             string+=str(num1)+","
         print "\n\nThe values of each row in the board(as binary number)are:"
         print string+" and therefor the board lucky number is:"+str(num2)

    total_points.append(all_points)
    hunter_.append(name)
    trap_status.append(trap)
    lucky_number.append(num2)
    all_points=0
    decision=raw_input("\nWould you like to play again? (y/n): ")     
print "\n\nTotal hunters that played: "+str(len(hunter_))
total=0
maximum=total_points[0]
minimum=lucky_number[0]
for i in range(len(total_points)-1):
    total+=total_points[i]
    maximum=max(maximum,total_points[i],total_points[i+1])
    minimum=min(minimum,lucky_number[i],lucky_number[i+1])
total=total+total_points[-1]
print "\nTotal points of all hunters: "+str(total)
print "\nMaximum hunter points:"
max_pos=total_points.index(maximum)
min_pos=lucky_number.index(minimum)
max_status=" who is fine,"
min_status=" who is fine,"
if trap_status[max_pos]=="y":
    max_status=" who is trapped,"
if trap_status[min_pos]=="y":
    min_status=" who is trapped,"
print "  The hunter "+str(hunter_[max_pos])+", "+max_status
print "  got the maximum points: "+str(total_points[max_pos])
print "\nMinimum lucky number:"
print "  The board with the hunter "+str(hunter_[min_pos])+", "+min_status
print "  got the minimum lucky number: "+str(lucky_number[min_pos])
print "\n\n\nBye"
