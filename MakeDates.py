def Make_Dates(start_Year, start_Month, start_Day, end_Year, end_Month, end_Day):

      DATE_LIST = []
      END = True
      while END:
          DATE_LIST.append([start_Year,start_Month,start_Day])
          start_Day = start_Day+1
          if((start_Month==1 or start_Month==3 or start_Month==5 or start_Month==7 or start_Month==8 or start_Month==10) and (start_Day==32)):
              start_Month= start_Month+1
              start_Day=1
          if((start_Month==4 or start_Month==6 or start_Month==9 or start_Month==11) and (start_Day==31)):
              start_Month= start_Month+1
              start_Day=1
          if(start_Month==2 and (start_Day==29)):
              start_Month= start_Month+1
              start_Day=1
          if((start_Month == 12) and (start_Day==32)):
              start_Month = 1
              start_Day = 1
              start_Year= start_Year+1
          if((start_Year==end_Year) and (start_Month==end_Month) and (start_Day==end_Day+1)):
              END = False
      return DATE_LIST



